{
    'name': 'Kanhasoft Bulk Invoice Delete',
    'version': '19.0.1.0.0',
    'summary': 'Bulk force delete invoices from tree view',
    'author': 'Kanhasoft',
    'website': 'https://kanhasoft.com',
    'category': 'Accounting',
    'depends': ['account'],
    'license' : 'OPL-1',
    'data': [
        'security/ir.model.access.csv',
        'views/account_move_views.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': False,
}