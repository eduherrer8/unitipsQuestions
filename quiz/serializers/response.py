# -*- coding: utf-8 -*-
"""
"""
from rest_framework import serializers

from quiz.models.question import Question, Answer


class ResponseSerializer(serializers.Serializer):
    question = serializers.SlugRelatedField(
        slug_field='pk',
        queryset=Question.objects.all(),
    )
    choice = serializers.SlugRelatedField(
        slug_field='pk',
        queryset=Answer.objects.all(),
    )
