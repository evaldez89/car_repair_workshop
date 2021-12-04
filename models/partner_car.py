from odoo import fields, models


class PartnerCar(models.Model):
    _name = "res.partner.car"
    _description = "Partner Car"

    licence_plate = fields.Char(string="Licence Plate")
    owner_id = fields.Many2one("res.partner", string="Owner", required=True)
