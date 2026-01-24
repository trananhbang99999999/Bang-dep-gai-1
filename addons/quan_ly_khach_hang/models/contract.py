from odoo import models, fields, api

class Contract(models.Model):
    _name = 'contract'
    _description = 'Bảng chứa thông tin hợp đồng'

    contract_id = fields.Char("Mã hợp đồng", required=True)
    contract_name = fields.Char("Tên hợp đồng")
    customer_id = fields.Many2one('customer', string="Khách hàng", required=True, ondelete='cascade')
    start_date = fields.Date("Ngày bắt đầu hợp đồng", required=True)
    end_date = fields.Date("Ngày kết thúc hợp đồng", required=True)
    state = fields.Selection([
        ('active', 'Đang hoạt động'),
        ('ended', 'Đã kết thúc')
    ], string="Trạng thái hợp đồng", required=True)

    # Đặt tên hiển thị cho bản ghi
    def name_get(self):
        result = []
        for record in self:
            name = f"[{record.contract_id}] {record.contract_name}"
            result.append((record.id, name))
        return result

    @api.model_create_multi
    def create(self, vals_list):
        records = super(Contract, self).create(vals_list)
        try:
            self.env['cskh_task'].create_from_contract(records)
        except Exception:
            pass
        try:
            self.env['sales_task'].create_from_contract(records)
        except Exception:
            pass
        return records
