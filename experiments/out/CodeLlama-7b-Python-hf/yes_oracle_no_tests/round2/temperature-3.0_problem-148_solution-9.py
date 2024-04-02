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
    
	Include these tokens in the code: ["
	Do not include these tokens in the code: ['
	'''


    pla_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    pla_dict = {"Mercury": 0, "Venus": 1, "Earth": 2, "Mars": 3, "Jupiter": 4, "Saturn": 5, "Uranus": 6, "Neptune": 7}

    if planet1 in pla_list and planet2 in pla_list:
        pla1 = pla_dict[planet1]
        pla2 = pla_dict[planet2]
        pla_list_bf = []
        for pla in pla_list:
            pla_dict[pla] = pla_dict[pla] + 1
        for pla in pla_list:
            pla_dict[pla] = pla_dict[pla] - 1
            if pla_dict[pla] >= pla1 and pla_dict[pla] <= pla2:
                pla_list_bf.append(pla)
        return pla_list_bf
    else:
        return ()
