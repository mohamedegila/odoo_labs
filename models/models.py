# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pharmacy(models.Model):
    _name = 'pharmacy.pharmacy'
    _description = 'pharmacy.pharmacy'
    name = fields.Text()
    price = fields.Integer()
    manufactor = fields.Text()
    description = fields.Text()

    
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
