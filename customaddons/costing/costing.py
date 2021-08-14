from odoo.exceptions import ValidationError
from odoo import api, models, fields, _


#1,3
class ProductCategoryLotCost(models.Model):
    """extends product.category models with selection fields added with lotcost"""

    _inherit = "product.category"

    #Selection field added along with lotcost
    property_cost_method = fields.Selection(
        selection_add=[('lotcost', 'Lot Cost')], ondelete={'lotcost': 'cascade'}
    )

    #This method will throw error when the product is not been tracked while setting the costmethod to lot cost reflects when save
    @api.constrains('property_cost_method')
    def _product_lot_check(self):
        if self.property_cost_method == 'lotcost':
            lines = self.env['product.template'].search([('categ_id.property_cost_method','=','lotcost')])
            print(lines)
            if any(line.tracking in ('none') for line in lines):
                raise ValidationError(_("Some Products within this Product Category are not tracked by Lot/SN. When using the costing method Cost per Lot/SN, this needs to be the case. Please configure all products within this category to tracking by Lot/SN before changing the costing method"))


#2 --> Defined in costing_view.xml

#3
class ProductTemplate(models.Model):
    """ While adding new product with product category as lot cost this performs validation check and throws error message while saving"""
    _inherit = 'product.template'

    #method will throw error when adding a new product category set to lot cost reflects when save
    @api.constrains('categ_id')
    def _categ_lot_check(self):
        if self.categ_id.property_cost_method == 'lotcost':
            lines = self.env['product.template'].search([('categ_id.property_cost_method','=','lotcost')])
            if any(line.tracking in ('none') for line in lines):
                raise ValidationError(_("You are trying to add this product to a category that uses the costing method Cost per Lot/SN. This product ist not tracked by either Lot or Serial Number. When using the costing method Cost per Lot/SN, this needs to be the case. Please configure the product to tracking by Lot/SN before changing Product Category"))

#4
class CostPerLot(models.Model):
    """Added new field in stocks to track the CostPerLot and displayed in the list view"""

    _inherit = 'stock.production.lot'

    cost_per_lot = fields.Float(string="Cost per Lot/So No")



#5
class AddCostPerLot(models.Model):

    _inherit = 'stock.inventory'



