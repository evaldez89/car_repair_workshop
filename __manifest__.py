# -*- coding: utf-8 -*-
{
    'name': "Car Repair WorkShop",

    'summary': """
        Hanldle car repairment services""",

    'description': """
        This module will help you repair center go to the next level allowing you to
        handle the flow of a repair service programatically.

    """,

    'author': "Facturedo",
    'website': "https://facturedo.pe/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/repair_service_data.xml',
        'views/car_workshop_sale_order_view.xml',
        'report/most_demanded_services.xml',
        'report/car_services_report.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
