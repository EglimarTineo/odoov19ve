# Part of Sumitic. See LICENSE file for full copyright and licensing details.
{
    "name": "Venezuela - Localización Sumitic",
    "version": "19.0.1.0.0",
    "category": "Accounting/Localizations/Account Charts",
    "summary": "Localización contable estandarizada para Venezuela por Sumitic",
    "author": "Sumitic",
    "website": "https://www.sumitic.lat/",
    "license": "LGPL-3",
    "depends": [
        "account",
        "base_vat",
        "purchase",
        "sale",
    ],
    "data": [
        "data/res_currency_data.xml",
        "data/template/account.tax.group.csv",
        "data/template/account.account.csv",
        "data/template/account_tax_data.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
