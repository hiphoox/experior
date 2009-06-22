import os, sys

#You need to set the path up before importing the WSGIHandler module
sys.path = ['/home/experior/webapps/django_trunk', '/home/experior/webapps/django_trunk/lib/python2.5'] + sys.path
sys.path.append('/home/experior/webapps/django_trunk/experior/')

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'experior.settings'
_application = WSGIHandler()

def application(environ, start_response): 
    '''FIX: https redirection broken. Hosting: webfactional. Webserver: Apache/mod_wsgi  
      This method was implemnented in order to get the https to work in the deployment server.
      We are forcing the use of https all the time. We can do that because at webfactional the hosting 
      site is configured to only acccept https requests. If we remove it all the POST operations will broke.
      This happens because webfactional doesn't set the wsgi.url_scheme enviroment flag. 
      If we change of hosting service we could remove it.'
      Reference: http://markmail.org/message/62cb2sdj54yey7qz#query:wsgi.url_scheme+page:1+mid:l72acuzuldfpmbdw+state:results
      Norberto Ortigoza. 
    '''
    environ['wsgi.url_scheme'] = 'https'
    environ['HTTPS'] = 'on'
    return _application(environ, start_response)
