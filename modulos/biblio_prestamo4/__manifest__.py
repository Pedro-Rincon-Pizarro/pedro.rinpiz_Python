# -*- coding: utf-8 -*-
{
    'name': "Biblioteca de Prestamos",

    'summary': "Modulo para la gestion de los prestamos de la biblioteca",

    'description': """
En este módulo guardaremos la información necesaria para la gestión y prestamos de la biblioteca
    """,

    'author': "Pedro Rincón Pizarro",
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
        'views/pelicula_views.xml',
        'views/autor_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

