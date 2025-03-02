{
    'name': 'Website History Partner',
    'version': '1.0',
    'description': 'Modulo para la consulta del historial de pagos de un cliente',
    'license': 'LGPL-3',
    'category': 'Apps',
    'depends': [
        'base','point_of_sale','contacts','account', 'website', 'cobratarios'
    ],
    'data': [
        'views/template_main.xml',
    ],
    'auto_install': False,
    'application': False,
    'installable': True,
}