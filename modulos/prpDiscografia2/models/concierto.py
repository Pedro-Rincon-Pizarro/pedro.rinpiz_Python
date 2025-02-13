from odoo import models, fields, api
from datetime import datetime


class Concierto(models.Model):
    _name = 'prp_discografia.concierto'
    _description = 'prp_discografia.concierto'

    titulo = fields.Char(string="Título", required= True)
    fecha = fields.Datetime(string="Fecha y hora", required= True)
    ubicacion = fields.Char(string="Ubicación", required= True, help="Lugar donde se realiza el concierto")
    pais = fields.Many2one("res.country",string="País", required= True)
    estado = fields.Selection([
        ("programado", "Programado"),
        ("realizado", "Realizado"),
        ("cancelado", "Cancelado"),
        ], string="Estado", required= True, default= "programado")
    artistas = fields.Many2many("prp_discografia.artista",string="Artistas participantes", required= True)
    aforo = fields.Integer(string="Aforo maximo", help="Capacidad máxima del lugar")
    entradas_vendidas = fields.Integer(string="Entradas vendidas", default= 0)
    entradas_disponibles = fields.Float(string="Entradas disponibles", compute= "_compute_entradas_disponibles")
    precio = fields.Float(string="Precio", required= True, default= 30.0)
    recaudacion = fields.Float(string="Recaudación", compute= "_compute_recaudacion")


    @api.depends('aforo', 'entradas_vendidas')
    def _compute_entradas_disponibles(self):
        for concierto in self:
            if concierto.entradas_vendidas and concierto.aforo:
                concierto.entradas_disponibles = ((concierto.aforo - concierto.entradas_vendidas) *100) / concierto.aforo

    @api.depends('entradas_vendidas', 'precio')
    def _compute_recaudacion(self):
        for concierto in self:
            if concierto.entradas_vendidas and concierto.precio:
                concierto.recaudacion = concierto.entradas_vendidas * concierto.precio

    @api.depends('titulo', 'fecha')
    def _compute_display_name(self):
        for concierto in self:
            if concierto.titulo and concierto.fecha:
                concierto.display_name = concierto.titulo + " (" + concierto.fecha.now.strftime("%Y-%m-%d %H:%M") + ")" or "Sin Titulo"
                
    @api.constrains('entradas_vendidas', 'aforo')
    def _check_entradas_vendidas_menor_aforo(self):
        for concierto in self:
            if concierto.entradas_vendidas > concierto.aforo:
                raise ValueError("Las entradas vendidas deben ser menor o igual al aforo")
            
    @api.constrains('precio')
    def _check_precio_no_negativo(self):
        for concierto in self:
            if concierto.precio < 0:
                raise ValueError("El precio no puede ser inferior a 0")
    
    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or [] # Nos aseguramos que tenemos args

        if not name: # Si no hay name (témino de búsqueda)
            return super().name_search(name, args, operator, limit)

        domain = [
            '|',
            ('titulo', operator, name),
            ('fecha', operator, name)
        ]
        objetos = self.search(args + domain, limit=limit)

        return [(objeto.id, objeto.display_name) for objeto in objetos.sudo()]