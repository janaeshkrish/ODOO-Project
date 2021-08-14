from odoo import api, models, fields, _

class ProductCategoryLotCost(models.Model):
    """extends product.category models with selection fields added with lotcost"""

    _inherit = "product.category"

    property_cost_method = fields.Selection(
        selection_add=[('lotcost', 'Lot Cost')], ondelete={'lotcost': 'cascade'}
    )

# class CostMethodCheck(models.Model):
#     _name = "product.category.method.check"
#     _inherits = {"product.category":"property_cost_method","product.template":"tracking"}
#     #_inherit = ["product.template","product.category"]
    
    
#     @api.onchange("property_cost_method")
#     def onchange_property_valuation_lotcost(self):
#         """Check of change in in property_cost_method"""

#         if self.property_cost_method == 'lotcost' & self.tracking == 'serial' or self.tracking == 'lot':
#             return {
#                 'warning': {
#                     'title': _("Warning"),
#                     'message': _("Some Products within this Product Category are not tracked by Lot/SN. When using the costing method Cost per Lot/SN, this needs to be the case. Please configure all products within this category to tracking by Lot/SN before changing the costing method"),
#                 }
#             }

#         if self.property_cost_method == 'lotcost':
#             return {
#                 'warning': {
#                     'title': _("Warning"),
#                     'message': _("You are trying to add this product to a category that uses the costing method Cost per Lot/SN. This product ist not tracked by either Lot or Serial Number. When using the costing method Cost per Lot/SN, this needs to be the case. Please configure the product to tracking by Lot/SN before changing Product Category"),
#                 }
#             }

#         else:
#             return {
#                 'warning': {
#                     'title': _("Warning"),
#                     'message': _("Changing your cost method is an important change that will impact your inventory valuation. Are you sure you want to make that change?"),
#                 }
#             }

