#!/usr/bin/env python
"""config.py
This is the file that saves all kinds of configures.
"""
import web

# Database setting
DB_TYPE = 'mysql'
DB_NAME = 'yyassistant'
DB_USER = 'sukiand'
DB_PWD = '3214664'
DB = web.database(dbn=DB_TYPE, db=DB_NAME, user=DB_USER, passwd=DB_PWD, charset=None)

TB_STUDENT = 'student'
TB_COURSE = 'course'

# Webpage setting
TITLE = 'Course Assistant'
BRAND = 'Course Assistant'

# server setting
web.config.debug = True

GLOBALS = {
        'title': TITLE,
        'brand': BRAND
        }

view = web.template.render('app/views/', base = 'base', globals=GLOBALS)
