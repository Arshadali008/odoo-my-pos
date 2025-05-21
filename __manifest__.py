# -*- coding: utf-8 -*-
{
    'name': "My Pos",
    'version': '1.0',
    'depends': [ 'base', 'point_of_sale'],
    'website': "cybrosys:8018/odoo/pos",
    'author': "Alex",
    'category': 'All',
    'description': """
    Description text
    """,
    'data': [
        'views/res_config_settings.xml',
        'views/pos_config_views.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'assets': {
        'point_of_sale._assets_pos': [
            # 'custom_pos_receipt/static/src/js/custom_pos_receipt.js',
            'my_pos/static/src/xml/pos_card.xml',
            'my_pos/static/src/js/product_screen.js',
            'my_pos/static/src/js/product_card.js',
        ]
    },
}
