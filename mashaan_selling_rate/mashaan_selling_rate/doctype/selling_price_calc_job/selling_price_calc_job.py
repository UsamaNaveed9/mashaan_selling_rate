# Copyright (c) 2023, smb and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint
from frappe.model.document import Document

class SellingPriceCalcJob(Document):
	def on_submit(self):
		items = frappe.db.get_list('Item',
			filters={
				'disabled': 0
			},
			fields=['name','margin']
		)

		for i in items:
			convt_margin = 0
			cal_margin = 0
			selling_rate = 0

			d_warehouse = frappe.db.get_value('Item Default', {'parent': i.name}, ['default_warehouse'])
			val_rate = frappe.db.get_value('Bin', {'item_code': i.name, 'warehouse': d_warehouse}, ['valuation_rate'])

			if i.margin and val_rate:
				convt_margin = i.margin/100
				cal_margin = convt_margin * val_rate
				selling_rate = cal_margin + val_rate

				if frappe.db.exists("Item Price", {"item_code": i.name,"price_list":"Standard Selling","selling":1}):
					name = frappe.get_value('Item Price',{'item_code': i.name,'price_list':'Standard Selling','selling':1},'name')
					p_record = frappe.get_doc("Item Price",name)
					p_record.price_list_rate = selling_rate
					p_record.save()
				else:
					pr_add = frappe.new_doc("Item Price")
					pr_add.item_code = i.name
					pr_add.price_list = "Standard Selling"
					pr_add.selling = 1
					pr_add.price_list_rate = selling_rate
					pr_add.save()

	def submit(self):
		msgprint(_("The Selling Price Calculation task has been enqueued as a background job. In case there is any issue on processing in background, the system will add a comment about the error on this Selling Price Calc Job and revert to the Draft stage"))
		self.queue_action('submit', timeout=7000)
