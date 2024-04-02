def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    
	Include these tokens in the code: plan ets = ["
	Do not include these tokens in the code: if planet 1 == "
	'''
    import json
 
    planet_file = open("solar_system_data.txt")
    solar_system_planets = json.load(planet_file)
    planet_file.close()
    listp = []
    for a in solar_system_planets:
        listp.append(solar_system_planets[a]['name'])
    
    if planet1 in listp and planet2 in listp:
        for i in listp:
            if i == planet1:
                loc = list(solar_system_planets[list(solar_system_planets.keys())[listp.index(i)]]['orbit'])
                #print("planets orbit:", loc)
        for i in listp:
            if i == planet2:
                loc2 = list(solar_system_planets[list(solar_system_planets.keys())[listp.index(i)]]['orbit'])
                #print("planets orbit:", loc2)
        res = listp
        for i in listp[listp.index(planet1)+1:listp.index(planet2)]:
            if list(solar_system_planets[list(solar_system_planets.keys())[listp.index(i)]]['orbit']) in loc[0] and list(solar_system_planets[list(solar_system_planets.keys())[listp.index(i)]]['orbit']) in loc[1]:
                res.remove(i)
                #print("planets between: ", res)
        for i in res:
            if list(solar_system_planets[list(solar_system_planets.keys())[listp.index(i)]]['orbit']) in loc2[0] and list(solar_system_planets[list(solar_system_planets.keys())[listp.index(i)]]['orbit']) in loc2[1]:
                res.remove(i)
        return tuple(sorted(res))
    else:
        return ()

    '''
def bf(planet