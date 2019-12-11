# -*- coding: utf-8 -*-
# Copyright (c) 2019, 	9t9it and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

from pos_bahrain.api.item import get_conversion_factor


def before_save(doc, method):
    doc.pb_conversion_factor = get_conversion_factor(doc.item_code, doc.uom)
