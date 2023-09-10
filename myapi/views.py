from django.shortcuts import render
from .models import dsa,users,visits
from django.http import HttpResponse, JsonResponse
import requests
import json


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
        dict[j]=i
        j+=1
    return JsonResponse(dict)

def leaderboardweek(request):
    dict={}
    j=1
    for i in list(users.objects.order_by("-week").values()):
        dict[j]=i
        j+=1
    return JsonResponse(dict)
    
def sync(request):
    for i in users.objects.all():
        name=i.user_name
        url="https://leetcode-stats-api.herokuapp.com/"+name
        obj = requests.get(url).json()
        i.total=obj["totalSolved"]
        i.save()
    return HttpResponse("Success")


def evaluate(request):
    for i in users.objects.all():
        name=i.user_name
        url="https://leetcode-stats-api.herokuapp.com/"+name
        obj = requests.get(url).json()
        total=obj["totalSolved"]
        i.today=total-i.total
        i.save()
    return HttpResponse("Success")

