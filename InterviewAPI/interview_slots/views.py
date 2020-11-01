import datetime

from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status, serializers
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveAPIView, \
    GenericAPIView, DestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.response import Response

from InterviewAPI import error_handling as err
from .models import CandidateTimeSlot, InterviewerTimeSlot
from .serializers import CandidateTimeSlotSerializer, InterviewerTimeSlotSerializer

# Create your views here.


class CandidateTimeSlotCreateUpdateView(CreateAPIView, UpdateAPIView):
    """
    API class to create/update candidate timeslots
    """
    serializer_class = CandidateTimeSlotSerializer

    def post(self, request, *args, **kwargs):
        candidate_id = request.data.get('candidate_id', None)
        if candidate_id:
            try:
                candidate_instance = CandidateTimeSlot.objects.get(id=candidate_id)
            except ObjectDoesNotExist:
                raise err.ValidationError("Candidate not found!", 400)
            serializer = self.get_serializer(candidate_instance, data=self.request.data)
        else:
            serializer = self.get_serializer(data=self.request.data)
        try:
            serializer.is_valid(raise_exception=True)
            if candidate_id:
                self.perform_update(serializer)
                response = Response({"message": "Candidate timeslot updated."}, status=status.HTTP_200_OK)
            else:
                serializer.save()
                response = Response({"message": "Candidate timeslot created successfully."},
                                    status=status.HTTP_201_CREATED)
            return response
        except Exception as e:
            raise err.ValidationError(*(str(e), 400))


class InterviewerTimeSlotCreateUpdateView(CreateAPIView, UpdateAPIView):
    """
    API class to create/update interviewer timeslots
    """
    serializer_class = InterviewerTimeSlotSerializer

    def post(self, request, *args, **kwargs):
        interviewer_id = request.data.get('interviewer_id', None)
        if interviewer_id:
            try:
                interviewer_instance = InterviewerTimeSlot.objects.get(id=interviewer_id)
            except ObjectDoesNotExist:
                raise err.ValidationError("Interviewer not found!", 400)
            serializer = self.get_serializer(interviewer_instance, data=self.request.data)
        else:
            serializer = self.get_serializer(data=self.request.data)
        try:
            serializer.is_valid(raise_exception=True)
            if interviewer_id:
                self.perform_update(serializer)
                response = Response({"message": "Interviewer timeslot updated."}, status=status.HTTP_200_OK)
            else:
                serializer.save()
                response = Response({"message": "Interviewer timeslot created successfully."},
                                    status=status.HTTP_201_CREATED)
            return response
        except Exception as e:
            raise err.ValidationError(*(str(e), 400))


class InterviewScheduleTimeSlotsView(RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        candidate_id = request.query_params.get('candidate_id', None)
        interviewer_id = request.query_params.get('interviewer_id', None)
        if not CandidateTimeSlot.objects.filter(id=candidate_id).exists():
            raise err.ValidationError("Candidate not found!", 400)
        if not InterviewerTimeSlot.objects.filter(id=interviewer_id).exists():
            raise err.ValidationError("Interviewer not found!", 400)

        try:
            candidate_instance = CandidateTimeSlot.objects.get(id=candidate_id)
            interviewer_instance = InterviewerTimeSlot.objects.get(id=interviewer_id)

            candidate_start_time = candidate_instance.start_datetime
            candidate_end_time = candidate_instance.end_datetime
            interviewer_start_time = interviewer_instance.start_datetime
            interviewer_end_time = interviewer_instance.end_datetime

            if candidate_start_time.date() != interviewer_start_time.date():
                raise err.ValidationError("Date mismatch for the candidate and interviewer.", 400)

            if candidate_start_time < interviewer_start_time:
                start_time = interviewer_start_time.strftime("%H:%M")
            else:
                start_time = candidate_start_time.strftime("%H:%M")
            if candidate_end_time < interviewer_end_time:
                end_time = candidate_end_time.strftime("%H:%M")
            else:
                end_time = interviewer_end_time.strftime("%H:%M")

            timeslots = []
            time = datetime.datetime.strptime(start_time, '%H:%M')
            end = datetime.datetime.strptime(end_time, '%H:%M')
            while time < end:
                start_time = time.strftime("%H:%M")
                time += datetime.timedelta(hours=1)
                end_time = time.strftime("%H:%M")
                timeslots.append({"start_time": start_time, "end_time": end_time})

            data = {
                "candidate_name": candidate_instance.candidate_name,
                "interviewer_name": interviewer_instance.interviewer_name,
                "timeslots": timeslots
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            raise err.ValidationError(*(str(e), 400))
