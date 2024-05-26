from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    domain = fields.Char('Domain', default="https://apiadmin-preprod-alsalam.ekiclik.dz")
    domain_cpa = fields.Char('Domain CPA', default="https://apiadmin.cpa-preprod.ekiclik.dz")
    codification = fields.Char('Codification', required=True)
    source = fields.Char('source', default="odoo", invisible=True)
    name_pos = fields.Char('name')
    address_pos = fields.Char('adrs')
    pos_phone_one = fields.Char('phone')
    pos_phone_two = fields.Char('phone')
    pos_wilaya = fields.Char('wilaya', required= True)
    pos_commune = fields.Char('commune')
    ek_user_emails = fields.Char('users')
    create_by = fields.Char('create_by')
    pos = fields.Boolean(string="Pos")
    users = fields.Many2one("res.users", string="Credit analyst")
    pos_user = fields.Many2one("res.users", string="POS")
    state_id = fields.Many2one(
        'res.country.state', compute='_compute_address', inverse='_inverse_state',
        string="Fed. State", domain="[('country_id', '=?', country_id)]"
    )
    city = fields.Char(compute='_compute_address', inverse='_inverse_city')
    street = fields.Char(compute='_compute_address', inverse='_inverse_street')
    phone = fields.Char(related='partner_id.phone', store=True, readonly=False)



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