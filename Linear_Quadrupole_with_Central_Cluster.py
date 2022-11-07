"""Plots field lines for linear quadrupole with a cluster at the center."""

from matplotlib import pyplot
from numpy import radians

import electrostatics
from electrostatics import PointCharge, ElectricField, Potential, GaussianCircle
from electrostatics import finalize_plot


XMIN, XMAX = -40, 40
YMIN, YMAX = -30, 30
ZOOM = 6
XOFFSET = 0

electrostatics.init(XMIN, XMAX, YMIN, YMAX, ZOOM, XOFFSET)

# Set up the charges, electric field, and potential
charges = [PointCharge(2, [-2, 0]),
           PointCharge(-1, [-2/3, 0]),
           PointCharge(-1, [0, -2/3]),
           PointCharge(-1, [0, 2/3]),
           PointCharge(-1, [2/3, 0]),
           PointCharge(2, [2, 0]),
           PointCharge(0, [0, 0])]
field = ElectricField(charges)
potential = Potential(charges)

# Set up the Gaussian surfaces
g = [GaussianCircle(charges[i].x, 0.1) for i in range(len(charges))]
g[2].a0 = radians(90)
g[3].a0 = radians(-90)

# Create the field lines
fieldlines = []
for g_ in [g[0], g[5]]:
    for x in g_.fluxpoints(field, 12):
        fieldlines.append(field.line(x))

# Plotting
pyplot.figure(figsize=(6, 4.5))
field.plot()
potential.plot()
for fieldline in fieldlines:
    fieldline.plot()
for charge in charges:
    charge.plot()
finalize_plot()
pyplot.show()
