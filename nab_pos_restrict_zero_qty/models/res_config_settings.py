# -*- coding: utf-8 -*-
# Copyright 2025 Numan Abdullah
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    """Extend settings to expose POS zero-quantity restriction toggle."""
    _name = 'res.config.settings'
    _inherit = ['res.config.settings', 'pos.load.mixin']

    enable_pos_restrict_zero_qty = fields.Boolean(
        related='pos_config_id.enable_pos_restrict_zero_qty',
        readonly=False,
    )

    @api.model
    def _load_pos_data_fields(self, config_id):
        result = super()._load_pos_data_fields(config_id)
        result.append('enable_pos_restrict_zero_qty')
        return result
