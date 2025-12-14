from odoo import models, fields, api
from datetime import datetime, timedelta

class RealEstate(models.Model):
    _name = 'y.realestate.property'
    _description = "Real Estate advertisement"
    _order = 'id desc'

    name = fields.Char(string="Name", required=True)
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
    