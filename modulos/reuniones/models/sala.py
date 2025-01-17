

from odoo import models, fields, api


class Sala(models.Model):
    _name = 'reuniones.sala'
    _description = 'Salas'

    name = fields.Char(String = "Sala",required = True)
    descripcion = fields.Text(String = "Descripcion")
    reuniones = fields.Many2one('reuniones.reunion',string = "Sala Reunion", required = True, ondelete = 'cascade')


