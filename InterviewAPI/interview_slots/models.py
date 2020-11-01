from datetime import datetime

from django.db import models

# Create your models here.


class TimeSlot(models.Model):
    """
    Model to store available timeslots
    """
    start_datetime = models.DateTimeField(default=datetime.now, null=False, blank=False)
    end_datetime = models.DateTimeField(default=datetime.now, null=False, blank=False)

    class Meta:
        verbose_name = "Time Slot"
        verbose_name_plural = "Time Slots"


class CandidateTimeSlot(TimeSlot):
    """
    Model to store available timeslots of Candidates
    """
    candidate_name = models.CharField(max_length=180, null=True, blank=True)

    class Meta:
        verbose_name = "Candidate Time Slot"
        verbose_name_plural = "Candidate Time Slots"

    def __str__(self):
        return self.candidate_name


class InterviewerTimeSlot(TimeSlot):
    """
    Model to store available timeslots of Interviewers
    """
    interviewer_name = models.CharField(max_length=180, null=True, blank=True)

    class Meta:
        verbose_name = "Interviewer Time Slot"
        verbose_name_plural = "Interviewer Time Slots"

    def __str__(self):
        return self.interviewer_name
