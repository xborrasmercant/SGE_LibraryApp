# -*- coding: utf-8 -*-
{
    'name': "Gestió de Biblioteca",

    'summary': """
        Gestió del cataleg de la biblioteca i els prestecs dels llibres""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Xavier Borrás Mercant",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Library',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/library_menu.xml',
        'security/library_security.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
