# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime

import logging
_logger = logging.getLogger(__name__)

class ResPartnerCobratariosModel(models.Model):
    _inherit = 'res.partner'

    cobratario_id = fields.Many2one(string='Cobratario asignado', comodel_name='res.users', ondelete='restrict')

    ultima_fecha_pago = fields.Date(string='Ultima fecha de pago')

    folio_tarjeta = fields.Char(string="Folio de tarjeta")
    
    ruta_id = fields.Many2one(string='Ruta de cobro', comodel_name='rutas.de.cobro')

    estado_pago = fields.Selection([
            ('al_corriente', 'Al corriente'),
            ('en_espera', 'En Espera'),
            ('atrasado', 'Atrasado')
        ],
        string="Estado de Pago",
        compute="_compute_estado_pago",
        store=True
    )

    @api.depends('ultima_fecha_pago')
    def _compute_estado_pago(self):
        for record in self:
            if record.credit < 1.00:
                record.estado_pago = 'al_corriente'
            elif record.ultima_fecha_pago:
                # Convertir ultima_fecha_pago a un objeto datetime
                ultima_fecha_pago = fields.Date.from_string(record.ultima_fecha_pago)
                hoy = fields.Date.context_today(record)
                
                # Calcular la diferencia en meses
                diferencia_dias = (hoy - ultima_fecha_pago).days

                if diferencia_dias <= 30:
                    record.estado_pago = 'al_corriente'
                elif 30 < diferencia_dias <= 90:
                    record.estado_pago = 'en_espera'
                else:
                    record.estado_pago = 'atrasado'
            else:
                record.estado_pago = 'al_corriente'
    
    @api.model
    def actualizar_estado_pagos(self):
        partners = self.search([('ultima_fecha_pago', '!=', False)])
        for partner in partners:
            partner._compute_estado_pago()


class RutasDeConbro(models.Model):
    _name = 'rutas.de.cobro'
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Ya existe una ruta con ese mismo nombre, ingrese un nombre de Ruta diferente'),   
    ]

    name = fields.Char(string='Nombre de la Ruta', required=True)