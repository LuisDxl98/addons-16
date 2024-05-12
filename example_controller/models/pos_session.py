# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class POSSession(models.Model):
    _inherit = "pos.session"

    def _loader_params_res_partner(self):
        res = super()._loader_params_res_partner()
        res["search_params"]["fields"].append("credit")
        res["search_params"]["fields"].append("vendor_id")
        res["search_params"]["fields"].append("barcode")
        res["search_params"]["fields"].append("vendor_name")
        return res
