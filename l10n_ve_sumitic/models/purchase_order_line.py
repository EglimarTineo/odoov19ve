# Part of Sumitic. See LICENSE file for full copyright and licensing details.
from odoo import models, fields

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    # Aumentamos la precisión del precio unitario a 10 decimales para evitar errores de redondeo en moneda extranjera
    price_unit = fields.Float(digits=(16, 10))
