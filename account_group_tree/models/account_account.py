# -*- coding: utf-8 -*-
# Copyright 2017 - Trey - Roberto Lizana
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class AccountAccount(models.Model):
    _inherit = 'account.account'

    group_child_ids = fields.One2many(
        comodel_name='account.account',
        inverse_name='group_id',
        string='Child Groups')
