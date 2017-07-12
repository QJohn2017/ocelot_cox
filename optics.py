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


