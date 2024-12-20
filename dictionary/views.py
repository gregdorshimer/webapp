from django.shortcuts import get_object_or_404, render
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone


def index(request):
    #return HttpResponse("Hello, world. You're at the dictionary index.")
    #context = {"latest_question_list": latest_question_list}
    return render(request, "dictionary/index.html", )
