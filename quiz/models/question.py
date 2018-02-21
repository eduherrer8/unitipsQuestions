from django.db import models

# Crea tus modelos de preguntas y respuestas para el quiz aquí.

class Question(models.Model):
    """
    """
    question = models.TextField()


    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'

    def __str__(self):
        return self.question


class Answer(models.Model):
    """
    """
    choice = models.TextField()
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(
        Question,
        related_name='answer',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'

    def __str__(self):
        return self.choice
