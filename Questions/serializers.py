from rest_framework import serializers

from .models import (
    Question,
    Answer,
    Helpful,
    SavedQuestion
)


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

    helpful_count = serializers.IntegerField(
        source="helpfuls.count",
        read_only=True
    )

    helpful = serializers.SerializerMethodField()

    saved = serializers.SerializerMethodField()

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
            "helpful_count",
            "helpful",
            "saved",
            "answers",
        ]

        read_only_fields = [
            "id",
            "author_username",
            "university",
            "created_at",
            "views_count",
            "answers_count",
            "helpful_count",
            "helpful",
            "saved",
            "answers",
        ]

    def get_helpful(self, obj):
        request = self.context.get("request")

        if not request or not request.user.is_authenticated:
            return False

        return obj.helpfuls.filter(
            user=request.user
        ).exists()

    def get_saved(self, obj):
        request = self.context.get("request")

        if not request or not request.user.is_authenticated:
            return False

        return obj.saved_by.filter(
            user=request.user
        ).exists()
    

    
class HelpfulSerializer(serializers.ModelSerializer):

    class Meta:
        model = Helpful

        fields = [
            "id",
            "user",
            "question",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "question",
            "created_at",
        ]


class SavedQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SavedQuestion

        fields = [
            "id",
            "user",
            "question",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "question",
            "created_at",
        ]