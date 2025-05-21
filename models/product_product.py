# -*- coding: utf-8 -*-
from ast import literal_eval
from odoo import models, api, fields


class ProductProduct(models.Model):
    _inherit = 'product.product'

    show_quantity_pos = fields.Boolean(compute='_compute_quantity_location')
    quantity_location = fields.Float("Quantity location", compute='_compute_quantity_location')

    @api.depends('quantity_location')
    def _compute_quantity_location(self):
        """Compute the quantity available in selected locations of products from settings"""
        icp_sudo = self.env['ir.config_parameter'].sudo()
        location_ids_str = icp_sudo.get_param('res.config.settings.location_ids')
        show_quantity_pos = icp_sudo.get_param('res.config.settings.show_quantity')
        self.show_quantity_pos = literal_eval(show_quantity_pos)
        if show_quantity_pos and location_ids_str == '[]':
            for product in self:
                quants = self.env['stock.quant'].search([
                    ('product_id', '=', product.id),
                    ('warehouse_id', '!=', False)
                ])
                product.quantity_location = sum(quants.mapped('available_quantity'))
        else:
            location_ids = literal_eval(location_ids_str)
            for product in self:
                quants = self.env['stock.quant'].search([
                    ('location_id', 'in', location_ids),
                    ('product_id', '=', product.id)
                ])
                product.quantity_location = sum(quants.mapped('available_quantity'))

    @api.model
    def _load_pos_data_fields(self, config_id):
        """This function will add the fields to the function"""
        result = super()._load_pos_data_fields(config_id)
        icp_sudo = self.env['ir.config_parameter'].sudo()
        if icp_sudo.get_param('res.config.settings.show_quantity'):
            result += ['show_quantity_pos','quantity_location']
        return result
