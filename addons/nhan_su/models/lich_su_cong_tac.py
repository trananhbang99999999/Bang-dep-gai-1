# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LichSuCongTac(models.Model):
    _name = 'lich_su_cong_tac'
    _description = 'Lịch sử công tác'
    _rec_name = 'nhan_vien_id'
    _order = 'ngay_bat_dau desc'

    nhan_vien_id = fields.Many2one(
        comodel_name='nhan_vien',
        string='Nhân viên',
        required=True,
        ondelete='cascade'
    )
    phong_ban_id = fields.Many2one(
        comodel_name='phong_ban',
        string='Phòng ban',
        required=True
    )
    chuc_vu_id = fields.Many2one(
        comodel_name='chuc_vu',
        string='Chức vụ',
        required=True
    )
    ngay_bat_dau = fields.Date("Ngày bắt đầu", required=True)
    ngay_ket_thuc = fields.Date("Ngày kết thúc")
    mo_ta = fields.Text("Mô tả công tác")