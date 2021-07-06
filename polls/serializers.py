from rest_framework import serializers
from polls.models import QuestionType, Question, Poll, Vote

class QuestionTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = QuestionType
		fields = ('id', 'text')

class QuestionSerializer(serializers.ModelSerializer):
    
    questtype = QuestionTypeSerializer(many=True, required=False)
    
    class Meta:
        model = Question
        fields = ('id', 'text', 'poll', 'questtype')
        read_only_fields = ('id', )
        
        extra_kwargs = {
            'poll': {'write_only': True}
        }

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id', 'title', 'start_dt', 'end_dt', 'descr')
        read_only_fields = ('id', )

    def validate_start_date(self, value):
        if self.instance and self.instance.start_date < value:
            raise serializers.ValidationError(
                "Невозожно измннить дату после создания"
            )

        return value
