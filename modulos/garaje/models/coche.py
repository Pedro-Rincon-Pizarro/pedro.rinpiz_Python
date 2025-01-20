# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Coche(models.Model):
    _name = 'garaje.coche'
    _inherit = 'garaje.vehiculo'

    name = fields.Char(String = "Nombre del modelo" required = True)
    color = fields.Char(String = "Color" required = True)
    puertas = fields.Integer(String = "Número de puertas")
    tipo_motor = fields.Selection(
        String = "Tipo de motor"
        selection=[
            ('gasolina', 'Gasolina'),
            ('diesel', 'Diesel'),
            ('electrico', 'Electrico'),
            ('hibrido', 'Hibrido'),
            
        ],
        string="Estado",
        default='gasolina',  # Valor por defecto
        required=True        # Obligatorio
    )
    marca = fields.Many2one(String = "Marca" required = True model = Marca ondelete = 'cascade')

