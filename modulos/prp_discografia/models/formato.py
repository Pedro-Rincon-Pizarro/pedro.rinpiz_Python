from odoo import models, fields, api


class Formato(models.Model):
    _name = 'prp_discografia.formato'
    _description = 'prp_discografia.formato'

    nombre = fields.Char(string="Nombre", required= True)
    es_fisico = fields.Boolean(string="Es Fisico", required= True)

    _sql_constraints =[
            ('nombre_genero_unico', 'UNIQUE(nombre)', 'Ya existe un Genero con ese Nombre.')
        ]

    @api.depends('nombre')
    def _compute_display_name(self):
        for record in self:
            if record.nombre:
                record.nombre = record.nombre or "Sin nombre"
                
                
    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or [] # Nos aseguramos que tenemos args

        if not name: # Si no hay name (témino de búsqueda)
            return super().name_search(name, args, operator, limit)

        domain = [
            ('nombre', operator, name),
        ]
        objetos = self.search(args + domain, limit=limit)

        return [(objeto.id, objeto.display_name) for objeto in objetos.sudo()]

