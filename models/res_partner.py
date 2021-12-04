from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    car_ids = fields.One2many('res.partner.car', 'owner_id', string='Cars', ondelete='cascade')
