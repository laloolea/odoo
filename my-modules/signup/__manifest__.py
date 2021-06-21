# -*- coding: utf-8 -*-
{
    'name': 'ZypArtGallery Signup Form',
    'version': '0.1',
    'category': 'Website',
    'summary': 'Custom Fields',
    'description': """
        This module add some custom fields
        * Personal details section
        * Education details section
        * Professional details section
        * Know you better section
    """,
    'sequence': 1,
    'author': "ZypArtGallery",
    'website': 'https://zypgallery.ca/',
    'depends': ['auth_signup'],
    'data': [
        'views/auth_signup_extend_views.xml',
        'views/res_partner_view.xml',
        'views/templates.xml'
    ],
    'images': [
        'static/description/auth_signup_banner.png',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3'
}
