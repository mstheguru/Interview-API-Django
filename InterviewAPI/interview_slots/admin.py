from django.contrib import admin
from.models import CandidateTimeSlot, InterviewerTimeSlot, TimeSlot

# Register your models here.

admin.site.register(CandidateTimeSlot)
admin.site.register(InterviewerTimeSlot)
admin.site.register(TimeSlot)
