from odoo import models, fields, api
from datetime import timedelta

class GymMember(models.Model):
    _name = 'gym.member'
    _description = 'Gym Member'
    
    name = fields.Char(string='Nombre', required=True)
    dni = fields.Char(string='DNI', required=True)
    email = fields.Char(string='Email', required=True)
    plan_id = fields.Many2one('gym.plan', string='Plan', required=True)
    start_date = fields.Date(string='Fecha de inicio', required=True)
    end_date = fields.Date(string='Fecha de fin', required=True, compute='_compute_end_date')
    active_membership = fields.Boolean(string='Miembro Activo', compute='_compute_active_membership')
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('active', 'Activo'),
        ('expired', 'Vencido')
    ], string='Estado', default='draft')


    @api.depends('start_date', 'plan_id.duration_days')
    def _compute_end_date(self):
        for record in self:
            if record.start_date and record.plan_id.duration_days:
                record.end_date = record.start_date + timedelta(days=record.plan_id.duration_days)
            else:
                record.end_date = False
    

    @api.depends('end_date')
    def _compute_active_membership(self):
        for record in self:
            if record.end_date and record.end_date > fields.Date.today():
                record.active_membership = True
            else:
                record.active_membership = False
    
    @api.constrains('dni')
    def _check_dni(self):
        for record in self:
            if record.dni:
                if not record.dni.isdigit():
                    raise ValidationError("El DNI debe contener solo números.")
                
                domain = [('dni', '=', record.dni), ('id', '!=', record.id)]
                if self.search_count(domain) > 0:
                    raise ValidationError("El DNI ya se encuentra registrado.")


    def action_renew_membership(self):
        for record in self:
            if record.end_date:
                record.end_date = record.end_date + timedelta(days=30)
            else:
                record.end_date = fields.Date.today() + timedelta(days=30)


class GymPlan(models.Model):
    _name = 'gym.plan'
    _description = 'Gym Plan'
    
    name = fields.Char(string='Nombre', required=True)
    duration_days = fields.Integer(string='Duración en días', required=True)
    price = fields.Float(string='Precio', required=True)




    
    