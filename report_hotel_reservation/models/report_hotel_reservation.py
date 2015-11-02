# -*- coding: UTF-8 -*-
# --------------------------------------------------------------------------
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012-Today Serpent Consulting Services PVT. LTD.
#    (<http://www.serpentcs.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# ---------------------------------------------------------------------------
from openerp import models, fields

AVAILABLE_STATES = [
    ('draft', 'Draft'),
    ('confirm', 'Confirm'),
    ('done', 'Done')]


class report_hotel_reservation_status(models.Model):

    _name = "report.hotel.reservation.status"
    _description = "Reservation By State"
    _auto = False

    reservation_no = fields.Char('Reservation No', size=64, readonly=True)
    nbr = fields.Integer('Reservation', readonly=True)
    state = fields.Selection(AVAILABLE_STATES, 'State', size=16,
                             readonly=True)

    def init(self, cr):
        """
        This method is for initialization for report hotel reservation
        status Module.
        @param self: The object pointer
        @param cr: database cursor
        """
        cr.execute("""
            create or replace view report_hotel_reservation_status as (
                select
                    min(c.id) as id,
                    c.reservation_no,
                    c.state,
                    count(*) as nbr
                from
                    hotel_reservation c
                group by c.state,c.reservation_no
            )""")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
