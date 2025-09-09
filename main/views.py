from django.shortcuts import render

def show_main(request):
    context = {
        'appname' : 'Football Store',
        'name': 'Angelo Johenry Apituley',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)