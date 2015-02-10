#!/usr/bin/env python

import web

from config import view

class index:
    """Index Page"""
    def GET(self):
        """GET handler"""
        return view.index()
