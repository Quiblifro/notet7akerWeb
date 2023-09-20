from django.shortcuts import render
from .models import User, Note
def index (request):
    return render(request, 'index.html')
def add_note(request):
    data = request.body
    print(data)