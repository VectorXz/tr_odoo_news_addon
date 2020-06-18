# -*- coding: utf-8 -*-
{
    'name': "News Content Management",

    'summary': """
        This module is for managing news contents.""",

    'description': """
        This module is for managing news contents...
    """,

    'author': "Trinity Roots Co., Ltd.",
    'website': "http://www.trinityroots.co.th",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/news.xml',
        'views/category.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}