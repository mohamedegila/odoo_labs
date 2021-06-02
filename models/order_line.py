# -*- coding: utf-8 -*-

from odoo import models, fields, api


class order_line(models.Model):
    _name = 'pharmacy.order_line'
    _description = 'pharmacy.order_line'
    name = fields.Many2one('pharmacy.pharmacy','Pharmacy')
    qty = fields.Integer()
    sub_total = fields.Float(compute='_compute')
    order = fields.Many2one('pharmacy.orders')

    @api.onchange('qty')
    def _compute(self):
        for line in self:
            line.sub_total = ( line.name.price * line.qty)


  