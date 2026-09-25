from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from Questions.serializers import (
    QuestionSerializer,
    AnswerSerializer
)

from .serializer import (
    RegisterSerializer,
    OnboardingSerializer,
    ProfileSerializer,
    ChangeProgramSerializer
)


class RegisterView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        user = serializer.save()

        return Response(
            {
                "message": "Account created successfully",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                }
            },
            status=status.HTTP_201_CREATED
        )


class OnboardingView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def patch(self, request):

        serializer = OnboardingSerializer(
            request.user,
            data=request.data,
            partial=True
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            {
                "message": "Onboarding completed successfully",
                "user": serializer.data
            },
            status=status.HTTP_200_OK
        )


class ProfileView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        profile = request.user.profile

        serializer = ProfileSerializer(
            profile
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def patch(self, request):

        profile = request.user.profile

        serializer = ProfileSerializer(
            profile,
            data=request.data,
            partial=True
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class MyQuestionsView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        questions = request.user.questions.all().order_by(
            "-created_at"
        )

        serializer = QuestionSerializer(
            questions,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class MyAnswersView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        answers = request.user.answers.all().order_by(
            "-created_at"
        )

        serializer = AnswerSerializer(
            answers,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class ChangeProgramView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def patch(self, request):

        serializer = ChangeProgramSerializer(
            request.user,
            data=request.data,
            partial=True
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            {
                "message": "Program changed successfully",
                "program": serializer.data["program"]
            },
            status=status.HTTP_200_OK
        )