from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
from .permissions import IsQuestionAuthor, IsAnswerAuthor


class QuestionListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.user.program:
            return Response(
                {"error": "Please complete onboarding first."},
                status=status.HTTP_400_BAD_REQUEST
            )

        questions = Question.objects.filter(
            program=request.user.program
        ).order_by("-created_at")

        serializer = QuestionSerializer(
            questions,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        if not request.user.program:
            return Response(
                {"error": "Please complete onboarding first."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = QuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        question = serializer.save(
            author=request.user,
            program=request.user.program
        )

        return Response(
            QuestionSerializer(question).data,
            status=status.HTTP_201_CREATED
        )



#explorer feature
class ExploreQuestionsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        questions = Question.objects.all().order_by("-created_at")

        serializer = QuestionSerializer(
            questions,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )




class QuestionDetailView(APIView):
    def get_permissions(self):
        if self.request.method in ["PATCH", "DELETE"]:
            return [IsAuthenticated(), IsQuestionAuthor()]

        return [IsAuthenticated()]

    def get_object(self, pk):
        return get_object_or_404(
            Question,
            pk=pk
        )

    def get(self, request, pk):
        question = self.get_object(pk)

        serializer = QuestionSerializer(question)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def patch(self, request, pk):
        question = self.get_object(pk)

        self.check_object_permissions(
            request,
            question
        )

        serializer = QuestionSerializer(
            question,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def delete(self, request, pk):
        question = self.get_object(pk)

        self.check_object_permissions(
            request,
            question
        )

        question.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class AnswerListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, question_id):
        question = get_object_or_404(
            Question,
            pk=question_id
        )

        answers = question.answers.all().order_by(
            "created_at"
        )

        serializer = AnswerSerializer(
            answers,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request, question_id):
        question = get_object_or_404(
            Question,
            pk=question_id
        )

        serializer = AnswerSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        answer = serializer.save(
            author=request.user,
            question=question
        )

        return Response(
            AnswerSerializer(answer).data,
            status=status.HTTP_201_CREATED
        )


class AnswerDetailView(APIView):
    def get_permissions(self):
        if self.request.method in ["PATCH", "DELETE"]:
            return [IsAuthenticated(), IsAnswerAuthor()]

        return [IsAuthenticated()]

    def get_object(self, pk):
        return get_object_or_404(
            Answer,
            pk=pk
        )

    def get(self, request, pk):
        answer = self.get_object(pk)

        serializer = AnswerSerializer(answer)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def patch(self, request, pk):
        answer = self.get_object(pk)

        self.check_object_permissions(
            request,
            answer
        )

        serializer = AnswerSerializer(
            answer,
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

    def delete(self, request, pk):
        answer = self.get_object(pk)

        self.check_object_permissions(
            request,
            answer
        )

        answer.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )