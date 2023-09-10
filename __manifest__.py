{
    'name' : 'Haus Indonesia Route Optimization ',
    'version' : '1.0',
    'summary':'Haus Indonesia Route Optimization',
    'sequence':10,
    'description':"""Route Optimization Platform Haus Indonesia""",
    'category':'Productivity',
    'website':'',
    'license': 'LGPL-3',
    'depends':[
        'sale',
        'mail',
        'website_slides',
        'board'
    ],
    'data':[
        'views/contents.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
    ],
    'demo':[],
    'qweb':[],
    'installable':True,
    'application':True,
    'auto_install':False,
    'css': [
    "static/src/css/custom.css",  # Path ke file CSS Anda
    ],
}