LOGGING = {
        'version':1,
        'disable_existing_loggers':False,
        'formatters':{
            'production':{
                'format':'%(asctime)s [%(levelname)s] %(process)d %(thread)d '
                            '%(pathname)s:%(lineno)d %(message)s'
                },
            },
        'handlers':{
            'file':{
                'level':'INFO',
                'class':'logging.FileHandler',
                'filename':'/var/log/{}/app.log'.format(PROJECT_NAME),
                'formatter':'production',
                },
            },
        'loggers':{
            '':{
                'handlers':['file'],
                'level':'INFO',
                'propagate':False,
                },
            'django':{
                'handlers':['file'],
                'level':'INFO',
                'propagate':False,
                },
            },
        }
