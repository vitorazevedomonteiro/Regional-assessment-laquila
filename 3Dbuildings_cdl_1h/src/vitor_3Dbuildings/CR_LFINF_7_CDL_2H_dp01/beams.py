import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 31.52032709, 0.00966944, 38.43167321, 0.06992498, 3.84316732, 0.30523971, -54.71335414, -0.01050587, -66.71014995, -0.07908934, -6.671015, -0.31440406, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 31.45457531, 0.00961654, 38.35150428, 0.07207393, 3.83515043, 0.31438036, -80.79639752, -0.01119204, -98.51232627, -0.08907219, -9.85123263, -0.33137863, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 29436362.02808156, 0.07, 0.00071458, 0.00023333, 12265150.84503398, 0.00060032)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.32813088878999996, 1001992, 0.32813088878999996, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 30.71959861, 0.00976967, 37.52167606, 0.09027989, 3.75216761, 0.39186903, -78.81328331, -0.01136765, -96.26448976, -0.11175847, -9.62644898, -0.41334761, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 30.71959861, 0.00976967, 37.52167606, 0.08986681, 3.75216761, 0.3877983, -78.81328331, -0.01136765, -96.26448976, -0.11124338, -9.62644898, -0.40917488, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 28792694.96131144, 0.07, 0.00071458, 0.00023333, 11996956.23387977, 0.00060032)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.25924957769999996, 1101992, 0.25924957769999996, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 30.39980444, 0.0095642, 37.17036318, 0.07628767, 3.71703632, 0.32165636, -78.02469537, -0.0111497, -95.40213554, -0.09434937, -9.54021355, -0.33971807, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 30.46857917, 0.009612, 37.25445522, 0.0739847, 3.72544552, 0.31228618, -52.85747841, -0.0104531, -64.62974698, -0.08372276, -6.4629747, -0.32202424, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 28391160.50611595, 0.07, 0.00071458, 0.00023333, 11829650.21088164, 0.00060032)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32533001263, 1201992, 0.32533001263, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 36.2045248, 0.00810714, 44.23864273, 0.08909697, 4.42386427, 0.36576122, -147.03587926, -0.01018815, -179.66449683, -0.12287465, -17.96644968, -0.39953891, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 53.67824426, 0.00837695, 65.58994168, 0.0895961, 6.55899417, 0.36206347, -147.0285865, -0.01013437, -179.65558574, -0.11328677, -17.96555857, -0.38575414, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 28643652.82535815, 0.1, 0.00133333, 0.00052083, 11934855.34389923, 0.00127345)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.32753290378000005, 1011992, 0.32753290378000005, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 53.7290909, 0.0082732, 65.76903761, 0.11393337, 6.57690376, 0.46666621, -147.12061594, -0.01004168, -180.08831271, -0.14423541, -18.00883127, -0.49696825, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 53.7290909, 0.0082732, 65.76903761, 0.11404643, 6.57690376, 0.46767527, -147.12061594, -0.01004168, -180.08831271, -0.14437901, -18.00883127, -0.49800784, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 27951374.46096892, 0.1, 0.00133333, 0.00052083, 11646406.02540372, 0.00127345)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.25883853327000006, 1111992, 0.25883853327000006, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 52.20134112, 0.00844113, 63.71668832, 0.09211396, 6.37166883, 0.3759311, -142.90158167, -0.0101776, -174.42493516, -0.1164463, -17.44249352, -0.40026345, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 35.30027309, 0.00817368, 43.08733167, 0.09066403, 4.30873317, 0.37116046, -142.97140466, -0.01022637, -174.51016075, -0.12500065, -17.45101608, -0.40549708, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 29043978.97606294, 0.1, 0.00133333, 0.00052083, 12101657.90669289, 0.00127345)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.32597906311999997, 1211992, 0.32597906311999997, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 30.78943519, 0.00959103, 37.55663268, 0.07104798, 3.75566327, 0.30865353, -53.4297395, -0.01041872, -65.17304029, -0.08036963, -6.51730403, -0.31797519, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 30.72237872, 0.00954308, 37.47483788, 0.07246873, 3.74748379, 0.31011392, -78.88676606, -0.01110198, -96.2252564, -0.08956601, -9.62252564, -0.32721121, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 29283224.30088076, 0.07, 0.00071458, 0.00023333, 12201343.45870032, 0.00060032)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.32601117949, 1021992, 0.32601117949, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 31.63066923, 0.00956064, 38.63121794, 0.09083137, 3.86312179, 0.39509524, -81.24736223, -0.01115499, -99.22915427, -0.11249411, -9.92291543, -0.41675799, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 31.63066923, 0.00956064, 38.63121794, 0.0901946, 3.86312179, 0.38883392, -81.24736223, -0.01115499, -99.22915427, -0.11170011, -9.92291543, -0.41033943, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 28824195.69846492, 0.07, 0.00071458, 0.00023333, 12010081.54102705, 0.00060032)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.26015632072, 1121992, 0.26015632072, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 31.33152153, 0.00922153, 38.25497482, 0.07432441, 3.82549748, 0.31682656, -80.47316304, -0.010771, -98.25564401, -0.0919499, -9.8255644, -0.33445205, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 31.38242612, 0.00928612, 38.317128, 0.07253027, 3.8317128, 0.31193494, -54.48092863, -0.01010779, -66.51980022, -0.08209293, -6.65198002, -0.3214976, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 28929762.98077119, 0.07, 0.00071458, 0.00023333, 12054067.90865466, 0.00060032)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.32542402849, 1221992, 0.32542402849, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 1002, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1002990, 30.12994872, 0.00977318, 36.74155398, 0.05893909, 3.6741554, 0.30330872, -30.12994872, -0.00977318, -36.74155398, -0.05893909, -3.6741554, -0.30330872, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1002991, 30.08754665, 0.00974999, 36.68984736, 0.05918918, 3.66898474, 0.29913479, -44.56322766, -0.01024024, -54.34201863, -0.06440189, -5.43420186, -0.3043475, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1002990, 29386806.03468633, 0.07, 0.00071458, 0.00023333, 12244502.51445264, 0.00060032)
    ops.section('Aggregator', 1002991, 1002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1002992, 1002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1002, 1002991, 0.3251695635, 1002992, 0.3251695635, 1002990)
    # Create element
    ops.element('forceBeamColumn', 1002, 2, 102, 1002, 1002)

    # Create geometric transformation
    ops.geomTransf('Linear', 1102, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1102990, 31.0849637, 0.00943566, 37.95643282, 0.07118097, 3.79564328, 0.37472317, -46.10179222, -0.00993005, -56.29279791, -0.0775733, -5.62927979, -0.38111551, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1102991, 31.0849637, 0.00943566, 37.95643282, 0.07185472, 3.79564328, 0.38331269, -46.10179222, -0.00993005, -56.29279791, -0.07831141, -5.62927979, -0.38976938, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1102990, 28905420.20168112, 0.07, 0.00071458, 0.00023333, 12043925.0840338, 0.00060032)
    ops.section('Aggregator', 1102991, 1102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1102992, 1102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1102, 1102991, 0.25754016383, 1102992, 0.25754016383, 1102990)
    # Create element
    ops.element('forceBeamColumn', 1102, 102, 202, 1102, 1102)

    # Create geometric transformation
    ops.geomTransf('Linear', 1202, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1202990, 30.49231407, 0.00927412, 37.37048378, 0.05915742, 3.73704838, 0.2980681, -45.2179292, -0.00977596, -55.4177648, -0.06442414, -5.54177648, -0.30333481, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1202991, 30.52938261, 0.0093168, 37.41591389, 0.05933051, 3.74159139, 0.30739803, -30.52938261, -0.0093168, -37.41591389, -0.05933051, -3.74159139, -0.30739803, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1202990, 27456101.43516937, 0.07, 0.00071458, 0.00023333, 11440042.26465391, 0.00060032)
    ops.section('Aggregator', 1202991, 1202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1202992, 1202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1202, 1202991, 0.3231087094, 1202992, 0.3231087094, 1202990)
    # Create element
    ops.element('forceBeamColumn', 1202, 202, 302, 1202, 1202)

    # Create geometric transformation
    ops.geomTransf('Linear', 1012, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1012990, 35.80155112, 0.0081758, 43.7833097, 0.09961986, 4.37833097, 0.40540229, -145.04950826, -0.01059019, -177.38749699, -0.13782237, -17.7387497, -0.4436048, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1012991, 35.80155112, 0.0081758, 43.7833097, 0.10007905, 4.37833097, 0.40586148, -145.04950826, -0.01059019, -177.38749699, -0.13846127, -17.7387497, -0.44424371, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1012990, 28319202.58833287, 0.08, 0.00106667, 0.00026667, 11799667.7451387, 0.00073242)
    ops.section('Aggregator', 1012991, 1012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1012992, 1012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1012, 1012991, 0.32702990144, 1012992, 0.32702990144, 1012990)
    # Create element
    ops.element('forceBeamColumn', 1012, 12, 112, 1012, 1012)

    # Create geometric transformation
    ops.geomTransf('Linear', 1112, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1112990, 36.76810334, 0.00828949, 45.01006532, 0.12175277, 4.50100653, 0.50382556, -148.95655984, -0.0107701, -182.34675928, -0.16863908, -18.23467593, -0.55071186, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1112991, 36.76810334, 0.00828949, 45.01006532, 0.12208413, 4.50100653, 0.50415691, -148.95655984, -0.0107701, -182.34675928, -0.16910011, -18.23467593, -0.5511729, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1112990, 27926998.09942062, 0.08, 0.00106667, 0.00026667, 11636249.20809192, 0.00073242)
    ops.section('Aggregator', 1112991, 1112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1112992, 1112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1112, 1112991, 0.26173023608, 1112992, 0.26173023608, 1112990)
    # Create element
    ops.element('forceBeamColumn', 1112, 112, 212, 1112, 1112)

    # Create geometric transformation
    ops.geomTransf('Linear', 1212, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1212990, 34.98122999, 0.00801292, 42.68896401, 0.09725468, 4.2688964, 0.40561444, -141.75486377, -0.01033529, -172.98900812, -0.13450324, -17.29890081, -0.442863, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1212991, 34.98122999, 0.00801292, 42.68896401, 0.09754356, 4.2688964, 0.40590332, -141.75486377, -0.01033529, -172.98900812, -0.13490519, -17.29890081, -0.44326495, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1212990, 29120433.77464605, 0.08, 0.00106667, 0.00026667, 12133514.07276919, 0.00073242)
    ops.section('Aggregator', 1212991, 1212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1212992, 1212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1212, 1212991, 0.32429652955, 1212992, 0.32429652955, 1212990)
    # Create element
    ops.element('forceBeamColumn', 1212, 212, 312, 1212, 1212)

    # Create geometric transformation
    ops.geomTransf('Linear', 1022, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1022990, 30.47127001, 0.00962888, 37.14334679, 0.05867855, 3.71433468, 0.30305725, -30.47127001, -0.00962888, -37.14334679, -0.05867855, -3.71433468, -0.30305725, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1022991, 30.42713968, 0.00960009, 37.08955355, 0.05911563, 3.70895536, 0.30130604, -45.0993834, -0.01008758, -54.9744739, -0.06433287, -5.49744739, -0.30652328, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1022990, 29524351.89707331, 0.07, 0.00071458, 0.00023333, 12301813.29044721, 0.00060032)
    ops.section('Aggregator', 1022991, 1022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1022992, 1022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1022, 1022991, 0.32511534142, 1022992, 0.32511534142, 1022990)
    # Create element
    ops.element('forceBeamColumn', 1022, 22, 122, 1022, 1022)

    # Create geometric transformation
    ops.geomTransf('Linear', 1122, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1122990, 31.65218282, 0.00947116, 38.64112484, 0.07066182, 3.86411248, 0.3731741, -46.94706322, -0.00996967, -57.31318252, -0.0770053, -5.73131825, -0.37951758, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1122991, 31.65218282, 0.00947116, 38.64112484, 0.07100807, 3.86411248, 0.37759665, -46.94706322, -0.00996967, -57.31318252, -0.07738462, -5.73131825, -0.3839732, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1122990, 28980980.88282336, 0.07, 0.00071458, 0.00023333, 12075408.7011764, 0.00060032)
    ops.section('Aggregator', 1122991, 1122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1122992, 1122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1122, 1122991, 0.25899140391, 1122992, 0.25899140391, 1122990)
    # Create element
    ops.element('forceBeamColumn', 1122, 122, 222, 1122, 1122)

    # Create geometric transformation
    ops.geomTransf('Linear', 1222, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1222990, 30.91758558, 0.00944698, 37.60717197, 0.05831554, 3.7607172, 0.30230624, -45.85222186, -0.00992623, -55.77319057, -0.06346274, -5.57731906, -0.30745344, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1222991, 30.95867884, 0.00948042, 37.65715651, 0.05718903, 3.76571565, 0.29502123, -30.95867884, -0.00948042, -37.65715651, -0.05718903, -3.76571565, -0.29502123, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1222990, 30253709.95416339, 0.07, 0.00071458, 0.00023333, 12605712.48090141, 0.00060032)
    ops.section('Aggregator', 1222991, 1222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1222992, 1222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1222, 1222991, 0.3253717302, 1222992, 0.3253717302, 1222990)
    # Create element
    ops.element('forceBeamColumn', 1222, 222, 322, 1222, 1222)

    # Create geometric transformation
    ops.geomTransf('Linear', 6200, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6200990, 30.30889529, 0.00952622, 36.93081279, 0.09076118, 3.69308128, 0.39720678, -77.79527898, -0.01106225, -94.79206869, -0.11235677, -9.47920687, -0.41880236, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6200991, 30.30889529, 0.00952622, 36.93081279, 0.09023568, 3.69308128, 0.39199976, -77.79527898, -0.01106225, -94.79206869, -0.11170151, -9.47920687, -0.41346559, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6200990, 29662880.71465981, 0.07, 0.00071458, 0.00023333, 12359533.63110826, 0.00060032)
    ops.section('Aggregator', 6200991, 6200990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6200992, 6200991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6200, 6200991, 0.25696264586, 6200992, 0.25696264586, 6200990)
    # Create element
    ops.element('forceBeamColumn', 6200, 1101, 1201, 6200, 6200)

    # Create geometric transformation
    ops.geomTransf('Linear', 6201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6201990, 38.3131611, 0.01201654, 46.68625577, 0.13320022, 4.66862558, 0.51886681, -103.634638, -0.01540705, -126.28332085, -0.16931642, -12.62833208, -0.554983, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6201991, 38.3131611, 0.01201654, 46.68625577, 0.13171998, 4.66862558, 0.51738656, -103.634638, -0.01540705, -126.28332085, -0.16743643, -12.62833208, -0.55310301, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6201990, 29644975.66119102, 0.06, 0.00045, 0.0002, 12352073.19216292, 0.00046953)
    ops.section('Aggregator', 6201991, 6201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6201992, 6201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6201, 6201991, 0.25929132637999996, 6201992, 0.25929132637999996, 6201990)
    # Create element
    ops.element('forceBeamColumn', 6201, 1102, 1202, 6201, 6201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 61.79659778, 0.00875398, 75.25646323, 0.08099852, 7.52564632, 0.32935255, -144.3922341, -0.01024592, -175.84218625, -0.0985588, -17.58421862, -0.34691283, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 91.18741845, 0.00906861, 111.04887405, 0.08582109, 11.10488741, 0.33642712, -212.52842664, -0.01102474, -258.81906609, -0.10484819, -25.88190661, -0.35545421, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 29853620.13862111, 0.1, 0.00133333, 0.00052083, 12439008.39109213, 0.00127345)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.36991596572999996, 2001992, 0.36991596572999996, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 125.96685557, 0.00676851, 153.56712502, 0.07154989, 15.3567125, 0.29425446, -192.62776399, -0.0073397, -234.83393136, -0.07896388, -23.48339314, -0.30166846, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 125.9259891, 0.0066864, 153.51730441, 0.07316202, 15.35173044, 0.29252379, -284.31615602, -0.00789036, -346.61192803, -0.08840825, -34.6611928, -0.30777003, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 29482518.93423047, 0.125, 0.00260417, 0.00065104, 12284382.88926269, 0.00178813)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.41162078088, 2101992, 0.41162078088, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 125.5929115, 0.00675401, 153.49145802, 0.07315877, 15.3491458, 0.29747422, -192.00056659, -0.00733447, -234.65055912, -0.08075352, -23.46505591, -0.30506896, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 125.57338444, 0.00666834, 153.46759331, 0.07463922, 15.34675933, 0.29427789, -283.35856164, -0.00789293, -346.30233702, -0.09022194, -34.6302337, -0.30986062, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 28573688.64502759, 0.125, 0.00260417, 0.00065104, 11905703.60209483, 0.00178813)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.41086403999, 2201992, 0.41086403999, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 62.23216084, 0.00841831, 75.93064179, 0.08177152, 7.59306418, 0.33000623, -145.48914022, -0.00989532, -177.51406416, -0.09956345, -17.75140642, -0.34779817, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 92.10681444, 0.00870751, 112.38127424, 0.08571816, 11.23812742, 0.32924854, -214.41917885, -0.01064073, -261.61691389, -0.10477978, -26.16169139, -0.34831016, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 29185890.74027833, 0.1, 0.00133333, 0.00052083, 12160787.80844931, 0.00127345)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.36761002548, 2301992, 0.36761002548, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 94.00489545, 0.00913208, 114.81893961, 0.08443114, 11.48189396, 0.32598477, -218.94627169, -0.01116086, -267.42414452, -0.10320765, -26.74241445, -0.34476127, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 63.60056766, 0.00882143, 77.68265368, 0.07979555, 7.76826537, 0.31996139, -148.65612624, -0.01036944, -181.57074373, -0.09712934, -18.15707437, -0.33729518, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 28795818.29242368, 0.1, 0.00133333, 0.00052083, 11998257.6218432, 0.00127345)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.37318683263, 2011992, 0.37318683263, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 125.94422091, 0.00672709, 153.42956464, 0.07168665, 15.34295646, 0.28948915, -284.47269126, -0.00792969, -346.55437827, -0.08661128, -34.65543783, -0.30441378, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 126.01109405, 0.00680738, 153.5110318, 0.07039171, 15.35110318, 0.29384331, -192.73150556, -0.0073781, -234.79212289, -0.07767879, -23.47921229, -0.30113039, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 29733250.87265645, 0.125, 0.00260417, 0.00065104, 12388854.53027352, 0.00178813)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.41230505808, 2111992, 0.41230505808, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 126.00256799, 0.00678764, 154.06751309, 0.07484026, 15.40675131, 0.29739178, -284.47686151, -0.00803378, -347.83928045, -0.09046181, -34.78392805, -0.31301333, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 126.06809564, 0.00687248, 154.14763592, 0.07210127, 15.41476359, 0.28933903, -192.77035047, -0.00746313, -235.70669208, -0.07958198, -23.57066921, -0.29681975, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 28386128.12075889, 0.125, 0.00260417, 0.00065104, 11827553.38364954, 0.00178813)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.41302112848, 2211992, 0.41302112848, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 89.81857119, 0.00872877, 109.76639599, 0.08592029, 10.9766396, 0.32972338, -209.17799758, -0.01067655, -255.63438173, -0.10503669, -25.56343817, -0.34883979, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 60.76560896, 0.00843171, 74.26105545, 0.08189164, 7.42610555, 0.32987918, -142.02323852, -0.00991772, -173.56520853, -0.09971632, -17.35652085, -0.34770386, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 28587531.62341041, 0.1, 0.00133333, 0.00052083, 11911471.50975434, 0.00127345)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.36547816802, 2311992, 0.36547816802, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)

    # Create geometric transformation
    ops.geomTransf('Linear', 2002, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2002990, 35.48898113, 0.00802451, 43.3464457, 0.09919248, 4.33464457, 0.40650505, -143.83085235, -0.01037734, -175.67583044, -0.13722537, -17.56758304, -0.44453794, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2002991, 52.68218624, 0.00831896, 64.34632533, 0.10111714, 6.43463253, 0.40842971, -143.90534815, -0.01030281, -175.76682003, -0.12816117, -17.576682, -0.43547374, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2002990, 28798483.4169515, 0.08, 0.00106667, 0.00026667, 11999368.09039646, 0.00073242)
    ops.section('Aggregator', 2002991, 2002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2002992, 2002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2002, 2002991, 0.32540159513, 2002992, 0.32540159513, 2002990)
    # Create element
    ops.element('forceBeamColumn', 2002, 2, 12, 2002, 2002)

    # Create geometric transformation
    ops.geomTransf('Linear', 2102, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2102990, 72.48809056, 0.00719265, 88.48189849, 0.07793144, 8.84818985, 0.32029015, -169.79470377, -0.00838431, -207.25829064, -0.09485653, -20.72582906, -0.33721524, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2102991, 72.37607224, 0.00711858, 88.34516439, 0.08067383, 8.83451644, 0.32492159, -250.19060888, -0.0090654, -305.39278776, -0.10756926, -30.53927878, -0.35181702, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2102990, 29030286.29871682, 0.1125, 0.00189844, 0.00058594, 12095952.62446534, 0.00152995)
    ops.section('Aggregator', 2102991, 2102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2102992, 2102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2102, 2102991, 0.36803583006999996, 2102992, 0.36803583006999996, 2102990)
    # Create element
    ops.element('forceBeamColumn', 2102, 102, 112, 2102, 2102)

    # Create geometric transformation
    ops.geomTransf('Linear', 2202, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2202990, 71.34974552, 0.00750467, 87.18076898, 0.07934753, 8.7180769, 0.32429533, -167.22373083, -0.00873477, -204.32719611, -0.09655663, -20.43271961, -0.34150443, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2202991, 71.16406505, 0.00744323, 86.95388988, 0.08158343, 8.69538899, 0.32404952, -246.328314, -0.00945373, -300.9834398, -0.10874094, -30.09834398, -0.35120703, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2202990, 28652942.77100291, 0.1125, 0.00189844, 0.00058594, 11938726.15458455, 0.00152995)
    ops.section('Aggregator', 2202991, 2202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2202992, 2202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2202, 2202991, 0.36987811554, 2202992, 0.36987811554, 2202990)
    # Create element
    ops.element('forceBeamColumn', 2202, 202, 212, 2202, 2202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2302, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2302990, 35.4255321, 0.00808784, 43.22441497, 0.09772747, 4.3224415, 0.40475734, -143.57002971, -0.0104318, -175.17677712, -0.13515336, -17.51767771, -0.44218322, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2302991, 52.55636692, 0.00838205, 64.12657985, 0.09986972, 6.41265798, 0.40689958, -143.61613912, -0.01035945, -175.23303745, -0.12655339, -17.52330374, -0.43358325, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2302990, 29177095.13891711, 0.08, 0.00106667, 0.00026667, 12157122.97454879, 0.00073242)
    ops.section('Aggregator', 2302991, 2302990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2302992, 2302991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2302, 2302991, 0.32570121155, 2302992, 0.32570121155, 2302990)
    # Create element
    ops.element('forceBeamColumn', 2302, 302, 312, 2302, 2302)

    # Create geometric transformation
    ops.geomTransf('Linear', 2012, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2012990, 53.23999194, 0.00861896, 65.06784797, 0.09912267, 6.5067848, 0.40385439, -145.46820152, -0.01066974, -177.78557954, -0.125614, -17.77855795, -0.43034571, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2012991, 35.90837539, 0.00831479, 43.88582014, 0.09843417, 4.38858201, 0.40316588, -145.44164605, -0.01074478, -177.75312448, -0.13613384, -17.77531245, -0.44086556, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2012990, 28565474.27165926, 0.08, 0.00106667, 0.00026667, 11902280.94652469, 0.00073242)
    ops.section('Aggregator', 2012991, 2012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2012992, 2012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2012, 2012991, 0.32815750513, 2012992, 0.32815750513, 2012990)
    # Create element
    ops.element('forceBeamColumn', 2012, 12, 22, 2012, 2012)

    # Create geometric transformation
    ops.geomTransf('Linear', 2112, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2112990, 71.45847979, 0.00716373, 87.37951285, 0.08327687, 8.73795128, 0.33128108, -247.09090072, -0.00913972, -302.143043, -0.11106906, -30.2143043, -0.35907327, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2112991, 71.5934456, 0.00723585, 87.54454919, 0.08034964, 8.75445492, 0.3257588, -167.71711048, -0.00844464, -205.08467927, -0.09782011, -20.50846793, -0.34322927, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2112990, 28364619.97943098, 0.1125, 0.00189844, 0.00058594, 11818591.65809624, 0.00152995)
    ops.section('Aggregator', 2112991, 2112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2112992, 2112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2112, 2112991, 0.36732609681000006, 2112992, 0.36732609681000006, 2112990)
    # Create element
    ops.element('forceBeamColumn', 2112, 112, 122, 2112, 2112)

    # Create geometric transformation
    ops.geomTransf('Linear', 2212, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2212990, 73.39601527, 0.00719384, 89.44365661, 0.08185703, 8.94436566, 0.33153618, -253.78759155, -0.00913861, -309.27687433, -0.10912619, -30.92768743, -0.35880535, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2212991, 73.50846743, 0.00726729, 89.58069582, 0.07927046, 8.95806958, 0.32864925, -172.21912393, -0.00845827, -209.87390291, -0.09647609, -20.98739029, -0.34585488, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2212990, 29616014.72932411, 0.1125, 0.00189844, 0.00058594, 12340006.13721838, 0.00152995)
    ops.section('Aggregator', 2212991, 2212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2212992, 2212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2212, 2212991, 0.37017950755, 2212992, 0.37017950755, 2212990)
    # Create element
    ops.element('forceBeamColumn', 2212, 212, 222, 2212, 2212)

    # Create geometric transformation
    ops.geomTransf('Linear', 2312, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2312990, 52.00926959, 0.00835989, 63.5073885, 0.09903454, 6.35073885, 0.4069018, -142.11671489, -0.01033913, -173.53563119, -0.1255005, -17.35356312, -0.43336775, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2312991, 35.068328, 0.00806581, 42.82117299, 0.09881523, 4.2821173, 0.40668248, -142.08215264, -0.01041145, -173.49342799, -0.13667711, -17.3493428, -0.44454436, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2312990, 28898196.10776486, 0.08, 0.00106667, 0.00026667, 12040915.04490202, 0.00073242)
    ops.section('Aggregator', 2312991, 2312990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2312992, 2312991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2312, 2312991, 0.32481531813, 2312992, 0.32481531813, 2312990)
    # Create element
    ops.element('forceBeamColumn', 2312, 312, 322, 2312, 2312)
