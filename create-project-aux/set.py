import os
import sys
import re

PROJECT_NAME = sys.argv[1]

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

with open(f'{PROJECT_NAME}/settings.py') as settings:
    settings_str = settings.read()
    
    installed_apps_conf = re.search('INSTALLED_APPS = \[\n(.*\,\n)*', settings_str).group()
    installed_apps_conf_new = f'{installed_apps_conf}    \'core\'\n]'
    
    set_language = 'LANGUAGE_CODE = \'en-us\''
    set_language_new = 'LANGUAGE_CODE = \'pt-br\''

    set_time_zone = 'TIME_ZONE = \'UTC\''
    set_time_zone_new = 'TIME_ZONE = \'America/Sao_Paulo\''

    changes = {
        f'{installed_apps_conf}]': installed_apps_conf_new,
        set_language: set_language_new,
        set_time_zone: set_time_zone_new
    }

    settings_str_new = replace_all(settings_str, changes)

    # settings_str_new = settings_str_new.replace(f'{set_language}]', set_language_new)
    # settings_str_new = settings_str.replace(f'{installed_apps_conf}]', installed_apps_conf_new)
    
    
    settings.close()

with open(f'{PROJECT_NAME}/settings.py', 'w') as settings:
    settings.write(settings_str_new)
    settings.close()