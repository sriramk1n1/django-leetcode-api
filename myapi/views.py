from django.shortcuts import render
from .models import dsa,users
from django.http import HttpResponse, JsonResponse
import requests
import json


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def week(request):
    dict={}
    j=1
    for i in list(dsa.objects.values()):
        dict[j]=i
        j+=1
    return JsonResponse(dict)
    
    
def progress(request):
    dict={}
    j=1
    for i in list(users.objects.values()):
        dict[j]=i
        j+=1
    return JsonResponse(dict)
    
def leaderboard(request):
    dict={}
    j=1
    for i in list(users.objects.order_by("-today").values()):
        dict[j]=i
        j+=1
    return JsonResponse(dict)
    
def leaderboardall(request):
    dict={}
    j=1
    for i in list(users.objects.order_by("-total").values()):
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

