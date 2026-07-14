from django.contrib import admin
from .models import JobCard, JobCardService


class JobCardServiceInline(admin.TabularInline):
    model = JobCardService
    extra = 1


@admin.register(JobCard)
class JobCardAdmin(admin.ModelAdmin):
    inlines = [JobCardServiceInline]