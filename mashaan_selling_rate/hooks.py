from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "mashaan_selling_rate"
app_title = "Mashaan Selling Rate"
app_publisher = "smb"
app_description = "Mashaan Item Selling price calculation on the basis of margin"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "usamanaveed9263@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mashaan_selling_rate/css/mashaan_selling_rate.css"
# app_include_js = "/assets/mashaan_selling_rate/js/mashaan_selling_rate.js"

# include js, css files in header of web template
# web_include_css = "/assets/mashaan_selling_rate/css/mashaan_selling_rate.css"
# web_include_js = "/assets/mashaan_selling_rate/js/mashaan_selling_rate.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "mashaan_selling_rate/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "mashaan_selling_rate.install.before_install"
# after_install = "mashaan_selling_rate.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mashaan_selling_rate.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Item": {
		"before_save": "mashaan_selling_rate.tasks.cal_selling_price"
	}
}

# Scheduled Tasks
# ---------------

scheduler_events = {
	# "cron": {
	# 	"*/30 * * * * *": [
	# 		"mashaan_selling_rate.tasks.cal_selling_price"
	# 	]
	# }
	# "*/10 * * * * *": [
	# 	"mashaan_selling_rate.tasks.cal_selling_price"
	# ]
# 	"all": [
# 		"mashaan_selling_rate.tasks.all"
# 	],
 	"daily": [
 		"mashaan_selling_rate.tasks.cal_selling_price"
 	]
# 	"hourly": [
# 		"mashaan_selling_rate.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mashaan_selling_rate.tasks.weekly"
# 	]
# 	"monthly": [
# 		"mashaan_selling_rate.tasks.monthly"
# 	],
}

# Testing
# -------

# before_tests = "mashaan_selling_rate.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mashaan_selling_rate.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "mashaan_selling_rate.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"mashaan_selling_rate.auth.validate"
# ]

fixtures = ["Custom Field"]