from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.uploadedfile import UploadedFile, InMemoryUploadedFile, TemporaryUploadedFile

# Create your views here.


@csrf_exempt
def app_uploads(request):
    file = request.FILES.get('file')
    if isinstance(file, InMemoryUploadedFile):
        return HttpResponse(content='Memory Uploaded File')
    elif isinstance(file, TemporaryUploadedFile):
        return HttpResponse(content='Temporary Uploaded File')
    return HttpResponse(content='Hello', status=200)
