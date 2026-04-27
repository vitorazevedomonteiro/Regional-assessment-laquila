import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (retained nodes & diaphrams).
    """
    # Floor no. 1
    # Retained floor node
    ops.node(91000, 6.65, 5.25667273, 3.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 1, 101, 201, 301, 11, 111, 211, 311, 21, 121, 221, 321)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Retained floor node
    ops.node(92000, 6.65, 5.24672224, 6.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 2, 102, 202, 302, 12, 112, 212, 312, 22, 122, 222, 322)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)
