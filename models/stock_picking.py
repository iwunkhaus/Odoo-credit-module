from odoo import api, fields, models, _
from odoo.exceptions import UserError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        for picking in self:
            if picking.sale_id and picking.sale_id.partner_id:
                partner = picking.sale_id.partner_id
                if partner.credit_active:
                    total_credit_after_delivery = partner.credit_used + picking.sale_id.amount_total
                    if total_credit_after_delivery > partner.credit_limit:
                        raise UserError(_('El límite de crédito para %s ha sido excedido con este despacho. No se puede validar el despacho..') % partner.name)
