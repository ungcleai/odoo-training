# -*- coding: utf-8 -*-
{
    'name': "Real Estate Adverting",
    'version': '1.0',
    'depends': ['base'],
    'author': "Chatpong Wongkanya",
    'category': 'Advertising',
    'description': """
    Real Estate Adverting Description
    """,
    'sequence': -1000,
    
    'data': [
        ### Start Add: ขั้นตอนที่ 3: การตั้งค่าความปลอดภัย (Security Configuration)
        'security/ir.model.access.csv',
        ### End Add: ขั้นตอนที่ 3: การตั้งค่าความปลอดภัย (Security Configuration)
        ### Start Add: ขั้นตอนที่ 4: ขั้นตอนที่ 4: การสร้างส่วนติดต่อผู้ใช้ (User Interface Creation)
        'views/property.xml',
        ### Start modify at 20241220-1450: Add property type views file ###
        'views/property_type_views.xml',
        ### End modify at 20241220-1450: Add property type views file ###
        ### Start modify at 20241220-1446: Add property tag views file ###
        'views/property_tag_views.xml',
        ### End modify at 20241220-1446: Add property tag views file ###
        'views/menu.xml',
        ### End Add: ขั้นตอนที่ 4: ขั้นตอนที่ 4: การสร้างส่วนติดต่อผู้ใช้ (User Interface Creation)
        ### Initialization Data
        'data/property_data.xml',
    ],
    
    'demo': [],
    'installable': True,
    'application': True,
    'autoinstall': False
}