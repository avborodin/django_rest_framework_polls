from django.shortcuts import render
from rest_framework import generics
from polls.serializers import QuestionTypeSerializer, QuestionSerializer, PollSerializer
from polls.models import QuestionType, Question, Poll, Vote

# Create your views here.

class QuestionTypeListView(generics.ListAPIView):
	serializer_class = QuestionTypeSerializer
	queryset = QuestionType.objects.all()

class PollListView(generics.ListAPIView):
	serializer_class = PollSerializer
	queryset = Poll.objects.all()
 
class QuestionListView(generics.ListAPIView):
	serializer_class = QuestionSerializer
	queryset = Question.objects.all()
