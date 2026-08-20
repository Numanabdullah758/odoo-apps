# -*- coding: utf-8 -*-
# Copyright 2025 Numan Abdullah
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class PosConfig(models.Model):
    """Extend POS configuration with zero-quantity restriction options."""
    _inherit = 'pos.config'

    enable_pos_restrict_zero_qty = fields.Boolean(
        string="Restrict Zero Quantity",
        help="Block payment when order contains products with zero or "
             "negative stock in the warehouse.",
    )
    enable_per_product_warning = fields.Boolean(
        string="Show Warning Per Product",
        help="When enabled, shows a separate warning for each out-of-stock "
             "product. Otherwise, a single combined warning is displayed.",
    )

    @api.model
    def _load_pos_data_fields(self, config):
        fields_list = super()._load_pos_data_fields(config)
        # Empty list means "all fields" in POS load. Only append when an
        # explicit list was returned, otherwise read() would fetch these
        # fields alone and drop currency_id / company_id.
        if fields_list:
            for fname in (
                'enable_pos_restrict_zero_qty',
                'enable_per_product_warning',
            ):
                if fname not in fields_list:
                    fields_list.append(fname)
        return fields_list
