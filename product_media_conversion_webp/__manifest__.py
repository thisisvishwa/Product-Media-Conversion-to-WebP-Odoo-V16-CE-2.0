{
    'name': 'Product Media Conversion to WebP',
    'version': '1.0',
    'author': 'Vishwa G',
    'website': 'https://thisis.com',
    'category': 'Website',
    'license': 'AGPL-3',
    'summary': 'Converts product images to WebP format for faster loading',
    'description': """
Product Media Conversion to WebP Module
======================================
This module automatically converts product images to the WebP format, ensuring faster loading times and preserving the original image quality.
""",
    'depends': ['base', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/res_config_settings_views.xml',
        'views/webp_conversion_error_views.xml',
        'data/ir_cron_data.xml',
        'static/src/xml/webp_conversion_templates.xml',
        'static/description/index.html',
    ],
    'demo': [],
    'qweb': [
        'static/src/xml/webp_conversion_templates.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}