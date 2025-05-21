# -*- coding: utf-8 -*-
from odoo import models, fields


class PosConfig(models.Model):
    _inherit = 'pos.config'

    enable_quantity_warning = fields.Boolean(
        string='Enable Quantity Warnings',
        default=False,
        help='Show warnings for low stock products'
    )
    minimum_quantity = fields.Integer(
        string='Minimum Quantity',
        default=0,
        help='Products with stock below this value will be showed with a warning color',
    )
