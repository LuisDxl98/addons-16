# -*- coding: utf-8 -*-
from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)



class ResPartnerCustomFields(models.AbstractModel):
    _inherit = 'res.partner'

    vendor_id = fields.Integer(related='user_id.id', string="ID del vendedor")
    vendor_name = fields.Char(related='user_id.name', string="Nombre del vendedor")
    superuser_ids = fields.Many2many("res.users", compute='_compute_res_users_admins', store=True )
    
    @api.depends('name')
    def _compute_res_users_admins(self):
        for record in self:
            admin_group_id = self.env.ref('base.group_erp_manager').id
            admins = self.env['res.users'].sudo().search([('groups_id', 'in', [admin_group_id])])
            record.superuser_ids = admins

    @api.model
    def create(self, vals):
        # Agregar codigo de validacion aca
        
        contact = super(ResPartnerCustomFields, self).create(vals)
        
        if contact:
            if contact.create_uid:
                _logger.warning("XXXXXXXXX SE CREO UN CONTACTO XXXXXXXX")
                _logger.warning(contact.create_uid.id)
                contact.write({'user_id': contact.create_uid.id})
        
        return contact
                

    
    
