import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 31.41229318, 0.00964839, 38.52960048, 0.05803681, 3.85296005, 0.29480718, -31.41229318, -0.00964839, -38.52960048, -0.05803681, -3.85296005, -0.29480718, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 31.37247596, 0.00960442, 38.48076158, 0.0591294, 3.84807616, 0.30156705, -46.52033934, -0.01012693, -57.06078441, -0.06438257, -5.70607844, -0.30682021, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 27108392.55636441, 0.07, 0.00071458, 0.00023333, 11295163.56515184, 0.00060032)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.3270077669, 1001992, 0.3270077669, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 31.29919716, 0.00966518, 38.15786649, 0.07014766, 3.81578665, 0.3722877, -46.41105698, -0.01016143, -56.58122498, -0.07642123, -5.6581225, -0.37856127, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 31.29919716, 0.00966518, 38.15786649, 0.07076262, 3.81578665, 0.38024063, -46.41105698, -0.01016143, -56.58122498, -0.07709493, -5.6581225, -0.38657295, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 29475256.65331643, 0.07, 0.00071458, 0.00023333, 12281356.93888185, 0.00060032)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.25945874472999997, 1101992, 0.25945874472999997, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 30.98682978, 0.00974674, 37.92260133, 0.05785809, 3.79226013, 0.29402503, -45.93515246, -0.01025937, -56.21680197, -0.06296635, -5.6216802, -0.29913329, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 31.03287298, 0.00978161, 37.97895035, 0.05751802, 3.79789504, 0.29674159, -31.03287298, -0.00978161, -37.97895035, -0.05751802, -3.79789504, -0.29674159, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 28034973.82473626, 0.07, 0.00071458, 0.00023333, 11681239.09364011, 0.00060032)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32710611162, 1201992, 0.32710611162, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 53.70872065, 0.01024298, 65.48265145, 0.07693043, 6.54826515, 0.28962046, -82.07779808, -0.01116252, -100.0707479, -0.08489412, -10.00707479, -0.29758414, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 53.70872065, 0.01024298, 65.48265145, 0.07750955, 6.54826515, 0.29460699, -82.07779808, -0.01116252, -100.0707479, -0.08553441, -10.00707479, -0.30263185, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 29450345.26958932, 0.07, 0.00071458, 0.00023333, 12270977.19566222, 0.00060032)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.36884514646000005, 1011992, 0.36884514646000005, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 54.16114993, 0.01042681, 66.17892873, 0.09324832, 6.61789287, 0.35430282, -82.76049733, -0.01137576, -101.12416486, -0.10294564, -10.11241649, -0.36400014, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 54.16114993, 0.01042681, 66.17892873, 0.09376176, 6.61789287, 0.35867146, -82.76049733, -0.01137576, -101.12416486, -0.10351331, -10.11241649, -0.36842301, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 28649820.16353298, 0.07, 0.00071458, 0.00023333, 11937425.06813874, 0.00060032)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.3028762984, 1111992, 0.3028762984, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 52.34994898, 0.01033291, 64.07018452, 0.07950578, 6.40701845, 0.29390947, -79.98651639, -0.01127883, -97.89409472, -0.08775837, -9.78940947, -0.30216207, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 52.34994898, 0.01033291, 64.07018452, 0.08001259, 6.40701845, 0.29816134, -79.98651639, -0.01127883, -97.89409472, -0.08831872, -9.78940947, -0.30646747, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 28017811.11938082, 0.07, 0.00071458, 0.00023333, 11674087.96640867, 0.00060032)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.36696454876, 1211992, 0.36696454876, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 31.70831596, 0.00956259, 38.86421546, 0.06036443, 3.88642155, 0.30526801, -31.70831596, -0.00956259, -38.86421546, -0.06036443, -3.88642155, -0.30526801, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 31.67460701, 0.00951589, 38.8228991, 0.06032844, 3.88228991, 0.29777574, -46.97257773, -0.01003396, -57.57329982, -0.06570015, -5.75732998, -0.30314745, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 27419150.79497631, 0.07, 0.00071458, 0.00023333, 11424646.16457346, 0.00060032)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.32714542541999997, 1021992, 0.32714542541999997, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 31.19029256, 0.00945126, 38.11106755, 0.0739093, 3.81110676, 0.38506045, -46.25789731, -0.00994967, -56.52200427, -0.08056478, -5.65220043, -0.39171593, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 31.19029256, 0.00945126, 38.11106755, 0.07355443, 3.81110676, 0.38065745, -46.25789731, -0.00994967, -56.52200427, -0.08017601, -5.65220043, -0.38727904, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 28649985.75818833, 0.07, 0.00071458, 0.00023333, 11937494.06591181, 0.00060032)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.2578385025, 1121992, 0.2578385025, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 30.94836567, 0.00937536, 37.8921831, 0.06094028, 3.78921831, 0.30643486, -45.89655155, -0.00987881, -56.19426092, -0.06636924, -5.61942609, -0.31186381, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 30.98526592, 0.00941799, 37.93736259, 0.05969285, 3.79373626, 0.29824609, -30.98526592, -0.00941799, -37.93736259, -0.05969285, -3.79373626, -0.29824609, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 27858930.99828696, 0.07, 0.00071458, 0.00023333, 11607887.9159529, 0.00060032)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.32476270961000003, 1221992, 0.32476270961000003, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 36.35083127, 0.00812227, 44.44776906, 0.09857913, 4.44477691, 0.40366853, -147.29970985, -0.01053551, -180.10986975, -0.13639412, -18.01098697, -0.44148352, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 53.9968128, 0.00842327, 66.02429108, 0.10000821, 6.60242911, 0.40509761, -147.41216194, -0.01045682, -180.2473699, -0.12677429, -18.02473699, -0.43186369, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 28382620.45334285, 0.08, 0.00106667, 0.00026667, 11826091.85555952, 0.00073242)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.3277727797, 2001992, 0.3277727797, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 81.5866225, 0.00653239, 100.04909508, 0.07914208, 10.00490951, 0.32350083, -191.45196185, -0.00757914, -234.77617955, -0.09633837, -23.47761795, -0.34069712, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 121.11383342, 0.00673932, 148.52103278, 0.08243852, 14.85210328, 0.32465652, -282.68039313, -0.00810616, -346.64895618, -0.10064207, -34.66489562, -0.34286007, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 27207609.17176319, 0.125, 0.00260417, 0.00065104, 11336503.821568, 0.00178813)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.37005526952, 2101992, 0.37005526952, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 81.20307816, 0.00647233, 99.0966927, 0.07890566, 9.90966927, 0.32972627, -190.70787903, -0.00746928, -232.73157264, -0.09601295, -23.27315726, -0.34683356, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 120.51367749, 0.00667562, 147.06963251, 0.0820008, 14.70696325, 0.32914154, -281.58781052, -0.0079758, -343.63747482, -0.10005451, -34.36374748, -0.34719524, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 29115299.28399481, 0.125, 0.00260417, 0.00065104, 12131374.7016645, 0.00178813)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.36913198939, 2201992, 0.36913198939, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 35.64245277, 0.00818857, 43.55458685, 0.09840018, 4.35545869, 0.4044039, -144.40110342, -0.01058552, -176.45616146, -0.13610291, -17.64561615, -0.44210663, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 52.86851612, 0.00848853, 64.60459925, 0.10056578, 6.46045992, 0.4065695, -144.44371451, -0.0105108, -176.50823161, -0.12745354, -17.65082316, -0.43345726, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 28619800.39311868, 0.08, 0.00106667, 0.00026667, 11924916.83046612, 0.00073242)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.32679341207, 2301992, 0.32679341207, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 52.80725601, 0.0086236, 64.3009331, 0.09910992, 6.43009331, 0.40427139, -144.36100691, -0.01061388, -175.78166618, -0.12553606, -17.57816662, -0.43069753, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 35.651577, 0.00832602, 43.41126279, 0.09747791, 4.34112628, 0.40263937, -144.37440528, -0.01068242, -175.79798074, -0.13472534, -17.57979807, -0.43988681, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 29897464.38024795, 0.08, 0.00106667, 0.00026667, 12457276.82510331, 0.00073242)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.3276953736, 2011992, 0.3276953736, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 122.24368273, 0.00665052, 149.97374987, 0.08349201, 14.99737499, 0.32964106, -284.94177977, -0.00801387, -349.57869604, -0.10194613, -34.9578696, -0.34809519, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 82.25861102, 0.00645016, 100.91836305, 0.07928879, 10.0918363, 0.32074228, -192.88726304, -0.007495, -236.64229918, -0.0965341, -23.66422992, -0.33798759, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 27015000.95574339, 0.125, 0.00260417, 0.00065104, 11256250.39822641, 0.00178813)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.36973135446, 2111992, 0.36973135446, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 122.47951955, 0.00659617, 149.67990454, 0.08248728, 14.96799045, 0.33154816, -285.68052558, -0.00790582, -349.12476759, -0.10067631, -34.91247676, -0.34973719, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 82.41118679, 0.00639986, 100.71315283, 0.07821743, 10.07131528, 0.32156013, -193.35988265, -0.0074048, -236.3014558, -0.09519574, -23.63014558, -0.33853844, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 28590364.30610924, 0.125, 0.00260417, 0.00065104, 11912651.79421218, 0.00178813)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.36947205487, 2211992, 0.36947205487, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 52.9956334, 0.00845066, 64.88721564, 0.10164804, 6.48872156, 0.40779391, -144.71557693, -0.01050164, -177.18801048, -0.12886701, -17.71880105, -0.43501287, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 35.70747191, 0.00814791, 43.7197988, 0.10102353, 4.37197988, 0.40716939, -144.6428983, -0.0105802, -177.09902365, -0.1398042, -17.70990236, -0.44595006, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 27852293.78754448, 0.08, 0.00106667, 0.00026667, 11605122.41147687, 0.00073242)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.32664168215, 2311992, 0.32664168215, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)
