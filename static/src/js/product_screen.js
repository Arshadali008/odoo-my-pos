/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { _t } from "@web/core/l10n/translation";

patch(ProductScreen.prototype, {
    async addProductToOrder(product) {
        const posConfig = this.pos.config;
        console.log(this.pos.config.enable_quantity_warning)
        if (posConfig.enable_quantity_warning) {
            if (product.quantity_location <= 0) {
                await this.notification.add(_t("This product is out of stock"), {
                    type: "danger",
                });
                return;
            }
            if (posConfig.enable_quantity_warning &&
                posConfig.minimum_quantity > 0 &&
                product.quantity_location > 0 &&
                product.quantity_location < posConfig.minimum_quantity) {
                await this.env.services.dialog.add(AlertDialog, {
                    title: _t("Low Stock Warning"),
                    body: _t("Warning! Selected product is below minimum quantity."),
                });
            }
        }
        return super.addProductToOrder(product);
    }
});
