from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from invest.models import user
from django.core import serializers
from invest.serializers import userserialize
from rest_framework import viewsets
import easyquotation


# def index(request):
#     MOCK_DATA = 'var hq_str_sz162411="华宝油气,0.489,0.488,0.491,0.492,0.488,0.490,0.491,133819867,65623147.285,2422992,0.490,4814611,0.489,2663142,0.488,1071900,0.487,357900,0.486,5386166,0.491,8094689,0.492,6087538,0.493,2132373,0.494,5180900,0.495,2019-03-12,15:00:03,00";\n'
#     user1=user.objects.all()
#     json1=serializers.serialize('json',user1)
#     print(json1)
#     sina = easyquotation.use("sina")
#     stock_name = sina.format_response_data(MOCK_DATA)["162411"]["name"]
#     print(stock_name)
#     #return HttpResponse(JsonResponse(json1,safe=False), content_type="application/json")
#     return HttpResponse(stock_name)

class userViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all();
    serializer_class = userserialize
# Create your views here.
