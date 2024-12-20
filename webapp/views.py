from django.shortcuts import get_object_or_404, render
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.utils import timezone
import mimetypes

from webapp.settings import RESUME_DIR


def index(request):
    #return HttpResponse("Hello, world. You're at the dictionary index.")
    #context = {"latest_question_list": latest_question_list}
    return render(request, "index.html", )

def resume(request):
    file_path = RESUME_DIR / "Greg-Dorshimer-resume.pdf"
    return FileResponse(open(file_path, 'rb'), as_attachment=False)
