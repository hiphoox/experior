from timetracking.models import *
from timetracking.widgets import *
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django import forms


############################################################################################################
#######################################   Catalogs Admin  ##################################################  
############################################################################################################
class CatalogAdmin(admin.ModelAdmin):
  list_filter = ('enabled',)
  save_on_top = True
  
admin.site.register(Region, CatalogAdmin)
admin.site.register(Currency, CatalogAdmin)
admin.site.register(Sector, CatalogAdmin)

admin.site.register(Activity, CatalogAdmin)
admin.site.register(Category, CatalogAdmin)
admin.site.register(WorkItem, CatalogAdmin)
admin.site.register(ProjectType, CatalogAdmin)
admin.site.register(ProjectStatus, CatalogAdmin)
admin.site.register(Application, CatalogAdmin)


############################################################################################################
#######################################   Employee Admin  ##################################################  
############################################################################################################
class CustomUserChangeForm(UserChangeForm):
  def __init__(self, *args, **kwargs):
    super(CustomUserChangeForm, self).__init__(*args, **kwargs)
    self.fields['first_name'].required = True
    self.fields['last_name'].required = True
    self.fields['email'].required = True


class EmployeeChangeForm(CustomUserChangeForm):  
  birth_date    = forms.DateField(required=False, widget=TTAdminDateWidget(), input_formats=('%Y-%m-%d',))
  contract_date = forms.DateField(initial=datetime.date.today, widget=TTAdminDateWidget(), input_formats=('%Y-%m-%d',))


class CustomUserAdmin(UserAdmin):
  form = CustomUserChangeForm


class EmployeeAdmin(admin.ModelAdmin):
  date_hierarchy = 'contract_date'
  exclude = ('password',)
  list_display = ('username', 'email', 'first_name', 'last_name', 'telephone', 'region','is_staff', 'last_login')
  list_filter = ('has_passport', 'is_technical', 'is_Manager', 'region', 'is_active')
  save_on_top =  True
  search_fields = ['first_name']
  actions = ['delete_selected']
  form = EmployeeChangeForm


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Employee, EmployeeAdmin)


############################################################################################################
#######################################   WorkSession Admin  ###############################################  
############################################################################################################
class WorkSessionChangeForm(forms.ModelForm):  
  work_date = forms.DateField(initial=datetime.date.today, widget=TTAdminDateWidget(), input_formats=('%Y-%m-%d',))

class WorkSessionAdmin(admin.ModelAdmin):
  date_hierarchy = 'work_date'
  list_filter = ('project', 'employee')
  save_on_top =  True
  actions = ['delete_selected']
  form = WorkSessionChangeForm

admin.site.register(WorkSession, WorkSessionAdmin)


############################################################################################################
#######################################   Company Admin  ################################################### 
############################################################################################################
class CompanyChangeForm(forms.ModelForm):  
  relationship_since = forms.DateField(initial=datetime.date.today, widget=TTAdminDateWidget(), input_formats=('%Y-%m-%d',))

class CompanyAdmin(admin.ModelAdmin):
  date_hierarchy = 'relationship_since'
  list_display = ('trade_name', 'legal_name')
  list_filter = ('sector',)
  save_on_top =  True
  search_fields = ['trade_name', 'legal_name']
  form = CompanyChangeForm

admin.site.register(Company, CompanyAdmin)


############################################################################################################
#######################################   BusinessUnit Admin  ############################################## 
############################################################################################################
class CompanyAdmin(admin.ModelAdmin):
  list_display = ('name', 'description', 'company', 'parent', 'enabled')
  list_filter = ('company',)
  save_on_top =  True
  search_fields = ['name', 'description']
  filter_vertical = ('company', 'parent')
  actions = 'delete_selected'  

admin.site.register(BusinessUnit)


############################################################################################################
#######################################   Project Admin  ################################################### 
############################################################################################################
class ProjectChangeForm(forms.ModelForm):  
  creation_date      = forms.DateField(required=False, widget=TTAdminDateWidget(), input_formats=('%Y-%m-%d',))
  request_date       = forms.DateField(required=False, initial=datetime.date.today, widget=TTAdminDateWidget(), input_formats=('%Y-%m-%d',))
  planned_start_date = forms.DateField(required=False, initial=datetime.date.today, widget=TTAdminDateWidget(), input_formats=('%Y-%m-%d',))
  real_start_date    = forms.DateField(required=False, widget=TTAdminDateWidget(), input_formats=('%Y-%m-%d',)) 
  planned_end_date   = forms.DateField(required=False, widget=TTAdminDateWidget(), input_formats=('%Y-%m-%d',)) 
  real_end_date      = forms.DateField(required=False, widget=TTAdminDateWidget(), input_formats=('%Y-%m-%d',))    

class ProjectAdmin(admin.ModelAdmin):
  date_hierarchy = 'creation_date'
  list_display  = ('name', 'description', 'external_id', 'creation_date', 'planned_start_date','enabled')
  list_filter   = ('customer',)
  save_on_top   =  True
  search_fields = ['name', 'description', 'external_id']
  actions       = 'delete_selected'  
  form          = ProjectChangeForm

admin.site.register(Project, ProjectAdmin)


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


