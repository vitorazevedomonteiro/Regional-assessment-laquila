import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 31.15828653, 0.00953101, 38.12851662, 0.0577669, 3.81285166, 0.29598493, -31.15828653, -0.00953101, -38.12851662, -0.0577669, -3.81285166, -0.29598493, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 31.11872437, 0.0094901, 38.08010426, 0.05840384, 3.80801043, 0.29702351, -46.14811481, -0.00999571, -56.47162788, -0.06358172, -5.64716279, -0.30220139, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 28075754.33631988, 0.07, 0.00071458, 0.00023333, 11698230.97346662, 0.00060032)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.32586164311, 1001992, 0.32586164311, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 30.53911824, 0.00988482, 37.34250184, 0.07326333, 3.73425018, 0.38047356, -45.24013044, -0.01039375, -55.31854721, -0.07982621, -5.53185472, -0.38703645, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 30.53911824, 0.00988482, 37.34250184, 0.07256738, 3.73425018, 0.37183576, -45.24013044, -0.01039375, -55.31854721, -0.07906379, -5.53185472, -0.37833216, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 28372569.70012724, 0.07, 0.00071458, 0.00023333, 11821904.04171968, 0.00060032)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.25890295058, 1101992, 0.25890295058, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 30.50552288, 0.00987505, 37.26759479, 0.06009424, 3.72675948, 0.30436259, -45.18815402, -0.01037941, -55.20488274, -0.06539557, -5.52048827, -0.30966393, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 30.55040848, 0.00990096, 37.32243005, 0.05940038, 3.73224301, 0.30297942, -30.55040848, -0.00990096, -37.32243005, -0.05940038, -3.73224301, -0.30297942, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 28718335.78296817, 0.07, 0.00071458, 0.00023333, 11965973.24290341, 0.00060032)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32679790738000003, 1201992, 0.32679790738000003, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 52.94372888, 0.00999561, 64.76962096, 0.07851529, 6.4769621, 0.29122899, -80.88285214, -0.01091957, -98.94942774, -0.08667693, -9.89494277, -0.29939063, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 52.94372888, 0.00999561, 64.76962096, 0.07902716, 6.4769621, 0.29552958, -80.88285214, -0.01091957, -98.94942774, -0.08724287, -9.89494277, -0.30374529, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 28184280.94550836, 0.07, 0.00071458, 0.00023333, 11743450.39396182, 0.00060032)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.36544318233, 1011992, 0.36544318233, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 52.51490422, 0.010199, 64.07428352, 0.09399605, 6.40742835, 0.35865073, -80.25209543, -0.0111145, -97.91687889, -0.10376296, -9.79168789, -0.36841764, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 52.51490422, 0.010199, 64.07428352, 0.09408263, 6.40742835, 0.35938645, -80.25209543, -0.0111145, -97.91687889, -0.10385869, -9.79168789, -0.3691625, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 29186731.40324803, 0.07, 0.00071458, 0.00023333, 12161138.08468668, 0.00060032)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.29843994918, 1111992, 0.29843994918, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 52.63101787, 0.01070045, 64.17839766, 0.07757556, 6.41783977, 0.29099699, -80.40040074, -0.01164305, -98.04045408, -0.08558212, -9.80404541, -0.29900355, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 52.63101787, 0.01070045, 64.17839766, 0.07698562, 6.41783977, 0.28596814, -80.40040074, -0.01164305, -98.04045408, -0.08492986, -9.80404541, -0.29391238, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 29396665.24234455, 0.07, 0.00071458, 0.00023333, 12248610.51764357, 0.00060032)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.37031269183000004, 1211992, 0.37031269183000004, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 30.7370239, 0.00957088, 37.6377071, 0.06086396, 3.76377071, 0.30763065, -30.7370239, -0.00957088, -37.6377071, -0.06086396, -3.76377071, -0.30763065, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 30.69355388, 0.00953306, 37.58447775, 0.0612628, 3.75844777, 0.30525414, -45.50905502, -0.01003994, -55.72616557, -0.06671093, -5.57261656, -0.31070227, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 27812925.18981815, 0.07, 0.00071458, 0.00023333, 11588718.8290909, 0.00060032)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.32516076930000004, 1021992, 0.32516076930000004, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 30.72233296, 0.00966928, 37.36304058, 0.06849749, 3.73630406, 0.36809724, -45.53702686, -0.01015249, -55.37996691, -0.07460001, -5.53799669, -0.37419975, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 30.72233296, 0.00966928, 37.36304058, 0.06911984, 3.73630406, 0.37629254, -45.53702686, -0.01015249, -55.37996691, -0.0752818, -5.53799669, -0.3824545, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 30312641.50156392, 0.07, 0.00071458, 0.00023333, 12630267.2923183, 0.00060032)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.25825568653, 1121992, 0.25825568653, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 30.8594718, 0.00976316, 37.87736036, 0.06201285, 3.78773604, 0.30768579, -45.7432603, -0.0102904, -56.14593683, -0.067531, -5.61459368, -0.31320395, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 30.90656304, 0.00980114, 37.93516082, 0.06081959, 3.79351608, 0.30039145, -30.90656304, -0.00980114, -37.93516082, -0.06081959, -3.79351608, -0.30039145, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 26811237.75249045, 0.07, 0.00071458, 0.00023333, 11171349.06353769, 0.00060032)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.32679267239000004, 1221992, 0.32679267239000004, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 35.85635392, 0.00796109, 43.78162238, 0.09823498, 4.37816224, 0.40526336, -145.33372156, -0.01030407, -177.45658498, -0.1359081, -17.7456585, -0.44293648, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 53.27084851, 0.00825419, 65.04521287, 0.10052919, 6.50452129, 0.40755757, -145.44865991, -0.01022835, -177.59692795, -0.12742224, -17.7596928, -0.43445062, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 28913344.31952253, 0.08, 0.00106667, 0.00026667, 12047226.79980106, 0.00073242)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.32570279072, 2001992, 0.32570279072, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 79.74201684, 0.00637854, 97.5310846, 0.0798618, 9.75310846, 0.32964477, -187.21801277, -0.00737742, -228.98312038, -0.09720453, -22.89831204, -0.3469875, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 118.34842571, 0.00657995, 144.74991701, 0.082962, 14.4749917, 0.32881307, -276.42108115, -0.00788345, -338.08585383, -0.10125408, -33.80858538, -0.34710516, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 28275234.42814945, 0.125, 0.00260417, 0.00065104, 11781347.6783956, 0.00178813)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.36626798322000004, 2101992, 0.36626798322000004, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 81.79804531, 0.00647149, 99.75465487, 0.07736578, 9.97546549, 0.32443922, -192.09753463, -0.00746567, -234.2674962, -0.09412798, -23.42674962, -0.34120141, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 121.43521148, 0.00667319, 148.09311843, 0.08083665, 14.80931184, 0.32773602, -283.68601181, -0.00796919, -345.96181478, -0.09862778, -34.59618148, -0.34552715, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 29361263.74725183, 0.125, 0.00260417, 0.00065104, 12233859.89468826, 0.00178813)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.36980532166, 2201992, 0.36980532166, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 35.75075674, 0.00819892, 43.65389652, 0.0986399, 4.36538965, 0.40436629, -144.85916194, -0.01058548, -176.88204225, -0.13642199, -17.68820422, -0.44214839, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 53.02993024, 0.00849807, 64.75284155, 0.10016884, 6.47528416, 0.40589523, -144.90068363, -0.01051161, -176.93274282, -0.12693809, -17.69327428, -0.43266449, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 28903076.48497003, 0.08, 0.00106667, 0.00026667, 12042948.53540418, 0.00073242)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.32708985015, 2301992, 0.32708985015, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 51.1494904, 0.00839709, 62.16682475, 0.0974856, 6.21668247, 0.40612073, -139.84743111, -0.01030781, -169.9698408, -0.12345471, -16.99698408, -0.43208984, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 34.55232808, 0.00811037, 41.99471994, 0.09629097, 4.19947199, 0.4049261, -139.87890064, -0.01037161, -170.00808871, -0.13306311, -17.00080887, -0.44169824, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 30517463.54592312, 0.08, 0.00106667, 0.00026667, 12715609.8108013, 0.00073242)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.3240071874, 2011992, 0.3240071874, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 120.83100974, 0.00661588, 147.83880365, 0.08193924, 14.78388036, 0.32716733, -281.98696149, -0.00793626, -345.0158624, -0.10001274, -34.50158624, -0.34524083, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 81.35403618, 0.00641596, 99.53805242, 0.0785638, 9.95380524, 0.32513695, -190.92352221, -0.00742826, -233.59818951, -0.09562294, -23.35981895, -0.34219609, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 28136087.48675968, 0.125, 0.00260417, 0.00065104, 11723369.78614987, 0.00178813)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.36847815238, 2111992, 0.36847815238, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 120.5678873, 0.00650758, 147.07240414, 0.08202118, 14.70724041, 0.33192608, -281.39510599, -0.00778033, -343.2543746, -0.10008936, -34.32543746, -0.34999427, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 81.14543841, 0.00631385, 98.98369275, 0.07804483, 9.89836928, 0.32441153, -190.4730984, -0.00729078, -232.34492312, -0.09497587, -23.23449231, -0.34134257, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 29271133.33965125, 0.125, 0.00260417, 0.00065104, 12196305.55818802, 0.00178813)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.36711171001000004, 2211992, 0.36711171001000004, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 53.10901461, 0.0085974, 64.64594914, 0.09582834, 6.46459491, 0.40076674, -145.19414604, -0.0105821, -176.7348434, -0.12136978, -17.67348434, -0.42630818, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 35.83748285, 0.00830057, 43.62250196, 0.09511787, 4.3622502, 0.40005627, -145.19236026, -0.01065111, -176.7326697, -0.13144577, -17.67326697, -0.43638417, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 30015550.95287529, 0.08, 0.00106667, 0.00026667, 12506479.56369804, 0.00073242)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.32793508243999997, 2311992, 0.32793508243999997, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)
