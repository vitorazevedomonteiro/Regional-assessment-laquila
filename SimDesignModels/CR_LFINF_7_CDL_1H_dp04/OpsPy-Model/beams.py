import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 29.68513388, 0.00941855, 36.13436896, 0.04591079, 3.6134369, 0.25210402, -29.68513388, -0.00941855, -36.13436896, -0.04591079, -3.6134369, -0.25210402, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 29.64286292, 0.00939279, 36.08291443, 0.04706244, 3.60829144, 0.26251071, -43.93059019, -0.00986376, -53.47471771, -0.05113162, -5.34747177, -0.2665799, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 30009000.71838697, 0.07, 0.00071458, 0.00023333, 12503750.2993279, 0.00060032)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.32216101412000003, 1001992, 0.32216101412000003, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 30.84149004, 0.00952719, 37.22332494, 0.0557386, 3.72233249, 0.32367231, -45.7272442, -0.00998518, -55.18929427, -0.06061073, -5.51892943, -0.32854444, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 30.84149004, 0.00952719, 37.22332494, 0.05460343, 3.72233249, 0.30718711, -45.7272442, -0.00998518, -55.18929427, -0.05936713, -5.51892943, -0.31195081, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 32623520.06581163, 0.07, 0.00071458, 0.00023333, 13593133.36075485, 0.00060032)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.25787520447, 1101992, 0.25787520447, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 30.91105112, 0.00987938, 37.51760875, 0.04506007, 3.75176088, 0.24914056, -45.79356759, -0.01036272, -55.58093595, -0.04890389, -5.5580936, -0.25298438, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 30.95231482, 0.00990156, 37.56769167, 0.04459613, 3.75676917, 0.24835292, -30.95231482, -0.00990156, -37.56769167, -0.04459613, -3.75676917, -0.24835292, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 30957536.61012978, 0.07, 0.00071458, 0.00023333, 12898973.58755407, 0.00060032)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32794259617, 1201992, 0.32794259617, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 54.00400403, 0.01019597, 65.99778138, 0.06610926, 6.59977814, 0.24773387, -82.51024053, -0.01113048, -100.83498277, -0.07294985, -10.08349828, -0.25457446, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 54.00400403, 0.01019597, 65.99778138, 0.06692185, 6.59977814, 0.25487025, -82.51024053, -0.01113048, -100.83498277, -0.07384827, -10.08349828, -0.26179668, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 28587433.32164377, 0.07, 0.00071458, 0.00023333, 11911430.5506849, 0.00060032)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.36883006917, 1011992, 0.36883006917, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 53.76294023, 0.01132345, 66.30387712, 0.08078856, 6.63038771, 0.29701367, -82.09226435, -0.01242608, -101.24140133, -0.08922873, -10.12414013, -0.30545385, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 53.76294023, 0.01132345, 66.30387712, 0.08564886, 6.63038771, 0.33949812, -82.09226435, -0.01242608, -101.24140133, -0.09460242, -10.12414013, -0.34845169, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 24488217.30390873, 0.07, 0.00071458, 0.00023333, 10203423.87662864, 0.00060032)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.3079394992, 1111992, 0.3079394992, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 52.95438522, 0.01030095, 64.29915435, 0.07485277, 6.42991544, 0.28628495, -80.93676224, -0.0111953, -98.27638157, -0.08256569, -9.82763816, -0.29399786, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 52.95438522, 0.01030095, 64.29915435, 0.07205473, 6.42991544, 0.26239039, -80.93676224, -0.0111953, -98.27638157, -0.07947209, -9.82763816, -0.26980775, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 30824736.07894094, 0.07, 0.00071458, 0.00023333, 12843640.03289206, 0.00060032)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.36819938626, 1211992, 0.36819938626, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 30.77028521, 0.00929092, 37.35027148, 0.05758436, 3.73502715, 0.30343107, -30.77028521, -0.00929092, -37.35027148, -0.05758436, -3.73502715, -0.30343107, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 30.7321376, 0.00925696, 37.30396629, 0.05668592, 3.73039663, 0.28493638, -45.58565089, -0.00972295, -55.33378792, -0.06168235, -5.53337879, -0.28993281, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 30927827.26157134, 0.07, 0.00071458, 0.00023333, 12886594.69232139, 0.00060032)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.32386634406000003, 1021992, 0.32386634406000003, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 30.44330573, 0.0098105, 37.2285082, 0.06560095, 3.72285082, 0.3495922, -45.10401511, -0.01031706, -55.15679576, -0.07143666, -5.51567958, -0.3554279, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 30.44330573, 0.0098105, 37.2285082, 0.06608097, 3.72285082, 0.35590255, -45.10401511, -0.01031706, -55.15679576, -0.07196252, -5.51567958, -0.3617841, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 28339675.64938219, 0.07, 0.00071458, 0.00023333, 11808198.18724258, 0.00060032)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.258257875, 1121992, 0.258257875, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 30.1044438, 0.00995382, 36.39369969, 0.04450369, 3.63936997, 0.2491319, -44.52427382, -0.0104205, -53.82604178, -0.0482706, -5.38260418, -0.25289881, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 30.12997771, 0.00996435, 36.424568, 0.04660782, 3.6424568, 0.28939048, -30.12997771, -0.00996435, -36.424568, -0.04660782, -3.6424568, -0.28939048, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 32155774.55701827, 0.07, 0.00071458, 0.00023333, 13398239.39875761, 0.00060032)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.32648999379000004, 1221992, 0.32648999379000004, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 36.25586669, 0.00868807, 44.36416646, 0.0859958, 4.43641665, 0.37849475, -146.57712142, -0.01122183, -179.35778145, -0.11878518, -17.93577815, -0.41128414, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 53.64368737, 0.00900523, 65.64061746, 0.08550428, 6.56406175, 0.36306117, -146.53824924, -0.01114636, -179.31021586, -0.10830399, -17.93102159, -0.38586088, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 28096085.88026876, 0.08, 0.00106667, 0.00026667, 11706702.45011198, 0.00073242)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.33119026934, 2001992, 0.33119026934, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 82.07013957, 0.00641058, 100.28478863, 0.07140842, 10.02847886, 0.29715354, -192.60088607, -0.00741444, -235.34673208, -0.08686885, -23.53467321, -0.31261396, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 121.93714152, 0.00660829, 148.99987411, 0.07637903, 14.89998741, 0.31619019, -284.52087304, -0.0079168, -347.66744352, -0.09320567, -34.76674435, -0.33301683, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 28634117.68370078, 0.125, 0.00260417, 0.00065104, 11930882.36820866, 0.00178813)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.36924826816, 2101992, 0.36924826816, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 81.20229527, 0.00621576, 97.86076515, 0.05968708, 9.78607652, 0.26598674, -190.86085092, -0.00711525, -230.01552907, -0.07247945, -23.00155291, -0.27877911, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 120.65333336, 0.00640165, 145.40509577, 0.06267427, 14.54050958, 0.27177414, -282.04284047, -0.00757032, -339.90330053, -0.07635886, -33.99033005, -0.28545873, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 33028574.6329582, 0.125, 0.00260417, 0.00065104, 13761906.09706592, 0.00178813)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.36635265758999996, 2201992, 0.36635265758999996, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 34.56306891, 0.0078952, 42.20125807, 0.08629768, 4.22012581, 0.38150229, -140.06132194, -0.01019553, -171.0138648, -0.11928209, -17.10138648, -0.4144867, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 51.27899894, 0.0081835, 62.61128819, 0.08886035, 6.26112882, 0.39621744, -140.10955262, -0.01012397, -171.0727541, -0.11258763, -17.10727541, -0.41994472, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 28924091.65756933, 0.08, 0.00106667, 0.00026667, 12051704.85732055, 0.00073242)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.32266366233000005, 2301992, 0.32266366233000005, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 55.95212016, 0.00830796, 68.28998752, 0.09764583, 6.82899875, 0.40123169, -152.51164672, -0.01031158, -186.14162292, -0.12377517, -18.61416229, -0.42736103, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 37.6059544, 0.0080103, 45.8983529, 0.08916693, 4.58983529, 0.3618622, -152.29076597, -0.010392, -185.87203628, -0.1233106, -18.58720363, -0.39600587, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 29070119.19385195, 0.08, 0.00106667, 0.00026667, 12112549.66410498, 0.00073242)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.32939610434000005, 2011992, 0.32939610434000005, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 122.59319071, 0.00659427, 150.10910123, 0.08321482, 15.01091012, 0.33153456, -285.75875048, -0.00792574, -349.89699636, -0.10158793, -34.98969964, -0.34990767, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 82.46862716, 0.00639788, 100.97862231, 0.07478204, 10.09786223, 0.28593773, -193.40140795, -0.00741918, -236.81014709, -0.09101307, -23.68101471, -0.30216876, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 27832180.07559527, 0.125, 0.00260417, 0.00065104, 11596741.6981647, 0.00178813)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.36940522493, 2111992, 0.36940522493, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 118.86492168, 0.00675143, 144.82691527, 0.07805506, 14.48269153, 0.31730018, -278.08503648, -0.00804118, -338.8232411, -0.09520388, -33.88232411, -0.334449, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 80.2001155, 0.00654162, 97.7170991, 0.06996683, 9.77170991, 0.2717902, -188.44134603, -0.00752999, -229.59993974, -0.08506199, -22.95999397, -0.28688536, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 29681470.45497989, 0.125, 0.00260417, 0.00065104, 12367279.35624162, 0.00178813)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.36890382554, 2211992, 0.36890382554, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 51.68104623, 0.00869404, 62.50306656, 0.08619207, 6.25030666, 0.39230783, -141.23917273, -0.01059926, -170.81468078, -0.10902566, -17.08146808, -0.41514143, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 34.99861632, 0.00840552, 42.32733285, 0.0823985, 4.23273328, 0.36567935, -141.329985, -0.01065672, -170.92450916, -0.11360804, -17.09245092, -0.3968889, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 32039352.41137284, 0.08, 0.00106667, 0.00026667, 13349730.17140535, 0.00073242)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.32667379812, 2311992, 0.32667379812, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)
