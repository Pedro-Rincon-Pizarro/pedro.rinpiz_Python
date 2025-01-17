# -*- coding: utf-8 -*-
# from odoo import http


# class Reuniones(http.Controller):
#     @http.route('/reuniones/reuniones', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reuniones/reuniones/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('reuniones.listing', {
#             'root': '/reuniones/reuniones',
#             'objects': http.request.env['reuniones.reuniones'].search([]),
#         })

#     @http.route('/reuniones/reuniones/objects/<model("reuniones.reuniones"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reuniones.object', {
#             'object': obj
#         })

