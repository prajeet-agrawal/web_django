from django.shortcuts import render


def home(request):
    template_name = "index.html"
    content = {"name": "Prajeet"}
    return render(request, template_name, content)