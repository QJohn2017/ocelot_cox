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

lattice_elements = {}
Drifts = {}
QuadLengths = {}
QuadGradients = {}
DipLengths = {}
DipAngles = {}
UndulConfigs = {}

cell_keys = ['LPWA-QAP1','QAP1','QAP1-QAP2','QAP2','QAP2-QAP3','QAP3','QAP3-IMG1','IMG1',\
  'IMG1-DIP1','DIP1','DIP1-DIP2','DIP2','DIP2-IMG2','IMG2','IMG2-DIP3','DIP3','DIP3-DIP4','DIP4',\
  'DIP4-QEM1','QEM1','QEM1-QEM2','QEM2','QEM2-IMG4','IMG4','IMG4-QEM3','QEM3','QEM3-QEM4','QEM4',\
  'QEM4-UNDL','UNDL1','UNDL2','UNDL-IMG5','IMG5']

Drifts['LPWA-QAP1'] = 0.04685
Drifts['QAP1-QAP2'] = 0.10295
Drifts['QAP2-QAP3'] = 0.09895
Drifts['QAP3-IMG1'] = 0.25085
Drifts['IMG1-DIP1'] = 0.533 # or add 0.04
Drifts['DIP1-DIP2'] = 0.2
Drifts['DIP2-IMG2'] = 0.275
Drifts['IMG2-DIP3'] = 0.275
Drifts['DIP3-DIP4'] = 0.2
Drifts['DIP4-QEM1'] = 0.32035
Drifts['QEM1-QEM2'] = 0.3867
Drifts['QEM2-IMG4'] = 0.14335
Drifts['IMG4-QEM3'] = 0.14335
Drifts['QEM3-QEM4'] = 0.3367
Drifts['QEM4-UNDL'] = 0.29135
Drifts['UNDL-IMG5'] = 0.573

QuadLengths['QAP1'] = 0.047
QuadLengths['QAP2'] = 0.0511
QuadLengths['QAP3'] = 0.0323
QuadLengths['QEM1'] = 0.2133
QuadLengths['QEM2'] = 0.2133
QuadLengths['QEM3'] = 0.2133
QuadLengths['QEM4'] = 0.2133

QuadGradients['QAP1'] = 174.5627
QuadGradients['QAP2'] = -171.7276
QuadGradients['QAP3'] = 153.0407

QuadGradients['QEM1'] = -13.95103
QuadGradients['QEM2'] = 10.13906
QuadGradients['QEM3'] = -10.90492
QuadGradients['QEM4'] = 3.273795

QuadTilt = {}
QuadTilt['QAP1'] = 0
QuadTilt['QAP2'] = 0
QuadTilt['QAP3'] = 0
QuadTilt['QEM1'] = 0
QuadTilt['QEM2'] = 0
QuadTilt['QEM3'] = 0
QuadTilt['QEM4'] = 0
lattice_elements['QuadTilt'] = QuadTilt

DipLengths['DIP1'] = 0.2
DipLengths['DIP2'] = 0.2
DipLengths['DIP3'] = 0.2
DipLengths['DIP4'] = 0.2

DipAngles['DIP1'] = 1
DipAngles['DIP2'] = -1
DipAngles['DIP3'] = -1
DipAngles['DIP4'] = 1

UndulConfigs['Period'] = 0.01816
UndulConfigs['Strength'] = 0.
UndulConfigs['NumPeriods'] = 54

BeamEnergy_ref = 0.176

lattice_elements['Drifts'] = Drifts
lattice_elements['QuadLengths'] = QuadLengths
lattice_elements['QuadGradients'] = QuadGradients
lattice_elements['DipLengths'] = DipLengths
lattice_elements['DipAngles'] = DipAngles
lattice_elements['UndulConfigs'] = UndulConfigs

latt_par_string = """
###############################
R_11 = {0:.3g}, R_33 = {1:.3g},
R_56 = {2:.3g} mm,
R_226 = {3:.3g}, R_446 = {4:.3g},
R_126 = {5:.3g}, R_346 = {6:.3g}
################################
"""
