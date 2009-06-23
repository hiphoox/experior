from timetracking.models import *
from django.contrib import admin

class EmployeeAdmin(admin.ModelAdmin):
  date_hierarchy = 'contract_date'
  exclude = ('password',)
  list_display = ('username', 'email', 'first_name', 'last_name', 'telephone', 'region','is_staff', 'last_login')
  list_filter = ('has_passport', 'is_technical', 'is_Manager', 'region', 'is_active')
  save_on_top =  True
  search_fields = ['first_name']

#  list_editable = ('username', 'email', 'first_name', 'last_name', 'telephone', 'region', 'is_staff', 'last_login')
#  filter_vertical = ('first_name', 'last_name')
#  actions = 'delete_selected'  
#  fieldsets = (
#      (None, {
#          'fields': ('username')
#      }),
#      ('Personal Info', {
#          'classes': ('collapse',),
#          'fields': ( 'telephone', 'birth_date', 'has_passport', 'marital_status')
#      }),
#      ('Permissions', {
#          'classes': ('collapse',),
#          'fields': ('is_staff', 'is_active', 'is_superuser')
#      }),
#      ('Contract info', {
#          'classes': ('collapse',),
#          'fields': ('salary', 'contract_date', 'can_travel', 'english_level', 'region', 'is_Manager', 'is_technical')
#      }),
#  )
#('first_name', 'last_name'), 'email',


admin.site.register(Region)
admin.site.register(Currency)
admin.site.register(Sector)
admin.site.register(Activity)
admin.site.register(Category)
admin.site.register(WorkItem)
admin.site.register(ProjectType)
admin.site.register(ProjectStatus)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(WorkSession)
admin.site.register(Company)
admin.site.register(BusinessUnit)
admin.site.register(Project)
