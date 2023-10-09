from django.shortcuts import render
from .models import dsa,users,visits
from django.http import HttpResponse, JsonResponse
import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor


def index(request):
    return HttpResponse("API for questions-list.vercel.app")

def week(request):
    v=visits.objects.get(id=1)
    v.no+=1
    v.save()
    dict={} 
    j=1
    id="id"+str(j)
    for i in list(dsa.objects.values()):
        dict[id]=i
        j+=1
        id="id"+str(j)
    return JsonResponse(dict)
    
    
    
def leaderboard(request):
    v=visits.objects.get(id=2)
    v.no+=1
    v.save()
    dict={}
    j=1
    for i in list(users.objects.order_by("-today").values()):
        i["week"]+=i["today"]
        dict[j]=i
        j+=1
    return JsonResponse(dict)
    
def leaderboardall(request):
    v=visits.objects.get(id=3)
    v.no+=1
    v.save()
    dict={}
    j=1
    for i in list(users.objects.order_by("-total").values()):
        i["week"]+=i["today"]
        dict[j]=i
        j+=1
    return JsonResponse(dict)

def leaderboardweek(request):
    dict={}
    j=1
    for i in list(users.objects.order_by("-week").values()):
        i["week"]+=i["today"]
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

def func2(i):
    name=i.user_name
    url="http://127.0.0.1:8080/"+name
    obj = requests.get(url).json()
    i.totalweek=obj["totalSolved"]
    i.save()
    
def syncweek(request):
    executor = ThreadPoolExecutor(max_workers=10)
    for i in users.objects.all():
        executor.submit(func2,i)
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
        
def func4(i):
    name=i.user_name
    url="http://127.0.0.1:8080/"+name
    obj= requests.get(url).json()
    total=obj["totalSolved"]
    i.week=total-i.totalweek
    i.save()

def evaluateweek(request):
    executor = ThreadPoolExecutor(max_workers=10)
    for i in users.objects.all():
        executor.submit(func4,i)
    executor.shutdown(wait=True)
    return HttpResponse("Successfuldone")

