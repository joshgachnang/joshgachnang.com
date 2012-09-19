""" Deployment of your django project.
"""

from fabric.api import *
import os

env.hosts = ['servercobra.com:6969']
env.user = "nang"

path = '/ebs/www/joshgachnang/test.joshgachnang.com/joshgachnang.com'

def update_django_project():
    """ Updates the remote django project.
    """
    with cd(path):
        sudo('git pull')
        with prefix('source ' + os.path.join(path, 'bin/activate')):
            sudo('pip install -r ' + os.path.join(path, 'requirements/requirements.txt'))
            sudo('python manage.py syncdb')
            sudo('python manage.py migrate') # if you use south
            sudo('python manage.py collectstatic --noinput')

def restart_webserver():
    """ Restarts remote nginx and uwsgi.
    """
    sudo("restart joshgachnang")
    sudo("/etc/init.d/nginx reload")

def deploy():
    """ Deploy Django Project.
    """
    update_django_project()
    restart_webserver()