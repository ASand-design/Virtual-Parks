from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def disney(request):
    return render(request, 'disney.html')

def universal(request):
    return render(request, 'universal.html')

def contact(request):
    return render(request, 'contact.html')

def main(request):
    return render(request, 'main.html')
