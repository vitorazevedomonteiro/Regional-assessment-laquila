import openseespy.opensees as ops


def add_joints() -> None:
    """Add components of joints to ops domain.
    """
    # -------------------------------------------------
    # Add stairs joints to ops domain
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (1, 0, 0.5)
    ops.node(1101, 5.0, 0.0, 1.5, '-mass', 3.4846850152905207, 3.4846850152905207, 3.4846850152905207, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (2, 0, 0.5)
    ops.node(1201, 8.3, 0.0, 1.5, '-mass', 3.4846850152905207, 3.4846850152905207, 3.4846850152905207, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (1, 0, 1.5)
    ops.node(1102, 5.0, 0.0, 4.5, '-mass', 3.4846850152905207, 3.4846850152905207, 3.4846850152905207, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (2, 0, 1.5)
    ops.node(1202, 8.3, 0.0, 4.5, '-mass', 3.4846850152905207, 3.4846850152905207, 3.4846850152905207, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (1, 0, 2.5)
    ops.node(1103, 5.0, 0.0, 7.5, '-mass', 3.4846850152905207, 3.4846850152905207, 3.4846850152905207, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (2, 0, 2.5)
    ops.node(1203, 8.3, 0.0, 7.5, '-mass', 3.4846850152905207, 3.4846850152905207, 3.4846850152905207, 0.0, 0.0, 0.0)

    # -------------------------------------------------
    # Add floor joints to ops domain
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 1)
    ops.node(1, 0, 0, 3.0, '-mass', 8.72262996941896, 8.72262996941896, 8.72262996941896, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10001, 0, 0, 3.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300001, 41058.26935)
    ops.uniaxialMaterial('Elastic', 400001, 35168.1308)
    ops.section('Aggregator', 10001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400001, 'My', 300001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10001, 1, 10001, 10001, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 0, 1)
    ops.node(101, 5, 0, 3.0, '-mass', 8.748140672782874, 8.748140672782874, 8.748140672782874, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10101, 5, 0, 3.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300101, 86128.94325)
    ops.uniaxialMaterial('Elastic', 400101, 76307.89115)
    ops.section('Aggregator', 10101, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400101, 'My', 300101, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10101, 101, 10101, 10101, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 0, 1)
    ops.node(201, 8.3, 0, 3.0, '-mass', 8.748140672782874, 8.748140672782874, 8.748140672782874, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10201, 8.3, 0, 3.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300201, 86128.94325)
    ops.uniaxialMaterial('Elastic', 400201, 76307.89115)
    ops.section('Aggregator', 10201, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400201, 'My', 300201, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10201, 201, 10201, 10201, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 0, 1)
    ops.node(301, 13.3, 0, 3.0, '-mass', 8.72262996941896, 8.72262996941896, 8.72262996941896, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10301, 13.3, 0, 3.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300301, 41058.26935)
    ops.uniaxialMaterial('Elastic', 400301, 35168.1308)
    ops.section('Aggregator', 10301, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400301, 'My', 300301, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10301, 301, 10301, 10301, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 1, 1)
    ops.node(11, 0, 5, 3.0, '-mass', 16.10336391437309, 16.10336391437309, 16.10336391437309, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10011, 0, 5, 3.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300011, 95052.5665)
    ops.uniaxialMaterial('Elastic', 400011, 66418.3289)
    ops.section('Aggregator', 10011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400011, 'My', 300011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10011, 11, 10011, 10011, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 1, 1)
    ops.node(111, 5, 5, 3.0, '-mass', 22.899036697247706, 22.899036697247706, 22.899036697247706, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10111, 5, 5, 3.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300111, 183243.50975)
    ops.uniaxialMaterial('Elastic', 400111, 142157.521)
    ops.section('Aggregator', 10111, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400111, 'My', 300111, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10111, 111, 10111, 10111, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 1, 1)
    ops.node(211, 8.3, 5, 3.0, '-mass', 22.899036697247706, 22.899036697247706, 22.899036697247706, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10211, 8.3, 5, 3.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300211, 183243.50975)
    ops.uniaxialMaterial('Elastic', 400211, 142157.521)
    ops.section('Aggregator', 10211, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400211, 'My', 300211, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10211, 211, 10211, 10211, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 1, 1)
    ops.node(311, 13.3, 5, 3.0, '-mass', 16.10336391437309, 16.10336391437309, 16.10336391437309, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10311, 13.3, 5, 3.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300311, 95052.5665)
    ops.uniaxialMaterial('Elastic', 400311, 66418.3289)
    ops.section('Aggregator', 10311, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400311, 'My', 300311, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10311, 311, 10311, 10311, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 2, 1)
    ops.node(21, 0, 10, 3.0, '-mass', 15.981039755351684, 15.981039755351684, 15.981039755351684, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10021, 0, 10, 3.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300021, 94869.34235)
    ops.uniaxialMaterial('Elastic', 400021, 66294.5714)
    ops.section('Aggregator', 10021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400021, 'My', 300021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10021, 21, 10021, 10021, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 2, 1)
    ops.node(121, 5, 10, 3.0, '-mass', 23.642415902140677, 23.642415902140677, 23.642415902140677, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10121, 5, 10, 3.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300121, 186127.4502)
    ops.uniaxialMaterial('Elastic', 400121, 144394.83805)
    ops.section('Aggregator', 10121, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400121, 'My', 300121, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10121, 121, 10121, 10121, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 2, 1)
    ops.node(221, 8.3, 10, 3.0, '-mass', 23.642415902140677, 23.642415902140677, 23.642415902140677, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10221, 8.3, 10, 3.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300221, 186127.4502)
    ops.uniaxialMaterial('Elastic', 400221, 144394.83805)
    ops.section('Aggregator', 10221, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400221, 'My', 300221, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10221, 221, 10221, 10221, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 2, 1)
    ops.node(321, 13.3, 10, 3.0, '-mass', 15.981039755351684, 15.981039755351684, 15.981039755351684, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10321, 13.3, 10, 3.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300321, 94869.34235)
    ops.uniaxialMaterial('Elastic', 400321, 66294.5714)
    ops.section('Aggregator', 10321, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400321, 'My', 300321, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10321, 321, 10321, 10321, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 3, 1)
    ops.node(31, 0, 15, 3.0, '-mass', 8.72262996941896, 8.72262996941896, 8.72262996941896, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10031, 0, 15, 3.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300031, 41058.26935)
    ops.uniaxialMaterial('Elastic', 400031, 35168.1308)
    ops.section('Aggregator', 10031, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400031, 'My', 300031, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10031, 31, 10031, 10031, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 3, 1)
    ops.node(131, 5, 15, 3.0, '-mass', 12.896694189602448, 12.896694189602448, 12.896694189602448, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10131, 5, 15, 3.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300131, 77882.19595)
    ops.uniaxialMaterial('Elastic', 400131, 73488.2853)
    ops.section('Aggregator', 10131, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400131, 'My', 300131, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10131, 131, 10131, 10131, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 3, 1)
    ops.node(231, 8.3, 15, 3.0, '-mass', 12.896694189602448, 12.896694189602448, 12.896694189602448, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10231, 8.3, 15, 3.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300231, 77882.19595)
    ops.uniaxialMaterial('Elastic', 400231, 73488.2853)
    ops.section('Aggregator', 10231, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400231, 'My', 300231, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10231, 231, 10231, 10231, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 3, 1)
    ops.node(331, 13.3, 15, 3.0, '-mass', 8.72262996941896, 8.72262996941896, 8.72262996941896, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10331, 13.3, 15, 3.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300331, 41058.26935)
    ops.uniaxialMaterial('Elastic', 400331, 35168.1308)
    ops.section('Aggregator', 10331, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400331, 'My', 300331, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10331, 331, 10331, 10331, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 0, 2)
    ops.node(2, 0, 0, 6.0, '-mass', 8.72262996941896, 8.72262996941896, 8.72262996941896, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10002, 0, 0, 6.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300002, 34165.43415)
    ops.uniaxialMaterial('Elastic', 400002, 29224.6716)
    ops.section('Aggregator', 10002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400002, 'My', 300002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10002, 2, 10002, 10002, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 0, 2)
    ops.node(102, 5, 0, 6.0, '-mass', 8.748140672782874, 8.748140672782874, 8.748140672782874, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10102, 5, 0, 6.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300102, 70444.8074)
    ops.uniaxialMaterial('Elastic', 400102, 61680.0954)
    ops.section('Aggregator', 10102, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400102, 'My', 300102, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10102, 102, 10102, 10102, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 0, 2)
    ops.node(202, 8.3, 0, 6.0, '-mass', 8.748140672782874, 8.748140672782874, 8.748140672782874, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10202, 8.3, 0, 6.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300202, 70444.8074)
    ops.uniaxialMaterial('Elastic', 400202, 61680.0954)
    ops.section('Aggregator', 10202, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400202, 'My', 300202, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10202, 202, 10202, 10202, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 0, 2)
    ops.node(302, 13.3, 0, 6.0, '-mass', 8.72262996941896, 8.72262996941896, 8.72262996941896, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10302, 13.3, 0, 6.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300302, 34165.43415)
    ops.uniaxialMaterial('Elastic', 400302, 29224.6716)
    ops.section('Aggregator', 10302, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400302, 'My', 300302, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10302, 302, 10302, 10302, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 1, 2)
    ops.node(12, 0, 5, 6.0, '-mass', 15.981039755351684, 15.981039755351684, 15.981039755351684, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10012, 0, 5, 6.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300012, 78469.43655)
    ops.uniaxialMaterial('Elastic', 400012, 55214.6592)
    ops.section('Aggregator', 10012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400012, 'My', 300012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10012, 12, 10012, 10012, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 1, 2)
    ops.node(112, 5, 5, 6.0, '-mass', 22.695978593272173, 22.695978593272173, 22.695978593272173, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10112, 5, 5, 6.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300112, 152647.18865)
    ops.uniaxialMaterial('Elastic', 400112, 118421.3616)
    ops.section('Aggregator', 10112, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400112, 'My', 300112, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10112, 112, 10112, 10112, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 1, 2)
    ops.node(212, 8.3, 5, 6.0, '-mass', 22.695978593272173, 22.695978593272173, 22.695978593272173, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10212, 8.3, 5, 6.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300212, 152647.18865)
    ops.uniaxialMaterial('Elastic', 400212, 118421.3616)
    ops.section('Aggregator', 10212, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400212, 'My', 300212, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10212, 212, 10212, 10212, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 1, 2)
    ops.node(312, 13.3, 5, 6.0, '-mass', 15.981039755351684, 15.981039755351684, 15.981039755351684, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10312, 13.3, 5, 6.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300312, 78469.43655)
    ops.uniaxialMaterial('Elastic', 400312, 55214.6592)
    ops.section('Aggregator', 10312, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400312, 'My', 300312, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10312, 312, 10312, 10312, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 2, 2)
    ops.node(22, 0, 10, 6.0, '-mass', 15.981039755351684, 15.981039755351684, 15.981039755351684, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10022, 0, 10, 6.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300022, 78388.2733)
    ops.uniaxialMaterial('Elastic', 400022, 55159.8085)
    ops.section('Aggregator', 10022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400022, 'My', 300022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10022, 22, 10022, 10022, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 2, 2)
    ops.node(122, 5, 10, 6.0, '-mass', 23.642415902140677, 23.642415902140677, 23.642415902140677, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10122, 5, 10, 6.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300122, 155020.0601)
    ops.uniaxialMaterial('Elastic', 400122, 120262.1991)
    ops.section('Aggregator', 10122, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400122, 'My', 300122, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10122, 122, 10122, 10122, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 2, 2)
    ops.node(222, 8.3, 10, 6.0, '-mass', 23.642415902140677, 23.642415902140677, 23.642415902140677, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10222, 8.3, 10, 6.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300222, 155020.0601)
    ops.uniaxialMaterial('Elastic', 400222, 120262.1991)
    ops.section('Aggregator', 10222, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400222, 'My', 300222, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10222, 222, 10222, 10222, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 2, 2)
    ops.node(322, 13.3, 10, 6.0, '-mass', 15.981039755351684, 15.981039755351684, 15.981039755351684, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10322, 13.3, 10, 6.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300322, 78388.2733)
    ops.uniaxialMaterial('Elastic', 400322, 55159.8085)
    ops.section('Aggregator', 10322, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400322, 'My', 300322, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10322, 322, 10322, 10322, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 3, 2)
    ops.node(32, 0, 15, 6.0, '-mass', 8.72262996941896, 8.72262996941896, 8.72262996941896, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10032, 0, 15, 6.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300032, 34165.43415)
    ops.uniaxialMaterial('Elastic', 400032, 29224.6716)
    ops.section('Aggregator', 10032, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400032, 'My', 300032, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10032, 32, 10032, 10032, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 3, 2)
    ops.node(132, 5, 15, 6.0, '-mass', 12.896694189602448, 12.896694189602448, 12.896694189602448, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10132, 5, 15, 6.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300132, 65030.5938)
    ops.uniaxialMaterial('Elastic', 400132, 60765.18145)
    ops.section('Aggregator', 10132, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400132, 'My', 300132, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10132, 132, 10132, 10132, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 3, 2)
    ops.node(232, 8.3, 15, 6.0, '-mass', 12.896694189602448, 12.896694189602448, 12.896694189602448, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10232, 8.3, 15, 6.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300232, 65030.5938)
    ops.uniaxialMaterial('Elastic', 400232, 60765.18145)
    ops.section('Aggregator', 10232, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400232, 'My', 300232, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10232, 232, 10232, 10232, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 3, 2)
    ops.node(332, 13.3, 15, 6.0, '-mass', 8.72262996941896, 8.72262996941896, 8.72262996941896, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10332, 13.3, 15, 6.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300332, 34165.43415)
    ops.uniaxialMaterial('Elastic', 400332, 29224.6716)
    ops.section('Aggregator', 10332, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400332, 'My', 300332, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10332, 332, 10332, 10332, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 0, 3)
    ops.node(3, 0, 0, 9.0, '-mass', 6.957186544342508, 6.957186544342508, 6.957186544342508, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10003, 0, 0, 9.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300003, 42301.8123)
    ops.uniaxialMaterial('Elastic', 400003, 36597.115)
    ops.section('Aggregator', 10003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400003, 'My', 300003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10003, 3, 10003, 10003, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 0, 3)
    ops.node(103, 5, 0, 9.0, '-mass', 7.374311926605504, 7.374311926605504, 7.374311926605504, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10103, 5, 0, 9.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300103, 59322.1075)
    ops.uniaxialMaterial('Elastic', 400103, 45135.93415)
    ops.section('Aggregator', 10103, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400103, 'My', 300103, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10103, 103, 10103, 10103, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 0, 3)
    ops.node(203, 8.3, 0, 9.0, '-mass', 7.374311926605504, 7.374311926605504, 7.374311926605504, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10203, 8.3, 0, 9.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300203, 59322.1075)
    ops.uniaxialMaterial('Elastic', 400203, 45135.93415)
    ops.section('Aggregator', 10203, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400203, 'My', 300203, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10203, 203, 10203, 10203, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 0, 3)
    ops.node(303, 13.3, 0, 9.0, '-mass', 6.957186544342508, 6.957186544342508, 6.957186544342508, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10303, 13.3, 0, 9.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300303, 42301.8123)
    ops.uniaxialMaterial('Elastic', 400303, 36597.115)
    ops.section('Aggregator', 10303, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400303, 'My', 300303, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10303, 303, 10303, 10303, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 1, 3)
    ops.node(13, 0, 5, 9.0, '-mass', 13.41896024464832, 13.41896024464832, 13.41896024464832, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10013, 0, 5, 9.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300013, 68538.86145)
    ops.uniaxialMaterial('Elastic', 400013, 68538.86145)
    ops.section('Aggregator', 10013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400013, 'My', 300013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10013, 13, 10013, 10013, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 1, 3)
    ops.node(113, 5, 5, 9.0, '-mass', 20.387798165137614, 20.387798165137614, 20.387798165137614, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10113, 5, 5, 9.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300113, 118402.05005)
    ops.uniaxialMaterial('Elastic', 400113, 104501.0721)
    ops.section('Aggregator', 10113, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400113, 'My', 300113, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10113, 113, 10113, 10113, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 1, 3)
    ops.node(213, 8.3, 5, 9.0, '-mass', 20.387798165137614, 20.387798165137614, 20.387798165137614, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10213, 8.3, 5, 9.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300213, 118402.05005)
    ops.uniaxialMaterial('Elastic', 400213, 104501.0721)
    ops.section('Aggregator', 10213, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400213, 'My', 300213, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10213, 213, 10213, 10213, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 1, 3)
    ops.node(313, 13.3, 5, 9.0, '-mass', 13.41896024464832, 13.41896024464832, 13.41896024464832, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10313, 13.3, 5, 9.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300313, 68538.86145)
    ops.uniaxialMaterial('Elastic', 400313, 68538.86145)
    ops.section('Aggregator', 10313, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400313, 'My', 300313, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10313, 313, 10313, 10313, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 2, 3)
    ops.node(23, 0, 10, 9.0, '-mass', 13.357798165137615, 13.357798165137615, 13.357798165137615, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10023, 0, 10, 9.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300023, 68395.33775)
    ops.uniaxialMaterial('Elastic', 400023, 59356.32825)
    ops.section('Aggregator', 10023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400023, 'My', 300023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10023, 23, 10023, 10023, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 2, 3)
    ops.node(123, 5, 10, 9.0, '-mass', 20.81137614678899, 20.81137614678899, 20.81137614678899, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10123, 5, 10, 9.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300123, 119515.5138)
    ops.uniaxialMaterial('Elastic', 400123, 91657.46945)
    ops.section('Aggregator', 10123, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400123, 'My', 300123, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10123, 123, 10123, 10123, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 2, 3)
    ops.node(223, 8.3, 10, 9.0, '-mass', 20.81137614678899, 20.81137614678899, 20.81137614678899, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10223, 8.3, 10, 9.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300223, 119515.5138)
    ops.uniaxialMaterial('Elastic', 400223, 91657.46945)
    ops.section('Aggregator', 10223, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400223, 'My', 300223, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10223, 223, 10223, 10223, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 2, 3)
    ops.node(323, 13.3, 10, 9.0, '-mass', 13.357798165137615, 13.357798165137615, 13.357798165137615, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10323, 13.3, 10, 9.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300323, 68395.33775)
    ops.uniaxialMaterial('Elastic', 400323, 59356.32825)
    ops.section('Aggregator', 10323, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400323, 'My', 300323, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10323, 323, 10323, 10323, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 3, 3)
    ops.node(33, 0, 15, 9.0, '-mass', 6.957186544342508, 6.957186544342508, 6.957186544342508, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10033, 0, 15, 9.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300033, 42301.8123)
    ops.uniaxialMaterial('Elastic', 400033, 36597.115)
    ops.section('Aggregator', 10033, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400033, 'My', 300033, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10033, 33, 10033, 10033, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 3, 3)
    ops.node(133, 5, 15, 9.0, '-mass', 10.797737003058105, 10.797737003058105, 10.797737003058105, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10133, 5, 15, 9.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300133, 70466.89935)
    ops.uniaxialMaterial('Elastic', 400133, 53818.0074)
    ops.section('Aggregator', 10133, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400133, 'My', 300133, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10133, 133, 10133, 10133, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 3, 3)
    ops.node(233, 8.3, 15, 9.0, '-mass', 10.797737003058105, 10.797737003058105, 10.797737003058105, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10233, 8.3, 15, 9.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300233, 70466.89935)
    ops.uniaxialMaterial('Elastic', 400233, 53818.0074)
    ops.section('Aggregator', 10233, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400233, 'My', 300233, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10233, 233, 10233, 10233, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 3, 3)
    ops.node(333, 13.3, 15, 9.0, '-mass', 6.957186544342508, 6.957186544342508, 6.957186544342508, 0.0, 0.0, 0.0)
    # Joint flexibility model: elastic
    ops.node(10333, 13.3, 15, 9.0) # Constrained floor node
    ops.uniaxialMaterial('Elastic', 300333, 42301.8123)
    ops.uniaxialMaterial('Elastic', 400333, 36597.115)
    ops.section('Aggregator', 10333, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 400333, 'My', 300333, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10333, 333, 10333, 10333, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)
