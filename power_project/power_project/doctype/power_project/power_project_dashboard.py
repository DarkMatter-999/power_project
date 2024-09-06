from frappe import _


def get_data():
	return {
		"heatmap": True,
		"heatmap_message": _("This is based on the Time Sheets created against this project"),
		"fieldname": "project",
		"transactions": [
			{
				"label": _("Power Project"),
				"items": ["Power Task", "Power Timesheet", "Issue", "Power Project Update"],
			},
			{"label": _("Material"), "items": ["Material Request", "BOM", "Stock Entry"]},
			{"label": _("Sales"), "items": ["Sales Order", "Delivery Note", "Sales Invoice"]},
			{"label": _("Purchase"), "items": ["Purchase Order", "Purchase Receipt", "Purchase Invoice"]},
		],
	}
