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

