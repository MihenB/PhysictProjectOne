"""Plots field lines for a false monopole."""

from matplotlib import pyplot
from numpy import radians

import electrostatics
from electrostatics import PointCharge
from electrostatics import ElectricField, Potential, GaussianCircle
from electrostatics import finalize_plot


XMIN, XMAX = -200, 200
YMIN, YMAX = -150, 150
ZOOM = 30
XOFFSET = 0

electrostatics.init(XMIN, XMAX, YMIN, YMAX, ZOOM, XOFFSET)

# Set up the charges, electric field, and potential
charges = [PointCharge(1, [-2, 0]),
           PointCharge(1, [2, 0]),
           PointCharge(1, [0, -2]),
           PointCharge(1, [0, 2]),
           PointCharge(-4, [0, 0])]
field = ElectricField(charges)
potential = Potential(charges)

# Set up the Gaussian surfaces
g = [GaussianCircle(charges[i].x, 0.1) for i in range(len(charges))]
g[2].a0 = radians(90)
g[3].a0 = radians(-90)

# Create the field lines
fieldlines = []
for g_ in g[:-1]:
    for x in g_.fluxpoints(field, 12):
        fieldlines.append(field.line(x))

# Plotting
pyplot.figure(figsize=(6, 4.5))
field.plot()
potential.plot()
for fieldline in fieldlines:
    fieldline.plot(endarrows=False)
for charge in charges:
    charge.plot()
finalize_plot()
pyplot.show()