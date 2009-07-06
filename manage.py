#!/usr/bin/env python
from django.core.management import execute_manager
try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

# Custome operations
# By Norberto Ortigoza
import os, sys 
deployment_server = "experior@experior.webfactional.com"
repository_path = "/home/experior/webapps/django_trunk/experior/"
ssh_key_file = "/home/experior/.ssh/id_rsa"
git_command = "git pull"
rebuild_remote_command = "manage.py rebuild_db; restart"
# The -t option allows direct interaction with the command's execution (passphrase entry)
remote_initialitation = "ssh -t " + deployment_server + " 'source .bash_profile; cd " +  repository_path + "; eval `ssh-agent`; ssh-add " + ssh_key_file  +  "; "

if len(sys.argv)  > 1:
  operation = sys.argv[1]
else:
  operation = ''
  
if operation == "rebuild_db":
  print "Rebuilding local DB:"
  os.system("rm experior.db")
  os.system("manage.py syncdb")

elif operation == "deploy": 
  print "Deploying local DB:"
  os.system("git push")
  os.system(remote_initialitation + git_command + "'")

elif operation == "rebuild_remote": 
  print "Rebuilding remote server:"
  os.system(remote_initialitation + rebuild_remote_command + "'")

else:
  if __name__ == "__main__":
      execute_manager(settings)
