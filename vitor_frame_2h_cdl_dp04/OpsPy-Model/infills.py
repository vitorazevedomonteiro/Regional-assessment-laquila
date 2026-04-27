import openseespy.opensees as ops


def add_infills() -> None:
    """Add components of all infills to ops domain
    """
    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2000, -1157.25129027, -0.0013, -11.5725129, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2000001, 70000, 11, 0.13300886377971516, 2000)
    ops.element('Truss', 2000002, 1, 70010, 0.13300886377971516, 2000)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2010, -1157.25129027, -0.0013, -11.5725129, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2010001, 70010, 21, 0.13300886377971516, 2010)
    ops.element('Truss', 2010002, 11, 70020, 0.13300886377971516, 2010)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2001, -1157.25129027, -0.0013, -11.5725129, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2001001, 1, 12, 0.13300886377971516, 2001)
    ops.element('Truss', 2001002, 2, 11, 0.13300886377971516, 2001)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2011, -1157.25129027, -0.0013, -11.5725129, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2011001, 11, 22, 0.13300886377971516, 2011)
    ops.element('Truss', 2011002, 12, 21, 0.13300886377971516, 2011)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2300, -1157.25129027, -0.0013, -11.5725129, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2300001, 70300, 311, 0.13300886377971516, 2300)
    ops.element('Truss', 2300002, 301, 70310, 0.13300886377971516, 2300)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2310, -1157.25129027, -0.0013, -11.5725129, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2310001, 70310, 321, 0.13300886377971516, 2310)
    ops.element('Truss', 2310002, 311, 70320, 0.13300886377971516, 2310)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2301, -1157.25129027, -0.0013, -11.5725129, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2301001, 301, 312, 0.13300886377971516, 2301)
    ops.element('Truss', 2301002, 302, 311, 0.13300886377971516, 2301)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2311, -1157.25129027, -0.0013, -11.5725129, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2311001, 311, 322, 0.13300886377971516, 2311)
    ops.element('Truss', 2311002, 312, 321, 0.13300886377971516, 2311)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3000, -1157.24467666, -0.0013, -11.57244677, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3000001, 70000, 101, 0.13301060201382886, 3000)
    ops.element('Truss', 3000002, 1, 70100, 0.13301060201382886, 3000)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3200, -1157.24467666, -0.0013, -11.57244677, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3200001, 70200, 301, 0.13301060201382886, 3200)
    ops.element('Truss', 3200002, 1201, 70300, 0.13301060201382886, 3200)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3001, -1157.24467666, -0.0013, -11.57244677, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3001001, 1, 102, 0.13301060201382886, 3001)
    ops.element('Truss', 3001002, 2, 101, 0.13301060201382886, 3001)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3201, -1157.24467666, -0.0013, -11.57244677, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3201001, 201, 302, 0.13301060201382886, 3201)
    ops.element('Truss', 3201002, 1202, 301, 0.13301060201382886, 3201)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3020, -977.23749873, -0.0013, -9.77237499, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3020001, 70020, 121, 0.15751081160675584, 3020)
    ops.element('Truss', 3020002, 21, 70120, 0.15751081160675584, 3020)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3120, -1035.58794272, -0.0013, -10.35587943, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3120001, 70120, 221, 0.11368141227562119, 3120)
    ops.element('Truss', 3120002, 121, 70220, 0.11368141227562119, 3120)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3220, -977.23749873, -0.0013, -9.77237499, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3220001, 70220, 321, 0.15751081160675584, 3220)
    ops.element('Truss', 3220002, 221, 70320, 0.15751081160675584, 3220)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3021, -977.23749873, -0.0013, -9.77237499, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3021001, 21, 122, 0.15751081160675584, 3021)
    ops.element('Truss', 3021002, 22, 121, 0.15751081160675584, 3021)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3121, -1035.58794272, -0.0013, -10.35587943, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3121001, 121, 222, 0.11368141227562119, 3121)
    ops.element('Truss', 3121002, 122, 221, 0.11368141227562119, 3121)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3221, -977.23749873, -0.0013, -9.77237499, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3221001, 221, 322, 0.15751081160675584, 3221)
    ops.element('Truss', 3221002, 222, 321, 0.15751081160675584, 3221)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2101, -477.94204056, -0.0013, -4.77942041, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2101001, 70100, 1201, 0.20020540803967407, 2101)
    ops.element('Truss', 2101002, 1101, 70200, 0.20020540803967407, 2101)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3222, -477.94204056, -0.0013, -4.77942041, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3222001, 1101, 201, 0.20020540803967407, 3222)
    ops.element('Truss', 3222002, 101, 1201, 0.20020540803967407, 3222)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2102, -477.94010363, -0.0013, -4.77940104, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2102001, 101, 1202, 0.2002074765678747, 2102)
    ops.element('Truss', 2102002, 1102, 201, 0.2002074765678747, 2102)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3102, -477.94010363, -0.0013, -4.77940104, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3102001, 1102, 202, 0.2002074765678747, 3102)
    ops.element('Truss', 3102002, 102, 1202, 0.2002074765678747, 3102)
