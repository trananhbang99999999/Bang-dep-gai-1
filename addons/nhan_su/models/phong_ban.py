# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PhongBan(models.Model):
    _name = 'phong_ban'
    _description = 'Bảng phòng ban'
    _rec_name = 'ten_phong'

    ten_phong = fields.Char("Tên phòng ban", required=True)
    ma_phong = fields.Char("Mã phòng ban", required=True)
    mo_ta = fields.Text("Mô tả phòng ban")

    nhan_vien_ids = fields.One2many(
        comodel_name='nhan_vien',
        inverse_name='phong_ban_id',
        string='Nhân viên'
    )

    lich_su_cong_tac_ids = fields.One2many(
        comodel_name='lich_su_cong_tac',
        inverse_name='phong_ban_id',
        string='Lịch sử công tác'
    )