from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    car_id = fields.Many2one(
        "res.partner.car",
        string="Car",
        rquired=True,
        domain="[('owner_id','=',partner_id)]",
    )
