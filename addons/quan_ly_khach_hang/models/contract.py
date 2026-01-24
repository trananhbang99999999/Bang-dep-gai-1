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
        # Award loyalty points for new contracts (default: 50 points per contract)
        try:
            for rec in records:
                try:
                    if rec.customer_id:
                        rec.customer_id.add_loyalty_points(50, reason=f'contract:create:{rec.contract_id}', user_id=self.env.uid)
                except Exception:
                    pass
        except Exception:
            pass
        return records

    def unlink(self):
        affected_customers = self.mapped('customer_id')
        res = super(Contract, self).unlink()
        for cust in affected_customers:
            try:
                cust._compute_customer_tier()
            except Exception:
                pass
        return res
