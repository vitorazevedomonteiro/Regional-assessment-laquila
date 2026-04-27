import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (retained nodes & diaphrams).
    """
    # Floor no. 1
    # Retained floor node
    ops.node(91000, 6.65, 7.7775052, 3.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 10001, 10101, 10201, 10301, 10011, 10111, 10211, 10311, 10021, 10121, 10221, 10321, 10031, 10131, 10231, 10331)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Retained floor node
    ops.node(92000, 6.65, 7.78520387, 6.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 10002, 10102, 10202, 10302, 10012, 10112, 10212, 10312, 10022, 10122, 10222, 10322, 10032, 10132, 10232, 10332)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Retained floor node
    ops.node(93000, 6.65, 7.76565163, 9.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 10003, 10103, 10203, 10303, 10013, 10113, 10213, 10313, 10023, 10123, 10223, 10323, 10033, 10133, 10233, 10333)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)
