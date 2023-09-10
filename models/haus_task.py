from odoo import api, fields, models, _
from datetime import datetime
class HausTaskRO(models.Model):
    _name = "haus.task"
    _description = "Haus Schedule Route Optimization Platform"

    flow = fields.Selection([
        ('delivery', 'Delivery'),
        ('pickup', 'Pickup')
    ], string="Flow", required=True)
    
    # schedule_name = fields.Char(string='Schedule Name')
    assignee = fields.Char(string='Assignee')
    
    customer_name = fields.Char(string='Customer Name', invisible=True)
    customer_address = fields.Text(string='Customer Adreess',invisible=True, widget='text', attrs={'rows': 10, 'cols': 100} )
    customer_coordinate = fields.Char(string='Customer Coordinate', invisible=True)
    # jika memilih delivery
    requester_name = fields.Char(string='Requester Name', invisible=True)
    requester_address = fields.Text(string='Requester Adreess',invisible=True, widget='text', attrs={'rows': 10, 'cols': 100} )
    pickup_point_coordinate = fields.Char(string='Pickup Point Coordinate', invisible=True)
    
    start_time = fields.Date(String="Start Time",  invisible=True, default=datetime.today())
    end_time = fields.Date(String="End Time", invisible=True)
    custom_title = fields.Char(string='Custom Title', compute='_compute_custom_title')
    # hours = fields.Float(String="Hours", invisible=True)
    # Button Field
    # button_field = fields.Char(string='Button Field', perform_action='perform_action')
    status = fields.Selection([
        ('ongoing', 'Ongoing'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', store=True, track_visibility='onchange', default='ongoing')

    # Fungsi ini akan dijalankan saat nilai field "Flow" berubah
    @api.onchange('flow')
    def _onchange_flow(self):
        if self.flow == 'delivery':
            self.customer_name = False  # Set visible saat "Delivery" dipilih
        else:
            self.customer_name = True  # Tetap invisible saat "Pickup" atau pilihan lainnya dipilih
    

    @api.depends('flow', 'requester_name', 'customer_name')
    def _compute_custom_title(self):
        for record in self:
            if record.flow == 'pickup':
                record.custom_title = record.requester_name
            elif record.flow == 'delivery':
                record.custom_title = record.customer_name
            else:
                record.custom_title = ""
                 # Method to be called when the button is clicked
    # def perform_action(self):
    #     # Add your custom logic here
    #     self.button_field = "Button Clicked"
    # # def action_done(self) :
    #     print("button clickedd!!!")
   
    def action_done(self):
        self.write({'status': 'done'})
    def action_cancel(self):
        self.write({'status': 'cancelled'})
#     def open_popup_form(self):
#         return {
#             'type': 'ir.actions.act_window',
#             'name': _('Popup Form'),
#             'res_model': 'popup.form.model',
#             'view_mode': 'form',
#             'view_id': self.env.ref('haus_task.view_popup_form').id,
#             'target': 'new',
#             'context': {
#                 'default_field1': '',  # Isi dengan nilai default jika diperlukan
#                 'default_field2': '',
#                 # Isi field lainnya sesuai kebutuhan
#             }
#         }

# class PopupFormModel(models.TransientModel):
#     _name = 'popup.form.model'
#     _description = 'Popup Form Model'

#     field1 = fields.Char(string='Field 1', required=True)
#     field2 = fields.Integer(string='Field 2', required=True)
#     # Tambahkan field lainnya sesuai kebutuhan Anda