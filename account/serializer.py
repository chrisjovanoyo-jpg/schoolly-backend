from rest_framework import serializers

from .models import User, Profile


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "password"
        ]

    def create(self, validated_data):

        user = User(
            username=validated_data["username"],
            email=validated_data["email"]
        )

        user.set_password(
            validated_data["password"]
        )

        user.save()

        return user


class OnboardingSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            "university",
            "program"
        ]


class ProfileSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source="user.username",
        read_only=True
    )

    university = serializers.CharField(
        source="user.university.name",
        read_only=True
    )

    program = serializers.CharField(
        source="user.program.name",
        read_only=True
    )

    questions_asked = serializers.IntegerField(
        source="user.questions.count",
        read_only=True
    )

    answers_given = serializers.IntegerField(
        source="user.answers.count",
        read_only=True
    )

    views = serializers.SerializerMethodField()

    class Meta:
        model = Profile

        fields = [
            "profile_picture",
            "username",
            "university",
            "program",
            "questions_asked",
            "answers_given",
            "views",
        ]

        read_only_fields = [
            "username",
            "university",
            "program",
            "questions_asked",
            "answers_given",
            "views",
        ]

    def get_views(self, obj):

        return sum(
            question.views_count
            for question in obj.user.questions.all()
        )


class ChangeProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            "program"
        ]