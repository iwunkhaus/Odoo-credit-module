from odoo import api, fields, models, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_credit_limit = fields.Float(related='partner_id.credit_limit', string='Límite de Crédito', readonly=True)
    partner_credit_used = fields.Float(related='partner_id.credit_used', string='Crédito Utilizado', readonly=True)

    @api.onchange('partner_id')
    def _onchange_partner_id_credit_limit(self):
        if self.partner_id:
            self.partner_credit_limit = self.partner_id.credit_limit
            self.partner_credit_used = self.partner_id.credit_used
            if not self.partner_id.credit_active:
                # Establecer la condición de pago a "Pago contado"
                # (Asumiendo que el identificador de "Pago contado" es 'cash')
                self.payment_term_id = self.env.ref('account.account_payment_term_immediate').id

   
