from odoo import fields, models

class Tag(models.Model):
    _name = 'todo.tag'
    name = fields.Char(string="Name")
