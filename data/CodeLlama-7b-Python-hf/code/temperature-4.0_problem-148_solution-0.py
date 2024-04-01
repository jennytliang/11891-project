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
    '''
    result = ()
    lis=['jupiter', 'uranus', 'saturn', 'venus', 'mercury']
    if all(planet in lis and planet1==planet.title() and planet2.title()) and planet1!='Uranus' and planet2!='Jupiter':
        if lis.index(planet2)<lis.index(planto1):
            return tuple(lis[lis.index(plant)+1:lis.index(planet2)+1] for plant1 in plan1, plant2 in tuple (planets[plant] for plant in planets if plants.index(plant[0]) > plant1.index(plant2)])