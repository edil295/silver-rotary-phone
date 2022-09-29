from rest_framework import serializers

from .models import Category, QuestionAnswer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = '__all__'
        exclude = ('answer', )
