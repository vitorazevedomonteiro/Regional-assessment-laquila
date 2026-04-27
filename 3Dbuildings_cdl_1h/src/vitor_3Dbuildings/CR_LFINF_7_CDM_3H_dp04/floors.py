import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (retained nodes & diaphrams).
    """
    # Floor no. 1
    # Retained floor node
    ops.node(91000, 6.65, 7.7790473, 3.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 1, 101, 201, 301, 11, 111, 211, 311, 21, 121, 221, 321, 31, 131, 231, 331)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Retained floor node
    ops.node(92000, 6.65, 7.78014494, 6.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 2, 102, 202, 302, 12, 112, 212, 312, 22, 122, 222, 322, 32, 132, 232, 332)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Retained floor node
    ops.node(93000, 6.65, 7.7596987, 9.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 3, 103, 203, 303, 13, 113, 213, 313, 23, 123, 223, 323, 33, 133, 233, 333)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)
