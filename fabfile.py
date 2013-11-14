from __future__ import with_statement
from datetime import datetime
import os

import settings

from fabric.api import run, local, cd,\
                       env, abort,\
                       sudo, get, prompt, put


PROJECT_PATH = '~/work/sfst/src/sfst'

def qa():
    from settings.qa import DATABASES
    env.user = 'sfst'
    env.hosts = ['qa.securebookingshuttletours.com', ]
    env.DATABASE_USER = DATABASES['default']['USER']
    env.DATABASE_PASSWORD = DATABASES['default']['PASSWORD']
    env.DATABASE_HOST = DATABASES['default']['HOST']
    env.DATABASE_NAME = DATABASES['default']['NAME']

staging = qa    # alias!


def prod():
    from settings.prod import DATABASES
    env.user = 'sfst'
    env.hosts = ['booking.sanfranshuttletours.com', ]
    env.DATABASE_USER = DATABASES['default']['USER']
    env.DATABASE_PASSWORD = DATABASES['default']['PASSWORD']
    env.DATABASE_HOST = DATABASES['default']['HOST']
    env.DATABASE_NAME = DATABASES['default']['NAME']

def deploy(quick=False):
    with cd(PROJECT_PATH):
        run('git pull')
        if not quick:
            run('workon sfst; pip install -r requirements.pip')
        run('workon sfst; ./manage.py syncdb')
        run('workon sfst; ./manage.py migrate')
    restart()

launch = deploy # alias!

def quicklaunch():
    return launch(quick=True)


def pull_static():
    local('rsync -a sfst@qa.securebookingshuttletours.com:/home/sfst/work/sfst/src/sfst/static/ ./static')

# def memcache_restart():
#     run('killall memcached')
#     with cd('~/'): # /bin here errors out with command not found!
#         run('bin/memcache-start')


def loaddata():
    "Call all of the fixtures"
    local('workon sfst; ./manage.py loaddata dayofweek')
    local('workon sfst; ./manage.py loaddata option')
    local('workon sfst; ./manage.py loaddata optiongroup')
    local('workon sfst; ./manage.py loaddata setting')
    local('workon sfst; ./manage.py loaddata shop_config')
    local('workon sfst; ./manage.py loaddata site')
    local('workon sfst; ./manage.py loaddata siteskin')
    local('workon sfst; ./manage.py loaddata tourschedule')
    local('workon sfst; ./manage.py loaddata tourtype')

def restart():
    sudo('apache2ctl graceful')

def updatelocaldb():
    """
    Does a mysqldump, removes your local database, and restores the dump to your local db.
    So, to make your local database like production:

        fab prod updatelocaldb
    """
    # backup local db first
    local('mysqldump -uroot %s > ../db_backups/sfst_%s.dump' % (env.DATABASE_NAME, datetime.now().strftime('%Y-%m-%d-%H-%M')))
    run('mysqldump -u%(DATABASE_USER)s -p%(DATABASE_PASSWORD)s -h%(DATABASE_HOST)s %(DATABASE_NAME)s > /tmp/sfst.dump' % env)
    run('gzip /tmp/sfst.dump')
    get('/tmp/sfst.dump.gz', './sfst.dump.gz')
    # Not sure if this will work on everyone's environment...
    local('gunzip ./sfst.dump.gz')
    local('mysql -uroot -e "drop database sfst"')
    local('mysql -uroot -e "create database sfst"')
    local('mysql -uroot sfst < ./sfst.dump')

    # Cleanup
    run("rm /tmp/sfst.dump*")
    local("rm ./sfst.dump*")

# def pushlocaldb():
#     """
#     Commented out because this is scary when prod is setup
#     Does a mysqldump of your local database and pushes it to the server.
#     MAKE SURE YOU KNOW WHAT YOU ARE DOING =)
#     """
#     # backup remote db first
#     env['date'] = datetime.now().strftime('%Y-%m-%d-%H-%M')
#     run('mysqldump -u%(DATABASE_USER)s -p%(DATABASE_PASSWORD)s -h%(DATABASE_HOST)s %(DATABASE_NAME)s > /home/sfst/backups/sfst_%(date)s.dump' % env)
#     local('mysqldump -uroot sfst > /tmp/sfst.dump')
#     # run('mysqldump -u%(DATABASE_USER)s -p%(DATABASE_PASSWORD)s -h%(DATABASE_HOST)s %(DATABASE_NAME)s > /tmp/sfst.dump' % env)
#     local('gzip /tmp/sfst.dump')
#     put('/tmp/sfst.dump.gz', '/tmp/sfst.dump.gz')
#     run('gunzip /tmp/sfst.dump.gz')
#     run('mysql -u%(DATABASE_USER)s -p%(DATABASE_PASSWORD)s -h%(DATABASE_HOST)s %(DATABASE_NAME)s < /tmp/sfst.dump' % env)
#     # local('mysql -uroot -e "drop database sfst"')
#     # local('mysql -uroot -e "create database sfst"')
#     # local('mysql -uroot sfst < ./sfst.dump')
#
#     # Cleanup
#     run("rm /tmp/sfst.dump*")
#     local("rm /tmp/sfst.dump*")


def restore():
    dumps = local('ls ../db_backups/')
    print dumps
    dump = prompt("Which dump?")
    local('mysql -uroot -e "drop database sfst"')
    local('mysql -uroot -e "create database sfst"')
    local('mysql -uroot sfst < ../db_backups/%s' % dump)

def init():
    s = """
    export DJANGO_SETTINGS_MODULE='sfst.settings'
    export SERVER_IDENTIFIER='dev'
    alias run='/Users/sheats/www/sfst/manage.py runserver'
    alias runvm='sudo /Users/sheats/www/sfst/manage.py runserver 172.16.177.1:80'
    alias d='cd /Users/sheats/www/sfst/'
    alias db='mysql -uroot sfst'
    """
    local('echo "%s" > ~/.current_django_project' % s)
