from django.contrib import admin
from .models import Project,Task


class ProjectAdmin(admin.ModelAdmin):
    list_display =('title','description','start_date','end_date','owner')

admin.site.register(Project,ProjectAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display=('title','description','priority','due_date','status','project','assigned_to')

admin.site.register(Task,TaskAdmin)



