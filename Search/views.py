from django.shortcuts import render

# Create your views here.
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from account.models import User
from Questions.models import Question

from .serializers import (
    SearchUserSerializer,
    SearchQuestionSerializer,
)


class SearchView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        query = request.query_params.get(
            "q",
            ""
        ).strip()

        if not query:
            return Response(
                {
                    "error": "Search query is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        questions = Question.objects.filter(
            Q(text__icontains=query)
        ).select_related(
            "author",
            "author__university"
        ).order_by(
            "-created_at"
        )

        users = User.objects.filter(
            Q(username__icontains=query)
        ).select_related(
            "university",
            "program"
        ).order_by(
            "username"
        )

        question_serializer = SearchQuestionSerializer(
            questions,
            many=True
        )

        user_serializer = SearchUserSerializer(
            users,
            many=True
        )

        return Response(
            {
                "questions": question_serializer.data,
                "users": user_serializer.data
            },
            status=status.HTTP_200_OK
        )