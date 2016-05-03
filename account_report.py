from openerp.osv import fields,osv
from openerp import tools

 
class account_receipt_report(osv.osv):
    _name = "account.receipt.report"
    _description = "Receipt Report"
    _auto = False
    _columns = {
	'customer_id': fields.many2one('res.partner','Customer'),
	'state': fields.char('State',size=32,readonly=True),
	'date': fields.date('Date',readonly=True),
	'journal_id': fields.many2one('account.journal','Journal Name'),
	'voucher_name': fields.char('Number',size=32,readonly=True),
	'amount': fields.float('Amount',readonly=True,group_operator="sum",digits=(16,2)), 
	'journal_id': fields.many2one('account.journal','Journal Name'),
	}
 
    def init(self, cr):
        tools.sql.drop_view_if_exists(cr, 'account_receipt_report')
	cr.execute("""
		create or replace view account_receipt_report as (
			select b.id,a.customer_id,a.state,a.date,b.number as voucher_name,
				b.amount,b.journal_id from account_voucher_receipt a inner join 
				account_voucher b on a.id = b.receipt_id where a.type = 'receipt'
				)
	""")	
 
account_receipt_report()

