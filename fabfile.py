""" Deployment of your django project.
"""

from fabric.api import *
import os
import time


env.hosts = ['servercobra.com:6969']
env.user = "nang"

path = '/ebs/www/joshgachnang/test.joshgachnang.com/joshgachnang.com'

def put_files():
    put('joshgachnang/production_settings.py', os.path.join(path, 'joshgachnang/'),use_sudo=True)

def update_django_project():
    """ Updates the remote django project.
    """
    with cd(path):
        sudo('git stash')
        sudo('git pull')

def django_functions():
    with cd(path):
        with prefix('source ' + os.path.join(path, 'bin/activate')):
            sudo('pip install -r ' + os.path.join(path, 'requirements/requirements.txt'))
            sudo('python manage.py syncdb')
            #sudo('python manage.py migrate') # if you use south
            sudo('python manage.py collectstatic --noinput')

def update_permissions():
    with cd(path):
        sudo('chown -R joshgachnang ' + path)

def restart_webserver():
    """ Restarts remote nginx and uwsgi.
    """
    sudo("stop joshgachnang")
    # Give uwsgi time to shut down cleanly
    time.sleep(2)
    sudo("start joshgachnang")
   
    
    sudo("/etc/init.d/nginx reload")

def deploy():
    """ Deploy Django Project.
    """
    update_django_project()
    put_files()
    update_permissions()
    django_functions()
    restart_webserver()