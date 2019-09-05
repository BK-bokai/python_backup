# Copyright (c) 2016 MetPy Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
"""
Skew-T with Complex Layout
==========================

Combine a Skew-T and a hodograph using Matplotlib's `GridSpec` layout capability.
"""
import glob
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import metpy.calc as mpcalc
from metpy.cbook import get_test_data
from metpy.plots import add_metpy_logo, Hodograph, SkewT
from metpy.units import units

###########################################
# Upper air data can be obtained using the siphon package, but for this example we will use
# some of MetPy's sample data.

# col_names = ['pressure', 'height', 'temperature', 'dewpoint', 'direction', 'speed']

# df = pd.read_fwf(get_test_data('may4_sounding.txt', as_file_obj=False),
#                  skiprows=5, usecols=[0, 1, 2, 3, 6, 7], names=col_names)
for x in (glob.glob('D:\\bokai\\python\\python-code\\批次讀檔\\data\\*.txt')):

    elements = []
    with open(x,"rt") as file:
        for line in file.readlines():
            line = line.strip().split()
            print(len(line))
            if (len(line)!=0):
                elements.append(line)
    ele_array = np.array(elements).reshape(19, 4)
    ele_array = ele_array.astype(np.float)



    temperature=np.array(ele_array[:,0])
    dewpoint=np.array(ele_array[:,1])
    speed=np.array(ele_array[:,2])
    direction=np.array(ele_array[:,3])
    pressure=[]
    for x in range(19):
        P=int(1000-(x*50))
        pressure.append(P)

    pressure = np.array(pressure).reshape(19)
    pressure = pressure.astype(np.float)

    # df['u_wind'], df['v_wind'] = mpcalc.wind_components(df['speed'],
    #                                                     np.deg2rad(df['direction']))

    # Drop any rows with all NaN values for T, Td, winds
    # df = df.dropna(subset=('temperature', 'dewpoint', 'direction', 'speed',
    #                        'u_wind', 'v_wind'), how='all').reset_index(drop=True)

    ###########################################
    # We will pull the data out of the example dataset into individual variables and
    # assign units.

    p = pressure * units.hPa
    T = temperature * units.degC
    Td = dewpoint * units.degC
    wind_speed = speed * units.knots
    wind_dir = direction * units.degrees
    u, v = mpcalc.wind_components(wind_speed, wind_dir)

    ###########################################

    # Create a new figure. The dimensions here give a good aspect ratio
    fig = plt.figure(figsize=(9, 9))
    add_metpy_logo(fig, 630, 80, size='large')

    # Grid for plots
    gs = gridspec.GridSpec(3, 3)
    skew = SkewT(fig, rotation=45, subplot=gs[:, :2])

    # Plot the data using normal plotting functions, in this case using
    # log scaling in Y, as dictated by the typical meteorological plot
    skew.plot(p, T, 'r')
    skew.plot(p, Td, 'g')
    skew.plot_barbs(p, u, v)
    skew.ax.set_ylim(1000, 100)

    # Add the relevant special lines
    skew.plot_dry_adiabats()
    skew.plot_moist_adiabats()
    skew.plot_mixing_lines()

    # Good bounds for aspect ratio
    skew.ax.set_xlim(-30, 40)

    # Create a hodograph
    ax = fig.add_subplot(gs[0, -1])
    h = Hodograph(ax, component_range=60.)
    h.add_grid(increment=20)
    h.plot(u, v)

    # Show the plot
    plt.show()
    # plt.savefig("skew.png",dpi=1000,format="png")
