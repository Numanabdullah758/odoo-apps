/**
 * @odoo-module
 * Copyright 2025 Numan Abdullah
 * License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
 */

import { PosStore } from "@point_of_sale/app/store/pos_store";
import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

patch(PosStore.prototype, {
    async pay() {
        const order = this.env.services.pos.get_order();
        const lines = order.get_orderlines();
        const config = this.config;

        const prodUsedQty = {};
        const restrictedProducts = [];
        let canProceed = true;

        if (config.enable_pos_restrict_zero_qty) {
            for (const line of lines) {
                const product = line.product_id;

                if (product.type === 'consu') {
                    const result = await this.env.services.pos.getProductInfo(product, 1);
                    const availableQty = result?.productInfo?.warehouses?.[0]?.available_quantity ?? 0;

                    if (product.id in prodUsedQty) {
                        const prevQty = prodUsedQty[product.id][1];
                        prodUsedQty[product.id] = [availableQty, line.qty + prevQty];
                    } else {
                        prodUsedQty[product.id] = [availableQty, line.qty];
                    }
                }
            }

            for (const [id, [available, required]] of Object.entries(prodUsedQty)) {
                const product = this.env.services.pos.models['product.product'].getBy('id', parseInt(id));
                const shortage = available - required;

                if (product.type === 'consu' && shortage < 0) {
                    canProceed = false;
                    const warning = `${product.display_name} (available: ${available}, required: ${required})`;

                    if (config.enable_per_product_warning) {
                        await this.dialog.add(AlertDialog, {
                            title: _t("Out of Stock"),
                            body: _t(warning),
                        });
                    } else {
                        restrictedProducts.push(warning);
                    }
                }
            }

            if (!config.enable_per_product_warning && restrictedProducts.length > 0) {
                this.dialog.add(AlertDialog, {
                    title: _t("Restricted Products"),
                    body: _t("The following products are out of stock:\n\n" + restrictedProducts.join("\n")),
                });
            }
        }

        if (canProceed) {
            super.pay();
        }
    },
});
