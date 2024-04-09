from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    domain = fields.Char('Domain')
    domain_cpa = fields.Char('Domain CPA')
    codification = fields.Char('Codification')
    source = fields.Char('source')
    name_pos = fields.Char('name')
    address_pos = fields.Char('adrs')
    pos_phone_one = fields.Char('phone')
    pos_phone_two = fields.Char('phone')
    pos_wilaya = fields.Char('wilaya')
    pos_commune = fields.Char('commune')
    ek_user_emails = fields.Char('users')
    create_by = fields.Char('create_by')


class ResConfig(models.TransientModel):
    _inherit = 'res.config.settings'

    domain = fields.Char(string="Domain ALSALAM", store=True)
    domain_cpa = fields.Char(string="Domain CPA", store=True)

    internal_project_id = fields.Char()
    leave_timesheet_task_id = fields.Char()

    @api.model
    def get_values(self):
        """ getting field values"""
        res = super(ResConfig, self).get_values()
        company = self.env.company

        company and res.update(
            domain =company.domain,
            domain_cpa =company.domain_cpa,

        )
        return res

    def set_values(self):
        """setting field values"""

        res = super(ResConfig, self).set_values()
        company = self.env.company
        company and company.write({
            'domain': self.domain,
            'domain_cpa': self.domain_cpa,

        })
        return res