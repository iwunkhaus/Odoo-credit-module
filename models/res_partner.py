from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    credit_limit = fields.Float(string='Límite de Crédito', default=0.0)
    credit_used = fields.Float(string='Crédito Utilizado', compute='_compute_credit_used')
    credit_active = fields.Boolean(string='Activar crédito', default=True)

    @api.depends('invoice_ids', 'invoice_ids.state')
    def _compute_credit_used(self):
        for partner in self:
            if partner.credit_active:
                unpaid_invoices = partner.invoice_ids.filtered(lambda inv: inv.state == 'posted')
                partner.credit_used = sum(unpaid_invoices.mapped('amount_total'))
            else:
                partner.credit_used = 0.0

