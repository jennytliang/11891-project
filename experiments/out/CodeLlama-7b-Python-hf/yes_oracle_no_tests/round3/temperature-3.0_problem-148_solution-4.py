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
    
	Do not include these tokens in the code: plan ets _ pos = {" Mer cur y ":
	'''



    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
    planet1 = planet1.replace(' ', '')
    planet2 = planet2.replace(' ', '')
    if planet1 in planets and planet2 in planets:
        pos = {"Mercury":0, "Venus":1, "Earth":2, "Mars":3, "Jupiter":4, "Saturn":5, "Uranus":6, "Neptune":7}
        if pos[planet1] > pos[planet2]:
            planet1, planet2 = planet2, planet1
        return tuple([planet for planet in planets[pos[planet1]+1:pos[planet2]]])
    else:
        return ()


print(bf("Jupiter", "Neptune"))
print(bf("Earth", "Mercury"))
print(bf("Mercury", "Uranus"))