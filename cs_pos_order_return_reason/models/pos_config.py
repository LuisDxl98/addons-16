# Copyright (C) Crypton Soft-tech
from odoo import fields, models, api

class PosConfig(models.Model):
    _inherit = 'pos.config'

    enable_order_return_reason = fields.Boolean(
        "Allow to Enter Reason")
    
    display_reason_in_receipt = fields.Boolean(
        "Display Reason in Receipt")
    
    is_reason_compulsory = fields.Boolean(string="Is Reason Compulsory ?")
        