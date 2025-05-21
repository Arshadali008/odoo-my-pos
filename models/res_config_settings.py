# -*- coding: utf-8 -*-
from ast import literal_eval
from email.policy import default

from odoo import api, fields, models, Command


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    show_quantity = fields.Boolean(string='Show Quantity',help='This field is used to enable setting'
                                        'show quantity in settings', default=False)
    location_ids = fields.Many2many('stock.location', string='Stock Locations',
                                    help='Set the stock locations',)

    @api.model
    def get_values(self):
        """Get the values from settings."""
        res = super(ResConfigSettings, self).get_values()
        icp_sudo = self.env['ir.config_parameter'].sudo()
        show_quantity = icp_sudo.get_param('res.config.settings.show_quantity')
        location_ids_str = icp_sudo.get_param('res.config.settings.location_ids')
        location_ids = False
        if location_ids_str: location_ids = [(Command.set(literal_eval(location_ids_str)))]
        res.update({
            'show_quantity': show_quantity,
            'location_ids': location_ids,
        })
        return res

    @api.model
    def set_values(self):
        """Set the values. The new values are stored in the configuration parameters."""
        res = super(ResConfigSettings, self).set_values()
        save_show_quantity = self.env['ir.config_parameter'].sudo().set_param('res.config.settings.show_quantity',
                                                                              self.show_quantity)
        if save_show_quantity:self.env['ir.config_parameter'].sudo().set_param('res.config.settings.location_ids',
                                                             self.location_ids.ids if self.location_ids else '[]')
        return res
