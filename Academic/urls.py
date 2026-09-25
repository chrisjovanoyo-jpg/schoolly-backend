from django.urls import path

from .views import (
    UniversityListView,
    UniversityDetailView,
    ProgramListView,
    ProgramDetailView,
)


urlpatterns = [
    path(
        "universities/",
        UniversityListView.as_view(),
        name="university-list",
    ),

    path(
        "universities/<int:pk>/",
        UniversityDetailView.as_view(),
        name="university-detail",
    ),

    path(
        "programs/",
        ProgramListView.as_view(),
        name="program-list",
    ),

    path(
        "programs/<int:pk>/",
        ProgramDetailView.as_view(),
        name="program-detail",
    ),
]