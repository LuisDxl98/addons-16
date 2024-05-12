# -*- coding: utf-8 -*-
from odoo import models, fields, api

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
    
    
    
