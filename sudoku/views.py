from django.shortcuts import get_object_or_404, render
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sudoku.models import GameModel
from math import floor

# TODO figure out out-of-band batch work for DB cleanup and pre-querying the external API

def index(request):
    return render(request, "sudoku/index.html", )


class GameAPIView(APIView):
    def get(self, request, *args, **kwargs):
        """
        gets a new easy game from the external sudoku API
        stores it locally with a gameID
        :return: the game and ID as JSON
        """
        # print(request.query_params['difficulty']) # how to access URL encoded params -> QueryDict
        difficulty = request.query_params.get('difficulty', 'easy') # difficulty is 'easy' if no difficulty supplied

        body = {
            "difficulty": difficulty,  # "easy", "medium", or "hard" (defaults to "easy")
            "solution": True,  # True or False (defaults to True)
            "array": False  # True or False (defaults to False)
        }
        headers = { "Content-Type": "application/json" }
        try :
            response = requests.post("https://youdosudoku.com/api/", json=body, headers=headers)
            json = response.json()

            # store game
            game = GameModel.objects.create(game=json['puzzle'], solution=json['solution'], difficulty=json['difficulty'], time_queried=timezone.now())
            # TODO catch errors on game duplication (see: get_or_create())

            del json['solution']
            return Response(json)
        except requests.exceptions.RequestException:
            return Response({'error': 'Sudoku games not available.'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)


    def post(self, request, *args, **kwargs):
        """
        takes game, submission
        looks up the game locally
        checks answers for correctness
        --depending on correctness, make some alteration to DB for submission tracking
        :return: "correct" or arrays of columns and rows that are wrong
        """
        # print('.data: ', request.data['submission']) # <-- how to access post request body
        game = request.data['game']
        submission = request.data['submission']
        solution = GameModel.objects.get(game=game).solution
        # TODO handle game not found case

        if solution == submission:
            return Response({'correct': True}, status=status.HTTP_200_OK)
        else:
            # compile rows and columns that are wrong
            rows = []
            columns = []
            for i in range(81):
                if submission[i] != solution[i]:
                    rows.append(floor(i / 9))
                    columns.append(i % 9)
            return Response({'correct': False,
                             'rows': rows,
                             'columns': columns},
                            status=status.HTTP_200_OK)

        # ex. of expected responses:
        # return Response({'rows': [2, 7], 'columns': [5, 7]}, status=status.HTTP_200_OK)
        # return Response({'correct': True}, status=status.HTTP_200_OK)

"""
class IndexView(generic.ListView):
    template_name = "dictionary/index.html"
    def get_queryset(self):
        return
"""
"""
class IndexView(generic.ListView):
    template_name = "wiki/index.html"

"""

