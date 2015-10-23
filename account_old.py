from openerp.osv import osv
from openerp.tools.translate import _

class account_invoice(osv.osv):
	_inherit = 'account.invoice'

	def invoice_pay_customer(self, cr, uid, ids, context=None):
		for invoice_id in ids:
			invoice = self.pool.get('account.invoice').browse(cr,uid,invoice_id)
			if invoice.type == 'out_refund' or invoice.refund_id.id != False:
				raise osv.except_osv('Error!',"No se puede pagar una NC o una factura con NC relacionada.")

		return super(account_invoice, self).invoice_pay_customer(cr, uid, ids, context=context)
