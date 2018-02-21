from django.conf.urls import url, include

from quiz.routers.question import question_router
from quiz.views.response import ResponseView

question_patterns = (question_router.urls, 'question')

app_name = "quiz_api"

response_patterns = ([
    url(r'^$', ResponseView.as_view(), name='response'),
], 'response')

urlpatterns = [
    url(r'^', include(question_patterns)),
    url(r'^response/', include(response_patterns)),
]
