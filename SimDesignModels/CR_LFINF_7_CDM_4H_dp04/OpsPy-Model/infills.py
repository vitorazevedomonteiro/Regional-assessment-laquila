import openseespy.opensees as ops


def add_infills() -> None:
    """Add components of all infills to ops domain
    """
    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2000, -972.73918781, -0.0013, -9.72739188, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2000001, 70000, 11, 0.1582368734571962, 2000)
    ops.element('Truss', 2000002, 1, 70010, 0.1582368734571962, 2000)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2010, -869.61999708, -0.0013, -8.69619997, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2010001, 70010, 21, 0.17700014801847805, 2010)
    ops.element('Truss', 2010002, 11, 70020, 0.17700014801847805, 2010)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2020, -972.73918781, -0.0013, -9.72739188, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2020001, 70020, 31, 0.1582368734571962, 2020)
    ops.element('Truss', 2020002, 21, 70030, 0.1582368734571962, 2020)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2001, -972.73918781, -0.0013, -9.72739188, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2001001, 1, 12, 0.1582368734571962, 2001)
    ops.element('Truss', 2001002, 2, 11, 0.1582368734571962, 2001)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2011, -869.61999708, -0.0013, -8.69619997, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2011001, 11, 22, 0.17700014801847805, 2011)
    ops.element('Truss', 2011002, 12, 21, 0.17700014801847805, 2011)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2021, -972.73918781, -0.0013, -9.72739188, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2021001, 21, 32, 0.1582368734571962, 2021)
    ops.element('Truss', 2021002, 22, 31, 0.1582368734571962, 2021)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2002, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2002001, 2, 13, 0.13366283492317738, 2002)
    ops.element('Truss', 2002002, 3, 12, 0.13366283492317738, 2002)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2012, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2012001, 12, 23, 0.13366283492317738, 2012)
    ops.element('Truss', 2012002, 13, 22, 0.13366283492317738, 2012)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2022, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2022001, 22, 33, 0.13366283492317738, 2022)
    ops.element('Truss', 2022002, 23, 32, 0.13366283492317738, 2022)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2003, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2003001, 3, 14, 0.13366283492317738, 2003)
    ops.element('Truss', 2003002, 4, 13, 0.13366283492317738, 2003)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2013, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2013001, 13, 24, 0.13366283492317738, 2013)
    ops.element('Truss', 2013002, 14, 23, 0.13366283492317738, 2013)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2023, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2023001, 23, 34, 0.13366283492317738, 2023)
    ops.element('Truss', 2023002, 24, 33, 0.13366283492317738, 2023)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2300, -972.73918781, -0.0013, -9.72739188, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2300001, 70300, 311, 0.1582368734571962, 2300)
    ops.element('Truss', 2300002, 301, 70310, 0.1582368734571962, 2300)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2310, -869.61999708, -0.0013, -8.69619997, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2310001, 70310, 321, 0.17700014801847805, 2310)
    ops.element('Truss', 2310002, 311, 70320, 0.17700014801847805, 2310)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2320, -972.73918781, -0.0013, -9.72739188, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2320001, 70320, 331, 0.1582368734571962, 2320)
    ops.element('Truss', 2320002, 321, 70330, 0.1582368734571962, 2320)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2301, -972.73918781, -0.0013, -9.72739188, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2301001, 301, 312, 0.1582368734571962, 2301)
    ops.element('Truss', 2301002, 302, 311, 0.1582368734571962, 2301)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2311, -869.61999708, -0.0013, -8.69619997, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2311001, 311, 322, 0.17700014801847805, 2311)
    ops.element('Truss', 2311002, 312, 321, 0.17700014801847805, 2311)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2321, -972.73918781, -0.0013, -9.72739188, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2321001, 321, 332, 0.1582368734571962, 2321)
    ops.element('Truss', 2321002, 322, 331, 0.1582368734571962, 2321)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2302, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2302001, 302, 313, 0.13366283492317738, 2302)
    ops.element('Truss', 2302002, 303, 312, 0.13366283492317738, 2302)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2312, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2312001, 312, 323, 0.13366283492317738, 2312)
    ops.element('Truss', 2312002, 313, 322, 0.13366283492317738, 2312)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2322, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2322001, 322, 333, 0.13366283492317738, 2322)
    ops.element('Truss', 2322002, 323, 332, 0.13366283492317738, 2322)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2303, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2303001, 303, 314, 0.13366283492317738, 2303)
    ops.element('Truss', 2303002, 304, 313, 0.13366283492317738, 2303)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2313, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2313001, 313, 324, 0.13366283492317738, 2313)
    ops.element('Truss', 2313002, 314, 323, 0.13366283492317738, 2313)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2323, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2323001, 323, 334, 0.13366283492317738, 2323)
    ops.element('Truss', 2323002, 324, 333, 0.13366283492317738, 2323)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3000, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3000001, 70000, 101, 0.1336628349231774, 3000)
    ops.element('Truss', 3000002, 1, 70100, 0.1336628349231774, 3000)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3200, -933.02460157, -0.0013, -9.33024602, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3200001, 70200, 301, 0.16497217149653415, 3200)
    ops.element('Truss', 3200002, 1201, 70300, 0.16497217149653415, 3200)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3001, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3001001, 1, 102, 0.1336628349231774, 3001)
    ops.element('Truss', 3001002, 2, 101, 0.1336628349231774, 3001)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3201, -933.02460157, -0.0013, -9.33024602, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3201001, 201, 302, 0.16497217149653415, 3201)
    ops.element('Truss', 3201002, 1202, 301, 0.16497217149653415, 3201)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3002, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3002001, 2, 103, 0.1336628349231774, 3002)
    ops.element('Truss', 3002002, 3, 102, 0.1336628349231774, 3002)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3202, -933.02460157, -0.0013, -9.33024602, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3202001, 202, 303, 0.16497217149653415, 3202)
    ops.element('Truss', 3202002, 1203, 302, 0.16497217149653415, 3202)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3003, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3003001, 3, 104, 0.1336628349231774, 3003)
    ops.element('Truss', 3003002, 4, 103, 0.1336628349231774, 3003)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3203, -933.02460157, -0.0013, -9.33024602, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3203001, 203, 304, 0.16497217149653415, 3203)
    ops.element('Truss', 3203002, 1204, 303, 0.16497217149653415, 3203)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3030, -972.73918781, -0.0013, -9.72739188, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3030001, 70030, 131, 0.1582368734571962, 3030)
    ops.element('Truss', 3030002, 31, 70130, 0.1582368734571962, 3030)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3130, -1030.72087464, -0.0013, -10.30720875, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3130001, 70130, 231, 0.11421632115760819, 3130)
    ops.element('Truss', 3130002, 131, 70230, 0.11421632115760819, 3130)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3230, -972.73918781, -0.0013, -9.72739188, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3230001, 70230, 331, 0.1582368734571962, 3230)
    ops.element('Truss', 3230002, 231, 70330, 0.1582368734571962, 3230)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3031, -972.73918781, -0.0013, -9.72739188, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3031001, 31, 132, 0.1582368734571962, 3031)
    ops.element('Truss', 3031002, 32, 131, 0.1582368734571962, 3031)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3131, -1030.72087464, -0.0013, -10.30720875, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3131001, 131, 232, 0.11421632115760819, 3131)
    ops.element('Truss', 3131002, 132, 231, 0.11421632115760819, 3131)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3231, -972.73918781, -0.0013, -9.72739188, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3231001, 231, 332, 0.1582368734571962, 3231)
    ops.element('Truss', 3231002, 232, 331, 0.1582368734571962, 3231)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3032, -972.73918781, -0.0013, -9.72739188, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3032001, 32, 133, 0.1582368734571962, 3032)
    ops.element('Truss', 3032002, 33, 132, 0.1582368734571962, 3032)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3132, -1030.72087464, -0.0013, -10.30720875, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3132001, 132, 233, 0.11421632115760819, 3132)
    ops.element('Truss', 3132002, 133, 232, 0.11421632115760819, 3132)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3232, -972.73918781, -0.0013, -9.72739188, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3232001, 232, 333, 0.1582368734571962, 3232)
    ops.element('Truss', 3232002, 233, 332, 0.1582368734571962, 3232)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3033, -972.73918781, -0.0013, -9.72739188, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3033001, 33, 134, 0.1582368734571962, 3033)
    ops.element('Truss', 3033002, 34, 133, 0.1582368734571962, 3033)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3133, -1030.72087464, -0.0013, -10.30720875, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3133001, 133, 234, 0.11421632115760819, 3133)
    ops.element('Truss', 3133002, 134, 233, 0.11421632115760819, 3133)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3233, -972.73918781, -0.0013, -9.72739188, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3233001, 233, 334, 0.1582368734571962, 3233)
    ops.element('Truss', 3233002, 234, 333, 0.1582368734571962, 3233)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2101, -416.72539182, -0.0013, -4.16725392, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2101001, 70100, 1201, 0.22961477758359702, 2101)
    ops.element('Truss', 2101002, 1101, 70200, 0.22961477758359702, 2101)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3234, -416.7286809, -0.0013, -4.16728681, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3234001, 1101, 201, 0.22961008167550095, 3234)
    ops.element('Truss', 3234002, 101, 1201, 0.22961008167550095, 3234)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2102, -416.73032546, -0.0013, -4.16730325, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2102001, 101, 1202, 0.22960773374013513, 2102)
    ops.element('Truss', 2102002, 1102, 201, 0.22960773374013513, 2102)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3235, -416.73032546, -0.0013, -4.16730325, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3235001, 1102, 202, 0.22960773374013513, 3235)
    ops.element('Truss', 3235002, 102, 1202, 0.22960773374013513, 3235)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2103, -416.73032546, -0.0013, -4.16730325, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2103001, 102, 1203, 0.22960773374013513, 2103)
    ops.element('Truss', 2103002, 1103, 202, 0.22960773374013513, 2103)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3236, -416.73032546, -0.0013, -4.16730325, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3236001, 1103, 203, 0.22960773374013513, 3236)
    ops.element('Truss', 3236002, 103, 1203, 0.22960773374013513, 3236)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2104, -416.72703635, -0.0013, -4.16727036, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2104001, 103, 1204, 0.22961242962332157, 2104)
    ops.element('Truss', 2104002, 1104, 203, 0.22961242962332157, 2104)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3104, -416.72703635, -0.0013, -4.16727036, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3104001, 1104, 204, 0.22961242962332157, 3104)
    ops.element('Truss', 3104002, 104, 1204, 0.22961242962332157, 3104)
