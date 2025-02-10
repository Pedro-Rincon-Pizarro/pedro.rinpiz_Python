from odoo import models, fields, api


class Artista(models.Model):
    _name = 'prp_discografia.artista'
    _description = 'prp_discografia.artista'

    foto = fields.Image(string="Fotografía")
    tipo = fields.Selection(
        ('solista', 'Solista'),
        ('grupo', 'Grupo'),
        string="Tipo", 
        required= True, 
        default='grupo')
    nombre_artistico = fields.Char(string="Nombre artístico", required= True)
    nombre_completo = fields.Char(string="Nombre completo", compute= '_calcular_nombre_completo')
    nombre = fields.Char(string="Nombre")
    apellido_1 = fields.Char(string="Primer apellido")
    apellido_2 = fields.Char(string="Segundo apellido")
    pais = fields.Many2one('res.country', string="País", required = True)
    es_activo =fields.Boolean(string="En activo", required= True, default = True)
    anno_inicio = fields.Integer(string="Año de inicio", required= True, help = "Año de formación o de inicio de actividad", default= 1980)
    anno_fin = fields.Integer(string="Año de fin", help="Año de disolución o de fin de actividad")
    annos_carrera = fields.Integer(string="Años en activo")
    bio = fields.Html(string="Biografía")
    discos = fields.One2many('prp_discografia.disco', string="Discos", required= True)
    
    _sql_constraints =[
            ('nombre_artistico_unico', 'UNIQUE(nombre_artistico)', 'Ya existe un Artista con ese nombre artistico.')
        ]

    @api.depends('nombre', 'apellido_1', 'apellido_2', 'tipo')
    def _calcular_nombre_completo(self):
        for record in self:
            if record.tipo == "solista":
                if record.apellido_2:
                    record.nombre_completo =record.apellido_2 + ", " + record.nombre + " " + record.apellido_1
                else:
                    record.nombre_completo = record.nombre + " " + record.apellido_1      
            else:
                record.nombre_completo = ""
                
    @api.depends('nombre', 'apellido_1', 'apellido_2', 'nombre_artistico')
    def _compute_display_name(self):
        for record in self:
            if record.tipo == "solista":
                if record.apellido_2:
                    record.nombre_artistico =record.nombre_artistico + "( " + record.apellido_2 + ", " + record.nombre + " " + record.apellido_1
                else:
                    record.nombre_artistico = record.nombre_artistico + "( " + record.apellido_1
                
    @api.constrains('anno_inicio', 'annio_fin')
    def _calculo_annos(self):
        for record in self:
            if record.anno_inicio and record.anno_fin and record.anno_inicio < record.anno_fin:
                record.annos_carrera = record.anno_fin - record.anno_inicio
                
    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or [] # Nos aseguramos que tenemos args

        if not name: # Si no hay name (témino de búsqueda)
            return super().name_search(name, args, operator, limit)

        domain = [
            '|',
            ('nombre_artistico', operator, name),
            ('nombre_completo', operator, name)
        ]
        objetos = self.search(args + domain, limit=limit)

        return [(objeto.id, objeto.display_name) for objeto in objetos.sudo()]