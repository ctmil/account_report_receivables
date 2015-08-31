from openerp import models, api, fields

class res_partner(models.Model):
	_inherit = "res.partner"

	move_line_ids = fields.One2many('account.move.line','partner_id',string="Account Move Lines for Partner")
	voucher_ids = fields.One2many('account.voucher','partner_id',string="Account Vouchers for Partner")

