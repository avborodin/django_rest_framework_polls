from django.contrib import admin
from django.urls import path, include
from polls.views import *


urlpatterns = [
    path('questiontype', QuestionTypeListView.as_view()),
    path('questions', QuestionListView.as_view()),
    path('polls', PollListView.as_view()),
]