from django.urls import path

from .views import (
    QuestionListCreateView,
    QuestionDetailView,
    AnswerListCreateView,
    AnswerDetailView,
    ExploreQuestionsView,
)


urlpatterns = [
    path(
        "",
        QuestionListCreateView.as_view(),
        name="question-list-create"
    ),

    path(
        "<int:pk>/",
        QuestionDetailView.as_view(),
        name="question-detail"
    ),

    path(
        "<int:question_id>/answers/",
        AnswerListCreateView.as_view(),
        name="answer-list-create"
    ),

    path(
        "answers/<int:pk>/",
        AnswerDetailView.as_view(),
        name="answer-detail"
    ),

    path(
    "explore/",
    ExploreQuestionsView.as_view(),
    name="explore-questions"
),
]