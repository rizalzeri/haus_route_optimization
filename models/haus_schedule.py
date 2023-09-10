from odoo import api, fields, models, _
from datetime import datetime
class HausScheduleRO(models.Model):
    _name = "haus.schedule"
    _description = "Haus Schedule Route Optimization Platform"

    flow = fields.Selection([
        ('delivery', 'Delivery'),
        ('pickup', 'Pickup')
    ], string="Flow", required=True)
    
    schedule_name = fields.Char(string='Schedule Name')
    assignee = fields.Char(string='Assignee')
    repeat_every = fields.Selection([
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('by date', 'By Date')
    ])
    status = fields.Selection([
        ('ongoing', 'Ongoing'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', store=True, track_visibility='onchange', default='ongoing')

    # jika memilih delivery
    customer_name = fields.Char(string='Customer Name', invisible=True)
    customer_address = fields.Text(string='Customer Adreess',invisible=True, widget='text', attrs={'rows': 10, 'cols': 100} )
    customer_coordinate = fields.Char(string='Customer Coordinate', invisible=True)
    # jika memilih delivery
    requester_name = fields.Char(string='Requester Name', invisible=True)
    requester_address = fields.Text(string='Requester Adreess',invisible=True, widget='text', attrs={'rows': 10, 'cols': 100} )
    pickup_point_coordinate = fields.Char(string='Pickup Point Coordinate', invisible=True)
    
    active_from = fields.Date(String="Active From",  invisible=True, default=datetime.today())
    active_to = fields.Date(String="Active To", invisible=True)
    hours = fields.Float(String="Hours", invisible=True)

    days = fields.Selection([
        ('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10'),
        ('11', '11'),('12', '12'),('13', '13'),('14', '14'),('15', '15'),('16', '16'),('17', '17'),('18', '18'),('19', '19'),('20', '20'),
        ('21', '21'),('22', '22'),('23', '23'),('24', '24'),('25', '25'),('26', '26'),('27', '27'),('28', '28'),('29', '29'),('30', '30'),('31', '31'),
    ])
    # Fungsi ini akan dijalankan saat nilai field "Flow" berubah
    @api.onchange('flow')
    def _onchange_flow(self):
        if self.flow == 'delivery':
            self.customer_name = False  # Set visible saat "Delivery" dipilih
        else:
            self.customer_name = True  # Tetap invisible saat "Pickup" atau pilihan lainnya dipilih
    def action_done(self):
        self.write({'status': 'done'})
    def action_cancel(self):
        self.write({'status': 'cancelled'})