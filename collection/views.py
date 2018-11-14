from django.shortcuts import render

def index(request):
    number = 2
    thing = "Thing name"
    return render(request, 'index.html', {'number': number, 'thing': thing,})