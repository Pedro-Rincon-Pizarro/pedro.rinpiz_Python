# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Pelicula(models.Model):
    _name = 'biblio_prestamo.pelicula'
    _description = 'Biblioteca Película'

    name = fields.Char(string="Ref.", compute = "_calcular_name", store= True)
    titulo = fields.Char(string="Título", required= True, help="Introduce el título de la pelicula")
    directores = fields.Many2many("biblio_prestamo.autor", string="Director/es", required= True)
    productora = fields.Char(string="Productora")
    paises_origen = fields.Many2many("res.country", string="País/es de origen")
    anno_estreno = fields.Integer(string="Año de estreno", required= True, default= fields.Date.today().year) 
    duracion = fields.Integer(string="Duración", required= True, help="Duración en minutos", default= "90", )
    clasificacion_edad = fields.Selection([
        ('A', 'Para todos los públicos'),
        ('+7', 'Mayores de 7'),
        ('+12', 'Mayores de 12'),
        ('+16', 'Mayores de 16'),
        ('+18', 'Mayores de 18'),
        ], string="Clasificación por edades", required= True)
    portada =fields.Image(string="Portada")
    _sql_constraints = [
    ('titulo_anno_estreno_unico', 'UNIQUE(titulo, anno_estreno)', 'Ya existe una película con ese título y año de estreno.')
]


    @api.depends('titulo','anno_estreno')
    def _calcular_name(self):
        for pelicula in self:
            if pelicula.titulo:
                pelicula.name = f"{pelicula.titulo}  {pelicula.anno_estreno}"
            else:
                pelicula.name = f" Sin título  {pelicula.anno_estreno}"
                
    @api.constrains('duracion')
    def _calcular_duracion(self):
        for pelicula in self:
            if pelicula.duracion <= 0:
                raise ValidationError("La duración debe ser mayor que 0")
            
            
    