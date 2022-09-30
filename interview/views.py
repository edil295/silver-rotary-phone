from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, \
    DestroyAPIView, RetrieveAPIView, ListCreateAPIView

from .models import Category, QuestionAnswer
from .serializers import CategorySerializer, QuestionAnswerListSer, QuestionAnswerDetailSer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionAnswerListView(ListCreateAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerListSer


class QuestionAnswerDetailView(UpdateAPIView, DestroyAPIView, RetrieveAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerDetailSer

