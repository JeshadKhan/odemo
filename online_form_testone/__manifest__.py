# -*- coding: utf-8 -*-
{
    'name': 'Test Online Form',
    'summary': '',
    'version': '13.0.1.0',
    'author': 'Jeshad Khan',
    'company': '',
    'website': '',
    'sequence': 1,
    'depends': [
        'base',
        'mail',
        'web',
        'website',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/online_form_template.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    "license": "OPL-1",
}
