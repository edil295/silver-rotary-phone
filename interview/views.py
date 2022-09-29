from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Category, QuestionAnswer
from .serializers import CategorySerializer, QuestionAnswerSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionAnswerViewSet(ModelViewSet):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer

