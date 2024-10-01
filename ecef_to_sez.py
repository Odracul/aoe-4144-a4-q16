# ecef_to_sez.py
#
# Usage: python3 ecef_to_sez.py o_x_km o_y_km o_z_km x_km y_km z_km
#  Converts ECEF vector components to SEZ
#  See "Fundamentals of Astrodynamics and Applications, Fourth Edition" by
#  David A. Vallado, pages 172-173
# Parameters:
#  r_x_km: ECEF x-component in km
#  r_y_km: ECEF y-component in km
#  r_z_km: ECEF z-component in km
# Output:
#  Prints the converged latitude (deg), longitude (deg), and HAE (km)
#
# Written by Lucas Libovicz-Kilgore
#
# This work is licensed under CC BY-SA 4.0

# import Python modules
import math # math module
import sys  # argv

# "constants"
R_E_KM = 6378.137
E_E    = 0.081819221456

# Given lat lon and vector values
# ECEF vector (308.764, 307.863, 309.966)

lat_deg = 40.496 
lat_rad = (lat_deg/180)*math.pi

lon_deg = -80.246
lon_rad = (lon_deg/180)*math.pi

# calculations
mx1 = [[math.sin(lat_rad), 0, -math.cos(lat_rad)], 
    [0, 1, 0],
    [math.cos(lat_rad), 0, math.sin(lat_rad)]]

mx2 = [[math.cos(lon_rad), math.sin(lon_rad), 0], 
    [0, math.cos(lon_rad), 0],
    [math.cos(lat_rad), 0, math.sin(lat_rad)]]

mx3 = [[308.764], 
    [307.683],
    [309.966]]



result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range (len(mx1)):
    for j in range(len(mx1)):
        for k in range(len(mx2)):
            result[i][j] = (mx1[i][0]*mx2[0][j]+mx1[i][1]*mx2[1][j])

for row in result:
    print(row)

mx4 = [[0.11001939556285438, -0.6400074586974964, 0.0],
[0.0, 0.1694183082290486, 0],
[0.12883437337596318, -0.749458397543439, 0.0]]

for i in range (len(mx4)):
    for j in range(len(mx4)):
        for k in range(len(mx3)):
            result[i][j] = (mx4[i][0]*mx3[0][j]+mx4[i][1]*mx3[1][j])

for row in result:
    print(row)



# print(s_km)
# print(e_km)
# print(z_km)