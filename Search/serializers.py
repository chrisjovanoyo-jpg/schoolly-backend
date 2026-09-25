from rest_framework import serializers

from account.models import User
from Questions.models import Question


class SearchUserSerializer(serializers.ModelSerializer):

    university = serializers.CharField(
        source="university.name",
        read_only=True
    )

    program = serializers.CharField(
        source="program.name",
        read_only=True
    )

    class Meta:
        model = User

        fields = [
            "id",
            "username",
            "university",
            "program",
        ]


class SearchQuestionSerializer(serializers.ModelSerializer):

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
        ]