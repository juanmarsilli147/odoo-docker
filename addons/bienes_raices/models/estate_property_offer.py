from odoo import models, fields


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property Offer"

    price = fields.Float(string="Precio", required=True)
    state = fields.Selection([
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ], string="Status", copy=False)
    property_id = fields.Many2one(comodel_name='estate.property', string="Property")
    partner_id = fields.Many2one(comodel_name='res.partner', string="Partner")

    
