# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime

import logging
_logger = logging.getLogger(__name__)



class CentroDeCobro(models.Model):
    _name = 'centro.de.cobro'
    _description = 'Modelo para el centro de cobros de Cobratarios'
    _rec_name = 'cobratario_id'

    cobratario_id = fields.Many2one(string='Cobratario', comodel_name='res.users')

    pago_de_clientes_ids = fields.Many2many('apartado.cobro.clientes', string='Clientes', default=False)

    fecha_de_carga = fields.Date(string='Fecha de carga', default=datetime.today().date())

    total_cobrado = fields.Float(string="Total cobrado", compute='_compute_total_cobrado' )

    cobros_generados = fields.Many2many('account.payment', string="Cobros generados")

    active = fields.Boolean(string="Active", default=True)

    state = fields.Selection([
        ('draft', 'Borrador'),
        ('generado', 'Generado'),
        ('cobrado', 'Cobrado'),
        ('cancelado', 'Cancelado'),
    ], default='draft')

    @api.onchange('cobratario_id')
    def onchange_cobratario_id(self):
        if self.cobratario_id:
            clients = self.env['res.partner'].sudo().search([('cobratario_id','=',self.cobratario_id.id)])
            if clients:
                for client in clients:
                    new_client = self.env['apartado.cobro.clientes'].sudo().create({
                        'cliente_id': client.id
                    })
                    self.pago_de_clientes_ids = [(4, new_client.id)]
    
    @api.depends('pago_de_clientes_ids')
    def _compute_total_cobrado(self):
        for record in self:
            if record.pago_de_clientes_ids:
                total = 0
                for pago in record.pago_de_clientes_ids:
                    total = total + pago.amount
                
                record.total_cobrado = total
            else:
                record.total_cobrado = 0
    

    def aplicar_cobros(self):
        for pago in self.pago_de_clientes_ids:
            if pago.amount > 0:
                cobro = self.env['account.payment'].sudo().create({
                    'payment_type': 'inbound',
                    'partner_id': pago.cliente_id.id,
                    'amount': pago.amount,
                    'date': pago.fecha_cobro,
                    'ref': 'Cobro realizado desde la aplicación de Cobratarios',
                    'journal_id': 8 if pago.tipo_pago == 'banco' else 7,
                })
                if cobro:
                    pago.cliente_id.sudo().write({
                        'ultima_fecha_pago': datetime.today().date()
                    })
                    self.cobros_generados = [(4, cobro.id)]
                    cobro.action_post()
        self.state = 'cobrado'

    def save_cobro(self):
        self.state = 'generado'
    
    def cancelar_cobro(self):
        self.state = 'cancelado'
        self.active = False

class ApartadoCobro(models.Model):
    _name = 'apartado.cobro.clientes'


    cliente_id = fields.Many2one(string='Cliente', comodel_name='res.partner', required=True)

    cobratario_id = fields.Many2one(string='Cobratario', comodel_name='res.users', related='cliente_id.cobratario_id', store=True)
    
    articulo_id = fields.Char(string='Articulo', related='cliente_id.barcode', store=True)

    ruta_name = fields.Char(string="Ruta de cobro", related='cliente_id.ruta_id.name', store=True)

    currency_id = fields.Many2one('res.currency', string='Currency', related='cliente_id.currency_id', store=True, readonly=True)

    credito = fields.Monetary(string='Credito Actual', related='cliente_id.credit', currency_field='currency_id', store=True, readonly=True)

    credito_final = fields.Monetary(string='Despues del cobro', currency_field='currency_id', compute='_compute_credito_final' )
    
    @api.depends('credito','amount')
    def _compute_credito_final(self):
        for record in self:
            if record.amount:
                record.credito_final = record.credito - record.amount
            else:
                record.credito_final = record.credito
    
    tipo_pago = fields.Selection(string='Tipo de pago', selection=[
        ('efectivo', 'Efectivo'),
        ('banco', 'Transferencia bancaria'),
    ], default="efectivo")
    
    amount = fields.Float(string='Total pagado: ')

    fecha_cobro = fields.Date(string='Fecha de cobro', default=datetime.today().date())