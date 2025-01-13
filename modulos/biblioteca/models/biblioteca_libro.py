# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Libro'

    name = fields.Char(string="Título", required=True, help="Introduce el titulo del libro")
    isbn = fields.Char(string="ISBN", required=True, help="Introduce el ISBN 13")
    precio = fields.Float(string="Precio", required=True)
    ejemplares = fields.Integer(string="Ejemplares")
    fecha = fields.Date(string="Fecha de compra")

