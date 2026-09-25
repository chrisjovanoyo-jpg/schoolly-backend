from rest_framework import serializers
from .models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(
        source="author.username",
        read_only=True
    )

    university = serializers.CharField(
        source="author.university.name",
        read_only=True
    )

    class Meta:
        model = Answer
        fields = [
            "id",
            "author_username",
            "university",
            "text",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "author_username",
            "university",
            "created_at",
        ]


class QuestionSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(
        source="author.username",
        read_only=True
    )

    university = serializers.CharField(
        source="author.university.name",
        read_only=True
    )

    answers_count = serializers.IntegerField(
        source="answers.count",
        read_only=True
    )

    answers = AnswerSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Question
        fields = [
            "id",
            "author_username",
            "university",
            "text",
            "created_at",
            "views_count",
            "answers_count",
            "answers",
        ]

        read_only_fields = [
            "id",
            "author_username",
            "university",
            "created_at",
            "views_count",
            "answers_count",
            "answers",
        ]