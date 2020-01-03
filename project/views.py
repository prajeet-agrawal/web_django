from django.shortcuts import render

def home(request):
    template_dir = "index.html"
    return render(request, 'index.html')