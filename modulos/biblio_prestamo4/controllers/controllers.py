# -*- coding: utf-8 -*-
# from odoo import http


# class BiblioPrestamo(http.Controller):
#     @http.route('/biblio_prestamo/biblio_prestamo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/biblio_prestamo/biblio_prestamo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('biblio_prestamo.listing', {
#             'root': '/biblio_prestamo/biblio_prestamo',
#             'objects': http.request.env['biblio_prestamo.biblio_prestamo'].search([]),
#         })

#     @http.route('/biblio_prestamo/biblio_prestamo/objects/<model("biblio_prestamo.biblio_prestamo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('biblio_prestamo.object', {
#             'object': obj
#         })

