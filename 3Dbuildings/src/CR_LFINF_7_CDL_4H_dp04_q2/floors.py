import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (retained nodes & diaphrams).
    """
    # Floor no. 1
    # Retained floor node
    ops.node(91000, 6.65, 7.7819678, 3.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 10001, 10101, 10201, 10301, 10011, 10111, 10211, 10311, 10021, 10121, 10221, 10321, 10031, 10131, 10231, 10331)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Retained floor node
    ops.node(92000, 6.65, 7.78354711, 6.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 10002, 10102, 10202, 10302, 10012, 10112, 10212, 10312, 10022, 10122, 10222, 10322, 10032, 10132, 10232, 10332)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Retained floor node
    ops.node(93000, 6.65, 7.7942964, 9.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 10003, 10103, 10203, 10303, 10013, 10113, 10213, 10313, 10023, 10123, 10223, 10323, 10033, 10133, 10233, 10333)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Retained floor node
    ops.node(94000, 6.65, 7.77186397, 12.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 10004, 10104, 10204, 10304, 10014, 10114, 10214, 10314, 10024, 10124, 10224, 10324, 10034, 10134, 10234, 10334)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
