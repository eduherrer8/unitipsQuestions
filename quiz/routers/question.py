# -*- coding: utf-8 -*-
"""
"""

from rest_framework.routers import SimpleRouter

from quiz.views.questionView import QuestionView

question_router = SimpleRouter()

question_router.register(
    r'question',
    QuestionView,
    base_name='question'
)
