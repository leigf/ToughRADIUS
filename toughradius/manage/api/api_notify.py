#!/usr/bin/env python
#coding=utf-8

import cyclone.auth
import cyclone.escape
import cyclone.web
import datetime
from toughradius.manage import models
from toughradius.manage.api.apibase import ApiHandler
from toughlib.permit import permit
from toughradius.manage.settings import * 
from toughlib import utils, apiutils

@permit.route(r"/api/notify")
class ExpireNotifyHandler(ApiHandler):

    def send_sms(self, req_msg):
        pass

    def send_mail(self, req_msg):
        pass

    def post(self):
        try:
            req_msg = self.parse_request()
        except Exception as err:
            return self.render_result(code=1, msg=utils.safeunicode(err.message))

        if 'sms' == req_msg['notify_type']:
            self.send_sms(req_msg)
        elif 'mail' == req_msg['notify_type']:
            self.send_mail(req_msg)


            