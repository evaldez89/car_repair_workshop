from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    car_id = fields.Many2one(
        "res.partner.car",
        string="Car",
        rquired=True,
        domain="[('owner_id','=',partner_id)]",
    )

    def _get_top_service(self):
        self.env.cr.execute(
            """
            select
                product.name,
                product.default_code,
                sum(line.quantity) total_quantity,
                sum(line.price_total) total_amount
            from
                account_move move
                join account_move_line line on line.move_id = move.id
                join product_template product on product.id = line.product_id
            where
                move.type = 'out_invoice'
                and move.invoice_payment_state = 'paid'
                and line.product_id is not null
            group by product.name, product.default_code
            order by total_quantity desc limit 1
        """
        )

        top_service = self.env.cr.dictfetchall()
        return top_service[0] if top_service else {}

    def print_top_services(self):
        data = self._get_top_service()

        return self.env.ref('car_workshop.report_car_workshop_products').report_action(
            [], data=data
        )
