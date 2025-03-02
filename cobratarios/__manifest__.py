{
    'name': 'Cobratarios',
    'version': '1.0',
    'description': 'Modulo de cobratarios para Point Of Sale',
    'license': 'LGPL-3',
    'category': 'Apps',
    'depends': [
        'base','point_of_sale','contacts','account'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/res_partner.xml',
        'views/centro_cobro_view.xml',
        'views/pagos_clientes_view.xml',
        'data/cron.xml',
    ],
    'auto_install': False,
    'application': True,
    'installable': True,
}