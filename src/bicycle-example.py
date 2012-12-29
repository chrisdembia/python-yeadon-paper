#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sympy as sym
import sympy.physics.mechanics as me

pi = sym.symbols('pi')
sommersault = sym.symbols('sommersault')
elevation, abduction, rotation = sym.symbols('elevation abduction rotation')
flexion = sym.symbols('betay')
Ls0, Ls4, La2, La0, La6 = sym.symbols('Ls0, Ls4 La2 La0 La6')
lambdafl, lambdast = sym.symbols('lambdafl lambdast')
lst, lsp, lcs, hbb, rr = sym.symbols('lst lsp lcs hbb rr')

bicycle = me.ReferenceFrame('B')
chest = bicycle.orientnew('C', 'Space', (pi, -pi / 2, -(pi / 2 - sommersault)), 'XZY')
midarm = chest.orientnew('A1', 'Body', (elevation, abduction, rotation), 'XYZ')
forearm = midarm.orientnew('A2', 'Axis', (flexion, midarm.y))

origin = me.Point('o')

seat = me.Point('s')
seatx = sym.sqrt(lcs**2 - (rr - hbb)**2) - (lst + lsp) * sym.cos(lambdast)
seaty = 0
seatz = (hbb + (lst + lsp) * sym.sin(lambdast))
seat.set_pos(origin,  seatx * bicycle.x + seaty * bicycle.y + seatz * bicycle.z)

shoulder = me.Point('La0')
shoulderwidth = sym.symbols('sw')
shoulder.set_pos(seat, shoulderwidth / 2 * chest.x + 0 * chest.y + (Ls4 - Ls0) * chest.z)

hand = me.Point('h')
hand.set_pos(shoulder, (La2 - La0) * midarm.z + (La6 - La2) * forearm.z)

handlebar = me.Point('La0')
d, e, f = sym.symbols('d e f')
handlebar.set_pos(origin, d * bicycle.x + e * bicycle.y + f * bicycle.z)

zero = hand.pos_from(origin) - handlebar.pos_from(origin)

f1 = zero.dot(chest.x)
f2 = zero.dot(chest.y)
f3 = zero.dot(chest.z)
f4 = midarm.y.dot(chest.z)
