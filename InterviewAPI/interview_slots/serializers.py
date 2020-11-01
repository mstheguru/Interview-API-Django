from datetime import datetime
import pytz

from django.utils import timezone
from rest_framework import serializers

from InterviewAPI import error_handling as err
from .models import CandidateTimeSlot, InterviewerTimeSlot


class CandidateTimeSlotSerializer(serializers.ModelSerializer):

    start_datetime = serializers.SerializerMethodField()
    end_datetime = serializers.SerializerMethodField()

    def get_start_datetime(self, instance):
        return instance.start_datetime.timestamp()

    def get_end_datetime(self, instance):
        return instance.end_datetime.timestamp()

    def validate(self, data):
        # Validate candidate name
        if not self.initial_data.get('candidate_name'):
            raise err.ValidationError("Candidate's name is required.", 400)
        # Start datetime and End datetime validations
        start_datetime = self.initial_data.get('start_datetime', None)
        if not start_datetime:
            raise err.ValidationError("Start date and time is required.", 400)
        start_datetime = float(start_datetime)
        end_datetime = self.initial_data.get('end_datetime', None)
        if not end_datetime:
            raise err.ValidationError("End date and time is required.", 400)
        end_datetime = float(end_datetime)

        if start_datetime < timezone.now().timestamp():
            raise serializers.ValidationError({"message": "Start datetime is lesser than current time."})
        if start_datetime >= end_datetime:
            raise serializers.ValidationError({"message": "End date time lesser than start date and time."})
        if end_datetime < timezone.now().timestamp():
            raise serializers.ValidationError({"message": "End date and time is lesser than current time."})
        # Convert the start and end datetime
        start_datetime = datetime.fromtimestamp(float(start_datetime), tz=pytz.UTC)
        end_datetime = datetime.fromtimestamp(float(end_datetime), tz=pytz.UTC)
        if start_datetime.date() != end_datetime.date():
            raise err.ValidationError("Please select the same date for the available time slot.", 400)
        data['start_datetime'] = str(start_datetime)
        data['end_datetime'] = str(end_datetime)

        return data

    def create(self, validated_data):
        """
        Overriding the create function to save the candidate timeslot
        :param validated_data:
        :return:
        """

        candidate_timeslot = CandidateTimeSlot.objects.create(
            candidate_name=validated_data['candidate_name'],
            start_datetime=validated_data['start_datetime'],
            end_datetime=validated_data['end_datetime']
        )

        return candidate_timeslot

    class Meta:
        model = CandidateTimeSlot
        fields = ('candidate_name', 'start_datetime', 'end_datetime')


class InterviewerTimeSlotSerializer(serializers.ModelSerializer):

    start_datetime = serializers.SerializerMethodField()
    end_datetime = serializers.SerializerMethodField()

    def get_start_datetime(self, instance):
        return instance.start_datetime.timestamp()

    def get_end_datetime(self, instance):
        return instance.end_datetime.timestamp()

    def validate(self, data):
        # Validate interviewer name
        if not self.initial_data.get('interviewer_name'):
            raise err.ValidationError("Interviewer's name is required.", 400)
        # Start datetime and End datetime validations
        start_datetime = self.initial_data.get('start_datetime', None)
        if not start_datetime:
            raise err.ValidationError("Start date and time is required.", 400)
        start_datetime = float(start_datetime)
        end_datetime = self.initial_data.get('end_datetime', None)
        if not end_datetime:
            raise err.ValidationError("End date and time is required.", 400)
        end_datetime = float(end_datetime)

        if start_datetime < timezone.now().timestamp():
            raise serializers.ValidationError({"message": "Start datetime is lesser than current time."})
        if start_datetime >= end_datetime:
            raise serializers.ValidationError({"message": "End date time lesser than start date and time."})
        if end_datetime < timezone.now().timestamp():
            raise serializers.ValidationError({"message": "End date and time is lesser than current time."})
        # Convert the start and end datetime
        start_datetime = datetime.fromtimestamp(float(start_datetime), tz=pytz.UTC)
        end_datetime = datetime.fromtimestamp(float(end_datetime), tz=pytz.UTC)
        if start_datetime.date() != end_datetime.date():
            raise err.ValidationError("Please select the same date for the available time slot.", 400)
        data['start_datetime'] = str(start_datetime)
        data['end_datetime'] = str(end_datetime)

        return data

    def create(self, validated_data):
        """
        Overriding the create function to save the interviewer timeslot
        :param validated_data:
        :return:
        """

        interviewer_timeslot = InterviewerTimeSlot.objects.create(
            interviewer_name=validated_data['interviewer_name'],
            start_datetime=validated_data['start_datetime'],
            end_datetime=validated_data['end_datetime']
        )

        return interviewer_timeslot

    class Meta:
        model = InterviewerTimeSlot
        fields = ('interviewer_name', 'start_datetime', 'end_datetime')
