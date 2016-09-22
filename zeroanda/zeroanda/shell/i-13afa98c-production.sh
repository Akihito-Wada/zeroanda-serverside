#!/bin/bash
export DJANGO_SETTINGS_MODULE=settings.aws-i-13afa98c_production_settings
. /home/akwada/Env/zeroanda/bin/activate
cd /home/project/zeroanda/server/production/zeroanda
python manage.py execute_process

