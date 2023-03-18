"""In this model used to  creating a delivery order in invoice and in this
model write a two function delivery_order is a  redirect to
delivery and function _compute_delivery_count will use to calculation of count"""

from odoo import models, fields


class DeliveryOrderInvoice(models.Model):
    _inherit = 'account.move'
    _description = 'Account Move'

    delivery = fields.Integer(string='Delivery',
                              compute='_compute_delivery_count')

    def delivery_order(self):
        """This delivery_order function will use to redirect
        to delivery order of corresponding sale order"""
        self.ensure_one()
        sales_id = self.invoice_line_ids.sale_line_ids.order_id
        # sale_id will represent corresponding sale order of self
        return {
            'type': 'ir.actions.act_window',
            'name': 'delivery Order',
            'view_mode': 'tree,form',
            'res_model': 'stock.picking',
            'domain': [('sale_id', '=', sales_id.id)],
        }

    def _compute_delivery_count(self):
        """_compute_delivery_count function will represent computing
        the delivery count of corresponding sale order"""
        sales_id = self.invoice_line_ids.sale_line_ids.order_id
        self.delivery = self.env['stock.picking'].search_count(
            [('sale_id', '=', sales_id.id)])
