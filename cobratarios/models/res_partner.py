# -*- coding: utf-8 -*-
from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

class ResPartnerCobratariosModel(models.Model):
    _inherit = 'res.partner'

    cobratario_id = fields.Many2one(string='Cobratario asignado', comodel_name='res.users', ondelete='restrict')

    ultima_fecha_pago = fields.Date(string='Ultima fecha de pago')

    folio_tarjeta = fields.Char(string="Folio de tarjeta")
    
    ruta_id = fields.Many2one(string='Ruta de cobro', comodel_name='rutas.de.cobro')

class RutasDeConbro(models.Model):
    _name = 'rutas.de.cobro'
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Ya existe una ruta con ese mismo nombre, ingrese un nombre de Ruta diferente'),   
    ]

    name = fields.Char(string='Nombre de la Ruta', required=True)