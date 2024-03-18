# Copyright (C) Crypton Soft-tech

from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    pos_enable_order_return_reason = fields.Boolean(related="pos_config_id.enable_order_return_reason", string=
        "Allow to Enter Reason", readonly=False)
    
    pos_display_reason_in_receipt = fields.Boolean(related="pos_config_id.display_reason_in_receipt",string=
        "Display Reason in Receipt", readonly=False)
    
    pos_is_reason_compulsory = fields.Boolean(related="pos_config_id.is_reason_compulsory",string="Is Reason Compulsory ?", readonly=False)
