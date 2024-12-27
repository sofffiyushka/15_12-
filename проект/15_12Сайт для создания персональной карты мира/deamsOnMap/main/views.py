from django.shortcuts import render

def index(requests):
    return render(requests, 'main/index.html')

def myvis(requests):
    return render(requests, 'main/myvis.html')

def favou(requests):
    return render(requests, 'main/favou.html')

def myimp(requests):
    return render(requests, 'main/myimp.html')

def mylin(requests):
    return render(requests, 'main/mylin.html')
