from django.shortcuts import render
from django.http import JsonResponse
import requests
from .forms import UploadImageForm

def compare_images(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            reference = request.FILES['reference']
            target = request.FILES['target']
            
            files = {
                'reference': reference,
                'target': target
            }
            response = requests.post('http://<tu-servidor>/compare', files=files)
            result = response.json()
            
            return render(request, 'compare/result.html', {'result': result})
    else:
        form = UploadImageForm()
    return render(request, 'compare/upload.html', {'form': form})