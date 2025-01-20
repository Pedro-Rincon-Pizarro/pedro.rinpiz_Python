#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Marca(models.Model):
    _name = 'garaje.marca'
    _description = 'garaje.marca'

    name = fields.Char(String ="Nombre de la marca" required = True)
    coches = fields.Many2one(String = "Coches" model = Coche)
