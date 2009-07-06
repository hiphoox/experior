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
  birth_date    = forms.DateField(widget=TTAdminTimeWidget(), input_formats=('%Y-%m-%d',))
  contract_date = forms.DateField(widget=TTAdminTimeWidget(), input_formats=('%Y-%m-%d',))


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
  work_date = forms.DateField(widget=TTAdminTimeWidget(), input_formats=('%Y-%m-%d',))

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
  relationship_since = forms.DateField(widget=TTAdminTimeWidget(), input_formats=('%Y-%m-%d',))

class CompanyAdmin(admin.ModelAdmin):
  date_hierarchy = 'relationship_since'
  list_display = ('trade_name', 'legal_name')
  list_filter = ('sector',)
  save_on_top =  True
  search_fields = ['trade_name', 'legal_name']
  form = CompanyChangeForm

admin.site.register(Company, CompanyAdmin)

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


admin.site.register(BusinessUnit)
admin.site.register(Project)
