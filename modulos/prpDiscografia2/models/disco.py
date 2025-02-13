from odoo import models, fields, api


class Disco(models.Model):
    _name = 'prp_discografia.disco'
    _description = 'prp_discografia.disco'

    titulo = fields.Char(string="Título", required= True)
    anno = fields.Integer(string="Año de lanzamiento", required= True, default= 1980)
    artista = fields.Many2one("prp_discografia_artista", string="Año de lanzamiento", required= True)
    generos = fields.Many2many("prp_discografia_generos", string="Géneros")
    portada = fields.Image(string="Portada")
    popularidad = fields.Selection([
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('muyAlta', 'Muy alta'),
        ('exito', 'Exito'),
        ],string="Popularidad", required= True, default='media')
    formatos = fields.Many2many('res.formato',string="Formatos")
    
    _sql_constraints =[
            ('titulo_anno_unico', 'UNIQUE(titulo, anno)', 'Ya existe un Disco con ese titulo y año.')
        ]

    @api.depends('titulo', 'anno')
    def titulo(self):
        for record in self:
            if record.titulo:
                    record.titulo =record.titulo + " (" + record.anno + ")"
            else:
                record.titulo =  "Sin título " + " (" + record.anno + ")"
                
    def name_search(self, name='', args=None, operator='ilike', limit=100):
         return super().name_search(name, args, operator, limit)
    
    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or [] # Nos aseguramos que tenemos args

        if not name: # Si no hay name (témino de búsqueda)
            return super().name_search(name, args, operator, limit)

        domain = [
            '|',
            ('titulo', operator, name),
            ('anno', operator, name)
        ]
        objetos = self.search(args + domain, limit=limit)

        return [(objeto.id, objeto.display_name) for objeto in objetos.sudo()]
            

