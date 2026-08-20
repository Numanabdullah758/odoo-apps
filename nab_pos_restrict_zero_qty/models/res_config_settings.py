# -*- coding: utf-8 -*-
# Copyright 2025 Numan Abdullah
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    """Expose POS zero-quantity restriction toggles in Settings."""
    _inherit = 'res.config.settings'

    pos_enable_pos_restrict_zero_qty = fields.Boolean(
        related='pos_config_id.enable_pos_restrict_zero_qty',
        readonly=False,
    )
    pos_enable_per_product_warning = fields.Boolean(
        related='pos_config_id.enable_per_product_warning',
        readonly=False,
    )
