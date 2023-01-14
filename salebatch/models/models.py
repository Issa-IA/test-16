from odoo import _, api, fields, models


class   Batchmodel(models.Model):
    _name = "batchsale"
    _description = 'sal par batch'
    batch_number = fields.Integer("Batch number")
    batch_date = fields.Datetime(string='Batch date')
    batch_quantity = fields.Float(string="Batch Quantity")
    batch_name= fields.Char(string='Batch name')
    batch_sale = fields.Many2one("Batchsal", string='Sale Number')
    _sql_constraints = [('name_of_field_unique', 'unique(batch_number)','Batch number must be unique')]


    def name_get(self):
        result = []
        for model in self:
            name = str(model.batch_number) +"("+ model.batch_name  + ")"
            result.append((model.id, name))
        return result

class Salelinebatch(models.Model):
    _inherit    = 'sale.order.line'
    sale_line_batch = fields.Many2one("batchsale", string='Batch Number')

class SalebatchHerit(models.Model):
    _inherit    = 'sale.order'
    def action_confirm(self):
        res = super(SalebatchHerit, self).action_confirm()
        for rec in self:
            for line in rec.order_line:
                quatity = line.sale_line_batch.batch_quantity
                quatity_1 = quatity - line.product_uom_qty
                line.sale_line_batch.batch_quantity= quatity_1

        return res


class Purchasebatch(models.Model):
    _inherit    = 'purchase.order'
    purchase_batch=fields.One2many('batchsale', inverse_name='batch_sale',string="Batchs")




