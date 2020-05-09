# Copyright 2020 Stefano Consolaro (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ServiceTemplate(models.Model):
    """
    Model of a service with definition of the required components
    """

    # model
    _name = 'service.template'
    _description = 'Model of a service'

    # fields
    # name
    name = fields.Char('Name', required=True)
    # global service reference
    service_global_ids = fields.Many2many('service.global', string='Global service')

    # standard duration
    duration = fields.Integer('Duration', required=True)
    # duration uom
    duration_uom_id = fields.Many2one('uom.uom', string='Unit of Measure')

    # expected vehicles
    exp_vehicle_ids = fields.Many2many('expected.vehicle', string='Vehicles')
    # expected jobs
    exp_job_ids = fields.Many2many('expected.job', string='Jobs')
    # expected equipments
    exp_equipment_ids = fields.Many2many('expected.equipment', string='Equipments')

    # product reference used to valorize
    product_id = fields.Many2one('product.product', string='Product reference')

    x_color = fields.Char('Color')
