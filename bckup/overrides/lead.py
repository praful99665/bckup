import frappe
from frappe.model.mapper import get_mapped_doc

def simple_make_customer(source_name, target_doc=None, ignore_permissions=False):
    # Step 1: Map the Lead to Customer
    doclist = get_mapped_doc(
        "Lead",
        source_name,
        {
            "Lead": {
                "doctype": "Customer",
                "field_map": {
                    "lead_name": "customer_name",
                    "gender":"custom_new_gender"

                }
            }
        },
        target_doc,
        ignore_permissions=ignore_permissions
    )

    # Step 2: Add a message in the console/log to see it works
    frappe.logger().info(f"✅ Simple Customer created from Lead: {source_name}")

    return doclist
