/**
 * @odoo-module
 * Copyright 2025 Numan Abdullah
 * License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
 */

import { PosStore } from "@point_of_sale/app/services/pos_store";
import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

patch(PosStore.prototype, {
    async pay() {
        const order = this.getOrder();
        const config = this.config;

        if (!config.enable_pos_restrict_zero_qty || !order) {
            return super.pay(...arguments);
        }

        const lines = order.getOrderlines();
        const prodUsedQty = {};
        const restrictedProducts = [];
        let canProceed = true;

        for (const line of lines) {
            const product = line.getProduct();
            const productTemplate = product?.product_tmpl_id;
            if (!productTemplate?.is_storable) {
                continue;
            }

            const result = await this.getProductInfo(productTemplate, 1, 0, product);
            const availableQty =
                result?.productInfo?.warehouses?.[0]?.available_quantity ?? 0;
            const lineQty = line.getQuantity();

            if (product.id in prodUsedQty) {
                const prevQty = prodUsedQty[product.id][1];
                prodUsedQty[product.id] = [availableQty, lineQty + prevQty];
            } else {
                prodUsedQty[product.id] = [availableQty, lineQty];
            }
        }

        for (const [id, [available, required]] of Object.entries(prodUsedQty)) {
            const product = this.models["product.product"].get(parseInt(id));
            const shortage = available - required;

            if (product?.product_tmpl_id?.is_storable && shortage < 0) {
                canProceed = false;
                const warning = `${product.display_name} (available: ${available}, required: ${required})`;

                if (config.enable_per_product_warning) {
                    await this.dialog.add(AlertDialog, {
                        title: _t("Out of Stock"),
                        body: warning,
                    });
                } else {
                    restrictedProducts.push(warning);
                }
            }
        }

        if (!config.enable_per_product_warning && restrictedProducts.length > 0) {
            this.dialog.add(AlertDialog, {
                title: _t("Restricted Products"),
                body: _t(
                    "The following products are out of stock:\n\n%s",
                    restrictedProducts.join("\n")
                ),
            });
        }

        if (canProceed) {
            return super.pay(...arguments);
        }
    },
});
