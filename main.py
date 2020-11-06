import math

# coordinates = [x, y, z]
coordinates = [0, 0, 0]

# Rotation to apply (in rad)
rot_x = math.pi / 2
rot_y = 0
rot_z = 0

# Zoom of the projection axis
zoom = 1

# Center of the projection axis
cx = 0
cy = 0

### ###

def rotate_coordinates(coordinates, rot_x, rot_y, rot_z):
    x1 = coordinates[0]
    y1 = coordinates[1]
    z1 = coordinates[2]

    # Z axis rotation, will create a new X 'x2' and Y 'y2':
    x2 = (math.cos(rot_z)*x1) - (math.cos(rot_z)*y1)
    y2 = (math.cos(rot_z)*x1) + (math.cos(rot_z)*y1)

    # Y axis rotation, with à partir de x2 and z1
    # Will create a new X 'x3' and Z 'z3':
    x3 = (math.cos(rot_y)*x2) + (math.sin(rot_y)*z1)
    z2 = (math.cos(rot_y)*z1) - (math.sin(rot_y)*x2)

    # X axis rotation, with x2 and z2 
    # Will create a new Y 'y3' and Z 'z3':
    y3 = (math.cos(rot_x)*y2) - (math.sin(rot_x)*z2)
    z3 = (math.sin(rot_x)*y2) + (math.cos(rot_x)*z2)

    return [x3, y3, z3]


def project_3d_coordinates(coordinates):
    """Project a 3D point in a 2D coordinate mark"""
    x3 = coordinates[0]
    y3 = coordinates[1]
    z3 = coordinates[2]

    px = cx + ((x3 * zoom) / (z3 + 2.5))
    py = cy + ((y3 * zoom) / (z3 + 2.5))

    return [px, py]

def rotate_and_project(coordinates, rot_x, rot_y, rot_z):
    return project_3d_coordinates(rotate_coordinates(coordinates, rot_x, rot_y, rot_z))