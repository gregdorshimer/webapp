from django.shortcuts import get_object_or_404, render
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def index(request):
    #return HttpResponse("Hello, world. You're at the dictionary index.")
    #context = {"latest_question_list": latest_question_list}
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
        return Response(
            { "game": "999000300010003780040100260400308020000204610002590400564000900001000000387002000",
              "difficulty": difficulty,
              'id': '1234'},
            status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        takes a "gameID", "game", and "answers"
        looks up the gameID locally
        checks answers for correctness
        --depending on correctness, make some alteration to DB for submission tracking
        :return: "correct" or arrays of columns and rows that are wrong
        """
        return Response(status=status.HTTP_200_OK)

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

