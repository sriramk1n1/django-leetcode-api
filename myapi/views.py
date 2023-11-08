from django.shortcuts import render
from .models import dsa,users
from django.http import HttpResponse, JsonResponse
import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor


def week(request):
    dict={} 
    j=1
    id="id"+str(j)
    for i in list(dsa.objects.values()):
        dict[id]=i
        j+=1
        id="id"+str(j)
    return JsonResponse(dict)
    
    
    
def leaderboardall(request):
    dict={}
    j=1
    for i in list(users.objects.order_by("-today","-total").values()):
        dict[j]=i
        j+=1
    return JsonResponse(dict)
    


def func1(i):
    name=i.user_name
    url="http://127.0.0.1:8080/"+name
    obj = requests.get(url).json()
    i.total=obj["totalSolved"]
    i.save()

def sync(request):
    executor = ThreadPoolExecutor(max_workers=10)
    for i in users.objects.all():
        executor.submit(func1,i)
    executor.shutdown(wait=True)
    return HttpResponse("Successfuldone")

def func3(i):
    name=i.user_name
    url="http://127.0.0.1:8080/"+name
    obj = requests.get(url).json()
    total=obj["totalSolved"]
    i.today=total-i.total
    i.save()

def evaluate(request):
    executor = ThreadPoolExecutor(max_workers=10)
    for i in users.objects.all():
        executor.submit(func3,i)
    executor.shutdown(wait=True)
    return HttpResponse("Successfuldone")
        
