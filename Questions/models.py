from django.conf import settings
from django.db import models


class Question(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="questions"
    )

    program = models.ForeignKey(
        "Academic.Program",
        on_delete=models.PROTECT,
        related_name="questions"
    )

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    views_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text[:50]


class Answer(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="answers"
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers"
    )

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:50]


class Helpful(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="helpful_questions"
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="helpfuls"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "question"],
                name="unique_user_question_helpful"
            )
        ]

    def __str__(self):
        return f"{self.user.username} marked question {self.question.id} helpful"


class SavedQuestion(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="saved_questions"
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="saved_by"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "question"],
                name="unique_user_question_save"
            )
        ]

    def __str__(self):
        return f"{self.user.username} saved question {self.question.id}"