# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render
import names

from random import choice

from .models import stats
# Create your views here.

class GenrateHero(APIView):
    def post(self, request):
        #gen = request.body['hero']
        #if gen:
        hero = 'Hero ' + names.get_full_name()
        name_list = [name.name for name in stats.objects.all()]
        if hero not in name_list:
            h = stats(name=hero, score=0, status='Alive')
            h.save()
        return Response({'name':hero, 'score':0, 'status': 'Alive'})

    def get(self, request):
        heros_list = [name.name for name in stats.objects.all()]
        if heros_list:
            return Response({'heros_list': heros_list})
        else:
            return Response('No heros found')

class Fight(APIView):
    def post(self, request):
        alive = stats.objects.filter(status='Alive')
        if len(alive)==1:
            return Response('Generate more heros or select the champion')
        else:
            hero1 = choice(alive)
            hero2 = choice(alive)
            if hero1.name == hero2.name:
                return Response('Try again')
        victory = choice([hero1, hero2])
        if victory == hero1:
            stats.objects.filter(name=hero2.name).update(status='Dead')
            stats.objects.filter(name=hero1.name).update(score=(hero1.score+1))
        else:
            stats.objects.filter(name=hero1.name).update(status='Dead')
            stats.objects.filter(name=hero2.name).update(score=(hero2.score+1))
        return Response(victory.name + ' is the winner')

class Champion(APIView):
    def post(self, request):
        champion = stats.objects.filter(status='Alive')
        l = []
        for c in champion:
            l.append((c.score, c.name))
        l.sort()
        top = l[-1][-1]
        winner = stats.objects.filter(name=top).values()[0]
        return Response({'name':winner['name'], 'score':winner['score']})
