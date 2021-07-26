# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re
from num2words import num2words


class testone(models.Model):
    _name = "test.one"

    name = fields.Char(string="Name")
    