from pyrr import Quaternion, Matrix44, Vector3
import numpy as np

point = Vector3([1.,2.,3.])
orientation = Quaternion()
translation = Vector3()
scale = Vector3([1.,1.,1.])

# translate along X by 1
translation += [1.0, 0.0, 0.0]

# rotate about Y by pi/2
rotation = Quaternion.from_y_rotation(np.pi / 2.0)
orientation = rotation * orientation

# create a matrix
matrix = Matrix44.identity()

# apply our translation
matrix = matrix * Matrix44.from_translation(translation)

# apply our orientation
# we can multiply matricies and quaternions directly!
matrix = matrix * orientation

# apply our scale
matrix = matrix * Matrix44.from_scale(scale)

# transform our point by the matrix
# vectors are transformable by matrices and quaternions directly
point = matrix * point

print(point)