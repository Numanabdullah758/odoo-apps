# -*- coding: utf-8 -*-
{
    'name': 'POS Restrict Zero Quantity',
    'version': '18.0.1.0.0',
    'category': 'Sales/Point of Sale',
    'summary': 'Prevent selling out-of-stock products in POS with configurable warnings',
    'description': """
POS Restrict Zero Quantity
==========================

Prevent the sale of products with zero or negative stock levels directly
from the Point of Sale interface.

Key Features
------------
* **Block Out-of-Stock Sales** - Automatically prevents payment when order
  contains products with zero or negative available quantity.
* **Real-Time Stock Check** - Fetches live warehouse stock data at the moment
  of payment, not stale cached values.
* **Combined or Per-Product Warnings** - Choose between a single summary
  dialog listing all restricted products, or individual pop-ups for each one.
* **POS Config Toggle** - Enable/disable the restriction per POS configuration
  from Settings > Point of Sale.
* **Consumable Product Aware** - Only checks consumable (storable) products;
  services and non-inventory items pass through normally.
* **Multi-Product Aggregation** - If the same product appears on multiple order
  lines, quantities are aggregated before checking against available stock.

Use Cases
---------
* Retail stores that must not oversell physical inventory.
* Warehouses using POS for dispatch that need strict stock discipline.
* Any business that wants real-time stock validation at checkout.
    """,
    'author': 'Numan Abdullah',
    'website': 'https://www.linkedin.com/in/numan-abdullah/',
    'support': 'numanabdullah758@gmail.com',
    'depends': ['point_of_sale', 'stock'],
    'data': [
        'views/pos_config_view.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'nab_pos_restrict_zero_qty/static/src/app/models/models.js',
        ],
    },
    'images': [
        'images/0_banner_screenshot.jpg',
        'images/1_pos_config.png',
        'images/2_onhand.png',
        'images/3_warning.png',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
