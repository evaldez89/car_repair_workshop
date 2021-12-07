from odoo import fields, models


class PartnerCar(models.Model):
    _name = "res.partner.car"
    _description = "Partner Car"


    name = fields.Char(string="Licence Plate")
    owner_id = fields.Many2one("res.partner", string="Owner", required=True)
