import openseespy.opensees as ops


def add_infills() -> None:
    """Add components of all infills to ops domain
    """
    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2000, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2000001, 70000, 11, 0.13366283492317738, 2000)
    ops.element('Truss', 2000002, 1, 70010, 0.13366283492317738, 2000)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2010, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2010001, 70010, 21, 0.13366283492317738, 2010)
    ops.element('Truss', 2010002, 11, 70020, 0.13366283492317738, 2010)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2300, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2300001, 70300, 311, 0.13366283492317738, 2300)
    ops.element('Truss', 2300002, 301, 70310, 0.13366283492317738, 2300)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 2310, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 2310001, 70310, 321, 0.13366283492317738, 2310)
    ops.element('Truss', 2310002, 311, 70320, 0.13366283492317738, 2310)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3000, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3000001, 70000, 101, 0.13366283492317738, 3000)
    ops.element('Truss', 3000002, 1, 70100, 0.13366283492317738, 3000)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3100, -1391.59854268, -0.0013, -13.91598543, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3100001, 70100, 201, 0.08459769881955345, 3100)
    ops.element('Truss', 3100002, 101, 70200, 0.08459769881955345, 3100)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3200, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3200001, 70200, 301, 0.13366283492317738, 3200)
    ops.element('Truss', 3200002, 201, 70300, 0.13366283492317738, 3200)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3020, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3020001, 70020, 121, 0.13366283492317738, 3020)
    ops.element('Truss', 3020002, 21, 70120, 0.13366283492317738, 3020)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3120, -1391.59854268, -0.0013, -13.91598543, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3120001, 70120, 221, 0.08459769881955345, 3120)
    ops.element('Truss', 3120002, 121, 70220, 0.08459769881955345, 3120)

    # Create the material for diagonal struts
    ops.uniaxialMaterial('Concrete01', 3220, -1151.58074737, -0.0013, -11.51580747, -0.0045)
    # Create the elements for diagonal struts
    ops.element('Truss', 3220001, 70220, 321, 0.13366283492317738, 3220)
    ops.element('Truss', 3220002, 221, 70320, 0.13366283492317738, 3220)
