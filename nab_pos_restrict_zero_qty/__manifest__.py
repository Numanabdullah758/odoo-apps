# -*- coding: utf-8 -*-
{
    'name': 'POS Out of Stock Validation - Block Zero Quantity Sales',
    'version': '18.0.1.0.0',
    'category': 'Sales/Point of Sale',
    'summary': 'Block POS payment for out-of-stock products with real-time '
               'stock check, zero quantity restriction & configurable warnings',
    'description': """
POS Out of Stock Validation
===========================

Prevent overselling by blocking Point of Sale payments for products with
zero or negative stock. Real-time warehouse stock check at checkout.

Why This Module?
----------------
* Cashiers accidentally sell products that are out of stock
* Inventory mismatches cause fulfillment problems
* You need real-time stock enforcement at the POS — not end-of-day surprises

Key Features
------------
* **Block Out-of-Stock Sales** — Automatically prevents payment when order
  contains products with zero or negative available quantity.
* **Real-Time Stock Check** — Fetches live warehouse stock data at the moment
  of payment, not stale cached values.
* **Combined or Per-Product Warnings** — Choose between a single summary
  dialog listing all restricted products, or individual pop-ups for each one.
* **Per-POS Configuration** — Enable/disable the restriction per POS shop
  from Settings > Point of Sale.
* **Smart Product Detection** — Only validates storable products; services
  and non-inventory items pass through normally.
* **Multi-Line Aggregation** — If the same product appears on multiple order
  lines, quantities are aggregated before checking against available stock.

Keywords: pos stock, pos inventory, pos out of stock, pos zero quantity,
pos restrict, pos block payment, pos stock check, pos stock validation,
point of sale stock, point of sale inventory check, pos oversell prevention
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
    'price': 0,
    'currency': 'USD',
    'installable': True,
    'auto_install': False,
    'application': False,
}
