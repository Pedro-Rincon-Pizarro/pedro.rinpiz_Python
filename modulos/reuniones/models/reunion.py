

from odoo import models, fields, api


class Reunion(models.Model):
    _name = 'reuniones.reunion'
    _description = 'Reunion'

    name = fields.Char(string = "Reunión",required = True,)
    fecha_inicio = fields.Date(string = "Fecha de inicio")
    duracion = fields.Integer(string = "Duracion de la reunion", help = "Duración en dias")
    asientos = fields.Integer(string = "Numero de asientos")
    responsable = fields.Many2one('res.partner',string = "Responsable de la reunion")
    asistentes = fields.Many2many('res.partner', string = "Asistentes a la Reunión")
    asientos_ocupados = fields.Float(string = "Asientos ocupados", compute = "_asientos_ocupados")
    
    @api.depends('asientos_ocupados', 'asistentes')
    def _asientos_ocupados(self):
        for reunion in self:
            if not reunion.asientos:
                reunion.asientos_ocupados = 0.0
            else:
                reunion.asientos_ocupados = 100.0 * len(reunion.asistentes) / reunion.asientos


