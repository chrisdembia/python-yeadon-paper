#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sympy as sym
import sympy.physics.mechanics as me

pi = sym.symbols('pi')
sommersault = sym.symbols('sommersault')

elevation, abduction, rotation = sym.symbols('elevation abduction rotation')
flexion = sym.symbols('betay')

# The following are measurements taken for the Yeadon model.
Ls0L, Ls4L, La2L, La0L, La5L = sym.symbols('Ls0, Ls4 La2 La0 La6')
Ls4w = sym.symbols('Ls4w') # shoulder width

# The following variables come from geometric measurements of the bicycle.
# lambdafl :
# lambdast : seat tube angle
# lst : seat tube length (bottom bracket to top tube)
# lsp : seat post length
# lcs : length of rear chainstay projection
# hbb : bottom bracket height
# rr : rear wheel radius
lambdafl, lambdast = sym.symbols('lambdafl lambdast')
lst, lsp, lcs, hbb, rr = sym.symbols('lst lsp lcs hbb rr')

seat_tube_length, seat_post_length = sym.symbols('lst, lsp')
rear_chainstay_length, bottom_bracket_height = sym.symbols('lcs, hbb')
rear_wheel_radius = sym.symbols('rr')

bicycle = me.ReferenceFrame('B')

# First we orient the hip relative to the bicycle frame. The bicycle is
# located in a reference frame which has the x axis pointing forward, y axis
# to the right, and the z axis downwards. The Yeadon model's reference
# orientation is within a reference frame with the x axis to the left, y
# axis pointing rearward ad z axis pointing upward. We first rotate the
# pelvis such that it is aligned correctly with the bicycle coordinate
# system.

torso = bicycle.orientnew('PTC', 'Space',
                          (pi, -pi / 2, -(pi / 2 - sommersault)), 'XZY')
pelvis_trunk_chest = bicycle.orientnew('PTC', 'Space', (pi, -pi / 2, -(pi / 2 - sommersault)), 'XZY')

# The left midarm, A1, is oriented with respect to the torso through the
# body fixed XYZ rotations through the elevation, abduction, and rotation
# angles.
midarm = chest.orientnew('A1', 'Body', (elevation, abduction, rotation), 'XYZ')

# The forearm is rotated through a simple rotation through the flexion angle
# about the Y axis.
forearm = midarm.orientnew('A2', 'Axis', (flexion, midarm.y))

# The origin is defined as the contact point of the bicycle rear wheel.
origin = me.Point('o')

# The "seat" location can be defined using some bicycle geometry, and this
# will be where the Yeadon model local origin will be located.
seat = me.Point('s')

seatx = sym.sqrt(lcs**2 - (rr - hbb)**2) - (lst + lsp) * sym.cos(lambdast)
seatz = (hbb + (lst + lsp) * sym.sin(lambdast))

seat.set_pos(origin,  seatx * bicycle.x + seatz * bicycle.z)

# The shoulders are located relative to the seat using the Yeadon
# measurements.
shoulder = me.Point('La0')
shoulder.set_pos(seat, shoulderwidth / 2 * torso.x + (Ls4 - Ls0) * torso.z)

# The point on the hands which will connect to the handlebar grip is located
hand = me.Point('h')
hand.set_pos(shoulder, (La2 - La0) * midarm.z + (La5 - La2) * forearm.z)

handlebar = me.Point('La0')
d, e, f = sym.symbols('d e f')
handlebar.set_pos(origin, d * bicycle.x + e * bicycle.y + f * bicycle.z)

zero = hand.pos_from(origin) - handlebar.pos_from(origin)

f1 = zero.dot(chest.x)
f2 = zero.dot(chest.y)
f3 = zero.dot(chest.z)
f4 = midarm.y.dot(chest.z)
