{
    'name': 'Tanmya Purchase order extension',
    'version': '1.0',
    'summary': 'Serve for purchase module',
    'description': "",
    'category': 'Inventory/Purchase',
    'author': 'Tanmya co.',
    'company': 'Tanmya',
    'post_init_hook': 'test_post_init_hook',
    'website': "https://www.altanmya.net",
    'depends': ['purchase'],
    'data': ['security/ir.model.access.csv','security/security.xml','views/view_actions.xml','views/view_menu.xml','views/view_pages.xml'],
    'demo': [],
    'qweb': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
