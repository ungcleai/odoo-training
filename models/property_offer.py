from odoo import models, fields, api
from odoo.exceptions import UserError
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
    
    ### Start add at 20250112-1130: Add action_accept method ###
    def action_accept(self):
        for record in self:
            if record.property_id.state in ['sold', 'canceled']:
                raise UserError("Cannot accept an offer for a sold or canceled property.")
            
            accepted_offers = record.property_id.offer_ids.filtered(lambda o: o.status == 'accepted')
            if accepted_offers:
                raise UserError("Another offer has already been accepted for this property.")
            
            record.status = 'accepted'
            record.property_id.selling_price = record.price
            record.property_id.state = 'offer_accepted'
    ### End add at 20250112-1130: Add action_accept method ###
    
    ### Start add at 20250112-1135: Add action_refuse method ###
    def action_refuse(self):
        for record in self:
            if record.property_id.state in ['sold', 'canceled']:
                raise UserError("Cannot refuse an offer for a sold or canceled property.")
            record.status = 'refused'
            record.property_id.state = 'offer_received'
    ### End add at 20250112-1135: Add action_refuse method ###
### End add at 20241220-1445: Create y.realestate.property.offer model ###
