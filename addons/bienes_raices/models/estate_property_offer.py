from odoo import api, models, fields


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property Offer"

    price = fields.Float(string="Precio", required=True)
    state = fields.Selection([
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ], string="Status", copy=False)
    validity = fields.Integer(string="Validity (days)", default=7)
    deadline_date = fields.Date(string="Date Deadline", compute='_compute_deadline_date')
    property_id = fields.Many2one(comodel_name='estate.property', string="Property")
    partner_id = fields.Many2one(comodel_name='res.partner', string="Partner")

    @api.depends("validity")
    def _compute_deadline_date(self):
        for offer in self:
            offer.deadline_date = fields.Date.add(offer.create_date or fields.Date.today(), days=offer.validity)

    def _inverse_deadline_date(self):
        for offer in self:
            create_date = fields.Date.to_date(offer.create_date)
            offer.validity = (offer.deadline_date - create_date).days
    
