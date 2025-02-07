from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Clase(models.Model):
    _name = 'gimnasio.clase'
    _description = 'gimnasio.clase'

    nombre = fields.Char(string="Nombre de la clase", required= True)
    capacidad_maxima = fields.Integer(string="Capacidad maxima", required= True)
    
    dia_semana = fields.Selection([
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miercoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sabado'),
        ], string="Dia de la semana", required= True)
    hora_inicio = fields.Float(string="Hora de inicio", required= True)
    hora_fin = fields.Float(string="Hora de finalizacion", compute="_hora_fin")
    duracion = fields.Float(string="Duración", required= True, help="Duración en horas", default= 1)
    entrenador = fields.Many2one("gimnasio.entrenador", string="Entrenador", required= True)
    # clientes = fields.Many2many(string="Clientes inscritos")
    #display_name = fields.Char(string="Nombre a mostrar", compute="_compute_display_name", store=False)

    @api.depends('hora_fin')
    def _hora_fin(self):
        for record in self:
            if record.hora_inicio and record.duracion:
                record.hora_fin = record.hora_inicio + record.duracion
            else:
                record.hora_fin = 0
            
    @api.constrains('duracion')
    def _check_duracion(self):
        for clase in self:
            if clase.duracion <= 0:
                raise ValidationError("La duración debe ser mayor que 0")
            
    @api.depends('nombre')
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.nombre or 'Sin nombre'