=============================
POS Restrict Zero Quantity
=============================

Prevent selling out-of-stock products in your Point of Sale with real-time
stock validation and configurable warnings.

Features
--------

* Block payment when order contains products with zero or negative stock.
* Real-time warehouse stock check at the moment of payment.
* Configurable warning modes: combined summary or per-product alerts.
* Per-POS configuration toggle from Settings.
* Smart product detection — only checks storable/consumable products.
* Multi-line quantity aggregation for accurate stock comparison.

Configuration
-------------

1. Go to **Point of Sale > Configuration > Settings**.
2. Enable **Restrict Zero Quantity**.
3. Optionally enable **Show Warning Per Product** in the POS config form.

Usage
-----

Open your POS session and add products to an order. When you click **Pay**,
the module checks live warehouse stock. If any storable product has
insufficient quantity, payment is blocked and a warning dialog is shown.

Bug Tracker
-----------

If you encounter any issues, please report them to:
**numanabdullah758@gmail.com**

Credits
-------

* **Author:** Numan Abdullah

License
-------

This module is licensed under LGPL-3.
