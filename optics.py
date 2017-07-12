# This file is a part of independent module for OCELOT beam tracking software
# https://github.com/iagapov/ocelot

# This module contains the functions needed for OCELOT to model 
# the COXINEL experiment. In particular it deals with the broad-spectrum 
# beam transport.
# Copyright (C)  2017 Igor A. Andriyash <igor.andriyash@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np
from copy import deepcopy
from numba import jit

def lattice_transfer_map_RT(lattice, energy):
    """ transfer map for the whole lattice"""
    Ra = np.eye(6)
    Ta = np.zeros((6, 6, 6))
    E = energy
    for i, elem in enumerate(lattice.sequence):
        Tc = np.zeros((6, 6, 6))
        Rb = elem.transfer_map.R(E)
        Tb = deepcopy(elem.transfer_map.t_mat_z_e(elem.l, E))
        Tb = sym_matrix_jit(Tb)
        Tc = conv_T_jit(Ta,Tb,Tc,Ra,Rb)
        Ra = np.dot(Rb, Ra)
        E += elem.transfer_map.delta_e
        Ta = Tc

    lattice.T_sym = Ta
    lattice.T = unsym_matrix_jit(deepcopy(Ta))
    lattice.R = Ra

def lattice_transfer_map_R(lattice, energy):
    """ transfer map for the whole lattice"""
    Ra = np.eye(6)
    E = energy
    for i, elem in enumerate(lattice.sequence):
        Rb = elem.transfer_map.R(E)
        Ra = np.dot(Rb, Ra)
        E += elem.transfer_map.delta_e
    lattice.R = Ra

@jit()
def conv_T_jit(Ta,Tb,Tc,Ra,Rb):
    for i in range(6):
        for j in range(6):
            for k in range(6):
                t1 = 0.
                t2 = 0
                for l in range(6):
                    t1 += Rb[i, l]*Ta[l, j, k]
                    for m in range(6):
                        t2 += Tb[i, l, m]*Ra[l, j]*Ra[m, k]
                Tc[i, j, k] = t1 + t2
    return Tc

@jit()
def sym_matrix_jit(T):
    for i in range(6):
        for j in range(6):
            for k in range(j, 6):
                if j != k:
                    a = T[i, j, k]/2.
                    T[i, k, j] = a
                    T[i, j, k] = a
    return T

@jit()
def unsym_matrix_jit(T):
    for i in range(6):
        for j in range(6):
            for k in range(j, 6):
                if j != k:
                    a = T[i, j, k]*2.
                    T[i, k, j] = 0
                    T[i, j, k] = a
    return T


