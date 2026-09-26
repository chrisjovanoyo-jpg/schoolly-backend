from django.urls import path

from .views import (
    QuestionListCreateView,
    QuestionDetailView,
    AnswerListCreateView,
    AnswerDetailView,
    ExploreQuestionsView,
    HelpfulQuestionView,
    SaveQuestionView,
    MySavedQuestionsView,
)

urlpatterns = [
    # Question list
    path("", QuestionListCreateView.as_view(), name="question-list-create"),

    # Question collections
    path("explore/", ExploreQuestionsView.as_view(), name="explore-questions"),
    path("saved/", MySavedQuestionsView.as_view(), name="my-saved-questions"),

    # Question actions
    path(
        "<int:question_id>/helpful/",
        HelpfulQuestionView.as_view(),
        name="helpful-question"
    ),
    path(
        "<int:question_id>/save/",
        SaveQuestionView.as_view(),
        name="save-question"
    ),

    # Answers
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

    # Question detail — keep generic route LAST
    path(
        "<int:pk>/",
        QuestionDetailView.as_view(),
        name="question-detail"
    ),
]