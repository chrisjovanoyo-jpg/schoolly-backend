from django.urls import path

from .views import (
    MySavedQuestionsView,
    QuestionListCreateView,
    QuestionDetailView,
    AnswerListCreateView,
    AnswerDetailView,
    ExploreQuestionsView,
    HelpfulQuestionView,
    
)


urlpatterns = [

    path(
        "",
        QuestionListCreateView.as_view(),
        name="question-list-create"
    ),

    path(
        "explore/",
        ExploreQuestionsView.as_view(),
        name="explore-questions"
    ),

    path(
        "<int:question_id>/helpful/",
        HelpfulQuestionView.as_view(),
        name="helpful-question"
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
        "saved/",
        MySavedQuestionsView.as_view(),
        name="my-saved-questions"
    ),
]