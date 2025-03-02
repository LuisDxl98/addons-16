# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime

import logging
_logger = logging.getLogger(__name__)

class PosOrderInheritGeminisModel(models.Model):
    _inherit = 'pos.order'

    @api.model
    def create(self, vals):
        # Agregar codigo de validacion aca
        res = super(PosOrderInheritGeminisModel, self).create(vals)

        if 'session_id' in vals and 'partner_id' in vals:
            partner = self.env['res.partner'].sudo().browse(vals['partner_id'])

            if partner:
                partner.sudo().write({
                    'ultima_fecha_pago': datetime.today().date()
                })
        
        return res