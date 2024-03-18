odoo.define("cs_pos_order_return_reason.models", function (require) {
    "use strict";
    
    const {Order} = require('point_of_sale.models');
    const Registries = require("point_of_sale.Registries");

    const CsOrderReturnReasonOrder = (Order) => class CsOrderReturnReasonOrder extends Order {
        constructor() {
            super(...arguments);
            this.is_refund_order = false;
            this.return_reason = false;
        }
        set_order_return_reason(return_reason){
        	this.return_reason = return_reason
        }
        get_order_return_reason(){
        	return this.return_reason;
        }
        export_as_JSON() {
            var json = super.export_as_JSON()
            json.return_reason = this.get_order_return_reason() || null;
            
            return json;
        }
        export_for_printing() {
            var self = this;
            var orders = super.export_for_printing()
            var new_val = {
            	return_reason: this.get_order_return_reason() || false,
            };
            $.extend(orders, new_val);
            return orders;
        }
    };
    Registries.Model.extend(Order, CsOrderReturnReasonOrder);
    
});
