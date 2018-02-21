# -*- coding: utf-8 -*-
"""
"""
from rest_framework.views import APIView
from rest_framework.response import Response

from quiz.models.question import Question, Answer
from quiz.serializers.response import ResponseSerializer


class ResponseView(APIView):
    serializer_class = ResponseSerializer

    def post(self, request):
        """
        """
        response = {}
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = Question.objects.get(pk=serializer.data['question'])
        answer = Answer.objects.get(pk=serializer.data['choice'])
        allow_anserws = Answer.objects.filter(question=question)
        if answer not in allow_anserws:
            response['error'] = "No es una opción correcta"
        elif answer.correct:
            response['mensaje'] = "Respuesta corrrecta"
        else:
            response['error'] = "Respuesta incorrecta"
        return Response(response)
