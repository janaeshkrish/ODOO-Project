from odoo import fields,models



#extends product.category models with selection fields added with Cost per Lot/Serial Number
class ProductCategory(models.Model):
    _inherit = "product.category"

    property_cost_method = fields.Selection(selection_add=[
        ('lotcost',"Cost per Lot/Serial Number")
    ])
