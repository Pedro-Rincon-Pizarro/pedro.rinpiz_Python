from odoo import models, fields, api
from odoo.exceptions import ValidationError


class gimnasio(models.Model):
    _name = 'gimnasio.suscripcion'
    _description = 'gimnasio.suscripcion'

    nombre = fields.Char(string="Nombre del plan", required= True)
    precio = fields.Float(string="Precio", required= True, help="Precio mensual de la suscripcion")
    duracion = fields.Integer(string="Duración", required= True, help="Duración en meses")
    # clientes = fields.One2many(string="Clientes", help="Clientes con esta suscripcion")
    #display_name = fields.Char(string="Nombre a mostrar", compute="_compute_display_name", store=False)
    _sql_constraints = [
        ('nombre_gim_unico', 'UNIQUE(nombre)', 'Ya existe un gimnasio con ese nombre.')
    ]


    @api.constrains('precio')
    def _calcular_precio(self):
        for gimnasio in self:
            if gimnasio.precio <= 0:
                raise ValidationError("El precio debe ser mayor que 0")
            
    @api.constrains('duracion')
    def _calcular_duraciono(self):
        for gimnasio in self:
            if gimnasio.precio <= 0:
                raise ValidationError("La duración debe ser mayor que 0")
            
    @api.depends('nombre')
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.nombre if record.nombre else 'Sin nombre'


