# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ChungChi(models.Model):
    _name = 'chung_chi'
    _description = 'Chứng chỉ'
    _rec_name = 'ten_chung_chi'

    nhan_vien_id = fields.Many2one(
        comodel_name='nhan_vien',
        string='Nhân viên',
        required=True,
        ondelete='cascade'
    )
    ten_chung_chi = fields.Char("Tên chứng chỉ", required=True)
    cap_tho_chap = fields.Char("Cơ quan cấp")
    ngay_cap = fields.Date("Ngày cấp", required=True)
    ngay_het_han = fields.Date("Ngày hết hạn")
    so_chung_chi = fields.Char("Số chứng chỉ")
    mo_ta = fields.Text("Mô tả")
    file_chung_chi = fields.Binary("Tệp chứng chỉ")
    file_name = fields.Char("Tên tệp")