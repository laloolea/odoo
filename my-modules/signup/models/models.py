# -*- coding: utf-8 -*-

from odoo import fields, models


class ResUser(models.Model):
    _inherit = "res.partner"
    birthday = fields.Date()
    age = fields.Char()


