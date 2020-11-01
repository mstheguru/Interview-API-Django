from django.urls import path

from interview_slots.views import CandidateTimeSlotCreateUpdateView, InterviewerTimeSlotCreateUpdateView, \
    InterviewScheduleTimeSlotsView


urlpatterns = [
    path('candidate_timeslot/create_or_update/', CandidateTimeSlotCreateUpdateView.as_view(),
         name="candidate-timeslot-create-update"),
    path('interviewer_timeslot/create_or_update/', InterviewerTimeSlotCreateUpdateView.as_view(),
         name="interviewer-timeslot-create-update"),
    path('available_timeslots/list/', InterviewScheduleTimeSlotsView.as_view(),
         name="available-timeslots-list"),
]
