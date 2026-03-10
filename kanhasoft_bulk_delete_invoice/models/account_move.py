from odoo import models, api, _
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_bulk_force_delete(self):
        if not self.env.user.has_group('base.group_system'):
            raise UserError(_("Only Administrator can delete invoices."))
        for move in self:
            if move.move_type not in ['out_invoice', 'in_invoice']:
                continue
            for line in move.line_ids:
                if line.reconciled:
                    line.remove_move_reconcile()
            if move.state == 'posted':
                move.button_draft()
            move.unlink()
        return True