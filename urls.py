# -*- coding: utf-8 -*-

from handlers import handlers


url_patterns = [
    (r"/", handlers.MainHandler),
    (r"/login", handlers.LoginHandler),
    (r"/signup", handlers.SignupHandler),
    (r"/connect/fitbit", handlers.FitbitConnectHandler),
    (r"/import/fitbit", handlers.FitbitImportHandler),
    (r"/push/fitbit", handlers.FitbitPushHandler),
    (r"/celery", handlers.CeleryTestHandler)
]