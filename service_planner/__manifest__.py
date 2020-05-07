# Copyright 2019 Stefano Consolaro (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name":     "Vertical NGO - Service Plan",
    "summary":  "Management of service planning.",
    "version":  "12.0.1.0.0",

    "author":   "Associazione PNLUG - Gruppo Odoo, Odoo Community Association (OCA)",
    "website":  "https://gitlab.com/PNLUG/",
    "license":  "AGPL-3",

    "category": "Logistics",

    "depends": [
        'fleet',
        'maintenance',
        'hr',
        'product',
        ],
    "data": [
        'security/ir.model.access.csv',
        'views/service_menu.xml',
        'views/service_view.xml',
        ],
    'installable': True,
}
