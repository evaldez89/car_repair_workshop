from odoo import api, models


class CarServicesReport(models.AbstractModel):
    _name = 'report.car_workshop.report_car_services'
    _description = 'Car Services Report'

    @api.model
    def _get_report_values(self, docids, data=None):
      
        report = self.env['ir.actions.report']._get_report_from_name('car_workshop.report_car_services')
        car_ids = self.env['res.partner.car'].search([])
        car_service_data = data.get('data')
        return {
            'doc_ids': car_ids.ids,
            'doc_model': report.model,
            'docs': car_ids,
            'get_data_from_report': car_service_data
        }
