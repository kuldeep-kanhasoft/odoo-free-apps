{
    'name': 'Kanhasoft Bulk Invoice Delete',
    'version': '17.0.1.0.0',
    'summary': 'Bulk force delete invoices from tree view',
    'author': 'Kanhasoft',
    'category': 'Accounting',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
}