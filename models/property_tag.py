from odoo import models, fields

### Start add at 20241220-1445: Create y.realestate.property.tag model ###
class YRealestatePropertyTag(models.Model):
    _name = 'y.realestate.property.tag'
    _description = 'Real Estate Property Tag'
    _order = 'name asc'
    
    name = fields.Char(string="Tag Name", size=100, required=True)
### End add at 20241220-1445: Create y.realestate.property.tag model ###
