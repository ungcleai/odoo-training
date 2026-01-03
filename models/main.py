from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime, timedelta

class RealEstate(models.Model):
    _name = 'y.realestate.property'
    _description = "Real Estate advertisement"
    _order = 'id desc'

    name = fields.Char(string="Name", required=True, size=100)
    description = fields.Text(string="Description", required=False)
    postcode = fields.Char(string="Postcode", required=False)
    date_availability = fields.Date(
        string="Date availability", 
        required=False, 
        copy=False,
        default=lambda self: (datetime.today() + timedelta(days=90)).date()
    )
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling price", required=False, readonly=True)
    bed_room = fields.Integer(string="Bed room", required=False, default=2, copy=False)
    living_area = fields.Integer(string="Living area", required=False)
    facades = fields.Integer(string="Facades", required=False)
    garage = fields.Boolean(string="Garage", required=False)
    garden = fields.Boolean(string="Garden", required=False)
    garden_area = fields.Integer(string="Garden area", required=False)
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=[
            ('north', 'North'),
            ('west', 'West'),
            ('east', 'East'),
            ('south', 'South'),
        ],
        required=False,
        default='north',
        help="Select the orientation of the garden."
    )
    
    ### Start add at 20250112-1045: Add _onchange_garden method ###
    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = False
    ### End add at 20250112-1045: Add _onchange_garden method ###
#### -------------------------------------------------- ####

### Start add at 20250110-1445: Add active and state fields for property status management ###
class RealEstatePropertyExtension(models.Model):
    _inherit = 'y.realestate.property'
    
    active = fields.Boolean(
        string="Active",
        required=False,
        default=True,
        help="Manage the status of the property usage"
    )
    ### Start add at 20250111-1455: Add property_type_id Many2one field ###
    property_type_id = fields.Many2one(
        'y.realestate.property.type',
        string="Property Type"
    )
    ### End add at 20250111-1455: Add property_type_id Many2one field ###
    ### Start add at 20241220-1450: Add offer_ids One2many field ###
    offer_ids = fields.One2many(
        'y.realestate.property.offer',
        'property_id',
        string="Offers"
    )
    ### End add at 20241220-1450: Add offer_ids One2many field ###
    ### Start add at 20241220-1502: Add property_tag_id Many2many field ###
    property_tag_id = fields.Many2many(
        'y.realestate.property.tag',
        string="Property Tags"
    )
    ### End add at 20241220-1502: Add property_tag_id Many2many field ###
    ### Start add at 20250112-1000: Add total_area computed field ###
    total_area = fields.Float(
        string="Total Area (sqm)",
        compute="_compute_total_area",
        store=True,
        help="Show Property Total Area"
    )
    ### End add at 20250112-1000: Add total_area computed field ###
    ### Start add at 20250112-1010: Add best_price computed field ###
    best_price = fields.Float(
        string="Best Offer Price",
        compute="_compute_best_price",
        store=True
    )
    ### End add at 20250112-1010: Add best_price computed field ###
    state = fields.Selection(
        string="State",
        selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled')
        ],
        required=True,
        default='new',
        copy=False,
        help="The current state of the property."
    )
    
    ### Start add at 20250112-1000: Add _compute_total_area method ###
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = (record.living_area or 0) + (record.garden_area or 0)
    ### End add at 20250112-1000: Add _compute_total_area method ###
    
    ### Start add at 20250112-1010: Add _compute_best_price method ###
    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped('price') or [0])
    ### End add at 20250112-1010: Add _compute_best_price method ###
    
    ### Start add at 20250112-1100: Add action_cancel method ###
    def action_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise UserError("A sold property cannot be canceled.")
            record.state = 'canceled'
    ### End add at 20250112-1100: Add action_cancel method ###
    
    ### Start add at 20250112-1105: Add action_set_sold method ###
    def action_set_sold(self):
        for record in self:
            if record.state == 'canceled':
                raise UserError("A canceled property cannot be set as sold.")
            record.state = 'sold'
    ### End add at 20250112-1105: Add action_set_sold method ###
### End add at 20250110-1445: Add active and state fields for property status management ###
