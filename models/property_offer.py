from odoo import models, fields, api
from datetime import timedelta

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
    ### Start add at 20250112-1030: Add validity and date_deadline fields ###
    validity = fields.Integer(string="Validity (days)", default=7)
    date_deadline = fields.Date(
        string="Offer dead line",
        compute="_compute_date_deadline",
        inverse="_inverse_date_deadline",
        store=True
    )
    ### End add at 20250112-1030: Add validity and date_deadline fields ###
    
    ### Start add at 20250112-1030: Add compute and inverse methods ###
    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date.date() + timedelta(days=record.validity)
            else:
                record.date_deadline = fields.Date.today() + timedelta(days=record.validity)
    
    def _inverse_date_deadline(self):
        for record in self:
            if record.create_date and record.date_deadline:
                record.validity = (record.date_deadline - record.create_date.date()).days
            elif record.date_deadline:
                record.validity = (record.date_deadline - fields.Date.today()).days
    ### End add at 20250112-1030: Add compute and inverse methods ###
### End add at 20241220-1445: Create y.realestate.property.offer model ###
