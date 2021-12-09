from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    order_partner_car_id = fields.Many2one(related='order_id.car_id', store=True, string='Car', readonly=False)