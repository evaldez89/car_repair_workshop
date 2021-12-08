from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    car_id = fields.Many2one(
        "res.partner.car",
        string="Car",
        rquired=True,
        domain="[('owner_id','=',partner_id)]",
    )

    def print_top_services(self):
        self.env['account.move.line']
        product_ids = self.env['product.product'].search(
            [
                (
                    'categ_id',
                    '=',
                    self.env.ref('car_workshop.product_category_repair_service').id,
                )
            ]
        )

        return self.env.ref('car_workshop.report_car_workshop_products').report_action(
            [], data={'name': 'Emmanuel Valdez', 'extras': {'age': 32}}
        )
