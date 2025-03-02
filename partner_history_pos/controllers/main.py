
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo.http import request
from odoo import http


class ControllerHistoryPartnerGeminis(http.Controller):

    @http.route('/history', type='http', auth='user', website=True, csrf=False)
    def partner_history_main(self, estado=None, search=None, **kw):
        domain = []

        if search:
            # Aplicar filtro de búsqueda para el campo 'name' o 'folio_tarjeta'
            domain = ['|', ('name', 'ilike', search), ('folio_tarjeta', 'ilike', search)]

        if estado:
            domain = [('estado_pago','=',estado)]

        partner_ids = request.env['res.partner'].sudo().search(domain)

        values = {
            'contactos': partner_ids,
            'user_id': request.env.user,
            'search': search if search else ''
        }

        return http.request.render("partner_history_pos.history_partner_main_template", values)
