# -*- coding: utf-8 -*-
{
    'name': "Gimnasio",

    'summary': "Modulo para la gestión del gimnasio.",

    'description': """
En este módulo guardaremos la información necesaria para la gestión del gimnasio.
    """,

    'author': "Pedro Rincón",
    'website': "https://www.yourcompany.com",
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/suscripcion.xml',
        'views/clase.xml',
        'views/entrenador.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

