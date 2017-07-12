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

from ocelot.gui.accelerator import *

def plot_API(lat, legend=True,**kw_fig):
    fig = plt.figure(**kw_fig)
    plt.rc('axes', grid=True)
    plt.rc('grid', color='0.75', linestyle='-', linewidth=0.5)
    left, width = 0.1, 0.85
    rect2 = [left, 0.2, width, 0.7]
    rect3 = [left, 0.05, width, 0.15]

    ax_xy = fig.add_axes(rect2)  #left, bottom, width, height
    ax_el = fig.add_axes(rect3, sharex=ax_xy)

    font_size = 16

    for ax in ax_xy, ax_el:
        if ax!=ax_el:
            for label in ax.get_xticklabels():
                label.set_visible(False)

    ax_xy.grid(True)
    ax_el.set_yticks([])
    ax_el.grid(True)
    #plt.xlim(S[0], S[-1])

    fig.subplots_adjust(hspace=0)

    #plot_xy(ax_xy, S, X, Y, font_size)

    #plot_elems(ax_el, lat, nturns = 1, legend = True) # plot elements
    new_plot_elems(fig, ax_el, lat, nturns = 1, legend = legend)
    return ax_xy,ax_el
