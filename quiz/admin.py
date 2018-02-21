from django.contrib import admin

from quiz.models.question import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    """
    """
    pass


class AnswerAdmin(admin.ModelAdmin):
    """
    """
    def save_model(self, request, obj, form, change):
        question_id = request.POST['question']
        if Answer.objects.filter(question__id=question_id).count() >= 4:
            return
        if "True" in Answer.objects.filter(question__id=question_id).values_list('correct',flat=True):
            return
        obj.save()

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
