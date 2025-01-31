#-*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class Autor(models.Model):
    _name = 'biblio_prestamo.autor'
    _description = 'biblio_prestamo.autor'

    name = fields.Char(string = "Nombre completo", compute = "_calcular_name", store= True)
    nombre = fields.Char(string="Nombre", required=True)
    apellido_1 = fields.Char(string="Primer Apellido", required=True)
    apellido_2 = fields.Char(string="Segundo Apellido")
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
    fecha_muerte = fields.Date(string="Fecha de muerte")
    fotografia = fields.Image(string="Fotografía")
    nacionalidad = fields.Many2one("res.country", string="Nacionalidad")
    es_escritor = fields.Boolean(string="Es Escritor")
    es_director = fields.Boolean(string="Es Director")

    @api.depends('apellido_1','apellido_1','nombre')
    def _calcular_name(self):
        for autor in self:
            if autor.apellido_2:
                autor.name = f"{autor.apellido_1 or 'apellido1'} {autor.apellido_2 or 'apellido2'}, {autor.nombre or 'Nombre'}"
            else:
                autor.name = f"{autor.apellido_1 or 'apellido1'}, {autor.nombre or 'Nombre'}"
                
    

    @api.constrains('fecha_nacimiento')
    def _check_fecha_nacimiento(self):
        
        today = date.today()
        for autor in self:
            if autor.fecha_nacimiento >= today:
                raise ValueError("La fecha debe ser inferior a hoy")
            


    @api.constrains('fecha_muerte')
    def _check_fecha_muerte(self):
        today = fields.date.today()
        for autor in self:
            if autor.fecha_muerte > today:
                raise ValueError("La fecha debe ser inferior a hoy")
            elif autor.fecha_muerte < autor.fecha_nacimiento:
                raise ValueError("La fecha de muerte debe ser superior a la fecha de nacimiento")
            

            