# Base Model Template
# Verified pattern for Odoo 19 model creation

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class {MODEL_CLASS}(models.Model):
    _name = '{MODEL_NAME}'
    _description = '{MODEL_DESCRIPTION}'
    _order = 'id desc'
    
    # Basic Fields
    name = fields.Char(string='Name', required=True, size=100)
    active = fields.Boolean(string='Active', default=True)
    description = fields.Text(string='Description')
    
    # Relational Fields Example
    # partner_id = fields.Many2one('res.partner', string='Partner')
    # line_ids = fields.One2many('related.model', 'parent_id', string='Lines')
    
    # Computed Field Example
    # total = fields.Float(string='Total', compute='_compute_total', store=True)
    
    # @api.depends('line_ids.amount')
    # def _compute_total(self):
    #     for record in self:
    #         record.total = sum(record.line_ids.mapped('amount'))
    
    # Constraint Example
    # @api.constrains('name')
    # def _check_name(self):
    #     for record in self:
    #         if not record.name:
    #             raise ValidationError("Name is required")
    
    # CRUD Override Example
    # @api.model
    # def create(self, vals):
    #     # Custom logic before create
    #     return super({MODEL_CLASS}, self).create(vals)
