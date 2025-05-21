/** @odoo-module **/
import { ProductCard } from "@point_of_sale/app/generic_components/product_card/product_card";
import { patch } from "@web/core/utils/patch";
import { usePos } from "@point_of_sale/app/store/pos_hook";

patch(ProductCard.prototype, {
   setup() {
        super.setup(...arguments);
        this.pos = usePos();
    },
});
export default ProductCard;