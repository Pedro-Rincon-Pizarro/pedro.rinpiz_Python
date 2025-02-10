from odoo import models, fields, api


class Genero(models.Model):
    _name = 'prp_discografia.genero'
    _description = 'prp_discografia.genero'

    nombre = fields.Char(string="Nombre", required = True)
    descripcion = fields.Text(string="Descripción")

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


