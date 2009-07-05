#!/usr/bin/env python
#
# Original string command:
# ssh -t experior@experior.webfactional.com 'cd /home/experior/webapps/django_trunk/experior/; eval `ssh-agent`; ssh-add /home/experior/.ssh/id_rsa; /home/experior/bin/git pull'
#
# TODO: This script needs a lot of refactoring. 
# We have to include:
# 1) Optional server restart
# 2) A better command string construction. Currently it is a mess!
# 3) Document the execution flow 
#
# Author: Norberto Ortigoza
# 
import os, sys 
deployment_server = "experior@experior.webfactional.com"
repository_path = "/home/experior/webapps/django_trunk/experior/"
ssh_key_file = "/home/experior/.ssh/id_rsa"
git_command = "/home/experior/bin/git"

operation = sys.argv[1]

if operation == "resetdb":
  print "Reseting DB:"
  os.system("rm experior.db")
  os.system("manage.py syncdb")

elif operation == "server": 
  os.system("git push")
  #The -t option allows direct interaction with the command's execution (passphrase entry)
  os.system("ssh -t " + deployment_server + " 'cd " +  repository_path + "; eval `ssh-agent`; ssh-add " + ssh_key_file  +  "; " + git_command  + " pull'")

else:
  print "Operations availables: resetdb : server"