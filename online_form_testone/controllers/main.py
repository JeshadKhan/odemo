# -*- coding: utf-8 -*

from odoo import http, tools
from odoo.exceptions import ValidationError
from datetime import datetime, date, timedelta
import calendar
import math
import pytz
import io, base64
import os


class OnlineController(http.Controller):

    @http.route('/formnew/online', auth='public', website=True)
    def formnew_init(self, **kw):
        return http.request.render("online_form_testone.online_formnew", {})


    @http.route('/formnew/online/submit', website=True, auth='public', type='http', methods=['POST', 'GET'])
    def formnew_online_submit(self, **kw):
        print("=============")
        http.session_gc(self)

        _name = kw['first_name'] + " " + kw['middle_name'] + " " + kw['last_name']
        values = {
            'name': _name
        }

        testone = http.request.env['test.one'].sudo().create(values)
        print(testone)
        print("=============")

        return http.request.render("online_form_testone.formnew_successful", {})


    