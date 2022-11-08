from matplotlib import pyplot
from numpy import radians

import electrostatics
from electrostatics import PointCharge, ElectricField, Potential, GaussianCircle
from electrostatics import finalize_plot


def show_electrostatic_field(type_of_struct, charge):
    XMIN, XMAX = -40, 40
    YMIN, YMAX = -30, 30
    ZOOM = 5
    XOFFSET = 0
    electrostatics.init(XMIN, XMAX, YMIN, YMAX, ZOOM, XOFFSET)
    if type_of_struct == 1:
        charges = [PointCharge(2, [2, 2]),
                   PointCharge(2, [-2, -2]),
                   PointCharge(-2, [2, -2]),
                   PointCharge(-2, [-2, 2])]
    elif type_of_struct == 2:
        count_of_points = 8
        coordinates = [[-2, 0], [-1.414, 1.414], [0, 2], [1.414, 1.414], [2, 0],
                       [1.414, -1.414], [0, -2], [-1.414, -1.414]]
        charges = [PointCharge(charge * (-1) ** i, coordinates[i]) for i in range(count_of_points)]
    elif type_of_struct == 3:
        charges = [PointCharge(2, [2, 2]),
                   PointCharge(2, [-2, -2]),
                   PointCharge(-2, [2, -2]),
                   PointCharge(-2, [-2, 2]),
                   PointCharge(2, [0, 0])]
    elif type_of_struct == 4:
        charges = [PointCharge(2, [2, 2]),
                   PointCharge(2, [-2, -2]),
                   PointCharge(-2, [2, -2]),
                   PointCharge(-2, [-2, 2]),
                   PointCharge(-2, [0, 0])]
    else:
        count_of_points = 0
        coordinates = []
        charges = [PointCharge(charge * (-1) ** i, coordinates[i]) for i in range(count_of_points)]
    field = ElectricField(charges)
    potential = Potential(charges)
    gaussian_list = [GaussianCircle(charges[i].x, 0.1) for i in range(len(charges))]
    fieldlines = []
    for g_ in gaussian_list[0:len(gaussian_list)]:
        for x in g_.fluxpoints(field, 12):
            fieldlines.append(field.line(x))
    for fieldline in fieldlines:
        fieldline.plot()
    for charge in charges:
        charge.plot()
    potential.plot()
    finalize_plot()
    pyplot.show()


def main():
    show_electrostatic_field(3, 1)


if __name__ == '__main__':
    main()
