# -*- coding: utf-8 -*-
"""
"""
from rest_framework import viewsets

from quiz.models.question import Question
from quiz.serializers.questionSerializer import QuestionSerializer


class QuestionView(viewsets.ModelViewSet):
    """
    """
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
