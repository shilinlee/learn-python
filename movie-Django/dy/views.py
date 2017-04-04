#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from movie_s import saveMovies
from models import  DyModels


def index(request,page=0):
    page = int(page)
    if page > 1:
        return render(request,'index.html',context={'movies':DyModels.objects.all()[(page-1)*15:page*15],'before':page-1,'next':page+1})
    #return HttpResponse("hello Django")
    return render(request,'index.html',context={'movies':DyModels.objects.all()[:15],'next':2})

def save(request):
    #saveMovies()
    return HttpResponse('OK')

def movie(request,id):
    detail = DyModels.objects.get(id = id)

    return render(request,'movie.html',context={'detail':detail})