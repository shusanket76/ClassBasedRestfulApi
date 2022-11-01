from django.urls import path
from .views import StudentApi

urlpatterns = [
    path("api", StudentApi.as_view()),
    path("api/<int:pk>", StudentApi.as_view()),

]
