# -*- coding: utf-8 -*-
# Copyright 2017 - Trey - Roberto Lizana
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Account Group Tree",
    "summary": "Add tree view for Chart of accounts",
    "version": "11.0.1.0.0",
    "category": "Accounting & Finance",
    "website": "https://www.trey.com/",
    "author": "Trey, "
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "account",
    ],
    "data": [
        "views/account_account_view.xml"
    ],
    "images": [
        'images/tax_balance.png',
    ]
}
