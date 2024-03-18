odoo.define("cs_pos_order_return_reason.TemplateOrderReturnPopupWidget", function (require) {
    "use strict";
    
    const Registries = require("point_of_sale.Registries");
    const AbstractAwaitablePopup = require("point_of_sale.AbstractAwaitablePopup");
    
    class TemplateOrderReturnPopupWidget extends AbstractAwaitablePopup {
        async confirm() {
            var self = this;
            this.props.resolve({ confirmed: true, payload: await this.getPayload() });
            this.cancel()
            var value = $("#textarea_note").val();
            this.env.pos.get_order().set_order_return_reason(value);
        }
    }

    TemplateOrderReturnPopupWidget.template = "TemplateOrderReturnPopupWidget";
    Registries.Component.add(TemplateOrderReturnPopupWidget);
    
    return TemplateOrderReturnPopupWidget
});
