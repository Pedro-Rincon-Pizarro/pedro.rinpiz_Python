from odoo import models, fields, api
from odoo.exceptions import ValidationError


class gimnasio(models.Model):
    _name = 'gimnasio.clase'
    _description = 'gimnasio.clase'

    nombre = fields.Char(string="Nombre de la clase", required= True)
    capacidad_maxima = fields.Integer(string="Capacidad maxima", required= True)
    dia_semana = fields.Selection([
        ('L', 'Lunes'),
        ('M', 'Martes'),
        ('X', 'Miercoles'),
        ('J', 'Jueves'),
        ('V', 'Viernes'),
        ('S', 'Sabado'),
        ], string="Dia de la semana", required= True)
    hora_inicio = fields.Char(string="Hora de inicio", required= True)
    hora_fin = fields.Char(string="Hora de finalizacion", compute="_hora_fin")
    duracion = fields.Float(string="Duración", required= True, help="Duración en horas", default= 1)
    # enternador = fields.Many2one(string="Entrenador", required= True)
    # clientes = fields.Many2many(string="Clientes inscritos")
    display_name = fields.Char(string="Nombre a mostrar", compute="_compute_display_name", store=False)

    @api.depends('hora_fin')
    def _hora_fin(self):
        for record in self:
            record.hora_fin =  record.hora_inicio + record.duracion
            
    @api.constrains('duracion')
    def _calcular_duraciono(self):
        for gimnasio in self:
            if gimnasio.precio <= 0:
                raise ValidationError("La duración debe ser mayor que 0")
            
    @api.depends('nombre')
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.nombre if record.nombre else 'Sin nombre'