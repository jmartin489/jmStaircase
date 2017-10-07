import bpy
import math

bpy.ops.object.select_all(action = 'SELECT')
bpy.ops.object.delete()

#Number of stairs to generate
number_of_stairs = 25

height_of_staircase = number_of_stairs

#Location of first step
x = 0
y = 0
z = 1

cube_resize_x = 1
cube_resize_y = 22

#Handrail dimensions & rotation
handrail_offset = 20        #So handrail does not lie on staircase
handrail_radius = 0.75
handrail_length = math.sqrt((height_of_staircase*height_of_staircase) + (number_of_stairs*number_of_stairs))
handrail_x_rotation = 0
handrail_z_rotation = 0
handrail_y_rotation = math.atan(height_of_staircase/number_of_stairs)
handrail_x_loc = number_of_stairs - cube_resize_x
handrail_y_loc = cube_resize_y - 2
handrail_z_loc = height_of_staircase + handrail_offset

#Baluster dimensions
baluster_resize_x = 0.5
baluster_resize_y = 0.25
baluster_resize_z = (handrail_z_loc - height_of_staircase)/2

for i in range(number_of_stairs):
    cube_resize_z = i + 1
    
    bpy.ops.mesh.primitive_cube_add(location = (x, y, z))
    bpy.ops.transform.resize(value=(cube_resize_x, cube_resize_y, cube_resize_z))
    bpy.ops.transform.translate(value=(i*2, y, i))
    
#Left Balusters
for c in range(number_of_stairs):
    bpy.ops.mesh.primitive_cube_add(location = (x, handrail_y_loc, z))
    bpy.ops.transform.resize(value=(baluster_resize_x, baluster_resize_y, baluster_resize_z))
    bpy.ops.transform.translate(value=(c*2 ,y, c*2 + handrail_offset/2))
    
#Right Balusters
for c in range(number_of_stairs):
    bpy.ops.mesh.primitive_cube_add(location = (x, handrail_y_loc * -1, z))
    bpy.ops.transform.resize(value=(baluster_resize_x, baluster_resize_y, baluster_resize_z))
    bpy.ops.transform.translate(value=(c*2, y ,c*2 + handrail_offset/2))
        
#Left Handrail    
bpy.ops.mesh.primitive_cylinder_add(radius = handrail_radius, 
location = (handrail_x_loc, handrail_y_loc, handrail_z_loc), 
rotation = (handrail_x_rotation, handrail_y_rotation, handrail_z_rotation))
bpy.context.object.scale[2] = handrail_length           #Scale on z-axis

#Right Handrail
bpy.ops.mesh.primitive_cylinder_add(radius = handrail_radius, 
location = (handrail_x_loc, handrail_y_loc * -1, handrail_z_loc), 
rotation = (handrail_x_rotation, handrail_y_rotation, handrail_z_rotation))
bpy.context.object.scale[2] = handrail_length

bpy.ops.object.select_all(action = 'DESELECT')