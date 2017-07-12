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
from scipy.constants import m_e,c,e

mc2_GeV = m_e*c**2/e*1e-9

def ocelot_to_chimera(p_arrays,beam,lam0,keep_orig=True,\
  monochrom=None, select_parts = None):
	"""
	Exports the list of ParticleArrays from OCELOT to CHIMERA

	Parameters
	----------
	p_arrays: list of oclt.ParticleArray objects
	  beam represented in the form of slices list
	beam : chimera.Species object
	  CHIMERA species obejct to populate with particles
	lam0: float
	  normalization length for CHIMERA in meters

	Returns
	-------
	beam : chimera.Species object
		CHIMERA species obejct populated with particles
	"""

	Np = np.int(np.sum([p_array.size() for p_array in p_arrays]))

	xx = np.hstack(([p_array.z_c - p_array.tau() for p_array in p_arrays]))/lam0
	yy = np.hstack(([p_array.y() + p_array.y_c for p_array in p_arrays]))/lam0
	zz = np.hstack(([p_array.x() + p_array.x_c for p_array in p_arrays]))/lam0

	gg = np.hstack(([(p_array.p()+1)*p_array.E for p_array in p_arrays]))/mc2_GeV
	oy = np.hstack(([p_array.py() for p_array in p_arrays]))
	oz = np.hstack(([p_array.px() for p_array in p_arrays]))

	qq = np.hstack(([p_array.q_array*1e12 for p_array in p_arrays]))

	px = np.sqrt( (gg**2-1.)/(1+oy**2+oz**2) )
	py = px*oy
	pz = px*oz
	qq = -qq/(beam.Args['weight2pC']*lam0*1e6)

	if monochrom is not None:
		emin,emax = monochrom
		indx = np.nonzero( (gg*mc2_GeV<emax)*(gg*mc2_GeV>emin)  )[0]
		xx = xx[indx]
		yy = yy[indx]
		zz = zz[indx]
		px = px[indx]
		py = py[indx]
		pz = pz[indx]
		qq = qq[indx]
		Np = indx.shape[0]

	if select_parts is not None:
		indx = np.arange(xx.shape[0])
		np.random.shuffle(indx)
		indx = indx[:select_parts]
		xx = xx[indx]
		yy = yy[indx]
		zz = zz[indx]
		px = px[indx]
		py = py[indx]
		pz = pz[indx]
		qq = qq[indx]*Np*1.0/select_parts
		Np = indx.shape[0]

	gg, oy, oz = None, None, None

	beam.Data['coords'] = np.zeros((3,Np))
	beam.Data['momenta'] = np.zeros((3,Np))
	beam.Data['weights'] = np.zeros(Np)

	beam.Data['coords'][0] = xx
	beam.Data['coords'][1] = yy
	beam.Data['coords'][2] = zz

	beam.Data['momenta'][0] = px
	beam.Data['momenta'][1] = py
	beam.Data['momenta'][2] = pz

	beam.Data['weights'][:] = qq

	beam.Data['coords'][0] -= (beam.Data['coords'][0]*beam.Data['weights']\
	  ).sum()/(beam.Data['weights']).sum()
	beam.Data['coords_halfstep'] = beam.Data['coords'].copy()
	if keep_orig is False:
		del p_arrays

	return  beam
