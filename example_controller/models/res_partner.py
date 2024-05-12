# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPartnerCustomFields(models.AbstractModel):
    _inherit = 'res.partner'

    vendor_id = fields.Integer(related='create_uid.id', string="ID del vendedor")
    vendor_name = fields.Char(related='create_uid.name', string="Nombre del vendedor")
