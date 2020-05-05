# Copyright 2020 Stefano Consolaro (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, api


class ServiceAllocate(models.Model):
    """
    Allocated service with definition of all the template components
    """

    # model
    _name = 'service.allocate'
    _description = 'Allocate service'

    # fields
    # template service reference
    service_template_id = fields.Many2one('service.template', string='Teplate service')

    # assigned vehicles
    vehicle_ids = fields.Many2many('fleet.vehicle', string='Vehicles')
    # assigned employee
    employee_ids = fields.Many2many('hr.employee', string='Équipe')
    # assigned equipments
    equipment_ids = fields.Many2many('maintenance.equipment', string='Equipments')

    # locality reference
    locality = fields.Char('Locality')

    # skeduled start time
    start_sked = fields.Datetime('Start skeduled')
    # effective start time
    start_real = fields.Datetime('Start real')
    # effective stop time
    stop_real = fields.Datetime('Stop real')

    # state of the service
    state_id = fields.Many2one('service.state', string='State')
