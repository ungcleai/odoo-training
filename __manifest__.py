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
        ### Start Add: ขั้นตอนที่ 4: ขั้นตอนที่ 4: การสร้างส่วนติดต่อผู้ใช้ (User Interface Creation)
        'views/property.xml',
        'views/menu.xml',
        ### End Add: ขั้นตอนที่ 4: ขั้นตอนที่ 4: การสร้างส่วนติดต่อผู้ใช้ (User Interface Creation)
        ### Start Add: ขั้นตอนที่ 3: การตั้งค่าความปลอดภัย (Security Configuration)
        'security/ir.model.access.csv',
        ### End Add: ขั้นตอนที่ 3: การตั้งค่าความปลอดภัย (Security Configuration)
    ],
    
    'demo': [],
    'installable': True,
    'application': True,
    'autoinstall': False
}