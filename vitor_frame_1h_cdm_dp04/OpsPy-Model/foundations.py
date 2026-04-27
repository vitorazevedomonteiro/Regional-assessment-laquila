import openseespy.opensees as ops


def add_foundations() -> None:
    """Add foundation components to ops domain (nodes and constraints).
    """
    # Foundation or support under the column 3000
    ops.node(70000, 0.0, 0.0, 0.0, '-mass', 0.23891437308868502, 0.23891437308868502, 0.23891437308868502, 0.0, 0.0, 0.0)
    ops.fix(70000, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3010
    ops.node(70010, 0.0, 5.0, 0.0, '-mass', 0.23891437308868502, 0.23891437308868502, 0.23891437308868502, 0.0, 0.0, 0.0)
    ops.fix(70010, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3020
    ops.node(70020, 0.0, 10.0, 0.0, '-mass', 0.23891437308868502, 0.23891437308868502, 0.23891437308868502, 0.0, 0.0, 0.0)
    ops.fix(70020, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3100
    ops.node(70100, 5.0, 0.0, 0.0, '-mass', 0.23891437308868502, 0.23891437308868502, 0.23891437308868502, 0.0, 0.0, 0.0)
    ops.fix(70100, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3110
    ops.node(70110, 5.0, 5.0, 0.0, '-mass', 0.23891437308868502, 0.23891437308868502, 0.23891437308868502, 0.0, 0.0, 0.0)
    ops.fix(70110, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3120
    ops.node(70120, 5.0, 10.0, 0.0, '-mass', 0.23891437308868502, 0.23891437308868502, 0.23891437308868502, 0.0, 0.0, 0.0)
    ops.fix(70120, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3200
    ops.node(70200, 8.3, 0.0, 0.0, '-mass', 0.23891437308868502, 0.23891437308868502, 0.23891437308868502, 0.0, 0.0, 0.0)
    ops.fix(70200, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3210
    ops.node(70210, 8.3, 5.0, 0.0, '-mass', 0.23891437308868502, 0.23891437308868502, 0.23891437308868502, 0.0, 0.0, 0.0)
    ops.fix(70210, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3220
    ops.node(70220, 8.3, 10.0, 0.0, '-mass', 0.23891437308868502, 0.23891437308868502, 0.23891437308868502, 0.0, 0.0, 0.0)
    ops.fix(70220, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3300
    ops.node(70300, 13.3, 0.0, 0.0, '-mass', 0.23891437308868502, 0.23891437308868502, 0.23891437308868502, 0.0, 0.0, 0.0)
    ops.fix(70300, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3310
    ops.node(70310, 13.3, 5.0, 0.0, '-mass', 0.23891437308868502, 0.23891437308868502, 0.23891437308868502, 0.0, 0.0, 0.0)
    ops.fix(70310, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3320
    ops.node(70320, 13.3, 10.0, 0.0, '-mass', 0.23891437308868502, 0.23891437308868502, 0.23891437308868502, 0.0, 0.0, 0.0)
    ops.fix(70320, 1, 1, 1, 1, 1, 1)
