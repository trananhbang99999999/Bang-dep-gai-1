# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ChucVu(models.Model):
    _name = 'chuc_vu'
    _description = 'Bảng chức vụ'
    _rec_name = 'ten_chuc_vu'

    ten_chuc_vu = fields.Char("Tên chức vụ", required=True)
    ma_chuc_vu = fields.Char("Mã chức vụ", required=True)
    mo_ta = fields.Text("Mô tả chức vụ")
    muc_luong_co_ban = fields.Float("Mức lương cơ bản")

    lich_su_cong_tac_ids = fields.One2many(
        comodel_name='lich_su_cong_tac',
        inverse_name='chuc_vu_id',
        string='Lịch sử công tác'
    )