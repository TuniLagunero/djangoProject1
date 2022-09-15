from django.shortcuts import render

def home_page(request):
    return render(request, "Home_page.html")


def contact