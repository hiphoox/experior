from django.http import HttpResponse 
from django.template import Context 
from django.template.loader import get_template 
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import gettext as _
from django.http import HttpResponseRedirect 
from django.contrib.auth import logout

def main_page(request): 
  variables = RequestContext(request, { 
    'user': request.user
  })
  
  return render_to_response( 
    'main.html', variables
  )
    
def activities_page(request): 
  variables = RequestContext(request, { 
    'activities_class': 'active'
  })
  return render_to_response( 
    'activities.html', variables
  )
  
def reports_page(request): 
  variables = RequestContext(request, { 
    'reports_class': 'active'
  })
  return render_to_response( 
    'reports.html', variables
  )

def misc_page(request): 
  variables = RequestContext(request, { 
    'misc_class': 'active'
  })
  return render_to_response( 
    'misc.html', variables
  )
  
def about_page(request): 
  variables = RequestContext(request, { 
    'about_class': 'active'
  })
  return render_to_response( 
    'about.html', variables
  )
  
def help_page(request): 
  variables = RequestContext(request, { 
    'help_class': 'active'
  })
  return render_to_response( 
    'help.html', variables
  )
  
def login_page(request): 
  variables = RequestContext(request, { 
    'login_class': 'active'
  })
  return render_to_response( 
    'login.html', variables
  )

def logout_page(request): 
  logout(request) 
  variables = RequestContext(request, { 
    'logged_out_class': 'active'
  })
  return render_to_response( 
    'logged_out.html', variables
  )
#  return HttpResponseRedirect('/') 

def account_page(request): 
  variables = RequestContext(request, { 
    'login_class': 'active'
  })
  return render_to_response( 
    'login.html', variables
  )
  