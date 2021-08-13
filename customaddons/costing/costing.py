from odoo import models, fields, _

class ProductCategoryCost(models.Model):
    """extends product.category models with selection fields added with lotcost"""

    _inherit = "product.category"

    property_cost_method = fields.Selection(
        selection_add=[('lotcost', 'Lot Cost')], ondelete={'lotcost': 'cascade'}
    )



