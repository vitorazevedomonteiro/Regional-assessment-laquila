import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 30.15249193, 0.00970314, 36.9808038, 0.06919653, 3.69808038, 0.29479091, -52.28375783, -0.01056903, -64.12390043, -0.078285, -6.41239004, -0.30387938, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 44.52667999, 0.01008008, 54.61016026, 0.07368027, 5.46101603, 0.31589038, -77.10581907, -0.01121097, -94.567148, -0.08360135, -9.4567148, -0.32581146, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 27149626.48515281, 0.07, 0.00071458, 0.00023333, 11312344.36881367, 0.00060032)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.32501992422000003, 1001992, 0.32501992422000003, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 46.48541005, 0.00975425, 56.85863361, 0.0821824, 5.68586336, 0.35650533, -80.47668955, -0.01084836, -98.43507027, -0.09328681, -9.84350703, -0.36760974, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 46.48541005, 0.00975425, 56.85863361, 0.08049658, 5.68586336, 0.33991466, -80.47668955, -0.01084836, -98.43507027, -0.09136799, -9.84350703, -0.35078607, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 28253758.7353456, 0.07, 0.00071458, 0.00023333, 11772399.47306067, 0.00060032)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.25812500719000003, 1101992, 0.25812500719000003, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 47.04254704, 0.01027194, 57.75920549, 0.06683068, 5.77592055, 0.27933944, -81.44553923, -0.01145075, -99.99946714, -0.07582647, -9.99994671, -0.28833523, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 31.79813103, 0.00989669, 39.04199284, 0.06420003, 3.90419928, 0.27475082, -55.17139767, -0.01080012, -67.73987158, -0.07260873, -6.77398716, -0.28315952, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 26669004.9072735, 0.07, 0.00071458, 0.00023333, 11112085.37803062, 0.00060032)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32984759663, 1201992, 0.32984759663, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 34.19525094, 0.0081145, 41.96455845, 0.08231468, 4.19645584, 0.33018612, -138.20863832, -0.01023289, -169.61023305, -0.1134725, -16.9610233, -0.36134394, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 66.7055105, 0.00863981, 81.86128827, 0.08266356, 8.18612883, 0.31853287, -138.04052321, -0.0101306, -169.40392147, -0.09825188, -16.94039215, -0.33412119, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 26886515.35762477, 0.1, 0.00133333, 0.00052083, 11202714.73234366, 0.00127345)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.32319009842999996, 1011992, 0.32319009842999996, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 74.53221679, 0.00873365, 90.90717901, 0.10704467, 9.0907179, 0.4443075, -154.24915163, -0.01020456, -188.13817493, -0.12723852, -18.81381749, -0.46450135, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 74.53221679, 0.00873365, 90.90717901, 0.10829185, 9.0907179, 0.45579228, -154.24915163, -0.01020456, -188.13817493, -0.12872322, -18.81381749, -0.47622364, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 29308649.26390244, 0.1, 0.00133333, 0.00052083, 12211937.19329268, 0.00127345)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.26369991488, 1111992, 0.26369991488, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 69.04370091, 0.00865845, 84.59968229, 0.09240544, 8.45996823, 0.36734549, -142.9208283, -0.01014416, -175.12179255, -0.10984042, -17.51217926, -0.38478047, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 35.28561044, 0.00813394, 43.23568108, 0.08737258, 4.32356811, 0.33933406, -143.01419576, -0.01024971, -175.23619629, -0.12049967, -17.52361963, -0.37246115, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 27545766.37532892, 0.1, 0.00133333, 0.00052083, 11477402.65638705, 0.00127345)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.32573219495, 1211992, 0.32573219495, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 61.62730839, 0.00846991, 75.65223056, 0.0943271, 7.56522306, 0.36745448, -143.54267473, -0.0102585, -176.20960266, -0.1152117, -17.62096027, -0.38833908, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 91.44154022, 0.00893731, 112.25147851, 0.0949618, 11.22514785, 0.36808918, -143.71930215, -0.01012444, -176.42642631, -0.10611323, -17.64264263, -0.37924062, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 26752867.9977388, 0.08, 0.00106667, 0.00026667, 11147028.33239117, 0.00073242)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.36612952811000005, 1021992, 0.36612952811000005, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 91.97224359, 0.00964035, 112.85087287, 0.09467201, 11.28508729, 0.39993416, -144.78037846, -0.01089639, -177.64698832, -0.10577736, -17.76469883, -0.41103952, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 91.97224359, 0.00964035, 112.85087287, 0.09460269, 11.28508729, 0.39927491, -144.78037846, -0.01089639, -177.64698832, -0.10570002, -17.76469883, -0.41037224, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 26955654.66896252, 0.08, 0.00106667, 0.00026667, 11231522.77873439, 0.00073242)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.30480309991000004, 1121992, 0.30480309991000004, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 93.17975011, 0.00932373, 114.49294692, 0.08254855, 11.44929469, 0.34063381, -146.51248575, -0.01056744, -180.02458941, -0.09227398, -18.00245894, -0.35035923, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 62.82740045, 0.00883408, 77.1980416, 0.08376257, 7.71980416, 0.35321553, -146.39772884, -0.01070591, -179.88358391, -0.10229969, -17.98835839, -0.37175265, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 26327845.82514008, 0.08, 0.00106667, 0.00026667, 10969935.76047503, 0.00073242)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.37112229207, 1221992, 0.37112229207, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 1031, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1031990, 32.93461358, 0.00970589, 40.24956077, 0.05809838, 4.02495608, 0.25889583, -57.17012716, -0.01057201, -69.86790665, -0.06565283, -6.98679067, -0.26645028, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1031991, 32.88449412, 0.0096354, 40.18830952, 0.06067723, 4.01883095, 0.27615896, -84.44407432, -0.01126939, -103.19953785, -0.0749151, -10.31995379, -0.29039684, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1031990, 28582886.79275702, 0.07, 0.00071458, 0.00023333, 11909536.16364876, 0.00060032)
    ops.section('Aggregator', 1031991, 1031990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1031992, 1031991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1031, 1031991, 0.33134016195, 1031992, 0.33134016195, 1031990)
    # Create element
    ops.element('forceBeamColumn', 1031, 31, 131, 1031, 1031)

    # Create geometric transformation
    ops.geomTransf('Linear', 1131, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1131990, 29.5934874, 0.0090735, 36.10655116, 0.0759103, 3.61065512, 0.33945432, -76.00918545, -0.01056615, -92.73761846, -0.09390713, -9.27376185, -0.35745115, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1131991, 29.5934874, 0.0090735, 36.10655116, 0.08015182, 3.61065512, 0.38510909, -76.00918545, -0.01056615, -92.73761846, -0.09919601, -9.27376185, -0.40415328, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1131990, 29196160.15912619, 0.07, 0.00071458, 0.00023333, 12165066.73296925, 0.00060032)
    ops.section('Aggregator', 1131991, 1131990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1131992, 1131991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1131, 1131991, 0.25268833738, 1131992, 0.25268833738, 1131990)
    # Create element
    ops.element('forceBeamColumn', 1131, 131, 231, 1131, 1131)

    # Create geometric transformation
    ops.geomTransf('Linear', 1231, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1231990, 29.55048653, 0.00938477, 35.95054502, 0.06963221, 3.5950545, 0.30134768, -75.809685, -0.01087435, -92.22858281, -0.08599884, -9.22285828, -0.31771431, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1231991, 29.61316078, 0.00942082, 36.02679329, 0.06880336, 3.60267933, 0.30556772, -51.35631342, -0.01021284, -62.47908832, -0.07780266, -6.24790883, -0.31456701, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1231990, 30195545.10115736, 0.07, 0.00071458, 0.00023333, 12581477.12548223, 0.00060032)
    ops.section('Aggregator', 1231991, 1231990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1231992, 1231991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1231, 1231991, 0.32238869599, 1231992, 0.32238869599, 1231990)
    # Create element
    ops.element('forceBeamColumn', 1231, 231, 331, 1231, 1231)

    # Create geometric transformation
    ops.geomTransf('Linear', 1002, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1002990, 30.74457891, 0.00989494, 37.62903914, 0.06457696, 3.76290391, 0.27993121, -53.30734997, -0.01076155, -65.24416433, -0.07300118, -6.52441643, -0.28835542, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1002991, 30.67399907, 0.00985107, 37.54265476, 0.06510205, 3.75426548, 0.27381982, -78.6661939, -0.0114849, -96.28147122, -0.08037914, -9.62814712, -0.28909691, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1002990, 28004175.94407554, 0.07, 0.00071458, 0.00023333, 11668406.64336481, 0.00060032)
    ops.section('Aggregator', 1002991, 1002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1002992, 1002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1002, 1002991, 0.32754972226, 1002992, 0.32754972226, 1002990)
    # Create element
    ops.element('forceBeamColumn', 1002, 2, 102, 1002, 1002)

    # Create geometric transformation
    ops.geomTransf('Linear', 1102, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1102990, 30.92478984, 0.0099235, 37.66423236, 0.07404348, 3.76642324, 0.3344723, -79.2937006, -0.01150441, -96.57418465, -0.0914577, -9.65741847, -0.35188651, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1102991, 30.92478984, 0.0099235, 37.66423236, 0.07330749, 3.76642324, 0.32670118, -79.2937006, -0.01150441, -96.57418465, -0.09053997, -9.65741847, -0.34393366, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1102990, 29819487.79576601, 0.07, 0.00071458, 0.00023333, 12424786.58156917, 0.00060032)
    ops.section('Aggregator', 1102991, 1102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1102992, 1102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1102, 1102991, 0.2606167255, 1102992, 0.2606167255, 1102990)
    # Create element
    ops.element('forceBeamColumn', 1102, 102, 202, 1102, 1102)

    # Create geometric transformation
    ops.geomTransf('Linear', 1202, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1202990, 33.11669065, 0.00971102, 40.57080191, 0.06845773, 4.05708019, 0.29160642, -85.00360562, -0.01139328, -104.13674728, -0.08464646, -10.41367473, -0.30779516, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1202991, 33.16481593, 0.00978647, 40.62975953, 0.06655658, 4.06297595, 0.28412382, -57.55623311, -0.01067725, -70.511349, -0.07529355, -7.0511349, -0.2928608, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1202990, 27619926.57618406, 0.07, 0.00071458, 0.00023333, 11508302.74007669, 0.00060032)
    ops.section('Aggregator', 1202991, 1202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1202992, 1202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1202, 1202991, 0.33223124853, 1202992, 0.33223124853, 1202990)
    # Create element
    ops.element('forceBeamColumn', 1202, 202, 302, 1202, 1202)

    # Create geometric transformation
    ops.geomTransf('Linear', 1012, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1012990, 69.09415284, 0.00872652, 84.34477366, 0.08107302, 8.43447737, 0.34479788, -160.57749725, -0.01052146, -196.0205329, -0.09895899, -19.60205329, -0.36268385, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1012991, 69.09415284, 0.00872652, 84.34477366, 0.08160262, 8.43447737, 0.34532748, -160.57749725, -0.01052146, -196.0205329, -0.09960637, -19.60205329, -0.36333123, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1012990, 29005702.65252272, 0.08, 0.00106667, 0.00026667, 12085709.43855113, 0.00073242)
    ops.section('Aggregator', 1012991, 1012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1012992, 1012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1012, 1012991, 0.37918306264, 1012992, 0.37918306264, 1012990)
    # Create element
    ops.element('forceBeamColumn', 1012, 12, 112, 1012, 1012)

    # Create geometric transformation
    ops.geomTransf('Linear', 1112, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1112990, 63.56843746, 0.00860264, 77.53866172, 0.10920099, 7.75386617, 0.43980775, -148.20824202, -0.01032849, -180.77947486, -0.13330152, -18.07794749, -0.46390828, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1112991, 63.56843746, 0.00860264, 77.53866172, 0.1066972, 7.75386617, 0.43730396, -148.20824202, -0.01032849, -180.77947486, -0.13024085, -18.07794749, -0.46084761, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1112990, 29289969.08201421, 0.08, 0.00106667, 0.00026667, 12204153.78417259, 0.00073242)
    ops.section('Aggregator', 1112991, 1112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1112992, 1112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1112, 1112991, 0.30247415213, 1112992, 0.30247415213, 1112990)
    # Create element
    ops.element('forceBeamColumn', 1112, 112, 212, 1112, 1112)

    # Create geometric transformation
    ops.geomTransf('Linear', 1212, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1212990, 59.30314623, 0.0091492, 72.35732898, 0.08390344, 7.2357329, 0.35523281, -138.18330835, -0.01091438, -168.60109011, -0.10229516, -16.86010901, -0.37362453, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1212991, 59.30314623, 0.0091492, 72.35732898, 0.08546303, 7.2357329, 0.3567924, -138.18330835, -0.01091438, -168.60109011, -0.10420162, -16.86010901, -0.37553099, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1212990, 29183722.21947141, 0.08, 0.00106667, 0.00026667, 12159884.25811309, 0.00073242)
    ops.section('Aggregator', 1212991, 1212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1212992, 1212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1212, 1212991, 0.36855575244, 1212992, 0.36855575244, 1212990)
    # Create element
    ops.element('forceBeamColumn', 1212, 212, 312, 1212, 1212)

    # Create geometric transformation
    ops.geomTransf('Linear', 1022, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1022990, 61.00500957, 0.00901694, 74.60446708, 0.0792991, 7.46044671, 0.33939974, -142.30995427, -0.0108151, -174.0342043, -0.09672913, -17.40342043, -0.35682978, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1022991, 61.00500957, 0.00901694, 74.60446708, 0.08297554, 7.46044671, 0.35310601, -142.30995427, -0.0108151, -174.0342043, -0.10122327, -17.40342043, -0.37135375, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1022990, 28325827.00030396, 0.08, 0.00106667, 0.00026667, 11802427.91679332, 0.00073242)
    ops.section('Aggregator', 1022991, 1022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1022992, 1022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1022, 1022991, 0.37019147766, 1022992, 0.37019147766, 1022990)
    # Create element
    ops.element('forceBeamColumn', 1022, 22, 122, 1022, 1022)

    # Create geometric transformation
    ops.geomTransf('Linear', 1122, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1122990, 61.82805517, 0.00902284, 75.86182921, 0.11104899, 7.58618292, 0.44067817, -144.18759817, -0.01088577, -176.91539734, -0.13560416, -17.69153973, -0.46523334, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1122991, 61.82805517, 0.00902284, 75.86182921, 0.10391982, 7.58618292, 0.41075919, -144.18759817, -0.01088577, -176.91539734, -0.12688935, -17.69153973, -0.43372872, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1122990, 26966099.08092866, 0.08, 0.00106667, 0.00026667, 11235874.61705361, 0.00073242)
    ops.section('Aggregator', 1122991, 1122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1122992, 1122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1122, 1122991, 0.3033711939, 1122992, 0.3033711939, 1122990)
    # Create element
    ops.element('forceBeamColumn', 1122, 122, 222, 1122, 1122)

    # Create geometric transformation
    ops.geomTransf('Linear', 1222, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1222990, 62.03845553, 0.00853404, 75.79163701, 0.08131133, 7.5791637, 0.34996126, -144.66126185, -0.01025903, -176.73092848, -0.09922316, -17.67309285, -0.36787308, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1222991, 62.03845553, 0.00853404, 75.79163701, 0.08089238, 7.5791637, 0.34588833, -144.66126185, -0.01025903, -176.73092848, -0.09871102, -17.67309285, -0.36370697, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1222990, 28711915.01307165, 0.08, 0.00106667, 0.00026667, 11963297.92211319, 0.00073242)
    ops.section('Aggregator', 1222991, 1222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1222992, 1222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1222, 1222991, 0.36757633932, 1222992, 0.36757633932, 1222990)
    # Create element
    ops.element('forceBeamColumn', 1222, 222, 322, 1222, 1222)

    # Create geometric transformation
    ops.geomTransf('Linear', 1032, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1032990, 33.1169938, 0.00982135, 40.14722918, 0.05432026, 4.01472292, 0.25149809, -57.51613649, -0.01064994, -69.72593973, -0.06129905, -6.97259397, -0.25847688, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1032991, 33.05780775, 0.00976437, 40.07547884, 0.05861908, 4.00754788, 0.29132414, -84.97686105, -0.01132277, -103.01615951, -0.07224131, -10.30161595, -0.30494636, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1032990, 31327586.89812392, 0.07, 0.00071458, 0.00023333, 13053161.20755164, 0.00060032)
    ops.section('Aggregator', 1032991, 1032990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1032992, 1032991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1032, 1032991, 0.33272712510999997, 1032992, 0.33272712510999997, 1032990)
    # Create element
    ops.element('forceBeamColumn', 1032, 32, 132, 1032, 1032)

    # Create geometric transformation
    ops.geomTransf('Linear', 1132, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1132990, 32.6015571, 0.01031731, 39.82760719, 0.06968297, 3.98276072, 0.31571093, -83.65875387, -0.01201087, -102.20149844, -0.08603583, -10.22014984, -0.33206379, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1132991, 32.6015571, 0.01031731, 39.82760719, 0.0713075, 3.98276072, 0.33360647, -83.65875387, -0.01201087, -102.20149844, -0.08806152, -10.22014984, -0.35036048, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1132990, 28724407.85201532, 0.07, 0.00071458, 0.00023333, 11968503.27167305, 0.00060032)
    ops.section('Aggregator', 1132991, 1132990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1132992, 1132991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1132, 1132991, 0.26676163501000005, 1132992, 0.26676163501000005, 1132990)
    # Create element
    ops.element('forceBeamColumn', 1132, 132, 232, 1132, 1132)

    # Create geometric transformation
    ops.geomTransf('Linear', 1232, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1232990, 31.74205005, 0.00938296, 38.97188932, 0.06979166, 3.89718893, 0.29358758, -81.45093889, -0.01103943, -100.00289741, -0.086365, -10.00028974, -0.31016093, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1232991, 31.79003554, 0.00945803, 39.03080438, 0.06901663, 3.90308044, 0.29784474, -55.15991088, -0.01033433, -67.72360128, -0.07812452, -6.77236013, -0.30695264, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1232990, 26683285.32375322, 0.07, 0.00071458, 0.00023333, 11118035.55156384, 0.00060032)
    ops.section('Aggregator', 1232991, 1232990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1232992, 1232991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1232, 1232991, 0.32713447373000004, 1232992, 0.32713447373000004, 1232990)
    # Create element
    ops.element('forceBeamColumn', 1232, 232, 332, 1232, 1232)

    # Create geometric transformation
    ops.geomTransf('Linear', 1003, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1003990, 30.58246452, 0.00970504, 37.56918357, 0.04930735, 3.75691836, 0.25865769, -30.58246452, -0.00970504, -37.56918357, -0.04930735, -3.75691836, -0.25865769, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1003991, 30.53574379, 0.00966613, 37.51178926, 0.05056932, 3.75117893, 0.26961016, -45.26325089, -0.01019287, -55.60387001, -0.05500316, -5.560387, -0.27404399, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1003990, 26431141.16087412, 0.07, 0.00071458, 0.00023333, 11012975.48369755, 0.00060032)
    ops.section('Aggregator', 1003991, 1003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1003992, 1003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1003, 1003991, 0.32545449226, 1003992, 0.32545449226, 1003990)
    # Create element
    ops.element('forceBeamColumn', 1003, 3, 103, 1003, 1003)

    # Create geometric transformation
    ops.geomTransf('Linear', 1103, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1103990, 31.40312971, 0.00934276, 37.99557522, 0.06883504, 3.79955752, 0.37686789, -46.58824496, -0.00980628, -56.36849519, -0.07498129, -5.63684952, -0.38301415, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1103991, 31.40312971, 0.00934276, 37.99557522, 0.06553333, 3.79955752, 0.33454794, -46.58824496, -0.00980628, -56.36849519, -0.0713642, -5.63684952, -0.34037881, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1103990, 31911362.07681601, 0.07, 0.00071458, 0.00023333, 13296400.86534001, 0.00060032)
    ops.section('Aggregator', 1103991, 1103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1103992, 1103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1103, 1103991, 0.25793915558999997, 1103992, 0.25793915558999997, 1103990)
    # Create element
    ops.element('forceBeamColumn', 1103, 103, 203, 1103, 1103)

    # Create geometric transformation
    ops.geomTransf('Linear', 1203, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1203990, 31.65815359, 0.00944962, 38.6745285, 0.04641042, 3.86745285, 0.25101369, -46.9551433, -0.00995031, -57.36177955, -0.05044162, -5.73617796, -0.25504489, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1203991, 31.69199226, 0.00949293, 38.7158668, 0.04874323, 3.87158668, 0.29222856, -31.69199226, -0.00949293, -38.7158668, -0.04874323, -3.87158668, -0.29222856, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1203990, 28729964.11972142, 0.07, 0.00071458, 0.00023333, 11970818.38321726, 0.00060032)
    ops.section('Aggregator', 1203991, 1203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1203992, 1203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1203, 1203991, 0.32684216504, 1203992, 0.32684216504, 1203990)
    # Create element
    ops.element('forceBeamColumn', 1203, 203, 303, 1203, 1203)

    # Create geometric transformation
    ops.geomTransf('Linear', 1013, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1013990, 35.33193578, 0.00802303, 43.11356023, 0.09915533, 4.31135602, 0.40676958, -143.20556647, -0.01035407, -174.74564242, -0.13715247, -17.47456424, -0.44476672, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1013991, 35.33193578, 0.00802303, 43.11356023, 0.09320841, 4.31135602, 0.38366382, -143.20556647, -0.01035407, -174.74564242, -0.12887812, -17.47456424, -0.41933353, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1013990, 29148951.62115, 0.08, 0.00106667, 0.00026667, 12145396.5088125, 0.00073242)
    ops.section('Aggregator', 1013991, 1013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1013992, 1013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1013, 1013991, 0.32508247079, 1013992, 0.32508247079, 1013990)
    # Create element
    ops.element('forceBeamColumn', 1013, 13, 113, 1013, 1013)

    # Create geometric transformation
    ops.geomTransf('Linear', 1113, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1113990, 35.73699534, 0.0081989, 43.79144553, 0.10968496, 4.37914455, 0.48576205, -144.73182643, -0.01066045, -177.3516725, -0.15186473, -17.73516725, -0.52794182, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1113991, 35.73699534, 0.0081989, 43.79144553, 0.11568397, 4.37914455, 0.50173894, -144.73182643, -0.01066045, -177.3516725, -0.16021155, -17.73516725, -0.54626652, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1113990, 27520394.68469054, 0.08, 0.00106667, 0.00026667, 11466831.11862106, 0.00073242)
    ops.section('Aggregator', 1113991, 1113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1113992, 1113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1113, 1113991, 0.25903046656, 1113992, 0.25903046656, 1113990)
    # Create element
    ops.element('forceBeamColumn', 1113, 113, 213, 1113, 1113)

    # Create geometric transformation
    ops.geomTransf('Linear', 1213, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1213990, 35.70836743, 0.00799763, 43.53640529, 0.09277354, 4.35364053, 0.39982441, -144.77316149, -0.01031742, -176.51053485, -0.12827177, -17.65105349, -0.43532264, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1213991, 35.70836743, 0.00799763, 43.53640529, 0.09326424, 4.35364053, 0.40031511, -144.77316149, -0.01031742, -176.51053485, -0.12895451, -17.65105349, -0.43600538, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1213990, 29449428.23349611, 0.08, 0.00106667, 0.00026667, 12270595.09729005, 0.00073242)
    ops.section('Aggregator', 1213991, 1213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1213992, 1213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1213, 1213991, 0.32567893223, 1213992, 0.32567893223, 1213990)
    # Create element
    ops.element('forceBeamColumn', 1213, 213, 313, 1213, 1213)

    # Create geometric transformation
    ops.geomTransf('Linear', 1023, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1023990, 52.74931024, 0.009972, 65.07831049, 0.10185271, 6.50783105, 0.37536542, -122.32614939, -0.0123981, -150.91721759, -0.12471454, -15.09172176, -0.39822725, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1023991, 52.74931024, 0.009972, 65.07831049, 0.09446444, 6.50783105, 0.34618266, -122.32614939, -0.0123981, -150.91721759, -0.11568301, -15.09172176, -0.36740122, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1023990, 24280907.01299474, 0.07, 0.00071458, 0.00023333, 10117044.58874781, 0.00060032)
    ops.section('Aggregator', 1023991, 1023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1023992, 1023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1023, 1023991, 0.3656137131, 1023992, 0.3656137131, 1023990)
    # Create element
    ops.element('forceBeamColumn', 1023, 23, 123, 1023, 1023)

    # Create geometric transformation
    ops.geomTransf('Linear', 1123, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1123990, 52.13145219, 0.01080706, 63.69982373, 0.09074014, 6.36998237, 0.38716101, -121.13084646, -0.01311652, -148.01071606, -0.11082799, -14.80107161, -0.40724885, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1123991, 52.13145219, 0.01080706, 63.69982373, 0.09624529, 6.36998237, 0.42618709, -121.13084646, -0.01311652, -148.01071606, -0.11755757, -14.80107161, -0.44749937, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1123990, 28644118.47833657, 0.07, 0.00071458, 0.00023333, 11935049.36597357, 0.00060032)
    ops.section('Aggregator', 1123991, 1123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1123992, 1123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1123, 1123991, 0.30308375624, 1123992, 0.30308375624, 1123990)
    # Create element
    ops.element('forceBeamColumn', 1123, 123, 223, 1123, 1123)

    # Create geometric transformation
    ops.geomTransf('Linear', 1223, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1223990, 52.54301806, 0.01050325, 64.19546746, 0.07834874, 6.41954675, 0.32785629, -122.18103927, -0.01277137, -149.27709178, -0.09570678, -14.92770918, -0.34521433, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1223991, 52.54301806, 0.01050325, 64.19546746, 0.08310605, 6.41954675, 0.35353886, -122.18103927, -0.01277137, -149.27709178, -0.1015222, -14.92770918, -0.371955, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1223990, 28686748.51554016, 0.07, 0.00071458, 0.00023333, 11952811.88147507, 0.00060032)
    ops.section('Aggregator', 1223991, 1223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1223992, 1223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1223, 1223991, 0.36977762150000004, 1223992, 0.36977762150000004, 1223990)
    # Create element
    ops.element('forceBeamColumn', 1223, 223, 323, 1223, 1223)

    # Create geometric transformation
    ops.geomTransf('Linear', 1033, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1033990, 30.45383293, 0.01050186, 37.39966231, 0.05833224, 3.73996623, 0.2930311, -30.45383293, -0.01050186, -37.39966231, -0.05833224, -3.73996623, -0.2930311, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1033991, 30.41521876, 0.01048368, 37.35224113, 0.05614454, 3.73522411, 0.25987002, -44.96408696, -0.01102994, -55.21937656, -0.06105235, -5.52193766, -0.26477783, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1033990, 26570535.04918827, 0.07, 0.00071458, 0.00023333, 11071056.27049511, 0.00060032)
    ops.section('Aggregator', 1033991, 1033990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1033992, 1033991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1033, 1033991, 0.32968040129000004, 1033992, 0.32968040129000004, 1033990)
    # Create element
    ops.element('forceBeamColumn', 1033, 33, 133, 1033, 1033)

    # Create geometric transformation
    ops.geomTransf('Linear', 1133, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1133990, 31.5858823, 0.00987411, 38.68904928, 0.07039264, 3.86890493, 0.36740852, -46.82801496, -0.01039914, -57.35889728, -0.07669843, -5.73588973, -0.37371431, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1133991, 31.5858823, 0.00987411, 38.68904928, 0.06887386, 3.86890493, 0.3485118, -46.82801496, -0.01039914, -57.35889728, -0.07503457, -5.73588973, -0.35467251, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1133990, 27687602.24921979, 0.07, 0.00071458, 0.00023333, 11536500.93717491, 0.00060032)
    ops.section('Aggregator', 1133991, 1133990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1133992, 1133991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1133, 1133991, 0.2611675634, 1133992, 0.2611675634, 1133990)
    # Create element
    ops.element('forceBeamColumn', 1133, 133, 233, 1133, 1133)

    # Create geometric transformation
    ops.geomTransf('Linear', 1233, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1233990, 31.12903443, 0.00950708, 38.33817964, 0.05686271, 3.83381796, 0.2846194, -46.15084918, -0.01004968, -56.83888301, -0.06192875, -5.6838883, -0.28968544, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1233991, 31.16360942, 0.00955864, 38.38076182, 0.05479883, 3.83807618, 0.26567935, -31.16360942, -0.00955864, -38.38076182, -0.05479883, -3.83807618, -0.26567935, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1233990, 25203991.21589882, 0.07, 0.00071458, 0.00023333, 10501663.00662451, 0.00060032)
    ops.section('Aggregator', 1233991, 1233990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1233992, 1233991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1233, 1233991, 0.32565154145, 1233992, 0.32565154145, 1233990)
    # Create element
    ops.element('forceBeamColumn', 1233, 233, 333, 1233, 1233)

    # Create geometric transformation
    ops.geomTransf('Linear', 6200, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6200990, 46.39531396, 0.00996034, 56.81862711, 0.10550949, 5.68186271, 0.45584857, -126.09536715, -0.01261234, -154.42433804, -0.13396456, -15.4424338, -0.48430364, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6200991, 46.39531396, 0.00996034, 56.81862711, 0.11088131, 5.68186271, 0.49523989, -126.09536715, -0.01261234, -154.42433804, -0.14078703, -15.4424338, -0.52514562, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6200990, 27761274.63398799, 0.07, 0.00071458, 0.00023333, 11567197.76416166, 0.00060032)
    ops.section('Aggregator', 6200991, 6200990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6200992, 6200991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6200, 6200991, 0.26017371282, 6200992, 0.26017371282, 6200990)
    # Create element
    ops.element('forceBeamColumn', 6200, 1101, 1201, 6200, 6200)

    # Create geometric transformation
    ops.geomTransf('Linear', 6201, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6201990, 43.12118163, 0.01028354, 52.77142255, 0.10646259, 5.27714225, 0.45816706, -117.09054202, -0.01292311, -143.2946463, -0.13507535, -14.32946463, -0.48677981, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6201991, 43.12118163, 0.01028354, 52.77142255, 0.10942814, 5.27714225, 0.4874025, -117.09054202, -0.01292311, -143.2946463, -0.13884174, -14.32946463, -0.5168161, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6201990, 28046706.94451572, 0.07, 0.00071458, 0.00023333, 11686127.89354822, 0.00060032)
    ops.section('Aggregator', 6201991, 6201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6201992, 6201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6201, 6201991, 0.25670523966000003, 6201992, 0.25670523966000003, 6201990)
    # Create element
    ops.element('forceBeamColumn', 6201, 1102, 1202, 6201, 6201)

    # Create geometric transformation
    ops.geomTransf('Linear', 6202, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6202990, 29.85927212, 0.00972402, 36.6231273, 0.0761182, 3.66231273, 0.33375129, -76.53253473, -0.01136091, -93.86902503, -0.09414997, -9.3869025, -0.35178307, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6202991, 29.85927212, 0.00972402, 36.6231273, 0.07584776, 3.66231273, 0.33099856, -76.53253473, -0.01136091, -93.86902503, -0.09381276, -9.3869025, -0.34896355, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6202990, 27126843.96777715, 0.07, 0.00071458, 0.00023333, 11302851.65324048, 0.00060032)
    ops.section('Aggregator', 6202991, 6202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6202992, 6202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6202, 6202991, 0.25684928939999996, 6202992, 0.25684928939999996, 6202990)
    # Create element
    ops.element('forceBeamColumn', 6202, 1103, 1203, 6202, 6202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 59.92209085, 0.00821295, 73.2521512, 0.07848257, 7.32521512, 0.31278399, -140.05861432, -0.00966973, -171.21556755, -0.09556844, -17.12155675, -0.32986986, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 88.63998794, 0.00849884, 108.358532, 0.07962412, 10.8358532, 0.2903936, -206.35474076, -0.01040735, -252.25970017, -0.09735203, -25.22597002, -0.30812152, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 28473169.1273508, 0.1, 0.00133333, 0.00052083, 11863820.4697295, 0.00127345)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.36227602417000004, 2001992, 0.36227602417000004, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 122.95688815, 0.00691015, 149.81884194, 0.07052712, 14.98188419, 0.29008427, -188.16493469, -0.0074835, -229.27265835, -0.07782028, -22.92726583, -0.29737743, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 122.76700452, 0.00683774, 149.5874751, 0.07328301, 14.95874751, 0.29880786, -277.67604393, -0.0080454, -338.33894107, -0.08852653, -33.83389411, -0.31405138, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 29667041.0600077, 0.125, 0.00260417, 0.00065104, 12361267.10833654, 0.00178813)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.41110217311999997, 2101992, 0.41110217311999997, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 123.90601659, 0.00634315, 151.17630794, 0.07406304, 15.11763079, 0.30299708, -189.21434421, -0.00688881, -230.85824849, -0.0817619, -23.08582485, -0.31069594, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 124.0688146, 0.0062549, 151.37493592, 0.07069642, 15.13749359, 0.25924622, -279.28319988, -0.00740598, -340.75022497, -0.08546009, -34.0750225, -0.27400989, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 29194928.64357661, 0.125, 0.00260417, 0.00065104, 12164553.60149025, 0.00178813)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.40319010895, 2201992, 0.40319010895, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 61.91977989, 0.00814023, 75.81160368, 0.08346804, 7.58116037, 0.33152567, -144.62872884, -0.00962217, -177.0764672, -0.10170409, -17.70764672, -0.34976172, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 91.8265813, 0.00841239, 112.42805452, 0.08722041, 11.24280545, 0.32856949, -213.33244604, -0.01035087, -261.1939978, -0.10668706, -26.11939978, -0.34803614, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 27864157.19194084, 0.1, 0.00133333, 0.00052083, 11610065.49664202, 0.00127345)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.36443708607, 2301992, 0.36443708607, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 99.45714219, 0.0094209, 121.84517539, 0.07663556, 12.18451754, 0.29351588, -231.33752466, -0.01158439, -283.41213757, -0.09374866, -28.34121376, -0.31062898, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 66.99600989, 0.00901442, 82.07696698, 0.07618663, 8.2076967, 0.30137686, -231.05026518, -0.0117134, -283.06021532, -0.10166919, -28.30602153, -0.32685943, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 27614522.81087329, 0.1, 0.00133333, 0.00052083, 11506051.17119721, 0.00127345)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.38091742425, 2011992, 0.38091742425, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 128.43979374, 0.00688557, 157.45411903, 0.06882813, 15.7454119, 0.270906, -289.71905192, -0.00818183, -355.1660802, -0.08320911, -35.51660802, -0.28528698, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 128.381554, 0.00680875, 157.38272303, 0.06938788, 15.7382723, 0.2612049, -381.15292219, -0.00871622, -467.25470223, -0.08958311, -46.72547022, -0.28140014, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 27344012.29851423, 0.125, 0.00260417, 0.00065104, 11393338.45771426, 0.00178813)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.41641967969000004, 2111992, 0.41641967969000004, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 123.49073744, 0.00652438, 150.05064872, 0.07099534, 15.00506487, 0.28952241, -278.94200496, -0.00767371, -338.935775, -0.08576349, -33.8935775, -0.30429055, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 123.41940843, 0.00645954, 149.96397854, 0.07219014, 14.99639785, 0.28416022, -367.09999399, -0.00814888, -446.05444412, -0.09308822, -44.60544441, -0.30505829, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 30602696.89919171, 0.125, 0.00260417, 0.00065104, 12751123.70799655, 0.00178813)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.40722658759, 2211992, 0.40722658759, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 95.98905459, 0.00962104, 118.003033, 0.08349298, 11.8003033, 0.31372116, -223.43061142, -0.01187392, -274.67183551, -0.10217616, -27.46718355, -0.33240434, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 64.78281667, 0.00920055, 79.64000568, 0.08266909, 7.96400057, 0.31898752, -223.3270265, -0.01200702, -274.54449458, -0.11039476, -27.45444946, -0.34671319, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 26098450.88697136, 0.1, 0.00133333, 0.00052083, 10874354.53623807, 0.00127345)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.3790259354, 2311992, 0.3790259354, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)

    # Create geometric transformation
    ops.geomTransf('Linear', 2021, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2021990, 62.36421761, 0.00806919, 76.59138737, 0.08130375, 7.65913874, 0.31056131, -214.61570383, -0.01057792, -263.57605592, -0.1086523, -26.35760559, -0.33790986, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2021991, 62.47348635, 0.00817047, 76.72558362, 0.07837258, 7.67255836, 0.30651901, -145.79526708, -0.00970444, -179.05558998, -0.09552062, -17.905559, -0.32366705, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2021990, 26551080.83256025, 0.1, 0.00133333, 0.00052083, 11062950.3469001, 0.00127345)
    ops.section('Aggregator', 2021991, 2021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2021992, 2021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2021, 2021991, 0.36532574001, 2021992, 0.36532574001, 2021990)
    # Create element
    ops.element('forceBeamColumn', 2021, 21, 31, 2021, 2021)

    # Create geometric transformation
    ops.geomTransf('Linear', 2121, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2121990, 127.42748777, 0.00670527, 155.3771931, 0.07025401, 15.53771931, 0.27701079, -378.79452936, -0.00850131, -461.87860849, -0.09062117, -46.18786085, -0.29737795, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2121991, 127.54033649, 0.0068586, 155.51479384, 0.0640495, 15.55147938, 0.25163286, -195.03297183, -0.00743803, -237.81113679, -0.07066997, -23.78111368, -0.25825332, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2121990, 29415456.23918602, 0.125, 0.00260417, 0.00065104, 12256440.09966084, 0.00178813)
    ops.section('Aggregator', 2121991, 2121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2121992, 2121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2121, 2121991, 0.41433277756000003, 2121992, 0.41433277756000003, 2121990)
    # Create element
    ops.element('forceBeamColumn', 2121, 121, 131, 2121, 2121)

    # Create geometric transformation
    ops.geomTransf('Linear', 2221, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2221990, 124.29864396, 0.00640005, 152.50334329, 0.07910546, 15.25033433, 0.30251075, -368.1176795, -0.00822418, -451.64754063, -0.1021766, -45.16475406, -0.3255819, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2221991, 124.1768687, 0.00657254, 152.35393591, 0.07509536, 15.23539359, 0.30123931, -189.64142301, -0.0071593, -232.67310176, -0.08292013, -23.26731018, -0.30906408, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2221990, 26990876.9163702, 0.125, 0.00260417, 0.00065104, 11246198.71515425, 0.00178813)
    ops.section('Aggregator', 2221991, 2221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2221992, 2221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2221, 2221991, 0.4064696312, 2221992, 0.4064696312, 2221990)
    # Create element
    ops.element('forceBeamColumn', 2221, 221, 231, 2221, 2221)

    # Create geometric transformation
    ops.geomTransf('Linear', 2321, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2321990, 63.12307235, 0.00855734, 77.04354876, 0.08078376, 7.70435488, 0.3172665, -217.87058819, -0.01102981, -265.91740008, -0.10775412, -26.59174001, -0.34423686, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2321991, 63.30169619, 0.00863495, 77.26156436, 0.07405991, 7.72615644, 0.27982296, -147.98376774, -0.01014981, -180.61849972, -0.09012632, -18.06184997, -0.29588938, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2321990, 29063671.63537061, 0.1, 0.00133333, 0.00052083, 12109863.18140442, 0.00127345)
    ops.section('Aggregator', 2321991, 2321990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2321992, 2321991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2321, 2321991, 0.37112294177, 2321992, 0.37112294177, 2321990)
    # Create element
    ops.element('forceBeamColumn', 2321, 321, 331, 2321, 2321)

    # Create geometric transformation
    ops.geomTransf('Linear', 2002, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2002990, 37.40899373, 0.00788166, 45.23114195, 0.06821889, 4.52311419, 0.29692153, -152.37177613, -0.00981013, -184.23241975, -0.09376131, -18.42324198, -0.32246395, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2002991, 73.55135324, 0.00827005, 88.93079892, 0.07283825, 8.89307989, 0.30646979, -224.72420852, -0.01050711, -271.71360579, -0.09471426, -27.17136058, -0.32834579, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2002990, 32111887.52634114, 0.1, 0.00133333, 0.00052083, 13379953.13597547, 0.00127345)
    ops.section('Aggregator', 2002991, 2002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2002992, 2002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2002, 2002991, 0.3285050066, 2002992, 0.3285050066, 2002990)
    # Create element
    ops.element('forceBeamColumn', 2002, 2, 12, 2002, 2002)

    # Create geometric transformation
    ops.geomTransf('Linear', 2102, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2102990, 82.0313097, 0.00653032, 100.64635626, 0.07362981, 10.06463563, 0.30073782, -192.44335902, -0.00758386, -236.11378316, -0.08960734, -23.61137832, -0.31671536, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2102991, 81.91375938, 0.00646415, 100.5021307, 0.07555819, 10.05021307, 0.30110901, -283.61259388, -0.00818968, -347.97169845, -0.10071916, -34.79716985, -0.32626998, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2102990, 26985438.41798908, 0.125, 0.00260417, 0.00065104, 11243932.67416212, 0.00178813)
    ops.section('Aggregator', 2102991, 2102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2102992, 2102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2102, 2102991, 0.37048647636, 2102992, 0.37048647636, 2102990)
    # Create element
    ops.element('forceBeamColumn', 2102, 102, 112, 2102, 2102)

    # Create geometric transformation
    ops.geomTransf('Linear', 2202, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2202990, 80.5874671, 0.00640445, 98.23319071, 0.07369101, 9.82331907, 0.30922776, -189.28563256, -0.00738363, -230.73230008, -0.0896358, -23.07323001, -0.32517254, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2202991, 80.45157103, 0.00634832, 98.06753834, 0.07285364, 9.80675383, 0.28511113, -279.07086385, -0.00794867, -340.17723072, -0.09701138, -34.01772307, -0.30926887, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2202990, 29524135.32539342, 0.125, 0.00260417, 0.00065104, 12301723.05224726, 0.00178813)
    ops.section('Aggregator', 2202991, 2202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2202992, 2202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2202, 2202991, 0.36766580540000005, 2202992, 0.36766580540000005, 2202990)
    # Create element
    ops.element('forceBeamColumn', 2202, 202, 212, 2202, 2202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2302, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2302990, 36.32053971, 0.00814489, 44.36933379, 0.07474483, 4.43693338, 0.30904157, -147.49670706, -0.01023018, -180.18263716, -0.10289509, -18.01826372, -0.33719182, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2302991, 71.05451625, 0.00856976, 86.8005149, 0.08367403, 8.68005149, 0.35469899, -217.16215315, -0.01100347, -265.28625774, -0.10895132, -26.52862577, -0.37997628, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2302990, 28737596.08587859, 0.1, 0.00133333, 0.00052083, 11973998.36911608, 0.00127345)
    ops.section('Aggregator', 2302991, 2302990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2302992, 2302991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2302, 2302991, 0.32801747277, 2302992, 0.32801747277, 2302990)
    # Create element
    ops.element('forceBeamColumn', 2302, 302, 312, 2302, 2302)

    # Create geometric transformation
    ops.geomTransf('Linear', 2012, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2012990, 71.67374822, 0.00826595, 87.67281772, 0.09317859, 8.76728177, 0.36464076, -218.60869308, -0.01066969, -267.4066946, -0.12140919, -26.74066946, -0.39287136, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2012991, 71.67374822, 0.00826595, 87.67281772, 0.0920046, 8.76728177, 0.35464811, -218.60869308, -0.01066969, -267.4066946, -0.11987812, -26.74066946, -0.38252163, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2012990, 28231181.42216064, 0.1, 0.00133333, 0.00052083, 11762992.2592336, 0.00127345)
    ops.section('Aggregator', 2012991, 2012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2012992, 2012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2012, 2012991, 0.32643469200999997, 2012992, 0.32643469200999997, 2012990)
    # Create element
    ops.element('forceBeamColumn', 2012, 12, 22, 2012, 2012)

    # Create geometric transformation
    ops.geomTransf('Linear', 2112, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2112990, 79.38889901, 0.00597359, 96.75328302, 0.06661487, 9.6753283, 0.27523843, -274.75060544, -0.00750128, -334.84559451, -0.08871099, -33.48455945, -0.29733454, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2112991, 118.18860511, 0.00614781, 144.03947783, 0.07445671, 14.40394778, 0.32292624, -362.40280668, -0.00790094, -441.66957544, -0.09698655, -44.16695754, -0.34545607, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2112990, 29592746.05904249, 0.125, 0.00260417, 0.00065104, 12330310.85793437, 0.00178813)
    ops.section('Aggregator', 2112991, 2112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2112992, 2112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2112, 2112991, 0.36177521857, 2112992, 0.36177521857, 2112990)
    # Create element
    ops.element('forceBeamColumn', 2112, 112, 122, 2112, 2112)

    # Create geometric transformation
    ops.geomTransf('Linear', 2212, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2212990, 82.35338666, 0.00643725, 100.55828816, 0.0791827, 10.05582882, 0.32325335, -285.43881615, -0.00808733, -348.53744199, -0.10550672, -34.8537442, -0.34957737, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2212991, 122.41648698, 0.00663025, 149.47767023, 0.07892767, 14.94776702, 0.29490214, -376.24209234, -0.00852716, -459.41353808, -0.10281442, -45.94135381, -0.31878889, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2212990, 28904242.15586885, 0.125, 0.00260417, 0.00065104, 12043434.23161202, 0.00178813)
    ops.section('Aggregator', 2212991, 2212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2212992, 2212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2212, 2212991, 0.37082050768, 2212992, 0.37082050768, 2212990)
    # Create element
    ops.element('forceBeamColumn', 2212, 212, 222, 2212, 2212)

    # Create geometric transformation
    ops.geomTransf('Linear', 2312, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2312990, 72.82405455, 0.00874217, 89.38125325, 0.08602782, 8.93812532, 0.33305546, -222.2583484, -0.01133709, -272.79076737, -0.1121298, -27.27907674, -0.35915744, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2312991, 72.82405455, 0.00874217, 89.38125325, 0.09015253, 8.93812532, 0.36960595, -222.2583484, -0.01133709, -272.79076737, -0.11750908, -27.27907674, -0.3969625, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2312990, 26831162.11786668, 0.1, 0.00133333, 0.00052083, 11179650.88244445, 0.00127345)
    ops.section('Aggregator', 2312991, 2312990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2312992, 2312991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2312, 2312991, 0.33078109494, 2312992, 0.33078109494, 2312990)
    # Create element
    ops.element('forceBeamColumn', 2312, 312, 322, 2312, 2312)

    # Create geometric transformation
    ops.geomTransf('Linear', 2022, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2022990, 69.86567813, 0.00827986, 85.32859935, 0.08151805, 8.53285993, 0.32187987, -213.43322641, -0.01063879, -260.67102978, -0.10615296, -26.06710298, -0.34651478, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2022991, 35.65279759, 0.00787293, 43.54360199, 0.07809955, 4.3543602, 0.32823015, -144.89436872, -0.00989653, -176.9629075, -0.10760748, -17.69629075, -0.35773808, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2022990, 28823579.45650716, 0.1, 0.00133333, 0.00052083, 12009824.77354465, 0.00127345)
    ops.section('Aggregator', 2022991, 2022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2022992, 2022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2022, 2022991, 0.32487272411, 2022992, 0.32487272411, 2022990)
    # Create element
    ops.element('forceBeamColumn', 2022, 22, 32, 2022, 2022)

    # Create geometric transformation
    ops.geomTransf('Linear', 2122, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2122990, 126.75229848, 0.00655554, 155.8405752, 0.07479563, 15.58405752, 0.28855781, -386.98792665, -0.0085854, -475.79745541, -0.09758127, -47.57974554, -0.31134345, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2122991, 85.05554339, 0.00644839, 104.5748674, 0.07102291, 10.45748674, 0.2964287, -199.01074211, -0.00752716, -244.68154734, -0.0864641, -24.46815473, -0.31186988, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2122990, 26040711.70201505, 0.125, 0.00260417, 0.00065104, 10850296.54250627, 0.00178813)
    ops.section('Aggregator', 2122991, 2122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2122992, 2122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2122, 2122991, 0.37248929003000003, 2122992, 0.37248929003000003, 2122990)
    # Create element
    ops.element('forceBeamColumn', 2122, 122, 132, 2122, 2122)

    # Create geometric transformation
    ops.geomTransf('Linear', 2222, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2222990, 121.08643349, 0.00629022, 147.18547344, 0.07986555, 14.71854734, 0.32130124, -371.56131697, -0.00805154, -451.64785826, -0.1040054, -45.16478583, -0.34544109, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2222991, 81.39854273, 0.00617477, 98.94323174, 0.07385768, 9.89432317, 0.31193532, -191.02457952, -0.00711479, -232.19812795, -0.08985146, -23.21981279, -0.3279291, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2222990, 30478293.64552809, 0.125, 0.00260417, 0.00065104, 12699289.01897004, 0.00178813)
    ops.section('Aggregator', 2222991, 2222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2222992, 2222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2222, 2222991, 0.36574280011000004, 2222992, 0.36574280011000004, 2222990)
    # Create element
    ops.element('forceBeamColumn', 2222, 222, 232, 2222, 2222)

    # Create geometric transformation
    ops.geomTransf('Linear', 2322, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2322990, 69.07537415, 0.00823272, 84.89982577, 0.0870592, 8.48998258, 0.33336795, -210.65258762, -0.0107184, -258.9109101, -0.1135206, -25.89109101, -0.35982935, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2322991, 35.22141218, 0.00781975, 43.29027232, 0.0811303, 4.32902723, 0.31952891, -142.99686624, -0.00994881, -175.75596481, -0.11195063, -17.57559648, -0.35034924, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2322990, 26193128.89939575, 0.1, 0.00133333, 0.00052083, 10913803.70808156, 0.00127345)
    ops.section('Aggregator', 2322991, 2322990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2322992, 2322991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2322, 2322991, 0.32358335645, 2322992, 0.32358335645, 2322990)
    # Create element
    ops.element('forceBeamColumn', 2322, 322, 332, 2322, 2322)

    # Create geometric transformation
    ops.geomTransf('Linear', 2003, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2003990, 36.14951125, 0.00803058, 44.41542483, 0.09908281, 4.44154248, 0.40521794, -146.28145009, -0.01053544, -179.73003026, -0.13722243, -17.97300303, -0.44335756, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2003991, 36.14951125, 0.00803058, 44.41542483, 0.09787665, 4.44154248, 0.40401179, -146.28145009, -0.01053544, -179.73003026, -0.13554422, -17.97300303, -0.44167935, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2003990, 26355157.00350049, 0.08, 0.00106667, 0.00026667, 10981315.4181252, 0.00073242)
    ops.section('Aggregator', 2003991, 2003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2003992, 2003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2003, 2003991, 0.3266531324, 2003992, 0.3266531324, 2003990)
    # Create element
    ops.element('forceBeamColumn', 2003, 3, 13, 2003, 2003)

    # Create geometric transformation
    ops.geomTransf('Linear', 2103, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2103990, 71.40256334, 0.00734517, 87.35584886, 0.069286, 8.73558489, 0.28254849, -167.30313307, -0.00857064, -204.68322877, -0.08428809, -20.46832288, -0.29755058, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2103991, 71.40256334, 0.00734517, 87.35584886, 0.07077044, 8.73558489, 0.29635643, -167.30313307, -0.00857064, -204.68322877, -0.08610269, -20.46832288, -0.31168869, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2103990, 28164960.19944092, 0.1125, 0.00189844, 0.00058594, 11735400.08310038, 0.00152995)
    ops.section('Aggregator', 2103991, 2103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2103992, 2103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2103, 2103991, 0.36823405506, 2103992, 0.36823405506, 2103990)
    # Create element
    ops.element('forceBeamColumn', 2103, 103, 113, 2103, 2103)

    # Create geometric transformation
    ops.geomTransf('Linear', 2203, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2203990, 71.29692522, 0.00723303, 87.19485141, 0.07451517, 8.71948514, 0.30333567, -167.03028745, -0.00844141, -204.2750238, -0.09068818, -20.42750238, -0.31950867, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2203991, 71.29692522, 0.00723303, 87.19485141, 0.07642863, 8.71948514, 0.32098777, -167.03028745, -0.00844141, -204.2750238, -0.09302722, -20.42750238, -0.33758636, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2203990, 28307310.01898805, 0.1125, 0.00189844, 0.00058594, 11794712.50791169, 0.00152995)
    ops.section('Aggregator', 2203991, 2203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2203992, 2203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2203, 2203991, 0.36691973483, 2203992, 0.36691973483, 2203990)
    # Create element
    ops.element('forceBeamColumn', 2203, 203, 213, 2203, 2203)

    # Create geometric transformation
    ops.geomTransf('Linear', 2303, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2303990, 36.02533363, 0.00813871, 43.5998812, 0.0826719, 4.35998812, 0.38213084, -146.15330805, -0.01037992, -176.88293838, -0.11408287, -17.68829384, -0.41354182, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2303991, 36.02533363, 0.00813871, 43.5998812, 0.08297773, 4.35998812, 0.38535961, -146.15330805, -0.01037992, -176.88293838, -0.11450839, -17.68829384, -0.41689028, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2303990, 31831834.62288607, 0.08, 0.00106667, 0.00026667, 13263264.42620253, 0.00073242)
    ops.section('Aggregator', 2303991, 2303990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2303992, 2303991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2303, 2303991, 0.32731660125, 2303992, 0.32731660125, 2303990)
    # Create element
    ops.element('forceBeamColumn', 2303, 303, 313, 2303, 2303)

    # Create geometric transformation
    ops.geomTransf('Linear', 2013, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2013990, 37.10821355, 0.00827632, 45.69534221, 0.0897842, 4.56953422, 0.38467005, -150.05093827, -0.01092331, -184.77389013, -0.12433062, -18.47738901, -0.41921647, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2013991, 37.10821355, 0.00827632, 45.69534221, 0.08967566, 4.56953422, 0.38363087, -150.05093827, -0.01092331, -184.77389013, -0.1241796, -18.47738901, -0.41813482, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2013990, 25278768.53482057, 0.08, 0.00106667, 0.00026667, 10532820.22284191, 0.00073242)
    ops.section('Aggregator', 2013991, 2013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2013992, 2013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2013, 2013991, 0.33018905892, 2013992, 0.33018905892, 2013990)
    # Create element
    ops.element('forceBeamColumn', 2013, 13, 23, 2013, 2013)

    # Create geometric transformation
    ops.geomTransf('Linear', 2113, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2113990, 73.65487512, 0.00741375, 89.90390151, 0.07016781, 8.99039015, 0.2893797, -172.58622183, -0.00863636, -210.66052538, -0.08534792, -21.06605254, -0.30455981, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2113991, 109.27037736, 0.00765319, 133.37655149, 0.0734056, 13.33765515, 0.29067731, -254.71207694, -0.00924951, -310.90419258, -0.08962631, -31.09041926, -0.30689802, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2113990, 29039336.91058471, 0.1125, 0.00189844, 0.00058594, 12099723.71274363, 0.00152995)
    ops.section('Aggregator', 2113991, 2113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2113992, 2113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2113, 2113991, 0.37189727449, 2113992, 0.37189727449, 2113990)
    # Create element
    ops.element('forceBeamColumn', 2113, 113, 123, 2113, 2113)

    # Create geometric transformation
    ops.geomTransf('Linear', 2213, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2213990, 71.11094212, 0.00709354, 87.31570216, 0.06784659, 8.73157022, 0.27309915, -166.37096833, -0.00832929, -204.28358122, -0.08259478, -20.42835812, -0.28784734, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2213991, 105.61474101, 0.00732137, 129.68222604, 0.07597895, 12.9682226, 0.31939672, -245.63306976, -0.00893622, -301.60792872, -0.09286435, -30.16079287, -0.33628211, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2213990, 26642713.50406478, 0.1125, 0.00189844, 0.00058594, 11101130.62669366, 0.00152995)
    ops.section('Aggregator', 2213991, 2213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2213992, 2213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2213, 2213991, 0.36494510625, 2213992, 0.36494510625, 2213990)
    # Create element
    ops.element('forceBeamColumn', 2213, 213, 223, 2213, 2213)

    # Create geometric transformation
    ops.geomTransf('Linear', 2313, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2313990, 34.9695518, 0.0077737, 42.86677844, 0.0838919, 4.28667784, 0.36574378, -141.60873986, -0.01014103, -173.58845522, -0.11604931, -17.35884552, -0.39790119, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2313991, 34.9695518, 0.0077737, 42.86677844, 0.08856971, 4.28667784, 0.3985504, -141.60873986, -0.01014103, -173.58845522, -0.12255786, -17.35884552, -0.43253855, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2313990, 27366930.71312473, 0.08, 0.00106667, 0.00026667, 11402887.7971353, 0.00073242)
    ops.section('Aggregator', 2313991, 2313990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2313992, 2313991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2313, 2313991, 0.32260074701, 2313992, 0.32260074701, 2313990)
    # Create element
    ops.element('forceBeamColumn', 2313, 313, 323, 2313, 2313)

    # Create geometric transformation
    ops.geomTransf('Linear', 2023, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2023990, 38.58609155, 0.00827379, 47.23019096, 0.09349707, 4.7230191, 0.39369466, -156.16219778, -0.01078822, -191.14582812, -0.12936501, -19.11458281, -0.4295626, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2023991, 38.58609155, 0.00827379, 47.23019096, 0.09560871, 4.7230191, 0.3958063, -156.16219778, -0.01078822, -191.14582812, -0.13230308, -19.11458281, -0.43250067, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2023990, 27972630.98987204, 0.08, 0.00106667, 0.00026667, 11655262.91244668, 0.00073242)
    ops.section('Aggregator', 2023991, 2023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2023992, 2023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2023, 2023991, 0.33311392684999996, 2023992, 0.33311392684999996, 2023990)
    # Create element
    ops.element('forceBeamColumn', 2023, 23, 33, 2023, 2023)

    # Create geometric transformation
    ops.geomTransf('Linear', 2123, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2123990, 105.78444039, 0.00759354, 129.27907414, 0.08271041, 12.92790741, 0.32556671, -246.75863667, -0.00918183, -301.56351887, -0.10100589, -30.15635189, -0.34386219, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2123991, 71.38302457, 0.00735069, 87.23713329, 0.07591408, 8.72371333, 0.29633376, -167.28674015, -0.0085657, -204.44098209, -0.09237869, -20.44409821, -0.31279836, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2123990, 28584752.64914077, 0.1125, 0.00189844, 0.00058594, 11910313.60380865, 0.00152995)
    ops.section('Aggregator', 2123991, 2123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2123992, 2123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2123, 2123991, 0.36831568028, 2123992, 0.36831568028, 2123990)
    # Create element
    ops.element('forceBeamColumn', 2123, 123, 133, 2123, 2123)

    # Create geometric transformation
    ops.geomTransf('Linear', 2223, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2223990, 106.12282588, 0.0073023, 130.01292827, 0.0784093, 13.00129283, 0.30547437, -246.90523592, -0.00888115, -302.48791869, -0.09580348, -30.24879187, -0.32286855, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2223991, 71.44730809, 0.00707679, 87.53134554, 0.07423155, 8.75313455, 0.29768195, -167.21633886, -0.00828592, -204.8596585, -0.09037697, -20.48596585, -0.31382737, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2223990, 27609427.88284411, 0.1125, 0.00189844, 0.00058594, 11503928.28451838, 0.00152995)
    ops.section('Aggregator', 2223991, 2223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2223992, 2223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2223, 2223991, 0.36529909123, 2223992, 0.36529909123, 2223990)
    # Create element
    ops.element('forceBeamColumn', 2223, 223, 233, 2223, 2223)

    # Create geometric transformation
    ops.geomTransf('Linear', 2323, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2323990, 36.42161409, 0.00816838, 44.21874889, 0.09038745, 4.42187489, 0.39498494, -147.7468532, -0.01046772, -179.37648192, -0.12486456, -17.93764819, -0.42946205, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2323991, 36.42161409, 0.00816838, 44.21874889, 0.09170799, 4.42187489, 0.39630548, -147.7468532, -0.01046772, -179.37648192, -0.12670192, -17.93764819, -0.4312994, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2323990, 30865800.3903298, 0.08, 0.00106667, 0.00026667, 12860750.16263742, 0.00073242)
    ops.section('Aggregator', 2323991, 2323990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2323992, 2323991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2323, 2323991, 0.32830211941, 2323992, 0.32830211941, 2323990)
    # Create element
    ops.element('forceBeamColumn', 2323, 323, 333, 2323, 2323)
