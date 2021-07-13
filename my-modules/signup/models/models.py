# -*- coding: utf-8 -*-

from datetime import date

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    mobile = fields.Char()
    reminder_question = fields.Char()
    reminder_answer = fields.Char()
    #last_name = fields.Char()
    #middle_name = fields.Char()
    #username = fields.Char()
