from django.shortcuts import render

def homeView(request):

    context={}
    return render(request, 'main/index.html', context)