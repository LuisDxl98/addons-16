odoo.define("cs_pos_order_return_reason.csReturnReasonButton", function (require) {
    "use strict";
    
    const PosComponent = require("point_of_sale.PosComponent");
    const { useListener } = require("@web/core/utils/hooks");
    const Registries = require("point_of_sale.Registries");
    const ProductScreen = require("point_of_sale.ProductScreen");
    
    class csReturnReasonButton extends PosComponent {
        setup() {
            super.setup();
            useListener('click', this.onClick);
        }
        onClick() {
        	let { confirmed, payload } = this.showPopup("TemplateOrderReturnPopupWidget");
            if (confirmed) {
            } else {
                return;
            }
        }
    }
    csReturnReasonButton.template = "csReturnReasonButton";
    ProductScreen.addControlButton({
        component: csReturnReasonButton,
        condition: function () {
            return this.env.pos.config.enable_order_return_reason && this.env.pos.get_order().is_refund_order;
        },
    });
    Registries.Component.add(csReturnReasonButton);
    return csReturnReasonButton
});
