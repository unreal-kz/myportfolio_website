from django.shortcuts import render

def homeView(request):

    context={}
    return render(request, 'base/index.html', context)