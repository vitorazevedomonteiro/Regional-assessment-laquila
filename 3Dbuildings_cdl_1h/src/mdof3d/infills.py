import openseespy.opensees as ops


def add_infills() -> None:
    """Add components of all infills to ops domain
    """
    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2000, -523.40578136, -0.0013, -5.23405781, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2000001, 70000, 11, 0.3049429593522586, 2000)
    ops.element('Truss', 2000002, 1, 70010, 0.3049429593522586, 2000)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2010, -479.91007478, -0.0013, -4.79910075, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2010001, 70010, 21, 0.3325777720901917, 2010)
    ops.element('Truss', 2010002, 11, 70020, 0.3325777720901917, 2010)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2020, -610.37179057, -0.0013, -6.10371791, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2020001, 70020, 31, 0.20490357996022812, 2020)
    ops.element('Truss', 2020002, 21, 70030, 0.20490357996022812, 2020)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2030, -479.91007478, -0.0013, -4.79910075, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2030001, 70030, 41, 0.3325777720901917, 2030)
    ops.element('Truss', 2030002, 31, 70040, 0.3325777720901917, 2030)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2040, -523.40578136, -0.0013, -5.23405781, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2040001, 70040, 51, 0.3049429593522586, 2040)
    ops.element('Truss', 2040002, 41, 70050, 0.3049429593522586, 2040)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2001, -441.49980718, -0.0013, -4.41499807, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2001001, 1, 12, 0.3486276037614604, 2001)
    ops.element('Truss', 2001002, 2, 11, 0.3486276037614604, 2001)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2011, -405.97205968, -0.0013, -4.0597206, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2011001, 11, 22, 0.3791336324340893, 2011)
    ops.element('Truss', 2011002, 12, 21, 0.3791336324340893, 2011)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2021, -526.22822767, -0.0013, -5.26228228, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2021001, 21, 32, 0.22370470431944123, 2021)
    ops.element('Truss', 2021002, 22, 31, 0.22370470431944123, 2021)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2031, -405.97205968, -0.0013, -4.0597206, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2031001, 31, 42, 0.3791336324340893, 2031)
    ops.element('Truss', 2031002, 32, 41, 0.3791336324340893, 2031)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2041, -441.49980718, -0.0013, -4.41499807, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2041001, 41, 52, 0.3486276037614604, 2041)
    ops.element('Truss', 2041002, 42, 51, 0.3486276037614604, 2041)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2002, -441.49980718, -0.0013, -4.41499807, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2002001, 2, 13, 0.3486276037614604, 2002)
    ops.element('Truss', 2002002, 3, 12, 0.3486276037614604, 2002)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2012, -405.97205968, -0.0013, -4.0597206, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2012001, 12, 23, 0.3791336324340893, 2012)
    ops.element('Truss', 2012002, 13, 22, 0.3791336324340893, 2012)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2022, -526.22822767, -0.0013, -5.26228228, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2022001, 22, 33, 0.22370470431944123, 2022)
    ops.element('Truss', 2022002, 23, 32, 0.22370470431944123, 2022)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2032, -405.97205968, -0.0013, -4.0597206, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2032001, 32, 43, 0.3791336324340893, 2032)
    ops.element('Truss', 2032002, 33, 42, 0.3791336324340893, 2032)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2042, -441.49980718, -0.0013, -4.41499807, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2042001, 42, 53, 0.3486276037614604, 2042)
    ops.element('Truss', 2042002, 43, 52, 0.3486276037614604, 2042)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2003, -441.49980718, -0.0013, -4.41499807, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2003001, 3, 14, 0.3486276037614604, 2003)
    ops.element('Truss', 2003002, 4, 13, 0.3486276037614604, 2003)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2013, -405.97205968, -0.0013, -4.0597206, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2013001, 13, 24, 0.3791336324340893, 2013)
    ops.element('Truss', 2013002, 14, 23, 0.3791336324340893, 2013)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2023, -526.22822767, -0.0013, -5.26228228, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2023001, 23, 34, 0.22370470431944123, 2023)
    ops.element('Truss', 2023002, 24, 33, 0.22370470431944123, 2023)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2033, -405.97205968, -0.0013, -4.0597206, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2033001, 33, 44, 0.3791336324340893, 2033)
    ops.element('Truss', 2033002, 34, 43, 0.3791336324340893, 2033)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2043, -441.49980718, -0.0013, -4.41499807, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2043001, 43, 54, 0.3486276037614604, 2043)
    ops.element('Truss', 2043002, 44, 53, 0.3486276037614604, 2043)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2004, -441.49884541, -0.0013, -4.41498845, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2004001, 4, 15, 0.34862964512164263, 2004)
    ops.element('Truss', 2004002, 5, 14, 0.34862964512164263, 2004)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2014, -405.97118896, -0.0013, -4.05971189, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2014001, 14, 25, 0.3791358396870425, 2014)
    ops.element('Truss', 2014002, 15, 24, 0.3791358396870425, 2014)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2024, -526.22728964, -0.0013, -5.2622729, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2024001, 24, 35, 0.22370603114218235, 2024)
    ops.element('Truss', 2024002, 25, 34, 0.22370603114218235, 2024)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2034, -405.97118896, -0.0013, -4.05971189, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2034001, 34, 45, 0.3791358396870425, 2034)
    ops.element('Truss', 2034002, 35, 44, 0.3791358396870425, 2034)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2044, -441.49884541, -0.0013, -4.41498845, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2044001, 44, 55, 0.34862964512164263, 2044)
    ops.element('Truss', 2044002, 45, 54, 0.34862964512164263, 2044)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2005, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2005001, 5, 16, 0.34863168649027615, 2005)
    ops.element('Truss', 2005002, 6, 15, 0.34863168649027615, 2005)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2015, -405.97031824, -0.0013, -4.05970318, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2015001, 15, 26, 0.37913804694907277, 2015)
    ops.element('Truss', 2015002, 16, 25, 0.37913804694907277, 2015)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2025, -526.2263516, -0.0013, -5.26226352, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2025001, 25, 36, 0.2237073579759088, 2025)
    ops.element('Truss', 2025002, 26, 35, 0.2237073579759088, 2025)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2035, -405.97031824, -0.0013, -4.05970318, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2035001, 35, 46, 0.37913804694907277, 2035)
    ops.element('Truss', 2035002, 36, 45, 0.37913804694907277, 2035)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2045, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2045001, 45, 56, 0.34863168649027615, 2045)
    ops.element('Truss', 2045002, 46, 55, 0.34863168649027615, 2045)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2006, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2006001, 6, 17, 0.34863168649027615, 2006)
    ops.element('Truss', 2006002, 7, 16, 0.34863168649027615, 2006)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2016, -405.97031824, -0.0013, -4.05970318, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2016001, 16, 27, 0.37913804694907277, 2016)
    ops.element('Truss', 2016002, 17, 26, 0.37913804694907277, 2016)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2026, -526.2263516, -0.0013, -5.26226352, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2026001, 26, 37, 0.2237073579759088, 2026)
    ops.element('Truss', 2026002, 27, 36, 0.2237073579759088, 2026)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2036, -405.97031824, -0.0013, -4.05970318, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2036001, 36, 47, 0.37913804694907277, 2036)
    ops.element('Truss', 2036002, 37, 46, 0.37913804694907277, 2036)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2046, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2046001, 46, 57, 0.34863168649027615, 2046)
    ops.element('Truss', 2046002, 47, 56, 0.34863168649027615, 2046)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2007, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2007001, 7, 18, 0.34863168649027615, 2007)
    ops.element('Truss', 2007002, 8, 17, 0.34863168649027615, 2007)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2017, -405.97031824, -0.0013, -4.05970318, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2017001, 17, 28, 0.37913804694907277, 2017)
    ops.element('Truss', 2017002, 18, 27, 0.37913804694907277, 2017)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2027, -526.2263516, -0.0013, -5.26226352, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2027001, 27, 38, 0.2237073579759088, 2027)
    ops.element('Truss', 2027002, 28, 37, 0.2237073579759088, 2027)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2037, -405.97031824, -0.0013, -4.05970318, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2037001, 37, 48, 0.37913804694907277, 2037)
    ops.element('Truss', 2037002, 38, 47, 0.37913804694907277, 2037)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2047, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2047001, 47, 58, 0.34863168649027615, 2047)
    ops.element('Truss', 2047002, 48, 57, 0.34863168649027615, 2047)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2700, -523.40578136, -0.0013, -5.23405781, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2700001, 70700, 711, 0.3049429593522586, 2700)
    ops.element('Truss', 2700002, 701, 70710, 0.3049429593522586, 2700)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2710, -479.91007478, -0.0013, -4.79910075, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2710001, 70710, 721, 0.3325777720901917, 2710)
    ops.element('Truss', 2710002, 711, 70720, 0.3325777720901917, 2710)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2720, -610.37179057, -0.0013, -6.10371791, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2720001, 70720, 731, 0.20490357996022812, 2720)
    ops.element('Truss', 2720002, 721, 70730, 0.20490357996022812, 2720)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2730, -479.91007478, -0.0013, -4.79910075, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2730001, 70730, 741, 0.3325777720901917, 2730)
    ops.element('Truss', 2730002, 731, 70740, 0.3325777720901917, 2730)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2740, -523.40578136, -0.0013, -5.23405781, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2740001, 70740, 751, 0.3049429593522586, 2740)
    ops.element('Truss', 2740002, 741, 70750, 0.3049429593522586, 2740)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2701, -441.49980718, -0.0013, -4.41499807, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2701001, 701, 712, 0.3486276037614604, 2701)
    ops.element('Truss', 2701002, 702, 711, 0.3486276037614604, 2701)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2711, -405.97205968, -0.0013, -4.0597206, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2711001, 711, 722, 0.3791336324340893, 2711)
    ops.element('Truss', 2711002, 712, 721, 0.3791336324340893, 2711)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2721, -526.22822767, -0.0013, -5.26228228, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2721001, 721, 732, 0.22370470431944123, 2721)
    ops.element('Truss', 2721002, 722, 731, 0.22370470431944123, 2721)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2731, -405.97205968, -0.0013, -4.0597206, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2731001, 731, 742, 0.3791336324340893, 2731)
    ops.element('Truss', 2731002, 732, 741, 0.3791336324340893, 2731)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2741, -441.49980718, -0.0013, -4.41499807, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2741001, 741, 752, 0.3486276037614604, 2741)
    ops.element('Truss', 2741002, 742, 751, 0.3486276037614604, 2741)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2702, -441.49980718, -0.0013, -4.41499807, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2702001, 702, 713, 0.3486276037614604, 2702)
    ops.element('Truss', 2702002, 703, 712, 0.3486276037614604, 2702)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2712, -405.97205968, -0.0013, -4.0597206, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2712001, 712, 723, 0.3791336324340893, 2712)
    ops.element('Truss', 2712002, 713, 722, 0.3791336324340893, 2712)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2722, -526.22822767, -0.0013, -5.26228228, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2722001, 722, 733, 0.22370470431944123, 2722)
    ops.element('Truss', 2722002, 723, 732, 0.22370470431944123, 2722)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2732, -405.97205968, -0.0013, -4.0597206, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2732001, 732, 743, 0.3791336324340893, 2732)
    ops.element('Truss', 2732002, 733, 742, 0.3791336324340893, 2732)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2742, -441.49980718, -0.0013, -4.41499807, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2742001, 742, 753, 0.3486276037614604, 2742)
    ops.element('Truss', 2742002, 743, 752, 0.3486276037614604, 2742)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2703, -441.49980718, -0.0013, -4.41499807, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2703001, 703, 714, 0.3486276037614604, 2703)
    ops.element('Truss', 2703002, 704, 713, 0.3486276037614604, 2703)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2713, -405.97205968, -0.0013, -4.0597206, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2713001, 713, 724, 0.3791336324340893, 2713)
    ops.element('Truss', 2713002, 714, 723, 0.3791336324340893, 2713)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2723, -526.22822767, -0.0013, -5.26228228, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2723001, 723, 734, 0.22370470431944123, 2723)
    ops.element('Truss', 2723002, 724, 733, 0.22370470431944123, 2723)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2733, -405.97205968, -0.0013, -4.0597206, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2733001, 733, 744, 0.3791336324340893, 2733)
    ops.element('Truss', 2733002, 734, 743, 0.3791336324340893, 2733)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2743, -441.49980718, -0.0013, -4.41499807, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2743001, 743, 754, 0.3486276037614604, 2743)
    ops.element('Truss', 2743002, 744, 753, 0.3486276037614604, 2743)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2704, -441.49884541, -0.0013, -4.41498845, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2704001, 704, 715, 0.34862964512164263, 2704)
    ops.element('Truss', 2704002, 705, 714, 0.34862964512164263, 2704)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2714, -405.97118896, -0.0013, -4.05971189, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2714001, 714, 725, 0.3791358396870425, 2714)
    ops.element('Truss', 2714002, 715, 724, 0.3791358396870425, 2714)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2724, -526.22728964, -0.0013, -5.2622729, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2724001, 724, 735, 0.22370603114218235, 2724)
    ops.element('Truss', 2724002, 725, 734, 0.22370603114218235, 2724)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2734, -405.97118896, -0.0013, -4.05971189, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2734001, 734, 745, 0.3791358396870425, 2734)
    ops.element('Truss', 2734002, 735, 744, 0.3791358396870425, 2734)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2744, -441.49884541, -0.0013, -4.41498845, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2744001, 744, 755, 0.34862964512164263, 2744)
    ops.element('Truss', 2744002, 745, 754, 0.34862964512164263, 2744)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2705, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2705001, 705, 716, 0.34863168649027615, 2705)
    ops.element('Truss', 2705002, 706, 715, 0.34863168649027615, 2705)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2715, -405.97031824, -0.0013, -4.05970318, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2715001, 715, 726, 0.37913804694907277, 2715)
    ops.element('Truss', 2715002, 716, 725, 0.37913804694907277, 2715)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2725, -526.2263516, -0.0013, -5.26226352, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2725001, 725, 736, 0.2237073579759088, 2725)
    ops.element('Truss', 2725002, 726, 735, 0.2237073579759088, 2725)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2735, -405.97031824, -0.0013, -4.05970318, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2735001, 735, 746, 0.37913804694907277, 2735)
    ops.element('Truss', 2735002, 736, 745, 0.37913804694907277, 2735)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2745, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2745001, 745, 756, 0.34863168649027615, 2745)
    ops.element('Truss', 2745002, 746, 755, 0.34863168649027615, 2745)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2706, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2706001, 706, 717, 0.34863168649027615, 2706)
    ops.element('Truss', 2706002, 707, 716, 0.34863168649027615, 2706)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2716, -405.97031824, -0.0013, -4.05970318, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2716001, 716, 727, 0.37913804694907277, 2716)
    ops.element('Truss', 2716002, 717, 726, 0.37913804694907277, 2716)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2726, -526.2263516, -0.0013, -5.26226352, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2726001, 726, 737, 0.2237073579759088, 2726)
    ops.element('Truss', 2726002, 727, 736, 0.2237073579759088, 2726)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2736, -405.97031824, -0.0013, -4.05970318, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2736001, 736, 747, 0.37913804694907277, 2736)
    ops.element('Truss', 2736002, 737, 746, 0.37913804694907277, 2736)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2746, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2746001, 746, 757, 0.34863168649027615, 2746)
    ops.element('Truss', 2746002, 747, 756, 0.34863168649027615, 2746)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2707, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2707001, 707, 718, 0.34863168649027615, 2707)
    ops.element('Truss', 2707002, 708, 717, 0.34863168649027615, 2707)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2717, -405.97031824, -0.0013, -4.05970318, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2717001, 717, 728, 0.37913804694907277, 2717)
    ops.element('Truss', 2717002, 718, 727, 0.37913804694907277, 2717)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2727, -526.2263516, -0.0013, -5.26226352, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2727001, 727, 738, 0.2237073579759088, 2727)
    ops.element('Truss', 2727002, 728, 737, 0.2237073579759088, 2727)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2737, -405.97031824, -0.0013, -4.05970318, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2737001, 737, 748, 0.37913804694907277, 2737)
    ops.element('Truss', 2737002, 738, 747, 0.37913804694907277, 2737)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2747, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2747001, 747, 758, 0.34863168649027615, 2747)
    ops.element('Truss', 2747002, 748, 757, 0.34863168649027615, 2747)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3000, -523.40578136, -0.0013, -5.23405781, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3000001, 70000, 101, 0.3049429593522586, 3000)
    ops.element('Truss', 3000002, 1, 70100, 0.3049429593522586, 3000)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3100, -493.58328202, -0.0013, -4.93583282, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3100001, 70100, 201, 0.2533827120147669, 3100)
    ops.element('Truss', 3100002, 101, 70200, 0.2533827120147669, 3100)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3200, -440.46139886, -0.0013, -4.40461399, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3200001, 70200, 301, 0.3623624719056952, 3200)
    ops.element('Truss', 3200002, 201, 70300, 0.3623624719056952, 3200)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3300, -493.58328202, -0.0013, -4.93583282, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3300001, 70300, 401, 0.2533827120147669, 3300)
    ops.element('Truss', 3300002, 301, 70400, 0.2533827120147669, 3300)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3400, -440.46139886, -0.0013, -4.40461399, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3400001, 70400, 501, 0.3623624719056952, 3400)
    ops.element('Truss', 3400002, 401, 70500, 0.3623624719056952, 3400)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3500, -493.58328202, -0.0013, -4.93583282, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3500001, 70500, 601, 0.2533827120147669, 3500)
    ops.element('Truss', 3500002, 501, 70600, 0.2533827120147669, 3500)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3600, -523.40578136, -0.0013, -5.23405781, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3600001, 70600, 701, 0.3049429593522586, 3600)
    ops.element('Truss', 3600002, 601, 70700, 0.3049429593522586, 3600)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3001, -441.49980718, -0.0013, -4.41499807, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3001001, 1, 102, 0.3486276037614604, 3001)
    ops.element('Truss', 3001002, 2, 101, 0.3486276037614604, 3001)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3101, -428.33755924, -0.0013, -4.28337559, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3101001, 101, 202, 0.27482519738905997, 3101)
    ops.element('Truss', 3101002, 102, 201, 0.27482519738905997, 3101)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3201, -373.57355559, -0.0013, -3.73573556, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3201001, 201, 302, 0.41201252142049144, 3201)
    ops.element('Truss', 3201002, 202, 301, 0.41201252142049144, 3201)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3301, -428.33755924, -0.0013, -4.28337559, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3301001, 301, 402, 0.27482519738905997, 3301)
    ops.element('Truss', 3301002, 302, 401, 0.27482519738905997, 3301)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3401, -373.57355559, -0.0013, -3.73573556, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3401001, 401, 502, 0.41201252142049144, 3401)
    ops.element('Truss', 3401002, 402, 501, 0.41201252142049144, 3401)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3501, -428.33755924, -0.0013, -4.28337559, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3501001, 501, 602, 0.27482519738905997, 3501)
    ops.element('Truss', 3501002, 502, 601, 0.27482519738905997, 3501)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3601, -441.49980718, -0.0013, -4.41499807, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3601001, 601, 702, 0.3486276037614604, 3601)
    ops.element('Truss', 3601002, 602, 701, 0.3486276037614604, 3601)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3002, -441.49980718, -0.0013, -4.41499807, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3002001, 2, 103, 0.3486276037614604, 3002)
    ops.element('Truss', 3002002, 3, 102, 0.3486276037614604, 3002)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3102, -428.33755924, -0.0013, -4.28337559, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3102001, 102, 203, 0.27482519738905997, 3102)
    ops.element('Truss', 3102002, 103, 202, 0.27482519738905997, 3102)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3202, -373.57355559, -0.0013, -3.73573556, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3202001, 202, 303, 0.41201252142049144, 3202)
    ops.element('Truss', 3202002, 203, 302, 0.41201252142049144, 3202)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3302, -428.33755924, -0.0013, -4.28337559, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3302001, 302, 403, 0.27482519738905997, 3302)
    ops.element('Truss', 3302002, 303, 402, 0.27482519738905997, 3302)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3402, -373.57355559, -0.0013, -3.73573556, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3402001, 402, 503, 0.41201252142049144, 3402)
    ops.element('Truss', 3402002, 403, 502, 0.41201252142049144, 3402)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3502, -428.33755924, -0.0013, -4.28337559, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3502001, 502, 603, 0.27482519738905997, 3502)
    ops.element('Truss', 3502002, 503, 602, 0.27482519738905997, 3502)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3602, -441.49980718, -0.0013, -4.41499807, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3602001, 602, 703, 0.3486276037614604, 3602)
    ops.element('Truss', 3602002, 603, 702, 0.3486276037614604, 3602)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3003, -441.49884541, -0.0013, -4.41498845, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3003001, 3, 104, 0.34862964512164263, 3003)
    ops.element('Truss', 3003002, 4, 103, 0.34862964512164263, 3003)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3103, -428.33682705, -0.0013, -4.28336827, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3103001, 103, 204, 0.2748268073365743, 3103)
    ops.element('Truss', 3103002, 104, 203, 0.2748268073365743, 3103)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3203, -373.57276583, -0.0013, -3.73572766, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3203001, 203, 304, 0.4120149074474273, 3203)
    ops.element('Truss', 3203002, 204, 303, 0.4120149074474273, 3203)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3303, -428.33682705, -0.0013, -4.28336827, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3303001, 303, 404, 0.2748268073365743, 3303)
    ops.element('Truss', 3303002, 304, 403, 0.2748268073365743, 3303)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3403, -373.57276583, -0.0013, -3.73572766, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3403001, 403, 504, 0.4120149074474273, 3403)
    ops.element('Truss', 3403002, 404, 503, 0.4120149074474273, 3403)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3503, -428.33682705, -0.0013, -4.28336827, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3503001, 503, 604, 0.2748268073365743, 3503)
    ops.element('Truss', 3503002, 504, 603, 0.2748268073365743, 3503)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3603, -441.49884541, -0.0013, -4.41498845, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3603001, 603, 704, 0.34862964512164263, 3603)
    ops.element('Truss', 3603002, 604, 703, 0.34862964512164263, 3603)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3004, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3004001, 4, 105, 0.34863168649027615, 3004)
    ops.element('Truss', 3004002, 5, 104, 0.34863168649027615, 3004)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3104, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3104001, 104, 205, 0.2748284172971905, 3104)
    ops.element('Truss', 3104002, 105, 204, 0.2748284172971905, 3104)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3204, -373.57197607, -0.0013, -3.73571976, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3204001, 204, 305, 0.41201729348411437, 3204)
    ops.element('Truss', 3204002, 205, 304, 0.41201729348411437, 3204)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3304, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3304001, 304, 405, 0.2748284172971905, 3304)
    ops.element('Truss', 3304002, 305, 404, 0.2748284172971905, 3304)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3404, -373.57197607, -0.0013, -3.73571976, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3404001, 404, 505, 0.41201729348411437, 3404)
    ops.element('Truss', 3404002, 405, 504, 0.41201729348411437, 3404)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3504, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3504001, 504, 605, 0.2748284172971905, 3504)
    ops.element('Truss', 3504002, 505, 604, 0.2748284172971905, 3504)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3604, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3604001, 604, 705, 0.34863168649027615, 3604)
    ops.element('Truss', 3604002, 605, 704, 0.34863168649027615, 3604)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3005, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3005001, 5, 106, 0.34863168649027615, 3005)
    ops.element('Truss', 3005002, 6, 105, 0.34863168649027615, 3005)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3105, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3105001, 105, 206, 0.2748284172971905, 3105)
    ops.element('Truss', 3105002, 106, 205, 0.2748284172971905, 3105)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3205, -373.57197607, -0.0013, -3.73571976, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3205001, 205, 306, 0.41201729348411437, 3205)
    ops.element('Truss', 3205002, 206, 305, 0.41201729348411437, 3205)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3305, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3305001, 305, 406, 0.2748284172971905, 3305)
    ops.element('Truss', 3305002, 306, 405, 0.2748284172971905, 3305)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3405, -373.57197607, -0.0013, -3.73571976, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3405001, 405, 506, 0.41201729348411437, 3405)
    ops.element('Truss', 3405002, 406, 505, 0.41201729348411437, 3405)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3505, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3505001, 505, 606, 0.2748284172971905, 3505)
    ops.element('Truss', 3505002, 506, 605, 0.2748284172971905, 3505)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3605, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3605001, 605, 706, 0.34863168649027615, 3605)
    ops.element('Truss', 3605002, 606, 705, 0.34863168649027615, 3605)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3006, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3006001, 6, 107, 0.34863168649027615, 3006)
    ops.element('Truss', 3006002, 7, 106, 0.34863168649027615, 3006)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3106, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3106001, 106, 207, 0.2748284172971905, 3106)
    ops.element('Truss', 3106002, 107, 206, 0.2748284172971905, 3106)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3206, -373.57197607, -0.0013, -3.73571976, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3206001, 206, 307, 0.41201729348411437, 3206)
    ops.element('Truss', 3206002, 207, 306, 0.41201729348411437, 3206)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3306, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3306001, 306, 407, 0.2748284172971905, 3306)
    ops.element('Truss', 3306002, 307, 406, 0.2748284172971905, 3306)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3406, -373.57197607, -0.0013, -3.73571976, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3406001, 406, 507, 0.41201729348411437, 3406)
    ops.element('Truss', 3406002, 407, 506, 0.41201729348411437, 3406)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3506, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3506001, 506, 607, 0.2748284172971905, 3506)
    ops.element('Truss', 3506002, 507, 606, 0.2748284172971905, 3506)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3606, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3606001, 606, 707, 0.34863168649027615, 3606)
    ops.element('Truss', 3606002, 607, 706, 0.34863168649027615, 3606)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3007, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3007001, 7, 108, 0.34863168649027615, 3007)
    ops.element('Truss', 3007002, 8, 107, 0.34863168649027615, 3007)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3107, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3107001, 107, 208, 0.2748284172971905, 3107)
    ops.element('Truss', 3107002, 108, 207, 0.2748284172971905, 3107)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3207, -373.57197607, -0.0013, -3.73571976, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3207001, 207, 308, 0.41201729348411437, 3207)
    ops.element('Truss', 3207002, 208, 307, 0.41201729348411437, 3207)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3307, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3307001, 307, 408, 0.2748284172971905, 3307)
    ops.element('Truss', 3307002, 308, 407, 0.2748284172971905, 3307)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3407, -373.57197607, -0.0013, -3.73571976, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3407001, 407, 508, 0.41201729348411437, 3407)
    ops.element('Truss', 3407002, 408, 507, 0.41201729348411437, 3407)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3507, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3507001, 507, 608, 0.2748284172971905, 3507)
    ops.element('Truss', 3507002, 508, 607, 0.2748284172971905, 3507)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3607, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3607001, 607, 708, 0.34863168649027615, 3607)
    ops.element('Truss', 3607002, 608, 707, 0.34863168649027615, 3607)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3050, -523.40578136, -0.0013, -5.23405781, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3050001, 70050, 151, 0.3049429593522586, 3050)
    ops.element('Truss', 3050002, 51, 70150, 0.3049429593522586, 3050)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3150, -493.58328202, -0.0013, -4.93583282, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3150001, 70150, 251, 0.2533827120147669, 3150)
    ops.element('Truss', 3150002, 151, 70250, 0.2533827120147669, 3150)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3250, -440.46139886, -0.0013, -4.40461399, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3250001, 70250, 351, 0.3623624719056952, 3250)
    ops.element('Truss', 3250002, 251, 70350, 0.3623624719056952, 3250)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3350, -493.58328202, -0.0013, -4.93583282, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3350001, 70350, 451, 0.2533827120147669, 3350)
    ops.element('Truss', 3350002, 351, 70450, 0.2533827120147669, 3350)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3450, -440.46139886, -0.0013, -4.40461399, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3450001, 70450, 551, 0.3623624719056952, 3450)
    ops.element('Truss', 3450002, 451, 70550, 0.3623624719056952, 3450)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3550, -493.58328202, -0.0013, -4.93583282, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3550001, 70550, 651, 0.2533827120147669, 3550)
    ops.element('Truss', 3550002, 551, 70650, 0.2533827120147669, 3550)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3650, -523.40578136, -0.0013, -5.23405781, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3650001, 70650, 751, 0.3049429593522586, 3650)
    ops.element('Truss', 3650002, 651, 70750, 0.3049429593522586, 3650)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3051, -441.49980718, -0.0013, -4.41499807, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3051001, 51, 152, 0.3486276037614604, 3051)
    ops.element('Truss', 3051002, 52, 151, 0.3486276037614604, 3051)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3151, -428.33755924, -0.0013, -4.28337559, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3151001, 151, 252, 0.27482519738905997, 3151)
    ops.element('Truss', 3151002, 152, 251, 0.27482519738905997, 3151)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3251, -373.57355559, -0.0013, -3.73573556, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3251001, 251, 352, 0.41201252142049144, 3251)
    ops.element('Truss', 3251002, 252, 351, 0.41201252142049144, 3251)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3351, -428.33755924, -0.0013, -4.28337559, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3351001, 351, 452, 0.27482519738905997, 3351)
    ops.element('Truss', 3351002, 352, 451, 0.27482519738905997, 3351)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3451, -373.57355559, -0.0013, -3.73573556, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3451001, 451, 552, 0.41201252142049144, 3451)
    ops.element('Truss', 3451002, 452, 551, 0.41201252142049144, 3451)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3551, -428.33755924, -0.0013, -4.28337559, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3551001, 551, 652, 0.27482519738905997, 3551)
    ops.element('Truss', 3551002, 552, 651, 0.27482519738905997, 3551)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3651, -441.49980718, -0.0013, -4.41499807, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3651001, 651, 752, 0.3486276037614604, 3651)
    ops.element('Truss', 3651002, 652, 751, 0.3486276037614604, 3651)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3052, -441.49980718, -0.0013, -4.41499807, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3052001, 52, 153, 0.3486276037614604, 3052)
    ops.element('Truss', 3052002, 53, 152, 0.3486276037614604, 3052)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3152, -428.33755924, -0.0013, -4.28337559, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3152001, 152, 253, 0.27482519738905997, 3152)
    ops.element('Truss', 3152002, 153, 252, 0.27482519738905997, 3152)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3252, -373.57355559, -0.0013, -3.73573556, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3252001, 252, 353, 0.41201252142049144, 3252)
    ops.element('Truss', 3252002, 253, 352, 0.41201252142049144, 3252)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3352, -428.33755924, -0.0013, -4.28337559, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3352001, 352, 453, 0.27482519738905997, 3352)
    ops.element('Truss', 3352002, 353, 452, 0.27482519738905997, 3352)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3452, -373.57355559, -0.0013, -3.73573556, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3452001, 452, 553, 0.41201252142049144, 3452)
    ops.element('Truss', 3452002, 453, 552, 0.41201252142049144, 3452)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3552, -428.33755924, -0.0013, -4.28337559, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3552001, 552, 653, 0.27482519738905997, 3552)
    ops.element('Truss', 3552002, 553, 652, 0.27482519738905997, 3552)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3652, -441.49980718, -0.0013, -4.41499807, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3652001, 652, 753, 0.3486276037614604, 3652)
    ops.element('Truss', 3652002, 653, 752, 0.3486276037614604, 3652)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3053, -441.49884541, -0.0013, -4.41498845, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3053001, 53, 154, 0.34862964512164263, 3053)
    ops.element('Truss', 3053002, 54, 153, 0.34862964512164263, 3053)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3153, -428.33682705, -0.0013, -4.28336827, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3153001, 153, 254, 0.2748268073365743, 3153)
    ops.element('Truss', 3153002, 154, 253, 0.2748268073365743, 3153)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3253, -373.57276583, -0.0013, -3.73572766, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3253001, 253, 354, 0.4120149074474273, 3253)
    ops.element('Truss', 3253002, 254, 353, 0.4120149074474273, 3253)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3353, -428.33682705, -0.0013, -4.28336827, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3353001, 353, 454, 0.2748268073365743, 3353)
    ops.element('Truss', 3353002, 354, 453, 0.2748268073365743, 3353)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3453, -373.57276583, -0.0013, -3.73572766, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3453001, 453, 554, 0.4120149074474273, 3453)
    ops.element('Truss', 3453002, 454, 553, 0.4120149074474273, 3453)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3553, -428.33682705, -0.0013, -4.28336827, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3553001, 553, 654, 0.2748268073365743, 3553)
    ops.element('Truss', 3553002, 554, 653, 0.2748268073365743, 3553)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3653, -441.49884541, -0.0013, -4.41498845, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3653001, 653, 754, 0.34862964512164263, 3653)
    ops.element('Truss', 3653002, 654, 753, 0.34862964512164263, 3653)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3054, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3054001, 54, 155, 0.34863168649027615, 3054)
    ops.element('Truss', 3054002, 55, 154, 0.34863168649027615, 3054)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3154, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3154001, 154, 255, 0.2748284172971905, 3154)
    ops.element('Truss', 3154002, 155, 254, 0.2748284172971905, 3154)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3254, -373.57197607, -0.0013, -3.73571976, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3254001, 254, 355, 0.41201729348411437, 3254)
    ops.element('Truss', 3254002, 255, 354, 0.41201729348411437, 3254)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3354, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3354001, 354, 455, 0.2748284172971905, 3354)
    ops.element('Truss', 3354002, 355, 454, 0.2748284172971905, 3354)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3454, -373.57197607, -0.0013, -3.73571976, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3454001, 454, 555, 0.41201729348411437, 3454)
    ops.element('Truss', 3454002, 455, 554, 0.41201729348411437, 3454)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3554, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3554001, 554, 655, 0.2748284172971905, 3554)
    ops.element('Truss', 3554002, 555, 654, 0.2748284172971905, 3554)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3654, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3654001, 654, 755, 0.34863168649027615, 3654)
    ops.element('Truss', 3654002, 655, 754, 0.34863168649027615, 3654)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3055, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3055001, 55, 156, 0.34863168649027615, 3055)
    ops.element('Truss', 3055002, 56, 155, 0.34863168649027615, 3055)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3155, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3155001, 155, 256, 0.2748284172971905, 3155)
    ops.element('Truss', 3155002, 156, 255, 0.2748284172971905, 3155)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3255, -373.57197607, -0.0013, -3.73571976, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3255001, 255, 356, 0.41201729348411437, 3255)
    ops.element('Truss', 3255002, 256, 355, 0.41201729348411437, 3255)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3355, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3355001, 355, 456, 0.2748284172971905, 3355)
    ops.element('Truss', 3355002, 356, 455, 0.2748284172971905, 3355)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3455, -373.57197607, -0.0013, -3.73571976, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3455001, 455, 556, 0.41201729348411437, 3455)
    ops.element('Truss', 3455002, 456, 555, 0.41201729348411437, 3455)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3555, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3555001, 555, 656, 0.2748284172971905, 3555)
    ops.element('Truss', 3555002, 556, 655, 0.2748284172971905, 3555)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3655, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3655001, 655, 756, 0.34863168649027615, 3655)
    ops.element('Truss', 3655002, 656, 755, 0.34863168649027615, 3655)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3056, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3056001, 56, 157, 0.34863168649027615, 3056)
    ops.element('Truss', 3056002, 57, 156, 0.34863168649027615, 3056)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3156, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3156001, 156, 257, 0.2748284172971905, 3156)
    ops.element('Truss', 3156002, 157, 256, 0.2748284172971905, 3156)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3256, -373.57197607, -0.0013, -3.73571976, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3256001, 256, 357, 0.41201729348411437, 3256)
    ops.element('Truss', 3256002, 257, 356, 0.41201729348411437, 3256)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3356, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3356001, 356, 457, 0.2748284172971905, 3356)
    ops.element('Truss', 3356002, 357, 456, 0.2748284172971905, 3356)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3456, -373.57197607, -0.0013, -3.73571976, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3456001, 456, 557, 0.41201729348411437, 3456)
    ops.element('Truss', 3456002, 457, 556, 0.41201729348411437, 3456)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3556, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3556001, 556, 657, 0.2748284172971905, 3556)
    ops.element('Truss', 3556002, 557, 656, 0.2748284172971905, 3556)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3656, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3656001, 656, 757, 0.34863168649027615, 3656)
    ops.element('Truss', 3656002, 657, 756, 0.34863168649027615, 3656)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3057, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3057001, 57, 158, 0.34863168649027615, 3057)
    ops.element('Truss', 3057002, 58, 157, 0.34863168649027615, 3057)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3157, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3157001, 157, 258, 0.2748284172971905, 3157)
    ops.element('Truss', 3157002, 158, 257, 0.2748284172971905, 3157)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3257, -373.57197607, -0.0013, -3.73571976, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3257001, 257, 358, 0.41201729348411437, 3257)
    ops.element('Truss', 3257002, 258, 357, 0.41201729348411437, 3257)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3357, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3357001, 357, 458, 0.2748284172971905, 3357)
    ops.element('Truss', 3357002, 358, 457, 0.2748284172971905, 3357)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3457, -373.57197607, -0.0013, -3.73571976, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3457001, 457, 558, 0.41201729348411437, 3457)
    ops.element('Truss', 3457002, 458, 557, 0.41201729348411437, 3457)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3557, -428.33609485, -0.0013, -4.28336095, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3557001, 557, 658, 0.2748284172971905, 3557)
    ops.element('Truss', 3557002, 558, 657, 0.2748284172971905, 3557)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3657, -441.49788363, -0.0013, -4.41497884, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3657001, 657, 758, 0.34863168649027615, 3657)
    ops.element('Truss', 3657002, 658, 757, 0.34863168649027615, 3657)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2120, -460.27376592, -0.0013, -4.60273766, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2120001, 70120, 131, 0.27171768777827104, 2120)
    ops.element('Truss', 2120002, 1121, 70130, 0.27171768777827104, 2120)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2221, -460.27376592, -0.0013, -4.60273766, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2221001, 70220, 231, 0.27171768777827104, 2221)
    ops.element('Truss', 2221002, 1221, 70230, 0.27171768777827104, 2221)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2520, -460.27376592, -0.0013, -4.60273766, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2520001, 70520, 531, 0.27171768777827104, 2520)
    ops.element('Truss', 2520002, 1521, 70530, 0.27171768777827104, 2520)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2621, -460.27376592, -0.0013, -4.60273766, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2621001, 70620, 631, 0.27171768777827104, 2621)
    ops.element('Truss', 2621002, 1621, 70630, 0.27171768777827104, 2621)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2121, -400.18213556, -0.0013, -4.00182136, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2121001, 121, 132, 0.29415750363784565, 2121)
    ops.element('Truss', 2121002, 1122, 131, 0.29415750363784565, 2121)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2222, -400.18213556, -0.0013, -4.00182136, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2222001, 221, 232, 0.29415750363784565, 2222)
    ops.element('Truss', 2222002, 1222, 231, 0.29415750363784565, 2222)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2521, -400.18213556, -0.0013, -4.00182136, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2521001, 521, 532, 0.29415750363784565, 2521)
    ops.element('Truss', 2521002, 1522, 531, 0.29415750363784565, 2521)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2622, -400.18213556, -0.0013, -4.00182136, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2622001, 621, 632, 0.29415750363784565, 2622)
    ops.element('Truss', 2622002, 1622, 631, 0.29415750363784565, 2622)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2122, -400.18213556, -0.0013, -4.00182136, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2122001, 122, 133, 0.29415750363784565, 2122)
    ops.element('Truss', 2122002, 1123, 132, 0.29415750363784565, 2122)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2223, -400.18213556, -0.0013, -4.00182136, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2223001, 222, 233, 0.29415750363784565, 2223)
    ops.element('Truss', 2223002, 1223, 232, 0.29415750363784565, 2223)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2522, -400.18213556, -0.0013, -4.00182136, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2522001, 522, 533, 0.29415750363784565, 2522)
    ops.element('Truss', 2522002, 1523, 532, 0.29415750363784565, 2522)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2623, -400.18213556, -0.0013, -4.00182136, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2623001, 622, 633, 0.29415750363784565, 2623)
    ops.element('Truss', 2623002, 1623, 632, 0.29415750363784565, 2623)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2123, -400.18145992, -0.0013, -4.0018146, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2123001, 123, 134, 0.2941592206657952, 2123)
    ops.element('Truss', 2123002, 1124, 133, 0.2941592206657952, 2123)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2224, -400.18145992, -0.0013, -4.0018146, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2224001, 223, 234, 0.2941592206657952, 2224)
    ops.element('Truss', 2224002, 1224, 233, 0.2941592206657952, 2224)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2523, -400.18145992, -0.0013, -4.0018146, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2523001, 523, 534, 0.2941592206657952, 2523)
    ops.element('Truss', 2523002, 1524, 533, 0.2941592206657952, 2523)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2624, -400.18145992, -0.0013, -4.0018146, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2624001, 623, 634, 0.2941592206657952, 2624)
    ops.element('Truss', 2624002, 1624, 633, 0.2941592206657952, 2624)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2124, -400.18145992, -0.0013, -4.0018146, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2124001, 124, 135, 0.2941592206657952, 2124)
    ops.element('Truss', 2124002, 1125, 134, 0.2941592206657952, 2124)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2225, -400.18145992, -0.0013, -4.0018146, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2225001, 224, 235, 0.2941592206657952, 2225)
    ops.element('Truss', 2225002, 1225, 234, 0.2941592206657952, 2225)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2524, -400.18145992, -0.0013, -4.0018146, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2524001, 524, 535, 0.2941592206657952, 2524)
    ops.element('Truss', 2524002, 1525, 534, 0.2941592206657952, 2524)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2625, -400.18145992, -0.0013, -4.0018146, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2625001, 624, 635, 0.2941592206657952, 2625)
    ops.element('Truss', 2625002, 1625, 634, 0.2941592206657952, 2625)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2125, -400.18078427, -0.0013, -4.00180784, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2125001, 125, 136, 0.29416093770764706, 2125)
    ops.element('Truss', 2125002, 1126, 135, 0.29416093770764706, 2125)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2226, -400.18078427, -0.0013, -4.00180784, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2226001, 225, 236, 0.29416093770764706, 2226)
    ops.element('Truss', 2226002, 1226, 235, 0.29416093770764706, 2226)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2525, -400.18078427, -0.0013, -4.00180784, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2525001, 525, 536, 0.29416093770764706, 2525)
    ops.element('Truss', 2525002, 1526, 535, 0.29416093770764706, 2525)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2626, -400.18078427, -0.0013, -4.00180784, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2626001, 625, 636, 0.29416093770764706, 2626)
    ops.element('Truss', 2626002, 1626, 635, 0.29416093770764706, 2626)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2126, -400.18010862, -0.0013, -4.00180109, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2126001, 126, 137, 0.29416265476340125, 2126)
    ops.element('Truss', 2126002, 1127, 136, 0.29416265476340125, 2126)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2227, -400.18010862, -0.0013, -4.00180109, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2227001, 226, 237, 0.29416265476340125, 2227)
    ops.element('Truss', 2227002, 1227, 236, 0.29416265476340125, 2227)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2526, -400.18010862, -0.0013, -4.00180109, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2526001, 526, 537, 0.29416265476340125, 2526)
    ops.element('Truss', 2526002, 1527, 536, 0.29416265476340125, 2526)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2627, -400.18010862, -0.0013, -4.00180109, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2627001, 626, 637, 0.29416265476340125, 2627)
    ops.element('Truss', 2627002, 1627, 636, 0.29416265476340125, 2627)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2127, -400.18010862, -0.0013, -4.00180109, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2127001, 127, 138, 0.29416265476340125, 2127)
    ops.element('Truss', 2127002, 1128, 137, 0.29416265476340125, 2127)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2228, -400.18010862, -0.0013, -4.00180109, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2228001, 227, 238, 0.29416265476340125, 2228)
    ops.element('Truss', 2228002, 1228, 237, 0.29416265476340125, 2228)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2527, -400.18010862, -0.0013, -4.00180109, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2527001, 527, 538, 0.29416265476340125, 2527)
    ops.element('Truss', 2527002, 1528, 537, 0.29416265476340125, 2527)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2628, -400.18010862, -0.0013, -4.00180109, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2628001, 627, 638, 0.29416265476340125, 2628)
    ops.element('Truss', 2628002, 1628, 637, 0.29416265476340125, 2628)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3658, -297.74480348, -0.0013, -2.97744803, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3658001, 70120, 1221, 0.32910098981199787, 3658)
    ops.element('Truss', 3658002, 1121, 70220, 0.32910098981199787, 3658)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3121, -297.74792245, -0.0013, -2.97747922, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3121001, 1121, 221, 0.3290916306949743, 3121)
    ops.element('Truss', 3121002, 121, 1221, 0.3290916306949743, 3121)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3659, -297.74480348, -0.0013, -2.97744803, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3659001, 70520, 1621, 0.32910098981199787, 3659)
    ops.element('Truss', 3659002, 1521, 70620, 0.32910098981199787, 3659)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3521, -297.74792245, -0.0013, -2.97747922, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3521001, 1521, 621, 0.3290916306949743, 3521)
    ops.element('Truss', 3521002, 521, 1621, 0.3290916306949743, 3521)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3660, -251.97589526, -0.0013, -2.51975895, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3660001, 121, 1222, 0.37972633723769944, 3660)
    ops.element('Truss', 3660002, 1122, 221, 0.37972633723769944, 3660)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3122, -251.97589526, -0.0013, -2.51975895, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3122001, 1122, 222, 0.37972633723769944, 3122)
    ops.element('Truss', 3122002, 122, 1222, 0.37972633723769944, 3122)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3661, -251.97589526, -0.0013, -2.51975895, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3661001, 521, 1622, 0.37972633723769944, 3661)
    ops.element('Truss', 3661002, 1522, 621, 0.37972633723769944, 3661)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3522, -251.97589526, -0.0013, -2.51975895, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3522001, 1522, 622, 0.37972633723769944, 3522)
    ops.element('Truss', 3522002, 522, 1622, 0.37972633723769944, 3522)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3662, -251.97497299, -0.0013, -2.51974973, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3662001, 122, 1223, 0.3797301116582525, 3662)
    ops.element('Truss', 3662002, 1123, 222, 0.3797301116582525, 3662)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3123, -251.97497299, -0.0013, -2.51974973, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3123001, 1123, 223, 0.3797301116582525, 3123)
    ops.element('Truss', 3123002, 123, 1223, 0.3797301116582525, 3123)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3663, -251.97497299, -0.0013, -2.51974973, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3663001, 522, 1623, 0.3797301116582525, 3663)
    ops.element('Truss', 3663002, 1523, 622, 0.3797301116582525, 3663)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3523, -251.97497299, -0.0013, -2.51974973, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3523001, 1523, 623, 0.3797301116582525, 3523)
    ops.element('Truss', 3523002, 523, 1623, 0.3797301116582525, 3523)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3664, -251.97405074, -0.0013, -2.51974051, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3664001, 123, 1224, 0.3797338860981343, 3664)
    ops.element('Truss', 3664002, 1124, 223, 0.3797338860981343, 3664)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3124, -251.97405074, -0.0013, -2.51974051, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3124001, 1124, 224, 0.3797338860981343, 3124)
    ops.element('Truss', 3124002, 124, 1224, 0.3797338860981343, 3124)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3665, -251.97405074, -0.0013, -2.51974051, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3665001, 523, 1624, 0.3797338860981343, 3665)
    ops.element('Truss', 3665002, 1524, 623, 0.3797338860981343, 3665)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3524, -251.97405074, -0.0013, -2.51974051, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3524001, 1524, 624, 0.3797338860981343, 3524)
    ops.element('Truss', 3524002, 524, 1624, 0.3797338860981343, 3524)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3666, -251.97220624, -0.0013, -2.51972206, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3666001, 124, 1225, 0.3797414350358834, 3666)
    ops.element('Truss', 3666002, 1125, 224, 0.3797414350358834, 3666)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3125, -251.971284, -0.0013, -2.51971284, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3125001, 1125, 225, 0.3797452095337505, 3125)
    ops.element('Truss', 3125002, 125, 1225, 0.3797452095337505, 3125)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3667, -251.97220624, -0.0013, -2.51972206, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3667001, 524, 1625, 0.3797414350358834, 3667)
    ops.element('Truss', 3667002, 1525, 624, 0.3797414350358834, 3667)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3525, -251.971284, -0.0013, -2.51971284, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3525001, 1525, 625, 0.3797452095337505, 3525)
    ops.element('Truss', 3525002, 525, 1625, 0.3797452095337505, 3525)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3668, -251.971284, -0.0013, -2.51971284, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3668001, 125, 1226, 0.3797452095337505, 3668)
    ops.element('Truss', 3668002, 1126, 225, 0.3797452095337505, 3668)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3126, -251.971284, -0.0013, -2.51971284, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3126001, 1126, 226, 0.3797452095337505, 3126)
    ops.element('Truss', 3126002, 126, 1226, 0.3797452095337505, 3126)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3669, -251.971284, -0.0013, -2.51971284, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3669001, 525, 1626, 0.3797452095337505, 3669)
    ops.element('Truss', 3669002, 1526, 625, 0.3797452095337505, 3669)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3526, -251.971284, -0.0013, -2.51971284, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3526001, 1526, 626, 0.3797452095337505, 3526)
    ops.element('Truss', 3526002, 526, 1626, 0.3797452095337505, 3526)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3670, -251.971284, -0.0013, -2.51971284, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3670001, 126, 1227, 0.3797452095337505, 3670)
    ops.element('Truss', 3670002, 1127, 226, 0.3797452095337505, 3670)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3127, -251.971284, -0.0013, -2.51971284, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3127001, 1127, 227, 0.3797452095337505, 3127)
    ops.element('Truss', 3127002, 127, 1227, 0.3797452095337505, 3127)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3671, -251.971284, -0.0013, -2.51971284, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3671001, 526, 1627, 0.3797452095337505, 3671)
    ops.element('Truss', 3671002, 1527, 626, 0.3797452095337505, 3671)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3527, -251.971284, -0.0013, -2.51971284, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3527001, 1527, 627, 0.3797452095337505, 3527)
    ops.element('Truss', 3527002, 527, 1627, 0.3797452095337505, 3527)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2128, -251.971284, -0.0013, -2.51971284, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2128001, 127, 1228, 0.3797452095337505, 2128)
    ops.element('Truss', 2128002, 1128, 227, 0.3797452095337505, 2128)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3128, -251.971284, -0.0013, -2.51971284, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3128001, 1128, 228, 0.3797452095337505, 3128)
    ops.element('Truss', 3128002, 128, 1228, 0.3797452095337505, 3128)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2528, -251.971284, -0.0013, -2.51971284, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2528001, 527, 1628, 0.3797452095337505, 2528)
    ops.element('Truss', 2528002, 1528, 627, 0.3797452095337505, 2528)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3528, -251.971284, -0.0013, -2.51971284, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3528001, 1528, 628, 0.3797452095337505, 3528)
    ops.element('Truss', 3528002, 528, 1628, 0.3797452095337505, 3528)
