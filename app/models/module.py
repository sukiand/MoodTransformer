#/!usr/bin/env python
"""module.py
design classes for mysql
"""

import web

from config import DB

class Course(object):
    """course entity"""
    GATEGORY = [ 'CORE_TECH',
                 'ELEC_TECH',
                 'POLICY',
                 'MANAGEMENT',
                 'HEALTH']
    SEMESTER = [ 'fall',
                 'spring']
    def __init__(self, course_no, semester, name, professor, category):
        self.course_no = course_no
        assert(semester in self.SEMESTER), "invalid semester"
        self.semester = semester
        self.name = name
        self.professor = professor
        assert(category in self.CATEGORY), "invalid semester"
        self.category = category

    def insert(self):
        DB.
