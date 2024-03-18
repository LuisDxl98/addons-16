# Copyright (C) Crypton Soft-tech
from odoo import fields, models, api
    
class PosOrder(models.Model):
    _inherit = 'pos.order'
    
    cs_return_reason = fields.Char(string="Return Reason")
    
    @api.model
    def _order_fields(self, ui_order):
        res = super(PosOrder, self)._order_fields(ui_order)
        print("\n\n\nui_order.get('reason') >>>>> ",ui_order.get('return_reason'))
        res['cs_return_reason'] = ui_order.get('return_reason', False)
        return res
    