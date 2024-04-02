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
    
	Include these tokens in the code: if
	'''


    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    if planet1 in planets and planet2 in planets:
        if planets.index(planet1) < planets.index(planet2):
            return tuple(planets[planets.index(planet1)+1:planets.index(planet2)])
        else:
            return tuple(planets[planets.index(planet2)+1:planets.index(planet1)])
    else:
        return ()










































































































































































































































































































































































































import numpy as np

def is_floats(x) -> bool:
    # check if it is float; List[float]; Tuple[float]
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all(isinstance(i, float) for i in x)
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False


def assertion(out, exp, atol):
    exact_match = out == exp

    if atol == 0 and is_floats(exp):
        atol = 1e-6
    if not exact_match and atol != 0:
        np.testing.assert_allclose(out, exp, atol=atol)
    else:
        assert exact_match


def check(candidate):
    inputs = [['Jupiter', 'Neptune'], ['Earth', 'Mercury'], ['Mercury', 'Uranus'], ['Neptune', 'Venus'], ['Earth', 'Earth'], ['Mars', 'Earth'], ['Jupiter', 'Makemake'], ['Neptune', 'Mercury'], ['Jupiter', 'Mars'], ['Mercury', 'Saturn'], ['Pluto', 'Mars'], ['Mercury', 'Venus'], ['Neptune', 'Saturn'], ['Earth', 'Neptune'], ['Uranus', 'Jupiter'], ['Mercury', 'Neptune'], ['Venus', 'Mars'], ['NeptunMarse', 'MeurJupitery'], ['MercuNeptunMarsery', 'Neptune'], ['Mercury', 'Mercury'], ['MercuNeptunMarsery', 'Mars'], ['', 'NeptuMarsn'], ['Pluto', 'Earth'], ['rn', 'Sturn'], ['ury', 'Mercrury'], ['Mar', 'Mar'], ['Earth', 'MerVenuscury'], ['rnth', 'Earath'], ['Pluto', 'Earath'], ['', 'NepntuMarsn'], ['Pluto', 'UranusEarth'], ['Pluto', 'Pluto'], ['Sturn', 'Sturn'], ['UranusEarth', 'Pluto'], ['UranusEarth', 'Mars'], ['xrON', 'Mars'], ['Puluto', 'Pluto'], ['NeptunePluto', 'UrntVenushranusEarth'], ['rnth', 'MeurJupitery'], ['Mars', 's'], ['tJupiter', 'Mars'], ['rnth', 'rntPlutoh'], ['rnthh', 'UrntVenushraMercurynusEarth'], ['Plo', 'Pluto'], ['Puluto', 'Earath'], ['Venus', 'MaNepntuMarsnrs'], ['Plsuto', 'Pluto'], ['Venus', 'UranusEarth'], ['Saturn', 'Saturn'], ['uSturnPuluto', 'rntPlutohuSturn'], ['sMaNepntuMarsnrs', 's'], ['Neptune', 'Neptune'], ['Mercrury', 'MarstJupiter'], ['Sturn', 'MarstJupiterSturn'], ['', 'NepntueMarsn'], ['aMars', 's'], ['NeptunMarse', 's'], ['Earath', 'Puluto'], ['NepPlutontueMarsn', 'NepntueMarsn'], ['NeptunMarse', 'NepntuMarsn'], ['ss', 's'], ['MarMr', 'Mar'], ['PuluMercruryo', 'Earath'], ['NepntueMarsn', 'NepntueMarsn'], ['Pluto', 'Plutuo'], ['NepPlutontueMarsn', 'NepPlutontueMarsn'], ['Neptuneuto', 'NeptunePluto'], ['Pluto', 'PMars'], ['Pluto', 'PMPPNepntuMarsnars'], ['MPlutuoercury', 'Mercury'], ['JupUranuser', 'Mars'], ['EartMeurJupiteryh', 'Mercury'], ['Pluto', 'tEarth'], ['Sturn', 'MarstJupiterSturnxrON'], ['lPluto', 'lPluto'], ['MPlutuoercury', 'MPlutuoPulutoury'], ['Pululto', 'Pululto'], ['tJupiter', 'PlsutoMars'], ['Earth', 'NeptuPulultone'], ['tJupiterMercurPMPPNepntuMarsnars', 'tJupiterMercury'], ['UrntVenushraMercurynusEarth', 'UrntVenushraMercurynusEarth'], ['', 'EarthPuluMercruryo'], ['PlutoaMars', 'Pluto'], ['rntPlutohuSturn', 'uSturnPuluto'], ['JupUranuser', 'ars'], ['aMarMMarMrr', 'aMar'], ['Pluto', 'MarMr'], ['Mar', 'Neptune'], ['PxrONlutto', 'tEarth'], ['urMarstJupiterSturnxrONy', 'Mercrury'], ['Earrth', 'MerVVenusenuscuruy'], ['cMerc', 'cMerc'], ['rn', 'SaturnStur'], ['Mercruy', 'MarsteJupiter'], ['Mrnercury', 'Mrnercury'], ['MarsteJuer', 'MarsteJupite'], ['Earth', 'NeptuPulultonne'], ['Earth', 'Sturn'], ['Earth', 'Mercy'], ['MeruVVenusnuscuruy', 'MeruVVen'], ['Mars', 'Neptune'], ['Saturn', 'Mercury'], ['Jupiter', 'Venus'], ['Jupiter', 'Jupiter'], ['Jupi', 'Jupiter'], ['Meurcury', 'Jupiter'], ['PUranuslMeurcuryuto', 'PUranusluto'], ['Jupiter', 'Veneus'], ['Jupi', 'Jiter'], ['Pluto', 'uto'], ['EaMercuryh', 'Pluto'], ['PUranuslMeurcuryuto', 'PUranuJiterury'], ['uto', 'JupitJupiterer'], ['MeVenusrcury', 'PUranusluto'], ['Jupi', 'J'], ['MeVenusrcurNeptuney', 'MeVenusrcurNeptuney'], ['PUranuslMeurcuryuto', 'PUranu'], ['Jupi', 'Uranus'], ['MeVenusrcurNeptuney', 's'], ['PUranusluto', 'Mars'], ['uto', 'uto'], ['Venues', 'Venus'], ['Merry', 'Mercury'], ['VeMeurcurynues', 'Venus'], ['JJupiterupiter', 'Vensus'], ['PUranu', 'Jupi'], ['Venus', 'Venues'], ['UrasnUus', 'Jupiter'], ['Venus', 'MeVenusrcurNeptuneyMercury'], ['UUranus', 'Jiter'], ['Mercury', 'MMercury'], ['VeMeurcurynues', 'Plut'], ['MMercur', 'MMercur'], ['Neptne', 'Neptune'], ['Venues', 'MeurcuryVensus'], ['Veneu', 'Jiter'], ['MeVenusrcury', 'Vensus'], ['Venus', 'MeVenusrcury'], ['uotoPlut', 'utoPlut'], ['JuVeMeurcurynuespi', 'J'], ['JuVeMeurcurynuespi', 'MMercury'], ['Mercury', 'MrerMcury'], ['Uranus', 'Pluto'], ['JupiutJupiterer', 'JupiutJupiterer'], ['Meuyrccury', 'Meurcury'], ['Mercury', 'MJiterercury'], ['JupitJupiterer', 'Jupupiterer'], ['s', 'Jupi'], ['Merry', 'MeVenusrcurNeptuney'], ['PlMeuyrccuryu', 'Pluto'], ['PUranuslMeurcurryuto', 'PUranuJiterury'], ['PlMeuyrcPUranucuryu', 'uto'], ['MMercury', 'MMercury'], ['MeVenusrcurNeptuney', 'Pluto'], ['MeVenusrcurNeptuneyMercury', 'MeVenusrcurNeptuney'], ['MeurcuryVensus', 'MeurcuryVensus'], ['Jiter', 'Mercury'], ['Plut', 'J'], ['Satuurn', 'Saturn'], ['MMercury', 'JuVeMeurcurynuespi'], ['MJSatuurniterercuryPUranuslMeurcuryuto', 'MJSatuurniterercuryPUranuslMeurcuryuto'], ['JupMercuryiutJupiterer', 'JupiutJupiterer'], ['s', 'JupiMerry'], ['JupiMerry', 'JupiMerry'], ['JMJSatuurniterercuryPUranuslMeurcuryuto', 'Jupi'], ['NpepteunVeneus', 'J'], ['MeVenusrcury', 'PUranJMJSatuurniterercuryPUranuslMeurcuryrutousluto'], ['uotoPlPut', 'utoPlut'], ['Jiter', 'Jiter'], ['ss', 'J'], ['Uranus', 'Uranus'], ['Veneu', 'Veneu'], ['PUranu', 'MercuryJupi'], ['utSatuurno', 'utoo'], ['Venues', 'MeMMercMury'], ['Veneu', 'PUranusluto'], ['Plut', 'Pluto'], ['Vensus', 'MeVenusrcury'], ['JMJSatuurniterercuryMeurcuryVensusPUranuslMeurcuryuto', 's'], ['PUranusluto', 'PtUranusluto'], ['UUranus', 's'], ['MeMMercMury', 'VenuJupMercuryiutJupiterers'], ['Jite', 'Jiter'], ['NppepteunVeneus', 'NpepteunVeneus'], ['Plut', 'JJupiter'], ['Meuyrccury', 's'], ['Jupiter', 'Venuus'], ['JupJupiteriter', 'Jupiter'], ['Earth', 'MercSaturnury'], ['Neptne', 'MMercur'], ['Jiter', 'Venuus'], ['JupJupiteriter', 'MMercury'], ['Pluto', 'Earrth'], ['JupJupiteriter', 'UrasnUus'], ['pNeptne', 'MMercur'], ['eVenues', 'Venus'], ['s', 's'], ['MrerMcury', 'Venus'], ['MJSatuurniterercuryPUranuslMeurcuryuto', 'PUrJJupiterupiteranu'], ['MeVenusrcMercuryJupiurNeptuney', 'Pluto'], ['PlMeuyrcPUranucuryu', 'MeVenusrcurNeptuneyMercury'], ['PUrJJupiterupiteranu', 'ss'], ['eVenues', 'eVenues'], ['rMerry', 'MercuMeVenusrcurNeptuneyry'], ['JupJiter', 'MJiterercury'], ['PUrannu', 'PUranu'], ['Mars', 'uotoPlPut'], ['utSatunurno', 'utoo'], ['VeneNpepteunVeneusu', 'Veneu'], ['Mas', 'MarMs'], ['rMerSaturnry', 'P'], ['SatPUranusVenuJupMercuryiutJupiterersJMJSatuurniterercuryPUranuslMeurcuryutolutourn', 'Mercury'], ['JupJiter', 'JupJiter'], ['PUrannu', 'PUrPlutoanu'], ['PUrVeneuJJupiterupiteranuotoPlutu', 'MJSatuurniterercuryPUranuslMeurcuryuto'], ['MarMs', 'JupitJupiterer'], ['NppeepteunVeneus', 'NppepteunVeneus'], ['Mars', 'Mars'], ['JupJtiter', 'JupJiter'], ['JuVeMeurcurynuespiVenuus', 'JuVeMeurcurynuespiVenuus'], ['VeMeurcurynues', 'lut'], ['MeVenusrcurNeptuneyMercury', 'Mercury'], ['MMercury', 'JuVeMeurcurynruespi'], ['Jiter', 'JitPUranuslMeurcuryutoJer'], ['Vensus', 'MeVenuotoPlPutusrcury'], ['UPUranuJiteruryMarMsranus', 'UPUranuJiteruryMarMsranus'], ['MUrasnUus', 'JMJSatuurniterercuryMeurcuryVensusPUranuslMeurcuryuto'], ['JJupiter', 'Pluto'], ['Meurcuury', 'Meurcury'], ['Saturn', 'Venus'], ['PUranuslMeurMMercuryryuto', 'PUranuslMeurcuryuto'], ['JitPUranuslMeurcuryutoJer', 'uotoPlPut'], ['PtUranursluto', 'JMJSatuurniterercuryPUranuslMueurcuryuto'], ['Satuurn', 'Satuurn'], ['Maas', 'MMercur'], ['eVenues', 'eVen'], ['PlMeuyrccuryPu', 'Pluto'], ['MercuMeVenusrurNeptuneyry', 'MercuMeVenusrcurNeptuneyry'], ['JitPUranuslMeurcuryutoJer', 'Vensus'], ['Venus', 'MeMMercMury'], ['NppepteunVeneus', 'NppepteunVeneus'], ['pNeptne', 'Jiter'], ['JupiMerry', 'Vensus'], ['Jupi', 'JuPtUranurslutoi'], ['JMJSatuurniterercuryPUranuslMeurcuryuto', 'JMJSatuurniterercuryPUranuslMeurcuryuto'], ['Venus', 'rMerry'], ['UPUranuJiteruryMarMsranus', 'UPUranuJPUrannuiteruryMarMsranus'], ['Venus', 'Venus'], ['Pluo', 'Pluto'], ['MMerMMercurcury', 'VeMeurcEarthurynues'], ['uto', 'UPUranuJiteruryMarMsranus'], ['Jupi', 'PUrJJupitrupiteranu'], ['JupJupiteriMrerMcuryter', 'JupJupiteriter'], ['utoo', 'MeVenuotoPlPutusrcury'], ['VenuPluts', 'MeMMercMury'], ['PlMeuyrcPUranucuryu', 'uuto'], ['JupJtiter', 'Pluto'], ['MeVenusrcury', 'MeVenusJupiutJupitererrcury'], ['VeJMJSatuurniterercuryMeurcuryVeneurcuryutous', 'Plut'], ['UUranus', 'Vensus'], ['JJupiteruMercuryJupipiter', 'JJupiterupiter'], ['VenuJupMercuryiutJupiterers', 'MeVenJJupiterusrcMercuryJupiurNeptuney'], ['utSatuurno', 'utSatuurno'], ['Jupi', 'PtUranusluto'], ['Jupiter', 'Vs'], ['utoo', 'NppepteunVeneus'], ['JuVeMeurcurynuespi', 'UrasnUus'], ['PlMeuyrccuryPu', 'Pluo'], ['Mercury', 'MeVenuotoPlPutusrcury'], ['uuto', 'uotoPlPut'], ['PlMeuycPUranucury', 'PlMeuycPUranucuryu'], ['utSatunurno', 'Pluo'], ['uuto', 'MercSaturnury'], ['MercSatucrnury', 'MercSaturnury'], ['JJupiteruMercuryJupipiter', 'JJupiteruMercuryJupipiter'], ['JJupiteruJMercuryJupipiter', 'JJupiteruMercuryJupipiter'], ['s', 'JuJupiterpiter'], ['Venuus', 'Venuus'], ['MeVenusrcurNeptuney', 'MeVenusrcurNeptuMeVenuotoPlPutusrcuryney'], ['Venuees', 'MeMMercMury'], ['uotoPlut', 'Satuurn'], ['Neptune', 'NNeptune'], ['PUranuUPUranuJiteruryMarMsranus', 'PUranu'], ['Venus', 'rMery'], ['Jupitreer', 'Jupitrer'], ['rMerSaturnry', 'NpepteunVeneus'], ['JuVeMeurcurynuespiVenuus', 'utSatunurno'], ['PMeurcuurytUrano', 'PMeurcuurytUranursluto'], ['s', 'PUrJJupiterupiteranu'], ['eVenues', 'MercuMeVenusrcurNeptuneyry'], ['MeVenusrncury', 'MeVenusrcury'], ['JupJiter', 'JupJiterMeVenusrcury'], ['Plutoo', 'Earth'], ['pNeptne', 'Mercury'], ['uotoPlut', 'Vensus'], ['VeMJSatuurniterercuryPUranuslMeurcuryutoMeurcurynues', 'lut'], ['ss', 'Jupi'], ['uuto', 'uuto'], ['PUMJSatuurniterernuuslMeurcuryutoranu', 'PUMJSatuurniterercuryPUranuuslMeurcuryutoranu'], ['rMetuneturnry', 'rMerSaNeptuneturnry'], ['MercuMeVenusrccurNeptuneyry', 'MercuMeVenusrcurNeptuneyry'], ['Maas', 'VVeneu'], ['MarMs', 'Mars'], ['MMeurcuryVensusPlMeuycPUranucuryu', 'PlMeuyrccuryPu'], ['Veneu', 'JiterVenuus'], ['MeVenuotoPloPutusrcury', 'MeVenuotoPlPutusrcury'], ['Mercury', 'MyJiterercury'], ['MeVenusrcury', 'MMercury'], ['oPlu', 'uto'], ['NppepteMMercuryunVeneus', 'NppepteunVeneus'], ['PUMJSatuurniterernuuslMeurcuryutoranu', 'PUMJSatuurnuryPUranuuslMeurcuryutoranu'], ['PUrJ', 'ss'], ['PUranusluto', 'MeVenusrcury'], ['MercuMeVenusrcurNeptuneyry', 'JupeiMerry'], ['VeJMJSatuurniterercuryMeurcuryVeneurcuryutous', 'VeJMJSatuurniterercuryMeurcuryVeneurcuryutous'], ['VeMeurcurynues', 'Pllut'], ['Mury', 'JJupiteruMercuryJupipiter'], ['Uranus', 'M'], ['Merry', 'PUranJMJSatuurniterercuryPUranuslMeurcuryrutousluto'], ['Mury', 'JMJSatuurniterercuryPUranuslMeurcuryuto'], ['Meuyrccury', 'eurccury'], ['VeMeurcusrynues', 'VeMeurcurynues'], ['rMerry', 'PlutMury'], ['Plutoo', 'Pluto'], ['MJiterercury', 'MJiterercury'], ['PluPto', 'Pluto'], ['JJupiteriuJMercuryJupipiter', 'JJupiteriuJMercuryJupipiter'], ['MuPlutoory', 'JMJSatuurniterercuryPUranuslMeurcuryuto'], ['VeMeurcEarthurynues', 'MMerMMercurceury'], ['PUrJJupitrupiteranu', 'VenPUrVeneuJJupiterupiteranuotoPlutuus'], ['JiterVenus', 'Venues'], ['VenuPluts', 'Saturn'], ['Pllut', 'Earth'], ['Mury', 'Jiter'], ['UPUranuJiteruryMarMsranMus', 'UPUranuJiteruryMarMsranMus'], ['MeVVenusrcury', 'MeVenusrcury'], ['utSatJiterunurno', 'MercuMeVenusrcurNeptuneyry'], ['Meuyrccury', 'MeVenusrcurNeptuneyMercury'], ['s', 'PUrJJupitePUrVeneuJJupiterupiteranuotoPJluturupiteranu'], ['PlMeuycPUranucury', 'PMeurcuurytUranursluto'], ['Neptuune', 'Neptuune'], ['PUranuslMeurcuerryutoJupiter', 'PUranuslMeurcuerryutoJupiter'], ['VenPUrVMerryeneuJJupiterupiteranuotoPlutuus', 'VenPUrVMerryeneuJJupiterupiteranuotoPlutuus'], ['JupiMerrry', 'JupiMerry'], ['PUrVeneuJJupiterupiteranuotoPlutu', 'uuto'], ['Mury', 'JJupiteruMerer'], ['PUranusluto', 'JupitJupiJupiutJupitererterer'], ['JupitePlutor', 'JupitePlutor'], ['Neptune', ''], ['eVenues', 'Jiter'], ['rMetuneturnry', 'PUrPlutoanu'], ['JuVeMMeVenusrcurNeptuneyeu', 'MMercury'], ['UPUranrMsranMus', 'UPUranuJiteruryMarMsranMus'], ['MeurcuryMVensus', 'MeuurcuryMVensus'], ['PUMJSatuurnuryPUranuuslMeurcuryutoranu', 'lut'], ['PUranuslMeurcurryuto', 'PUVeMJSatuurniterercuryPUranuslMeurcuryutoMeurcurynuesranuJiterury'], ['Mrry', 'Mry'], ['MeVenusrcury', 'MeVenusrcury'], ['pNeptpne', 'MMercur'], ['MeVenusrcurNeptuney', 'MeVeneVenuesuotoPlPutusrcury'], ['PUranuslMeurcuerryutoJupiter', 'PUranuslMeurcuerryutoJJJupiteruMererer'], ['PtUranurNppeepteunVeneusto', 'PtUranursluto'], ['JupitEarrthJupiterer', 'Jupupiterer'], ['VenuPlJuVeMeMJSatuurniterercuryPUranuslMeurcuryutourcurynuespiuts', 'VenuPlJuVeMeurcurynuespiuts'], ['VenuJupJupiterers', 'VenuJupMercuryiutJupiterers'], ['PlMeuyrcPUranucuryulut', 'lut'], ['J', 'J'], ['uPUranuslMeurcurryutouto', 'uotoPlPut'], ['SaturUPUranuJPUrannuiteruryMarMsranusn', 'Venus'], ['UUranMuPlutooryus', 'Vensus'], ['PUrJJupitrupiteranu', 'PUrJJupitrupiteranu'], ['JMJSaVenuJupJupitererstuurnieurPUrannucuryuto', 'JMJSatuurnieurPUrannucuryuto'], ['MeurcuryMVensus', 'Veneu'], ['rMury', 'JJupiteruMercuryJupipiter'], ['utSatuuPUranuslMeurcuerryutoJJJupiteruMerererrno', 'utSatuurno'], ['Jiteir', 'Jiter'], ['JupJtiteer', 'JupJiter'], ['MercuMeVenusrurNeputuneyry', 'MercuMeVenusrcurNeptuneyry'], ['Jupitreer', 'VeJMJSatuurniterercuryMeurcuryVeneurcuryutous'], ['MMerMMercurcury', 'VeMeurcEartluthurynues'], ['JJJiteirupiteruJMercuryPUranuJupipiter', 'JJJiteirupiteruJMercuryJupipiter'], ['JMJSaVenuJupJupitererstuurnieurPUrannucuryuto', 'Plutoo'], ['PiUranuJiterury', 'PUranuJiterury'], ['rMerry', 'PlutMurrMerSaNeptuneturnry'], ['VePUranuJiterurysus', 'Vensus'], ['MeurcuryMVensus', 'MeurcuryMVensus'], ['JiterVenus', 'JJupiteruMercuryJupipiter'], ['MercuMeVenusruruNeptuneyry', 'MercuMeVenusrurNeptuneyry'], ['VenNppepteunVeneussus', 'Vensus'], ['Venues', 'Jupi'], ['eurccury', 'euUUranMuPlutooryusrccury'], ['JuVeMeurcurynuespi', 'JuVeMeurcurynuespi'], ['Jiter', 'MMerMMercurcury'], ['PlMeuyrcPUranucuryulut', 'Pluto'], ['JMJSaVenuJupJupitererstuurnieurPUrannucuryuto', 'JMJSatuurniterercuryMeurcuryVensusPUranuslMeurcuryuto'], ['Jupitrer', 'Venuees'], ['Veneu', 'Meurcuury'], ['MMercur', 'Mercur'], ['MercuMeVenusrcurNeptuneyry', 'Venuees'], ['VeMeeurMerryrcusrynues', 'VVensuseMeurcurynues'], ['MercuMeptuneyry', 'Venuees'], ['rMerSaturnry', 'rMerSaturnry'], ['utSatJiterunurno', 'utSatJiterunurno'], ['utSatuurno', 'uutSatuurno'], ['JupJiterMeVJupitreerenusrcury', 'JupJiterMeVenuotoPlPutusrcuryMeVenusrcury'], ['VVeneu', 'Jiupiter'], ['MMerceury', 'MMercury'], ['Uranus', 'JupJiter'], ['JitPUMJSatuurniterercuryPUranuuslMeurcuryutoranur', 'Jiter'], ['JitPUMJSatuurnitNeptuneerercuryPUranuuslMeurcuryutoranur', 'Jiter'], ['JuPtUranurrsluatoi', 'JuPtUranursluatoi'], ['JupJupiteriMrer', 'JupJupiteriter'], ['PJMJSatuurniterercuryMeurcuryVensusPUranuslMeurcuryutoUranu', 'MercuryJupi'], ['JMJSatrannucuryuto', 'JMJSatuurnieurPUrannucuryuto'], ['SaturUPUranuJPUrannuiteruryMarMsranusn', 'MercSaturnury'], ['PUranruslMeurPlMeuyrccuryur', 'PUranruslMeurcuerryutoJJJupiteruMererer'], ['UPUranuJiteruryMaruMsranus', 'UPUranuJiteruryMarMsranus'], ['Venuus', 'Pluto'], ['MMury', 'MMury'], ['MeVenusrcury', 'MeVenusrncury'], ['VVeneu', 'utSatMaruurno'], ['Meurcury', 'P'], ['PiUranuJiterury', 'JJupiteruMercuryJupipiter'], ['Neptune', 'NNepteune'], ['MeVenuotoPloPutusrcury', 'MeVenusJupiutJupitererrcury'], ['Maas', 'MeVenJJupiterusrcMercuryJupiurNeptuney'], ['MMerMMercuy', 'MMerMMercurcury'], ['MMerMMercuy', 'MMerMMercuy'], ['PUrJJupiJitPUranuslMeurcuryutoJerterupiteranu', 'VVeneu'], ['JJupiMJSatuurniterercuryPUranuslMeurcuryutoer', 'Plut'], ['rMerry', 'PUranuslMeurcuerryutoJupiter'], ['JutSatuuPUranuslMeurcrMuryuerryutoJJJupiteruMerererrnoupi', 'Jupiter'], ['JupitEarrthJupitererVeneNpepteunVeneusu', 'Veneu'], ['PUMJSatuurnuryPUranuuslMeurcuryutoranu', 'Jupiter'], ['MeVenusrcurNeptuneyMercury', 'MeVenusrcurNeptuneyMercury'], ['MaEarrthrMs', 'VenuJupJupiterers'], ['Satuurn', 'Saturun'], ['Uranus', 'JJJiteirupiteruJMercuryPUranuJupipiter'], ['SatPUranusVenuJupMercuryiutJupitereorsJMJSatuurniterercurPUranuslMeurcuryutolutourn', 'SatPUranusVenuJupMercuryiutJupitereorsJMJSatuurniterercurPUranuslMeurcuryutolutourn'], ['PUranruslMeurPlMeuyrccuryur', 'PUranruslMeurPlMeuyrccuryur'], ['SatPUranusVenuJupMercuryiutJupitereorsJMJSatuurniterercurPUranuslMeurcuryutolutourn', 'MeVenuotoPlPutusrcury'], ['MrerMcuryJitPUMJSatuurniterercuryPUranuuslMeurcuryutoranur', 'JitPUMJSatuurniterercuryPUranuuslMeurcuryutoranur'], ['VePUranuJiterurysus', 'VePUranuJiteruryrMeryus'], ['PlMeuyrcPUranucuryu', 'PlMeuyrcPUranucuryu'], ['Neptune', 'PtUranursluto'], ['Plutoo', 'oPlutoo'], ['JJupiteruMercuuryJupipiter', 'JJupiteruMercuryJupipiter'], ['Satuurn', 'SatPrun'], ['uuuto', 'uuto'], ['SatPrun', 'MeuurcuryMVensus'], ['PUVeMJSatuurniterercuryPUranuslMeurcuryutoMeurcurynuesranuJiterury', 'PUVeMJSatuurniterercuryPUranuslMeurcuryutoMeurcurynuesranuJiterury'], ['VeJMJSatuurniterercuryMeurcuryVeneurcuryutous', 'Mars'], ['VeMJSatuurniterercuryPUranuslMeurcuryutoMeurcurynues', 'JuVeMeurcurynruespi'], ['Jiitier', 'JitPUMJSatuurniterercuryPUranuuslMeurcuryutoranur'], ['Saturn', 'PtUranusluto'], ['uto', 'JupitJupitVenPUrVeneuJJupiterupiteranuotoPlutuuserer'], ['JupJupiteriter', 'MyJiterercury'], ['VenuPluts', 'Jitupiter'], ['PUranu', 'Mercury'], ['PtUranurNppeepteunVeneusto', 'PtUranurNppeepteunVeneusto'], ['JupitEarrthJupitererVeneNpepteunVeneusu', 'JupitEarrthJupitererVeneNpepteunVeneusu'], ['utoPJuPtUranurrsluratoilut', 'utoPJuPtUranurrsluatoilut'], ['PUrJJJupitEarrthJupitererVeneNpepteunVeneusuupitrupiteranu', 'PUrJJupitrupiteranu'], ['Plut', 'MyJiterercury'], ['MJSatuurniterercuryPUranuslMeurcuryuPlutto', 'MJSatuurniterercuryPUranuslMeurcuryuto'], ['Jiter', 'VenuJupJupiterersluto'], ['oPlutoo', 'MeVenusrcurNeptuney'], ['pJupiJupJiterMeVJupitreerenusrcury', 'Jupiter'], ['JupiMerry', 'VeJMJSatuurniterercuryMeurcuryVeneurcuryutous'], ['MMMercury', 'MMercury'], ['NNepteune', 'NNepteune'], ['JuVeMMeVenusrcurNeptuneyeu', 'PlMeuyrccuryPu'], ['MercuryJupi', 'MercuryJupi'], ['UPUranuJiteruryMarMsranus', 'rMerSaturnryJupitEarrthJupiterer'], ['MarMMs', 'MarMs'], ['Jite', 'MMerMMerrcuy'], ['PUranruslMeurPlMeuyrccuryurM', 'Meuyrccury'], ['MeMMercMury', 'Veneus'], ['SatPUranusVeanuJupMercuryiutJupiterersJMJSatuurniterercuryPUranuslMeurcuryutolutourn', 'SatPUranusVenuJupMercuryiutJupiterersJMJSatuurniterercuryPUranuslMeurcuryutolutourn'], ['VeJMJSatuurniterercuryMeurcuryVeneurcuryutous', 'VeJMJSatuurnryVeneurcuryutous'], ['JupJtiteer', 'JupJter'], ['PUranu', 'VeJMJSatuurnryVeneurcuryutous'], ['PUranruslMeurcuerryutoJJJupiteruMererer', 'PUranruslMeurcuerryutoJJJupiteruMererer'], ['PUranusluto', 'JupitJitererterer'], ['JupJiterMeVenusrcury', 'Jiter'], ['VeMeurcusrynues', 'Pluto'], ['PUranruslMeurPlMeuyrccuryurM', 'Mrry'], ['pNeptne', 'PllutJiter'], ['eJiter', 'eJiter'], ['MeuurcuryMeVensusury', 'MMerMMercuy'], ['PUranussluto', 'Mars'], ['MeMMerMMercurceuryurcuMry', 'Meurucuury'], ['JMJSatuurniterercuryPUranuslMeurcuryuto', 'oPlu'], ['utSatunuorno', 'Pluo'], ['PlMeuyrcPUranucuryu', 'PlMeuyrcPUranucuJitPUranuslMeurcuryutoJerryu'], ['uotoPluMeVenuotoPloPutusrcuryt', 'uotoPlut'], ['NppepteMMercuryunVeneus', 'MeVenusrcurNeptuney'], ['JitVenueser', 'Jiter'], ['Jiter', 'JitPiUranuJiteruryr'], ['JuVeMeurcurynuespi', 'PUranruslMeurPlMeuyrccuryur'], ['JupJupiteriter', 'uuto'], ['Venues', 'rMurSatPUranusVeanuJMMury'], ['MMerMMercurcurPy', 'VeMeurcEartluthurynues'], ['MercuMeVenusrurNeputuneyry', 'MercuMeVenusrurNeputuneyry'], ['PUranusslutto', 'NNeptune'], ['JMJSatuurniterercuryPUranuslMeurcuryuto', 'JMJeurcuryutoUPUranuJiteruryMarMsranus'], ['PtUranurNppeepteunVeeneusto', 'PtUranurNppeepteunVeneusto'], ['JupitJitererterer', ''], ['s', 'Plutoo'], ['JiterVenuus', 'Jiter'], ['UrasnUus', 'arrMurSatPUranusVeanuJMMury'], ['PlMeryu', 'Pluto'], ['uotoPlut', 'Satuuurn'], ['Jiteir', 'JiMuPlutooryter'], ['uotoPlPut', 'utPJitPUranuslMeurcuryutoJerlut'], ['PUrJJupitrupiteranu', 'MuPlutoory'], ['', 'uto'], ['Mars', 'NeptunePUranuslMeurMMercuryryuto'], ['Jupitrer', 'Veenuees'], ['MMerMMerrcuy', 'Pluo'], ['MMeurucuryVensusPlMeuycPUranucuryu', 'PlMeuyrccuryPu'], ['uotoPlPut', 'Venus'], ['MMercury', 'MMercur'], ['Veunus', 'MeVenusrcurNeptuneyMercury'], ['PUMJSatuurniterercuryPUranuuslMerMerSaturnryJupitEarrthJupitererurcuryutoranu', 'PUMJSatuurniterercuryPUranuuslMerMerSaturnryJupitEarrthJupitererurcuryutoranu'], ['VeJMJSatuurniterercuryMeurcuryPlMeuyrcPUranucuryulutVeneurcuryutous', 'Marslut'], ['anus', 'Uranus'], ['eVenues', 'MercuMeVenusrcurNeptuJitupiterry'], ['NppeepnteunVeneus', 'NppepteunVeneus'], ['s', ''], ['Jiupiter', 'VVeneu'], ['MeVenuotoPloPutMMerMMercurceuryusrcury', 'MeVenuotoPloPutusrcury'], ['JupJiter', 'Jupiter'], ['Plutlu', 'Plutlut'], ['NeptunePUranuslMeurMMercu', 'NeptunePUranuslMeurMMercuryryuto'], ['Venues', 'Saturn'], ['MeuurcuryMVensus', 'MeVenusrcurNeptuneyMercury'], ['VerJMJSatuurniterercuryMeurcuryPlMeuyrcPUranucuryulutVeneurcuryutous', 'Venus'], ['VePUranuJiterurysus', 'VePUranuJiteruruuutoyrMeryus'], ['PUranruslMeurPlMeuyrccuryurM', 'MJSatuurniterercuryPUranuslMeurcuryuto'], ['JupiMerry', 'PUVeMJSatuurniterercuryPUranuslMeurcuryutoMeurcurynuesranuJiterury'], ['Maas', 'MeVenJJupiterey'], ['Pl', 'JJupiter'], ['MercuMeVenusrurNeptuneyry', 'Plut'], ['MMerMMerccuy', 'MMerMMercuy'], ['Mar', 'VeMeurcEarthurynJitPUMJSatuurniterercuryPUranuuslMeurcuryutoranurues'], ['Jitupitter', 'Jitupiter'], ['MeVenuotoPlPutusrcury', 'MeVenuotoPlPutusrcury'], ['MMerMMerrcuy', 'oPlVVensuseMeurcurynuesutoo'], ['UUrarnus', 's'], ['ss', ''], ['MMercur', 'Mercr'], ['Jiupiter', 'PUranruslMeurcuerryutoJJJupiteruMerererJiterury'], ['Mars', 'rMury'], ['VenuPlJuVeMeMJSatuurniterercuryPUranuslMeurcuryutourcurynuespiuts', 'VenuPlJuVeMeMJSatuurniterercuryPUranuslMeurcuryutourcurynuespiuts'], ['MeVenusrcurNeptunJJupiteruMercuryJupipiterey', 'MeVenusrcurNeptuney'], ['NNePUranJMJSatuurniterercuryPUranuslMeurcuryrutouslutopteune', 'NNepteune'], ['PlMeuyrcPUranNNepteuneucuryu', 'PJupitJupiJupiutJupiterertererlMeuyrcPUranucuJitPUranuslMeurcuryutoJerryu'], ['MMerMMercurcurPy', 'PtUranurNppeeptenunVeneusto'], ['Pluto', 'Plouto'], ['SatPUuranusVenuJupMercuryiutJupitereorsJMJSatuurniterercurPUranuslMeurcuryutolutourn', 'SatPUranusVenuJupMercuryiutJupitereorsJMJSatuurniterercurPUranuslMeurcuryutolutourn'], ['Venuuus', 'Veenuus'], ['JupJiterMeVJupitreerenusrcury', 'JupJiPlMeuyrccuryuenuotoPlPutusrcuryMeVenusrcury'], ['Venus', 'JuPtUranursluatoi'], ['JJupiteruJMercuryJupipiter', 'PlMeuyrcPUranNNepteuneucuryu'], ['UUranustupitter', 'Jitupitter'], ['VeJMJSatuurniterercuryMeurcuryVeneurcuryutous', 'MercuryJupi'], ['JVenuuusupiter', 'Veneus'], ['MercuMeVenusrurNeptuneyry', 'Jitup'], ['rMetuneturnry', 'Saturun'], ['JJupiter', 'pNeptne'], ['Venuuus', 'MeurcuryMVensus'], ['PlMeuyMMerMMerrcuyrccuryPu', 'PlMeuyrccuryPu'], ['VenuPlJuVeMeurcurynuespiuts', 'VeMeurcEarthurynJitPUMJSatuurniterercuryPUranuuslMeurcuryutoranurues'], ['Uranuus', 'Uranus'], ['NNePUranJMJSatuurniterercuryPUranuslMeurcuryrutouslutopteune', 'JupitJupiJupiutJupiterertetrer'], ['', ''], ['Mercury', ''], ['', 'Saturn'], ['S', 'MSaturnercury'], ['Venus', 'Uranus'], ['Jupirter', 'Pluto'], ['Saturn', 'MaNeptune'], ['MSaturnercury', 'Venus'], ['Neptu', 'Neptu'], ['SaturEarthn', 'MaNeptune'], ['MaNeptune', 'Neptune'], ['Neptu', 'Mercury'], ['MSaturnercury', 'Vs'], ['cMercry', 'Mercry'], ['Neptu', 'Earth'], ['Jupiter', 'Veunus'], ['Jupiter', 'Vnus'], ['MarsMSaturneMercuryrcury', 'MarsMSaturneMercuryrcury'], ['uVnus', 'Jupiter'], ['MarsMSaturneMercuryrcurypiter', 'VenuscMercry'], ['Neptu', 'Pluto'], ['MVenuscMercryarsMSaturneMercuryrcury', 'MarsMSaturneMercuryrcury'], ['Jupiter', 'MSaturnercury'], ['eJupirter', 'Pluto'], ['SaturEarthhtn', 'VeunMVenuscMercryarsMSaturneMercuryrcuryus'], ['MarsMSaturneMercuryrcurypiter', 'MSaturnercury'], ['Venus', 'Ms'], ['SaturEarthhtn', 'SaturEarthn'], ['MSaturnercury', 'Neptu'], ['Jupiter', 'MSatuy'], ['MaNeptune', 'SaturEarthn'], ['Jupirter', 'Jupiter'], ['Mercrry', 'Mercry'], ['Vnuss', 'Vs'], ['Jupiter', 'MaNeptune'], ['Vnuss', 'MSatuy'], ['MSMaturnercury', 'MSaturnercury'], ['MVenusMercurycMercryarsMSaturneMercuryrcury', 'Neptu'], ['JupiUranuster', 'MSaturnercury'], ['MSaturnercury', 'Vnuss'], ['MarsMSaturneMercuryrcurypiter', 'MarsMSaturneMercuryrcurypiter'], ['Neptu', 'Vnus'], ['Jupirt', 'JuMercurypiter'], ['SaturEarthhtn', 'Mercrry'], ['Jupirter', 'Neptune'], ['Jupiter', 'JuepiMSatuyter'], ['MaNeptuMVenuscMercryarsMSaturneMercuryrcuryune', 'MaNeptuune'], ['MSaturnercury', 'MSMaturnercury'], ['uVnMSaturnercury', 'MarsMSaturneMercuryrcury'], ['Pluto', 'Neptune'], ['Pluto', 'Neptu'], ['MSaturnercurMarsy', 'Vs'], ['Vnuss', 'Vnuss'], ['VenusUranuscMercry', 'VenusUranuscMercry'], ['SatuMercuryrEarthhtn', 'SatuMercuryrEarthhtn'], ['Ms', 'Mercury'], ['Jupiter', 'NeptuneVnus'], ['eJupirter', 'MarsMSaturneMercuryrcurypiter'], ['MSaturnercury', 'MSaturnercury'], ['MaNeptune', 'MSaturnercury'], ['MaNeptVeunMVenuscMercryarsMSaturneMercuryrcuryusune', 'MSaturnercury'], ['Jupitter', 'Jupitter'], ['MarsMSaturrneMercuryrcurypiter', 'MarsMSaturneMercuryrcurypiter'], ['Ea', 'Earth'], ['Vs', 'Vs'], ['JuMerJuMercurypitercurypiter', 'JuMercurypiter'], ['VsSatuMercuryrEarthhtn', 'Vs'], ['Ms', 'MarsMSaturneMercuryrcury'], ['MSaturnercury', 'MEarthSaturnercury'], ['upiUranuster', 'MSaturnercuryVenusUranuscMercry'], ['VenuscMercry', 'MarsMSaturneMercuryrcurypiteMaNeptuuner'], ['uss', 'MarsMSaturrneMercuryrcurypiter'], ['Mss', 'MarsMSaturneuMercuryrcury'], ['Pluto', 'Mercury'], ['uVnMSaturnercuVenusry', 'uVnyMSaturnercury'], ['SaturEarthhtn', 'Jupiter'], ['NeptuneVnus', 'MarsMSaturneMercuryrcury'], ['Neptu', 'Neptuu'], ['uss', 'ss'], ['Mercrry', 'Mercrry'], ['JuMercurypiter', 'Mercrry'], ['JuJuepiMSatuyterpirter', 'JuJuepiMSatuyterpirter'], ['uVnMSaturnercuVenusry', 'Mercury'], ['MaNeptune', 'MSMaturnercury'], ['Mrcrry', 'Mercrry'], ['JuMerJuMercurypitercurypiter', 'Neptu'], ['Mercrry', 'VenuscMercry'], ['MaMarsMSaturneuMercuryrcurys', 'Neptu'], ['MarsMSaturneMercuryrcuryPluto', 'Mercury'], ['MarsMSaturneMercuryrcuryrpiter', 'MarsMSaturneMercuryrcurypiter'], ['sVeunusVnus', 'sVnus'], ['MaNeptVeunMVenuscMercryarsMSaturneMercuryrcuryusune', 'MarsMSaturneMercuryrcurypiter'], ['MarsMSaturneMercuryrcurypiter', 'JuJuepiMSatuyterpirter'], ['uJuMerJuMercurypitercurypiterVnMSaturnercury', 'uVnMSaturnercury'], ['JupirsVnusr', 'JupiVsSatuMercuryrEarthhtnrtuer'], ['PlutEa', 'Jupirt'], ['Jupiter', 'VeunMVenuscMercryarsMSaturneMercuryrcuryus'], ['Neptune', 'Pluto'], ['Ms', 'VeunusMs'], ['Jupiiter', 'MaNeptVeunMVenuscMercryarsMSaturneMercuryrcuryusune'], ['SS', 'MSaturnercury'], ['MSatuy', 'Pluto'], ['JupiVsSatuMercuryrEarthhtnrtuer', 'Mercry'], ['Jeupirter', 'Jupiter'], ['SaturEarthn', 'MVsSatuMercuryrEarthhtnaNeptunUranuse'], ['MaMarsMSaturneuMercuryrcurys', 'Neptune'], ['VenusUranuscMercryMarsMSaturneMercuryrcury', 'VenusUranuscMercryMarsMSaturneMercuryrcury'], ['uVnus', 'MarsMSaturneMercuryrcurypiter'], ['sVnuss', 'Vnuss'], ['VeuNeptuneVnusnus', 'Veunus'], ['VenusUranuscMercryMarsMSaturneMercuryrcury', 'uVnus'], ['SaturEarthn', 'SaturEarthn'], ['Nepttu', 'Neptuu'], ['VsSatuMercuryrEarthhtn', 'MaNepMtune'], ['MarsMSaturneMercuryrcurypiter', 'Neptuu'], ['MSatuy', 'Vs'], ['MSatuy', 'PlutoV'], ['VVenus', 'Mars'], ['uVnryMSaturnercury', 'Mercrry'], ['VsSatuMercuryrEarthhtnJupiter', 'VsSatuMercuryrEarthhhtnJupiter'], ['Jupiitier', 'Jupiter'], ['PtlutE', 'PtlutE'], ['Jupiitier', 'Jupiiter'], ['JupNeptuneVnusirter', 'JupNeptuneVnurter'], ['VenuscMercry', 'VenuscMercry'], ['Neptu', 'MarsMSaturneMercuryrcuryPluto'], ['JuJpiter', 'Jupiter'], ['VVenus', 'Ms'], ['Mercyry', 'Mercry'], ['MSaturnerScury', 'MEarthSaturnercury'], ['SaturEarthn', 'sMVsSatuMercuryrEarthhtnaNeptunUranuseVeunusVnus'], ['Vnuss', 'cMercry'], ['MSaturneVeunMVenuscMercryarsMSaturneMercuryrcuryusrScury', 'MSaturneVeunMVenuscMercryarsMSaturneMercuryrcuryusrScury'], ['Vnsus', 'Jupiter'], ['JupMaNeptVeunMVenuscMercryarsMSaturneMercuryrcuryusuneiter', 'Jupiter'], ['uVnMSaturnercuVenusry', 'JupirsVnusr'], ['Venus', 'sMMars'], ['MaNeptunePlutEa', 'MaNeptune'], ['MarsMSaturneMercuryrScurypitePlutEar', 'JuJuepiMSatuyterpirter'], ['VsSatuMercuryrEanJupiter', 'VsSatuMercuryrEarthhhtnJupiter'], ['Mercyry', 'MSaturneVeunMVenuscMercryarsMSaturneMercuryrcuryusrScury'], ['VeuNeptunMarsMSaturneMercuryrcurypitereVnusnus', 'VeuNeptuneVnusnus'], ['VVenus', 'VVenus'], ['uVnyMSaturnercury', 'MarsMSaturrneMercuryrcurypiter'], ['SaturEarthn', 'uss'], ['VsSatuMercuryrEarrthhtn', 'VsSatuMercuryrEarthhtn'], ['VenusUranuscMercryMarsMSaturneMercuryrcury', 'Vs'], ['VenuscMMarsMSaturneMercuryrcuryercrPlutEa', 'VenuscMMarsMSaturneMercuryrcuryercrPlutEa'], ['uVnryMSaturnercury', 'uVnryMSaturnercury'], ['Mrcrry', 'Mrcrry'], ['Vs', 'uVnuss'], ['MarsMSaturrneMercuryrcurypiter', 'MarsMSaturneMercuryrcuryPluto'], ['SS', 'SS'], ['MarsMtSaturneMercuryrcurypiteMaNeptuuner', 'Neptu'], ['MSaturnercury', 'sMVsSatuMercuryrEarthhtnaNeptunUranuseVeunusVnus'], ['MSaturnercurMarsy', 'MSaturnercurMarsy'], ['Jupiitier', 'Saturn'], ['MercurrMSaturnercuryy', 'MercurMSaturnercuryy'], ['sMVsSatuMercuryrEarthhtnaNeptunUranuseVcMercryeunusVnus', 'sMVsSatuMercuryrEarthhtnaNeptunUranuseVeunusVnus'], ['JupitSaturEarthhtner', 'VensVeunusVnuss'], ['Uranus', 'MarsMSaturneuMercuryrcury'], ['MaNeptune', 'SaturEahn'], ['MSaturnerrcury', 'MSaturnercucry'], ['SaturEarthhtn', 'MarsMSaturrneMercuryrcurypiter'], ['sVnJuMercuirypiteruss', 'sVnJuMercurypiteruss'], ['Neptuu', 'Jupiiter'], ['Uranurs', 'Uranus'], ['VVenus', 'MarsMSaturrneMercuryrcurypiter'], ['JuJuepiMSatuyterpirter', 'MaNeptVeunMVenuscMercryarsMSaturneMercuryrcuryusune'], ['MaNepMtune', 'MSaturnercucry'], ['uVnMSaturnercuVenusry', 'Mercurssy'], ['MSMaturnercury', 'MSMaturnercury'], ['VVs', 'VVenus'], ['VsSatuMercuryrEarrthhtn', 'Vs'], ['VeuNeptunMarsMSaturneMercuryrcurypitereVnusnus', 'MSatuy'], ['SaturEarthn', 'MuSaturnercurMarsy'], ['VenuscMMarsMSaturneMercuryrcuryercrPlutEa', 'cMercry'], ['JuMerJuMercurypitercypiteJupiiterr', 'JuMerJuMercurypitercypiter'], ['VsSatuMercuryrEarthhtn', 'VsSatuMercuryrEarrthhtn'], ['uVnryMSaturnnercury', 'uVnryMSaturnercury'], ['MarsMSaturneMercuryrcurypiter', 'MarsMSaturneMercuryrcuryrpiter'], ['MuSatursy', 'Mercury'], ['sMVsSatuMercuryrEarthhMaNeptuunetnaNeptunUranuseVeunusVnus', 'sMVsSatuMercuryrEarthhtnaNeptunUranuseVeunusVnus'], ['PlutEa', 'MarsMSaturneMercuryrcuryPluto'], ['VVs', 'upiUranuster'], ['Neptu', 'SatuMercuryrEarthhtn'], ['Jupiitter', 'MaNeptVeunMVenuscMercryarsMSaturneMercuryrcuryusune'], ['MarrsMSaturneMercuryrcurJupirtery', 'MarrsMSaturneMercuryrcury'], ['Uranurs', 'MarsMSaturneMercuryrcurypiter'], ['MaMarsMSaturneuMercueryrcurys', 'Vs'], ['pitter', 'rJupiter'], ['Mercurssy', 'Neptu'], ['Mercyry', 'JupiVsSatuMercuryrEarthhtnrtuer'], ['VenusUranuscMercryMarturnnercuryrcury', 'VenusUranuscMercryMarsMSaturneMercuryrcury'], ['MSaturnercury', 'MarsMSaturrneMercuryrcurypiter'], ['uVnryMSaturnercury', 'VsSatuMercuryrEarthhtn'], ['MarrsMSaturneMercuryrcury', 'S'], ['pitter', 'sVnJuMercurypiteruss'], ['Neptune', 'MEarthSaturnercury'], ['SatuMercuryrEarthhtn', 'NJuJpitereptune'], ['JupMaNeptVeunMVenuscMercryarsMSaturneMercuryrcMVenusMercurycMercryarsMSaturneMercuryrcuryuryusuneiter', 'Jupiter'], ['SaturEarthn', 'SaturEarthhtn'], ['Mars', 'Neptu'], ['Venus', 'ars'], ['MVenuscMercryarsMSaturneMercuryrcury', 'sVnJuMercurypiteruss'], ['Mercuryuss', 'Mercury'], ['SaturEarthn', 'SaturEaMSaturnercuryrthn'], ['SaturuaEarthn', 'SaturMSaturnerScuryaEarthn'], ['VVMSaturnerScuryenus', 'MarsMSaturrneMercuryrcurypiter'], ['VenuMarssUranuscMercryMarturnnercuryrcury', 'VenusUranuscMercryMarsMSaturneMercuryrcury'], ['NJuJpitereptJupirsVnusrune', 'NJuJpitereptJupirsVnusrune'], ['Plluto', 'Mercury'], ['MuSaturnercurMarsy', 'MSaturnercury'], ['SaturEarthn', 'rJupiter'], ['nVnuss', 'Vnuss'], ['pitter', 'pitter'], ['Venus', 'MJupirsVnusrs'], ['lPlutEa', 'eJupirter'], ['MarsMSaturneMercuryrcuryrSaturn', 'MarsMSaturneMercuryrcuryrSaturn'], ['Uranus', 'S'], ['VMaNeptunePlutEas', 'VVenus'], ['MSaturnerScury', 'MuSaturnercurMarsy'], ['VsSatuMercuryrEarthhtn', 'VsSatuMercuryrEarthhtn'], ['JuMerJuMercurypitercypiter', 'JuepiMSatuyter'], ['JuMerJuMercurypitercurypiter', 'VsSatuMercuryrEarthhtn'], ['aSatturEarthn', 'aSaturEarthn'], ['MSMaturnercury', 'MarsMSaturrneMercuryrcurypiter'], ['NJuJpitereptJupirsVnusrune', 'SatuMercuryrEarthhtn'], ['MarsMSaturrneMercuryrcurypiter', 'Mercury'], ['PllutVenuscMercry', 'Plluto'], ['sMVsSatuMercuryrEarthhtnaNeptunUranuseVeunusVnus', 'sMVsSatuMercuryrEarthhtnaNeptunUranuseVeunusVnus'], ['MaNeptVeunMVenuscMercryarsMSaturneMercuryrcuryusune', 'JuJuepiMSatuyterpirter'], ['Vnssus', 'Jupiter'], ['Jupirter', 'r'], ['VsSatuMercuryrEarthhhtnJupiter', 'Neptu'], ['PlutEa', 'PlutEa'], ['MarsMSaturneeMercuryrcuryrpSiter', 'MarsMSaturneMercuryrcurypiter'], ['Juipirter', 'uVnus'], ['VenuscMercry', 'Mercrry'], ['uVnryMSaturnercury', 'VsSatuMercuryrEanJupiter'], ['MaNeptune', 'MaNeptune'], ['MSaturnercursy', 'MSaturJupiitaernercurMarsy'], ['JupMaNeptVeunMVenuscMercryarsMSaturneMercuryrcMVenusMercurycMercryarsMSaturneMercuryrcuryuryusuneiter', 'VsSatuMercuryrEarthhhtnJupiter'], ['uss', 'uss'], ['MaNeptVeunMVenuscMercryarsMSaturneMercuryrcuryusune', 'lPlutEa'], ['tu', 'tu'], ['MarsMSaturneMercuryrcurypiter', 'MarsMSaturneMercuryuVnyMSaturnercuryrcurypiter'], ['uVnus', 'VeuNeptunMarsMSaturneMercuryrcurypitereVnusnus'], ['MaMarsMSaturneuMercueryrcurys', 'VMVsSatuMercuryrEarthhtnaNeptunUranuses'], ['uVnMSaturnercury', 'MarsMSaeMercuryrcury'], ['Juipirter', 'MarsMSaturneuMercuryrcury'], ['SaturEarnttn', 'SaturEarnthhtn'], ['MSaturnercury', 'MarsMSaturrneMercuryrcuMSaturnercursyrypiter'], ['MSaturnercury', 'MSatuy'], ['Mercyry', 'JupNeptuneVnurter'], ['MeVMVsSatuMercuryrEarthhtnaNeptunUranusesrcury', 'Mercury'], ['SaturEarJupirtthhtn', 'VeunMVenuscMercryarsMSaturneMercuryrcuryus'], ['Jupiiter', 'Pluto'], ['JupirsVnusr', 'Neptu'], ['Neputune', 'MEarthSaturnercury'], ['MaNeptunJuMerJuMercurypitercypiteJupiiterre', 'SaturEa'], ['VenusUranuscMercryMarsMSaturneMercuryrcury', 'uVunus'], ['MVenusMercurycMercryarsMSaturneMercuryrcury', 'Mercyry'], ['NepMercurrMSaturnercuryyttu', 'Neptuu'], ['Neptuu', 'Neptuu'], ['SaturuaEarthn', 'MSaturnercury'], ['SaturEaMSaturnercuryrthn', 'SaturEaMSaturnercuryrthn'], ['NeptuSatuMercuryrEarthhtn', 'Neptu'], ['Uranurs', 'UranuMercurMSaturnercuryys'], ['uVnryMSaturnercury', 'VhsSatuMercuryrEarthhtn'], ['Pllutlo', 'Mercury'], ['Neptu', 'MuSaturnercurMarsy'], ['Mercuryuss', 'Venus'], ['SaturEarthhcMercrytn', 'SaturEarthhtn'], ['SaturEa', 'MercurMSaturnercuryy'], ['ssVnuss', 'ssVnuss'], ['sMVsSatuMercuryrEarthhMaNeptuunetnaNeptunUranuseVeunusVnus', 'Venus'], ['pitter', 'rpJupiter'], ['Pllluto', 'Mercury'], ['aaSaturEarthn', 'MVenuscMercryarsMSaturneMercuryrcury'], ['JuMcurypiter', 'JuMercurypiter'], ['uVnMSaturnercuVenusry', 'ars'], ['MarsMSaturrneMercuryrcuMSaturnercursyrypiter', 'MarsMSaturrneMerycuryrcuMSaturnercursyrypiter'], ['Neptu', 'VenusUranuscMercryMarturnnercuryrcury'], ['SaturEarthhttn', 'SaturEarthn'], ['SatuMercuryrEarthhtn', 'SatuMercMJupirsVnusrsrthhtn'], ['JupirsVnusr', 'uVnMSaturnercuVenusry'], ['MaNeptunePlutEa', 'MarsMSaturrneMercuryrcurypiter'], ['JupNeptuneVMVenusMercurycMercryarsMSaturneMercuryrcurynusirter', 'JupNeptuneVnusirter'], ['MarsMSaturneMercuryrcurypiteMaNeptuuner', 'Mercury'], ['SaturEarrthhttn', 'SaturEarrthhttn'], ['SatturEarthn', 'MaNeptune'], ['Mercury', 'Neptu'], ['SatuVsrEarthn', 'Jupiitier'], ['MrcrrysVeunusVnus', 'MrcrrysVeunusVnus'], ['MarsMtSaturneMercuryrcurypiteMaNeptuuner', 'yuVnyMSaturnercury'], ['Usranus', 'Jupiter'], ['MarsMSaturneuMercuryrcury', 'MarsMSaturneuMercuryrcury'], ['VsSatuMerrcuryrEarthhtn', 'VsSatuMercuryrEarthhtn'], ['uVnMSaturnercuVenusry', 'Plluto'], ['Jupititer', 'Jupititer'], ['MSatuy', 'yuVnyMSaturnercury'], ['sMMars', 'VVs'], ['uJuMerJuMercurypitercurypiterVnMSaturnMaMarsMSaturneuMercueryrcurysercury', 'uVnMSaurnercury'], ['sVnJuMercuuirypiteruss', 'sVnJuMercurypiteruss'], ['MarsMSaturneMerMcuryrcuryPluto', 'Mercury'], ['MarsMSaturneMerMcauryrcuryPluto', 'Mercury'], ['Neptu', 'Vnssus'], ['sVnJuMercurypiteruss', 'aSaturEarthn'], ['VsSatuMercury', 'VsSatuMercuryrEarthEahtn'], ['SaturEarthhhtn', 'SaturEarthhtn'], ['MarrsMSaturneMercuryrcurJupirter', 'MarrsMSaturneMercuryrcurJupirtery'], ['cMercPllutVenuscMercryy', 'cMercMry'], ['Mercrcrry', 'Merrcrry'], ['cMercry', 'SaturEaMSaturnercuryrthn'], ['PlutVenuscMMarsMSaturneMercuryrcuryercrPlutEao', 'Pluto'], ['VenusUranuscMercryMaMaNeptunJuMerJuMeVnusteJupiiterrercury', 'VenusUranuscMercryMaMaNeptunJuMerJuMeVnusteJupiiterrercury'], ['Neptu', 'JuMcurypiter'], ['SS', 'r'], ['JupirsVnusr', 'uVnMSaturnMaNeptuuneercuVenusry'], ['NVVMSaturnerScuryenuseptu', 'Vnssus'], ['pittper', 'pittper'], ['JupiVsSatuMercuryrEarthhtnrtuer', 'MEarthSaturnercury'], ['PlutEa', 'SaturMSaturnerScuryaEarthn'], ['NVVuMSaturnerScuryenuseptu', 'NVVMSaturnerScuryenuseptu'], ['MuStatuy', 'MSatuy'], ['MSaturnerccury', 'MEarthSaturnercury'], ['cMercPllutVenEarcryy', 'cMercPllutVenuscMercryy'], ['Jupiitier', 'Juppiter'], ['VsSatuMerrcuryrEaarthhtn', 'VsSatuMercuryrEarthhtn'], ['SaturEarrathn', 'Earth'], ['Uranurs', 'MarsMSaturneMerMcuryrcuryPluto'], ['MSaturnerScury', 'NeptMarsMSaturneeMercuryrcuryrpSiteruu'], ['auaSaturEarthn', 'MVenuscMercryarsMSaturneMercuryrcury'], ['sVnJuMercurypiteruss', 'sVnJuMercurypiteruss'], ['MarsMSaturneMpercuryrScurypitePlutEar', 'MaNeptunJuMerJuMercurypitercypiteJupiiterre'], ['Mss', 'MarsMSatMurneuMercuryrcury'], ['MSaturnercucry', 'MSMaturnercury'], ['SatulPlurtEaruaEarthn', 'SaturuaEarthn'], ['MSaturJupiitaernercurMarsy', 'MuSaturnercurMarsy'], ['MarsMSMSaturnercurMarsyaturneMercuryrcuryPluto', 'Mercury'], ['Jupititer', 'JupiUranusterupititer'], ['MercurrMSaturnercuryy', 'Jupiter'], ['VsSatuMerrcuryrEarthhtn', 'uVnMSaturnMaNeptuuneercuVenusry'], ['VsSaSaturEarrathnMerrcuryrEarthhtn', 'uVnMSaturnMaNeptuuneercuVenusry'], ['MarsMSaturneMpercuryrScurypitePrlutEar', 'MaNeptunJuMerJuMercurypitercypiteJupiiterre'], ['SaturEarrathn', 'V'], ['MaNepMtune', 'JuJuepiMSatuyterpirterpitter'], ['VenuscMMarsMSaturneMercuryrcuryercrPlutEa', 'PlutVenuscMMarsMSaturneMercuryrcuryercrPlutEao'], ['VsSatuMerrcuryrEaarthMuSatursyhtn', 'VsSatuMercuryrEarthhtn'], ['MarsMSaturneMVsSatuMercuryrEarthhhtnJupiterercuryrcurypiter', 'MarsMSaturneMercuryrcurypiter'], ['SatuMhercuryrEarthhtn', 'SatuMhercuryrEthhtn'], ['JupiitierSatulPlurtEaruaEarthn', 'Santurn'], ['MJuMcurypiterSaturnercucry', 'MSMaturnercury'], ['JuepiMSatuyter', 'JuepiMSatuyter'], ['MSatuy', 'uVnus'], ['auaSaturEarthn', 'JupiitierSatulPlurtEaruaEarthn'], ['MaNeptVeunMVenusccMercryarsMSaturneMercuryrcuryusune', 'MaNeptVeunMVenusccMercryarsMSaturneMercuryrcuryusune'], ['Jupiter', 'VeunMVenuscMercryarsMSaturyus'], ['JupirsVnusr', 'uVnMSJuMerJuMercurypitercypiteJupiiterraturnMaNeptuuneercuVenusry'], ['MarsMSaturneMercuryrcurypiter', 'MarsMSaturneMercuryrcurypaSaturEarthnitMercrryer'], ['VnssMarrsMSaturneMercuryrcuryus', 'Vnssus'], ['tpitMarsMSaturneMpercuryrScurypitePlutEarter', 'sVnJuMercurypiteruss'], ['MaNeMarsMSMSaturnercurMarsyaturneMercuryrcuryPlutoptune', 'MaNeptunePlutEa'], ['MaaNepMtune', 'sMVsSatuMercuryrEarthhtnaNeptunUranuseVeunusVnus'], ['pittper', 'pitrtper'], ['Nepttu', 'uVunus'], ['NeptuSaEarthhtn', 'NeplPlutEaPlllutou'], ['uVnrySaturEaMSaturnercuryrthncury', 'uVnryMSaturnercury'], ['SaturEarnttn', 'Jupiitier'], ['MarsMSaturneeMercuryrcuryrpSiter', 'MarsMSaturneMercuryrcurSypiter'], ['Ea', 'cMercPllutVenEarcryy'], ['MarsMSMSaturnercurMarsyaturneMercuryrcury', 'MarsMSMSaturnercurMarsyaturneMercuryrcuryPluto'], ['SaturEarthn', 'SaturEaJupiUranusterMSaturnercuryrthn'], ['MuSatursy', 'MarsMSaturneuMercuryrcury'], ['VsSatuMercuryrEarrthhtnJuepiMSatuyter', 'JuepiMSatuyter'], ['MSatuy', 'yuVnyMrSaturnercury'], ['MarsMSaturneMercuryrcurypiteMaNeptuuner', 'MercMury'], ['Jupirter', 'MaNeptuune'], ['Mercyry', 'MaNeptunJuMerJuMercurypitercypiteJupiiterre'], ['VsSatuMercuryrEarthhtn', 'VsSatuMercuryrEarrthhNeputunetn'], ['MarsMSMSaturnercurMarsyaturMarsMSaturneMercuryrcurypiteMaNeptuunerneMercuryrcuryPluto', 'MarsMSMSaturnercurMarsyaturneMercuryrcury'], ['NepMercurrMSaturnercuryyttu', 'rpJupiter'], ['VsSatuMercuryrEarrthhtn', 'MarrsMSaturneMercuryrcury'], ['Jupirter', 'uss'], ['VnssusNeptuu', 'pitterNeptuMSaturneVeunMVenuscMercryarsMSaturneMercuryrcuryusrScuryu'], ['MarsMSaturneMpercuryrScurypitePlutEar', 'VenuMarssUranuscMerccryMarturnnercuryrcury'], ['JupNeptuneVnusirter', 'MarrsMSaturneMercuryrcury'], ['sMVsSatuMercuryrEarthhMaNeptuunMaNeptVeunMVenusccMercryarsMSaturneMercuryrcuryusuneetnaNeptunUranuseVeunusVnus', 'MarsMSaturneMercuryrcurypaSaturEarthnitMercrryer'], ['JuJuepiMSatuyterpirterpitter', 'Jupiter'], ['MarsMSaturrneMercuryrcurypiter', 'VsSatuMercuryrEarthhhtnJupiter'], ['JuMercurypiter', 'JVsSatuMercuryrEarthEahtnuMercurypiter'], ['NeptuSaEarthhtn', 'MarsMSaturneMercuryrcuryPluto'], ['JuepiMSatuyteVenuMarssUranuscMerccryMarturnnercuryrcury', 'JuepiMSatuyter'], ['NVVuMSaturnerScuryenuseptu', 'NVVuMSaturnerScuryenuseptu'], ['uss', 'ssVnJuVeuNeptuneVnusnusMercuuirypiterusss'], ['Jupr', 'NeptuneVnus'], ['Venus', 'NepMercurrMSaturnercuryyttu'], ['McMercrySatuy', 'PlutuVnMSaturnercuryoV']]
    results = [('Saturn', 'Uranus'), ('Venus',), ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn'), ('Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus'), (), (), (), ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus'), (), ('Venus', 'Earth', 'Mars', 'Jupiter'), (), (), ('Uranus',), ('Mars', 'Jupiter', 'Saturn', 'Uranus'), ('Saturn',), ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus'), ('Earth',), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ('Jupiter', 'Saturn', 'Uranus'), ('Venus', 'Earth', 'Mars', 'Jupiter'), ('Earth', 'Mars'), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ('Earth', 'Mars', 'Jupiter'), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ('Earth', 'Mars', 'Jupiter', 'Saturn'), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ()]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(bf)