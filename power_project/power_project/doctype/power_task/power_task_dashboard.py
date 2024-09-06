from frappe import _


def get_data():
	return {
		"fieldname": "task",
		"transactions": [
			{"label": _("Power Activity"), "items": ["Power Timesheet"]},
		],
	}
