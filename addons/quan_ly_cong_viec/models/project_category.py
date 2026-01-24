# -*- coding: utf-8 -*-
from odoo import models, fields


class ProjectCategory(models.Model):
    _name = 'project.category'
    _description = 'Phân loại/Dự án công việc'
    _order = 'name asc'

    name = fields.Char("Tên phân loại", required=True, unique=True)
    description = fields.Text("Mô tả")
    active = fields.Boolean("Hoạt động", default=True)
    color = fields.Char(
        "Màu sắc",
        default="#3498db",
        help="Mã màu hex (vd: #FF0000)"
    )

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Tên phân loại phải duy nhất!'),
    ]
