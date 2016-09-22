#!/bin/bash
export DJANGO_SETTINGS_MODULE=settings.aws-i-13afa98c_production_settings
. /home/akwada/Env/zeroanda/bin/activate
cd /home/project/zeroanda/serverside/production
python manage.py execute_process