from django.shortcuts import render
from cv.models import Cv


def main(request):
    data = Cv.objects.filter().first()
    return render(request, 'main.html', {'data': data})
