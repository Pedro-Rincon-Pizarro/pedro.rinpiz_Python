# -*- coding: utf-8 -*-
# from odoo import http


# class PrpDiscografia(http.Controller):
#     @http.route('/prp_discografia/prp_discografia', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prp_discografia/prp_discografia/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('prp_discografia.listing', {
#             'root': '/prp_discografia/prp_discografia',
#             'objects': http.request.env['prp_discografia.prp_discografia'].search([]),
#         })

#     @http.route('/prp_discografia/prp_discografia/objects/<model("prp_discografia.prp_discografia"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prp_discografia.object', {
#             'object': obj
#         })

