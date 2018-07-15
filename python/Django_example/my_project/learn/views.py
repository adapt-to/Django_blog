# coding:utf-8
from django.http import HttpResponse
def index(request):
    return HttpResponse("欢迎光临，这是由Django创建的网页!")
# Create your views here.
