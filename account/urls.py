

from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenBlacklistView,
    TokenRefreshView,
)

from .views import (
    RegisterView,
    OnboardingView,
    ProfileView,
    MyQuestionsView,
    MyAnswersView,
    ChangeProgramView
)


urlpatterns = [

    path(
        "register/",
        RegisterView.as_view(),
        name="register"
    ),

    path(
        "login/",
        TokenObtainPairView.as_view(),
        name="login"
    ),

    path(
        "logout/",
        TokenBlacklistView.as_view(),
        name="logout"
    ),

    path(
        "token/refresh/", 
        TokenRefreshView.as_view(),
        name = "refresh"
    ),

    path(
        "onboarding/",
        OnboardingView.as_view(),
        name="onboarding"
    ),

    path(
        "profile/",
        ProfileView.as_view(),
        name="profile"
    ),

    path(
        "profile/questions/",
        MyQuestionsView.as_view(),
        name="my-questions"
    ),

    path(
        "profile/answers/",
        MyAnswersView.as_view(),
        name="my-answers"
    ),

    path(
        "profile/change-program/",
        ChangeProgramView.as_view(),
        name="change-program"
    ),
]