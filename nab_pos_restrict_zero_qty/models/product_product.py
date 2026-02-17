# -*- coding: utf-8 -*-
# Copyright 2025 Numan Abdullah
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, models


class ProductProduct(models.Model):
    """Extend product to load qty_available into POS data."""
    _name = 'product.product'
    _inherit = ['product.product', 'pos.load.mixin']

    @api.model
    def _load_pos_data_fields(self, config_id):
        result = super()._load_pos_data_fields(config_id)
        result.append('qty_available')
        return result
