config.fab_hosts = ['experior@experior.webfactional.com'] 
def deploy(): 
    local("gh push") 
    run("cd /home/experior/webapps/django_trunk/experior/") 
    run("gh pull") 
    sudo("restart")