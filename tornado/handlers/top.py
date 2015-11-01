# -*- coding: utf-8 -*-
from base import BaseHandler
from MyModel import MyModel

import logging
app_log = logging.getLogger("tornado")

class TopHandler(BaseHandler):

    def get(self):

        self.render("index.html")

    def post(self):
        pass
