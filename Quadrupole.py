"""Plots field lines for a quadrupole."""

from matplotlib import pyplot
from numpy import radians

import electrostatics
from electrostatics import PointCharge
from electrostatics import ElectricField, Potential, GaussianCircle
from electrostatics import finalize_plot


XMIN, XMAX = -200, 200
YMIN, YMAX = -150, 150
ZOOM = 33
XOFFSET = 0

electrostatics.init(XMIN, XMAX, YMIN, YMAX, ZOOM, XOFFSET)

# Set up the charges and electric field
charges = [PointCharge(1, [-2, 0]),
           PointCharge(1, [2, 0]),
           PointCharge(-1, [0, -2]),
           PointCharge(-1, [0, 2]),
           PointCharge(0, [0, 0])]
field = ElectricField(charges)
potential = Potential(charges)

# Set up the Gaussian surfaces
g = [GaussianCircle(charges[i].x, 0.1) for i in range(len(charges))]
g[2].a0 = radians(90)
g[3].a0 = radians(-90)

# Create the field lines
fieldlines = []
for g_ in g[2:4]:
    for x in g_.fluxpoints(field, 12):
        fieldlines.append(field.line(x))
fieldlines.append(field.line([-1, 0]))
fieldlines.append(field.line([1, 0]))
fieldlines.append(field.line([-3, 0]))
fieldlines.append(field.line([3, 0]))

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