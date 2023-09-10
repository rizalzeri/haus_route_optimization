from odoo import api, fields, models, _
from datetime import datetime
class HausTaskRO(models.Model):
    _name = "haus.dashboard"
    _description = "Haus Dashboard Route Optimization Platform"
    task_id = fields.Many2one('haus.task', string='task')
    # ...

    @api.depends('task_id')
    def compute_hours_from_task(self):
        for dashboard in self:
            if dashboard.task_id:
                dashboard.hours = dashboard.task_id.hours
            else:
                dashboard.hours = 0  # Atur nilai default sesuai kebutuhan Anda

    status = fields.Float(string='status', compute='compute_hours_from_task', store=True)