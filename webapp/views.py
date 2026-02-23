from django.shortcuts import render
from django.http import FileResponse

from webapp.settings import RESUME_DIR

def index(request):
    #return HttpResponse('Hello, world. You're at the dictionary index.')
    #context = {'latest_question_list': latest_question_list}
    # source_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
    print('### Request from:', ip)
    return render(request, "index.html", )

def resume(request):
    file_path = RESUME_DIR / "Greg-Dorshimer-resume.pdf"
    return FileResponse(open(file_path, 'rb'), as_attachment=False)
