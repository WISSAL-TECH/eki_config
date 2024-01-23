from odoo import models, fields, api

class ResConfig(models.TransientModel):
    _inherit = 'res.config.settings'

    domain = fields.Char(string="Domain", store=True)

    internal_project_id = fields.Char()
    leave_timesheet_task_id = fields.Char()

    def set_values(self):
        """employee setting field values"""
        res = super(ResConfig, self).set_values()
        self.env['ir.config_parameter'].set_param('eki_config.domain', self.domain)
        return res

    def get_values(self):
        """employee limit getting field values"""
        res = super(ResConfig, self).get_values()
        value = self.env['ir.config_parameter'].sudo().get_param('eki_config.domain')
        res.update(
            domain=str(value)
        )
        return res