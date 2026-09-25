from rest_framework.permissions import BasePermission


class IsQuestionAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsAnswerAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user