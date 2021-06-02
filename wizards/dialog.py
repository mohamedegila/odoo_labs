# -*- coding: utf-8 -*-

from odoo import models, fields, api


class dialog(models.TransientModel):
    _name = 'dialog'
    _description = 'dialog'


    
    def createNewOrderWithSaveValues(self):
        self.ensure_one()
        id=self._context.get('active_ids', False)
        print("==========================")
        print(id)
        print("==========================")
        order = self.env["pharmacy.orders"].browse(self._context.get('active_ids', False))
        print("==========================")
        print (order.timestamp)
        print("==========================")
       
        customer = self.env['res.partner'].browse(order.customer.id)
        print("==========================")
        print (customer)
        print("==========================")

        newOrder = self.env['pharmacy.orders'].create({
            'timestamp': order.timestamp,
            'customer':customer.id,
            'total':order.total
            })
        for  lines in order.order_lines :
            medicine = self.env['pharmacy.pharmacy'].browse(lines.name.id)
            order = self.env['pharmacy.orders'].browse(newOrder.id)
            self.env['pharmacy.order_line'].create(
            {
                'name':medicine.id,
                'qty':lines.qty,
                'sub_total':lines.sub_total,
                'order': order.id
            }
        )
        