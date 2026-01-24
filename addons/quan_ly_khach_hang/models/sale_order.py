from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _name = 'sale_order'
    _description = 'Bảng chứa thông tin lịch sử giao dịch'

    sale_order_id = fields.Char("Mã lịch sử giao dịch", required=True)
    sale_order_name = fields.Char("Tên lịch sử giao dịch")
    customer_id = fields.Many2one('customer', string="Khách hàng", required=True, ondelete='cascade')
    date_order = fields.Datetime("Ngày đặt hàng", required=True)
    amount_total = fields.Float("Tổng giá trị đơn hàng", required=True)

    # Đặt tên hiển thị cho bản ghi
    def name_get(self):
        result = []
        for record in self:
            name = f"[{record.sale_order_id}] {record.sale_order_name}"
            result.append((record.id, name))
        return result

    @api.model_create_multi
    def create(self, vals_list):
        records = super(SaleOrder, self).create(vals_list)
        try:
            self.env['cskh_task'].create_from_sale_order(records)
        except Exception:
            pass
        try:
            self.env['sales_task'].create_from_sale_order(records)
        except Exception:
            pass
        # Recompute loyalty points and tiers from history for affected customers
        try:
            affected_customers = records.mapped('customer_id')
            for cust in affected_customers:
                try:
                    cust.recompute_loyalty_points()
                    cust._compute_customer_tier()
                except Exception:
                    _logger.exception('Failed to update loyalty/tier for customer %s', cust.id)
        except Exception:
            _logger.exception('Error while processing loyalty points on sale order create')
        return records

    def unlink(self):
        affected_customers = self.mapped('customer_id')
        res = super(SaleOrder, self).unlink()
        for cust in affected_customers:
            try:
                cust.recompute_loyalty_points()
                cust._compute_customer_tier()
            except Exception:
                _logger.exception('Failed to update customer after sale_order unlink %s', cust.id)
        return res
