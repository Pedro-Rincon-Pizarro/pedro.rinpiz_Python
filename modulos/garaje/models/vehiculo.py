# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Vehiculo(models.AbstractModel):
    _name = 'garaje.vehiculo'


    matricula = fields.Char(String = "Matrícula" required = True)
    fecha_fabricacion = fields.Date(String = "Fecha de fabricación" required = True)
    propietario = fields.Many2one(String = "Propietario" help = "Contacto")
    kilometros = fields.Integer(String = "Kilómetros recorridos")
    antiguedad = fields.Integer(String = "Antigüedad")
    
    
    

    
