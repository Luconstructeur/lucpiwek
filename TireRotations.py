from math import pi

def tire_rotations(tire_size,distance_km):

    if not isinstance(tire_size,str):
        return 'Tire size must be a string'
    
    if not isinstance(distance_km,(float)):
        if isinstance(distance_km,int):
            distance_km = float(distance_km)
        else:
            return 'Distance must be a float'

    width_tire = tire_size[0:3]
    diameter_tire = tire_size[-2:] #en inch
    diameter_tire = float(diameter_tire) * 25.4 #en mm
    pourcentage_sidewall = tire_size[4:6]
    sidewall_height = (float(pourcentage_sidewall)/100) * float(width_tire)

    rayon = sidewall_height + (float(diameter_tire)/2)

    perimetre_roue = 2 * pi * rayon #perimetre en mm
    nb_tour = (distance_km * 1000000) / perimetre_roue

    return nb_tour


print(tire_rotations('250/55R16',110.0))