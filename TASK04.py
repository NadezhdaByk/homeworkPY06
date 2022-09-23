
orbits=[(1,3),(2.5, 10), (7,2), (6,6), (4,3)]
def find_farthest_orbit(list_of_orbit):
    max=0
    for i in list_of_orbit:
        if (i[0]*i[1]*3.14159)>max and i[0]!=i[1]:
            max=i[0]*i[1]*3.14159
            planet=[(i[0], i[1])]
    return planet

print(find_farthest_orbit(orbits))