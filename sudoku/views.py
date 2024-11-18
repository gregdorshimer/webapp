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
            # TODO store data from external API call locally, including gameID and timestamp
            # TODO add gameID to json object
            del json['solution']
            json['gameID'] = '5678'
            return Response(json)
        except requests.exceptions.RequestException:
            return Response({'error': 'Sudoku games not available.'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)


    def post(self, request, *args, **kwargs):
        """
        takes a "gameID", "answers"
        looks up the gameID locally
        checks answers for correctness
        --depending on correctness, make some alteration to DB for submission tracking
        :return: "correct" or arrays of columns and rows that are wrong
        """
        # TODO get body data
        # TODO look up game locally
        # TODO respond with result of local DB lookup

        return Response({'rows': [4, 7], 'columns': [5, 7]}, status=status.HTTP_200_OK)

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

