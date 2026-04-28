import openseespy.opensees as ops


def add_joints() -> None:
    """Add components of joints to ops domain.
    """
    # -------------------------------------------------
    # Add stairs joints to ops domain
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (1, 0, 0.5)
    ops.node(1101, 5.0, 0.0, 1.5, '-mass', 3.541756880733946, 3.541756880733946, 3.541756880733946, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (2, 0, 0.5)
    ops.node(1201, 8.3, 0.0, 1.5, '-mass', 3.541756880733946, 3.541756880733946, 3.541756880733946, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (1, 0, 1.5)
    ops.node(1102, 5.0, 0.0, 4.5, '-mass', 3.4891957186544356, 3.4891957186544356, 3.4891957186544356, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (2, 0, 1.5)
    ops.node(1202, 8.3, 0.0, 4.5, '-mass', 3.4891957186544356, 3.4891957186544356, 3.4891957186544356, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (1, 0, 2.5)
    ops.node(1103, 5.0, 0.0, 7.5, '-mass', 3.4891957186544356, 3.4891957186544356, 3.4891957186544356, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (2, 0, 2.5)
    ops.node(1203, 8.3, 0.0, 7.5, '-mass', 3.4891957186544356, 3.4891957186544356, 3.4891957186544356, 0.0, 0.0, 0.0)

    # -------------------------------------------------
    # Add floor joints to ops domain
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 1)
    ops.node(1, 0, 0, 3.0, '-mass', 9.297935779816513, 9.297935779816513, 9.297935779816513, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 0, 1)
    ops.node(101, 5, 0, 3.0, '-mass', 9.330187054026505, 9.330187054026505, 9.330187054026505, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 0, 1)
    ops.node(201, 8.3, 0, 3.0, '-mass', 9.330187054026505, 9.330187054026505, 9.330187054026505, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 0, 1)
    ops.node(301, 13.3, 0, 3.0, '-mass', 9.297935779816513, 9.297935779816513, 9.297935779816513, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 1, 1)
    ops.node(11, 0, 5, 3.0, '-mass', 16.560932721712536, 16.560932721712536, 16.560932721712536, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 1, 1)
    ops.node(111, 5, 5, 3.0, '-mass', 23.116252548419975, 23.116252548419975, 23.116252548419975, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 1, 1)
    ops.node(211, 8.3, 5, 3.0, '-mass', 23.116252548419975, 23.116252548419975, 23.116252548419975, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 1, 1)
    ops.node(311, 13.3, 5, 3.0, '-mass', 16.560932721712536, 16.560932721712536, 16.560932721712536, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 2, 1)
    ops.node(21, 0, 10, 3.0, '-mass', 16.560932721712536, 16.560932721712536, 16.560932721712536, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 2, 1)
    ops.node(121, 5, 10, 3.0, '-mass', 24.325331294597348, 24.325331294597348, 24.325331294597348, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 2, 1)
    ops.node(221, 8.3, 10, 3.0, '-mass', 24.325331294597348, 24.325331294597348, 24.325331294597348, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 2, 1)
    ops.node(321, 13.3, 10, 3.0, '-mass', 16.560932721712536, 16.560932721712536, 16.560932721712536, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 3, 1)
    ops.node(31, 0, 15, 3.0, '-mass', 9.297935779816513, 9.297935779816513, 9.297935779816513, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 3, 1)
    ops.node(131, 5, 15, 3.0, '-mass', 13.46462359836901, 13.46462359836901, 13.46462359836901, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 3, 1)
    ops.node(231, 8.3, 15, 3.0, '-mass', 13.46462359836901, 13.46462359836901, 13.46462359836901, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 3, 1)
    ops.node(331, 13.3, 15, 3.0, '-mass', 9.297935779816513, 9.297935779816513, 9.297935779816513, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 0, 2)
    ops.node(2, 0, 0, 6.0, '-mass', 9.297935779816513, 9.297935779816513, 9.297935779816513, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 0, 2)
    ops.node(102, 5, 0, 6.0, '-mass', 9.250548929663609, 9.250548929663609, 9.250548929663609, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 0, 2)
    ops.node(202, 8.3, 0, 6.0, '-mass', 9.250548929663609, 9.250548929663609, 9.250548929663609, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 0, 2)
    ops.node(302, 13.3, 0, 6.0, '-mass', 9.297935779816513, 9.297935779816513, 9.297935779816513, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 1, 2)
    ops.node(12, 0, 5, 6.0, '-mass', 16.560932721712536, 16.560932721712536, 16.560932721712536, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 1, 2)
    ops.node(112, 5, 5, 6.0, '-mass', 22.956976299694187, 22.956976299694187, 22.956976299694187, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 1, 2)
    ops.node(212, 8.3, 5, 6.0, '-mass', 22.956976299694187, 22.956976299694187, 22.956976299694187, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 1, 2)
    ops.node(312, 13.3, 5, 6.0, '-mass', 16.560932721712536, 16.560932721712536, 16.560932721712536, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 2, 2)
    ops.node(22, 0, 10, 6.0, '-mass', 16.560932721712536, 16.560932721712536, 16.560932721712536, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 2, 2)
    ops.node(122, 5, 10, 6.0, '-mass', 24.16605504587156, 24.16605504587156, 24.16605504587156, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 2, 2)
    ops.node(222, 8.3, 10, 6.0, '-mass', 24.16605504587156, 24.16605504587156, 24.16605504587156, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 2, 2)
    ops.node(322, 13.3, 10, 6.0, '-mass', 16.560932721712536, 16.560932721712536, 16.560932721712536, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 3, 2)
    ops.node(32, 0, 15, 6.0, '-mass', 9.297935779816513, 9.297935779816513, 9.297935779816513, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 3, 2)
    ops.node(132, 5, 15, 6.0, '-mass', 13.384985474006115, 13.384985474006115, 13.384985474006115, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 3, 2)
    ops.node(232, 8.3, 15, 6.0, '-mass', 13.384985474006115, 13.384985474006115, 13.384985474006115, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 3, 2)
    ops.node(332, 13.3, 15, 6.0, '-mass', 9.297935779816513, 9.297935779816513, 9.297935779816513, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 0, 3)
    ops.node(3, 0, 0, 9.0, '-mass', 7.645259938837919, 7.645259938837919, 7.645259938837919, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 0, 3)
    ops.node(103, 5, 0, 9.0, '-mass', 7.998853211009173, 7.998853211009173, 7.998853211009173, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 0, 3)
    ops.node(203, 8.3, 0, 9.0, '-mass', 7.998853211009173, 7.998853211009173, 7.998853211009173, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 0, 3)
    ops.node(303, 13.3, 0, 9.0, '-mass', 7.645259938837919, 7.645259938837919, 7.645259938837919, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 1, 3)
    ops.node(13, 0, 5, 9.0, '-mass', 14.334862385321099, 14.334862385321099, 14.334862385321099, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 1, 3)
    ops.node(113, 5, 5, 9.0, '-mass', 21.044820336391435, 21.044820336391435, 21.044820336391435, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 1, 3)
    ops.node(213, 8.3, 5, 9.0, '-mass', 21.044820336391435, 21.044820336391435, 21.044820336391435, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 1, 3)
    ops.node(313, 13.3, 5, 9.0, '-mass', 14.334862385321099, 14.334862385321099, 14.334862385321099, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 2, 3)
    ops.node(23, 0, 10, 9.0, '-mass', 14.334862385321099, 14.334862385321099, 14.334862385321099, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 2, 3)
    ops.node(123, 5, 10, 9.0, '-mass', 21.708333333333332, 21.708333333333332, 21.708333333333332, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 2, 3)
    ops.node(223, 8.3, 10, 9.0, '-mass', 21.708333333333332, 21.708333333333332, 21.708333333333332, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 2, 3)
    ops.node(323, 13.3, 10, 9.0, '-mass', 14.334862385321099, 14.334862385321099, 14.334862385321099, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 3, 3)
    ops.node(33, 0, 15, 9.0, '-mass', 7.645259938837919, 7.645259938837919, 7.645259938837919, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 3, 3)
    ops.node(133, 5, 15, 9.0, '-mass', 11.453841743119265, 11.453841743119265, 11.453841743119265, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 3, 3)
    ops.node(233, 8.3, 15, 9.0, '-mass', 11.453841743119265, 11.453841743119265, 11.453841743119265, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 3, 3)
    ops.node(333, 13.3, 15, 9.0, '-mass', 7.645259938837919, 7.645259938837919, 7.645259938837919, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid
