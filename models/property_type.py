from odoo import models, fields

### Start add at 20241220-1445: Create property type model ###
class PropertyType(models.Model):
    _name = 'y.realestate.property.type'
    _description = 'Property Type Classification'
    _order = 'name asc'
    
    name = fields.Char(string="Property Type", required=True, size=50)
    sequence = fields.Integer(string="Sequence", default=10)
### End add at 20241220-1445: Create property type model ###
