# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class ProjectTask(models.Model):
    _name = 'project_task'
    _description = 'Bảng chứa thông tin nhiệm vụ'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    project_task_id = fields.Char("Mã nhiệm vụ", required=True, copy=False, default="New", index=True)
    name = fields.Char("Tên nhiệm vụ", required=True, tracking=True)

    customer_id = fields.Many2one(
        'customer', string="Khách hàng",
        required=True, ondelete='cascade', index=True
    )

    nhan_vien_id = fields.Many2one(
        'nhan_vien', string="Nhân viên phụ trách",
        ondelete='set null', tracking=True
    )

    description = fields.Text("Mô tả")

    deadline = fields.Date("Hạn chót", tracking=True)
    actual_completion_date = fields.Date("Ngày hoàn thành thực tế", tracking=True)

    state = fields.Selection([
        ('todo', 'Chưa làm'),
        ('doing', 'Đang làm'),
        ('done', 'Hoàn thành'),
        ('cancel', 'Hủy'),
    ], default='todo', string="Trạng thái", tracking=True)

    is_overdue = fields.Boolean("Quá hạn", compute="_compute_is_overdue", store=True)

    @api.depends('deadline', 'actual_completion_date', 'state')
    def _compute_is_overdue(self):
        today = date.today()
        for rec in self:
            if rec.state == 'done' and rec.actual_completion_date and rec.deadline:
                rec.is_overdue = rec.actual_completion_date > rec.deadline
            elif rec.state != 'done' and rec.deadline:
                rec.is_overdue = today > rec.deadline
            else:
                rec.is_overdue = False

    def action_start(self):
        for rec in self:
            rec.state = 'doing'

    def action_done(self):
        for rec in self:
            if rec.state == 'cancel':
                raise ValidationError("Công việc đã hủy, không thể hoàn thành.")
            rec.state = 'done'
            if not rec.actual_completion_date:
                rec.actual_completion_date = fields.Date.today()

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def name_get(self):
        res = []
        for rec in self:
            code = rec.project_task_id or ''
            display = f"[{code}] {rec.name}" if code else rec.name
            res.append((rec.id, display))
        return res

    @api.model
    def create(self, vals):
        if vals.get('project_task_id', 'New') == 'New':
            vals['project_task_id'] = self.env['ir.sequence'].next_by_code('project_task.id') or 'TASK00001'
        return super().create(vals)
