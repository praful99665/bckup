from frappe import _
import frappe
def get_data(doctype=None, data=None):
    return {
        "fieldname": "customer",  # Main linking field in Customer
        "non_standard_fieldnames": {
            "Customer Custody Items": "customer",  # Link Customer Custody Items to Customer
        },
    "transactions": [
        {"label": _("Customer Records"), "items": ["Customer Custody Items"]},
        {"label": _("Orders"), "items": ["Sales Order", "Delivery Note","Purchase Order"]}

    ]
    }
