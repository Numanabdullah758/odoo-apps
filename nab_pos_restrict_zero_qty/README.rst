=============================================
POS Out of Stock Validation (Odoo 18)
=============================================

Block Point of Sale payments for products with zero or negative stock.
Real-time warehouse stock check at checkout prevents overselling.

Features
--------

* Block payment for out-of-stock products at the POS.
* Real-time warehouse stock check at the moment of payment.
* Configurable warning mode: combined summary or per-product alerts.
* Per-POS configuration — enable or disable per shop.
* Smart product detection — only checks storable products.
* Multi-line quantity aggregation for accurate stock comparison.

Configuration
-------------

1. Go to **Point of Sale > Configuration > Settings**.
2. Enable **Zero Quantity Product Validation**.
3. Optionally enable **Show Warning Per Product** for individual alerts.

Usage
-----

Open your POS session and add products to an order. When you click **Pay**,
the module checks live warehouse stock. If any storable product has
insufficient quantity, payment is blocked and a warning dialog is shown.

Compatibility
-------------

* Odoo 18 Community & Enterprise

Bug Tracker
-----------

If you encounter any issues, please report them to:
**numanabdullah758@gmail.com**

Credits
-------

* **Author:** Numan Abdullah
* **Website:** https://www.linkedin.com/in/numan-abdullah/

License
-------

This module is licensed under LGPL-3.
