from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import University, Program
from .serializers import UniversitySerializer, ProgramSerializer


class UniversityListView(APIView):

    def get(self, request):
        universities = University.objects.all()

        serializer = UniversitySerializer(universities, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class ProgramListView(APIView):

    def get(self, request):
        programs = Program.objects.all()

        serializer = ProgramSerializer(programs, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class UniversityDetailView(APIView):

    def get(self, request, pk):
        university = University.objects.get(pk=pk)

        serializer = UniversitySerializer(university)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class ProgramDetailView(APIView):

    def get(self, request, pk):
        program = Program.objects.get(pk=pk)

        serializer = ProgramSerializer(program)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )