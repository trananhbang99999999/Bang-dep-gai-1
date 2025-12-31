# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Loai_tai_san(models.Model):
    _name = 'loai_tai_san'
    _description = 'Bảng loại tài sản'
    _rec_name = 'ten_loai'

    ten_loai = fields.Char("Tên loại", required=True)
    ma_loai = fields.Char("Mã loại", required=True)
    mo_ta = fields.Text("Mô tả loại")
    muc_luong_co_ban = fields.Float("Mức lương cơ bản")
    
