# -*- coding: utf-8 -*-
{
    'name': "Gestión de la sala de Reuniones",

    'summary': "Módulo para la gestión de las salas de reuniones de la empresa.",

    'description': """
        Módulo para la gestión de las salas de reuniones de la empresa.
    """,

    'author': "Pedro Rincon",
    'website': "https://www.yourcompany.com",

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
        'views/reunion_views.xml',
        'views/sala_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

