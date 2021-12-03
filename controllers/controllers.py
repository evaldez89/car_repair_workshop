# -*- coding: utf-8 -*-
# from odoo import http


# class CardWorkshop(http.Controller):
#     @http.route('/card_workshop/card_workshop/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/card_workshop/card_workshop/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('card_workshop.listing', {
#             'root': '/card_workshop/card_workshop',
#             'objects': http.request.env['card_workshop.card_workshop'].search([]),
#         })

#     @http.route('/card_workshop/card_workshop/objects/<model("card_workshop.card_workshop"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('card_workshop.object', {
#             'object': obj
#         })
