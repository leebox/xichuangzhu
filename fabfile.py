from fabric.api import run, env, cd, prefix
from xichuangzhu import config


def deploy():
    env.host_string = config.HOST_STRING
    with cd('/var/www/xichuangzhu'):
        run('git pull')
        run('bower install --allow-root')
        with prefix('source venv/bin/activate'):
            run('pip install -r requirements.txt')
        run('supervisorctl restart xcz')


def restart():
    env.host_string = config.HOST_STRING
    run('supervisorctl restart xcz')