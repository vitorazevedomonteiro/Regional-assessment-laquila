import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (retained nodes & diaphrams).
    """
    # Floor no. 1
    # Retained floor node
    ops.node(91000, 6.65, 5.0, 3.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 10001, 10101, 10201, 10301, 10011, 10111, 10211, 10311, 10021, 10121, 10221, 10321)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)
