from odoo import models, fields

### Start add at 20241220-1445: Create y.realestate.property.offer model ###
class YRealestatePropertyOffer(models.Model):
    _name = 'y.realestate.property.offer'
    _description = 'Real Estate Property Offer'
    _order = 'price desc'
    
    price = fields.Float(string="Offer Price", required=True)
    status = fields.Selection(
        selection=[('new', 'New'), ('accepted', 'Accepted'), ('refused', 'Refused')],
        string="Status",
        default='new'
    )
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    property_id = fields.Many2one('y.realestate.property', string="Property", required=True)
### End add at 20241220-1445: Create y.realestate.property.offer model ###
