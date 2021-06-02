# -*- coding: utf-8 -*-

from odoo import models, fields, api


class orders(models.Model):
    _name = 'pharmacy.orders'
    _description = 'pharmacy.orders'

    customer = fields.Many2one('res.partner')
    order_lines = fields.One2many("pharmacy.order_line","order")
    total = fields.Float(compute='_compute')
    # date = fields.Date()
    timestamp= fields.Datetime()

    @api.onchange('order_lines')
    def _compute(self):
        for line in self:
            t = 0
            for i in line.order_lines:
                t = t+i.sub_total
            line.total = t

  