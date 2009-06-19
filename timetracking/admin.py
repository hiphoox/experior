from timetracking.models import *
from django.contrib import admin

class WorkSessionAdmin(admin.ModelAdmin):
  list_display = ('',)
  search_fields = ('',)

admin.site.register(Region)
admin.site.register(Currency)
admin.site.register(Sector)
admin.site.register(Activity)
admin.site.register(Category)
admin.site.register(WorkItem)
admin.site.register(ProjectType)
admin.site.register(ProjectStatus)
admin.site.register(Employee)
admin.site.register(WorkSession)
admin.site.register(Company)
admin.site.register(BusinessUnit)
admin.site.register(Project)