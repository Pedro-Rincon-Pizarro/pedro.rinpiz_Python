from odoo import models, fields, api


class Entrenador(models.Model):
    _name = 'gimnasio.entrenador'
    _description = 'gimnasio.entrenador'

    nombre = fields.Char(string="Nombre", requuired= True)
    apellido_1 = fields.Char(string="Primer apellido", required= True)
    apellido_2 = fields.Char(string="Segundo apellido")
    dni = fields.Char(string="DNI", required= True)
    email = fields.Char(string="Correo electrónico", required= True)
    telefono = fields.Char(string="Teléfono")
    clases = fields.One2many("gimnasio.clase", "entrenador", string="Clases que imparte")
    
    #display_name = fields.Char(string="Nombre a mostrar", compute="_compute_display_name", store=False)
    _sql_constraints = [
        ('dni_entrenador_unico', 'UNIQUE(nombre)', 'Ya existe un entrenador con ese DNI.')
    ]

    @api.depends('dni')
    def _check_dni(self):
        for record in self:
            letras_validas = 'TRWAGMYFPDXBNJZSQVHLCKE'
        
        if len(self.dni) != 9:
            return False
            
        dni = self.dni.upper()
        numeros = dni[:8]
        letra = dni[8]

        if not numeros.isdigit() or not letra.isalpha():
            return False

        try:
            numero = int(numeros)
            return letras_validas[numero % 23] == letra
        except:
            return False
            
            
    @api.depends('nombre')
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.nombre if record.nombre else 'Sin nombre'