from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    car_id = fields.Many2one(
        "res.partner.car",
        string="Car",
        required=True,
        domain="[('owner_id','=',partner_id)]",
    )

    def _get_top_service(self):
        self.env.cr.execute(
            """
            select
                product.name,
                product.default_code,
                sum(line.qty_invoiced) total_quantity,
                sum(line.price_total) total_amount
            from
                sale_order_line line
                join product_template product on product.id = line.product_id
            where
                line.invoice_status = 'invoiced'
            group by product.name, product.default_code
            order by total_quantity desc limit 1;
        """
        )

        top_service = self.env.cr.dictfetchall()
        return top_service[0] if top_service else {}

    def print_top_services(self):
        data = self._get_top_service()

        return self.env.ref('car_workshop.report_car_workshop_products').report_action(
            [], data=data
        )
