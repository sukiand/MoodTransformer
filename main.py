#!/usr/bin/env python

import web
import config
import app.controllers

URLS = (
        '/','app.controllers.base.index'
        )

if __name__ == "__main__":
    app = web.application(URLS, globals())
    app.run()
