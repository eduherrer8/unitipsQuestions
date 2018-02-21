# -*- coding: utf-8 -*-
"""
"""
from rest_framework import serializers

from quiz.models.question import Question, Answer


class AnserSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = Question
        fields = ('id', 'question',)
        read_only_fields = (
            'id',
        )
