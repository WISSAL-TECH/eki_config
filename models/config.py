from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    domain = fields.Char('domain')


class ResConfig(models.TransientModel):
    _inherit = 'res.config.settings'

    domain = fields.Char(string="Domain", store=True)

    internal_project_id = fields.Char()
    leave_timesheet_task_id = fields.Char()

    @api.model
    def get_values(self):
        """ getting field values"""
        res = super(ResConfig, self).get_values()
        company = self.env.company

        company and res.update(
            domain =company.domain,

        )
        return res

    def set_values(self):
        """setting field values"""

        res = super(ResConfig, self).set_values()
        company = self.env.company
        company and company.write({
            'domain': self.domain,

        })
        return res