# -*- coding: utf-8 -*-
{
    'name': "Discografia (Pedro Rincón)",

    'summary': "Módulo para gestionar artistas, discos y géneros musicales.",

    'description': """
Este módulo permite la gestión discográfica; la administración de géneros musicales, artistas (solistas y grupos), discos, etc.
    """,

    'author': "Pedro Rincón Pizarro",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/formatos.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

