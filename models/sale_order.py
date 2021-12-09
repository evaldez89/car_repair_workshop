from odoo import fields, models
from collections import defaultdict


class SaleOrder(models.Model):
    _inherit = "sale.order"

    car_id = fields.Many2one(
        "res.partner.car",
        string="Car",
        required=True,
        domain="[('owner_id','=',partner_id)]",
    )

    def _get_car_services_report_data(self):
        self.env.cr.execute(
            """
            select
                partner.name client,
                car.name licence,
                product.name service,
                sum(line.price_total) total_price,
                count(*)
            from
                sale_order_line line
                join res_partner_car car on car.id = line.order_partner_car_id
                join res_partner partner on partner.id = car.owner_id
                join product_template product on product.id = line.product_id
            group by car.name, product.name, partner.name
            order by count(*) desc;
        """
        )

        data = defaultdict(list)
        for car_service_data in self.env.cr.dictfetchall():
            data_key = f"{car_service_data.pop('licence')}-{car_service_data.pop('client')}"
            data[data_key].append({key: value for key, value in car_service_data.items()})

        return {"data": data}

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

    def print_car_services(self):
        data = self._get_car_services_report_data()

        return self.env.ref('car_workshop.report_car_services').report_action(
            [], data=data
        )
