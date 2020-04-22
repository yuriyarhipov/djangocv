import datetime 

from django.shortcuts import render
from cv.models import Cv


def main(request):
    data = Cv.objects.filter().first()
    result = {'data': data}
    result['year'] = datetime.datetime.now().year    
    return render(request, 'main.html', result)
