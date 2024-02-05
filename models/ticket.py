from odoo import fields, models

class Ticket(models.Model):
    _name = 'todo.ticket'
    _description = 'This is a description'
    _order = 'id desc'
    # _sql_constraints
    name = fields.Char(string="Name")
    number = fields.Char(string="Number")
    tag = fields.Many2one('todo.tag', string="Tag")
    state = fields.Selection([('new', 'New'), ('doing', 'Doing'), ('done', 'Done')], string="State", default="new")
    file = fields.Binary(string="File")
    assign_to = fields.Many2one('res.users', string="Assign To")
    description = fields.Text(string="Description")
