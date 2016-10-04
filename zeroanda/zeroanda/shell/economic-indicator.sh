#!/bin/bash
export DJANGO_SETTINGS_MODULE=settings.practice_settings
. /home/akwada/Env/zeroanda/bin/activate
cd /home/project/zeroanda-serverside/zeroanda
python manage.py get_weekly_economic_indicator