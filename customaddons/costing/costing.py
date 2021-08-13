from odoo import models, fields, api, _



#extends product.category models with selection fields added with Cost per Lot/Serial Number
class ProductCategoryCost(models.Model):
    _inherit = "product.category"

    property_cost_method = fields.Selection(
        selection_add=[('lotcost',"Cost per Lot/Serial Number")]
        )
