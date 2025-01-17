// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.views.calendar["Power Task"] = {
	field_map: {
		start: "exp_start_date",
		end: "exp_end_date",
		id: "name",
		title: "subject",
		allDay: "allDay",
		progress: "progress",
	},
	gantt: true,
	filters: [
		{
			fieldtype: "Link",
			fieldname: "project",
			options: "Power Project",
			label: __("Project"),
		},
	],
	get_events_method: "frappe.desk.calendar.get_events",
};
