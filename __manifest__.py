{
    'name': 'Credit Limit Module',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Manage credit limits for customers',
    'depends': ['base', 'sale', 'account', 'stock'],
    'data': [
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': True,
}