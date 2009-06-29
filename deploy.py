import os
deployment_server = "experior@experior.webfactional.com"
repository_path = "/home/experior/webapps/django_trunk/experior/"
ssh_key_file = "/home/experior/.ssh/id_rsa"
git_command = "/home/experior/bin/git"
#os.system("ssh experior@experior.webfactional.com 'cd /home/experior/webapps/django_trunk/experior/; eval `ssh-agent`; ssh-add /home/experior/.ssh/id_rsa; /home/experior/bin/git pull'")
os.system("ssh " + deployment_server + " 'cd " +  repository_path + "; eval `ssh-agent`; ssh-add " + ssh_key_file  +  "; " + git_command  + " pull'")
