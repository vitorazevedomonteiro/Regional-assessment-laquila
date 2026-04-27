import openseespy.opensees as ops


def add_joints() -> None:
    """Add components of joints to ops domain.
    """
    # -------------------------------------------------
    # Add stairs joints to ops domain
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (1, 2, 0.5)
    ops.node(1121, 5.0, 10.0, 1.7, '-mass', 3.4320212028542314, 3.4320212028542314, 3.4320212028542314, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (2, 2, 0.5)
    ops.node(1221, 8.3, 10.0, 1.7, '-mass', 3.4320212028542314, 3.4320212028542314, 3.4320212028542314, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (5, 2, 0.5)
    ops.node(1521, 21.6, 10.0, 1.7, '-mass', 3.432021202854227, 3.432021202854227, 3.432021202854227, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (6, 2, 0.5)
    ops.node(1621, 24.9, 10.0, 1.7, '-mass', 3.432021202854227, 3.432021202854227, 3.432021202854227, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (1, 2, 1.5)
    ops.node(1122, 5.0, 10.0, 4.9, '-mass', 3.446344036697249, 3.446344036697249, 3.446344036697249, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (2, 2, 1.5)
    ops.node(1222, 8.3, 10.0, 4.9, '-mass', 3.446344036697249, 3.446344036697249, 3.446344036697249, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (5, 2, 1.5)
    ops.node(1522, 21.6, 10.0, 4.9, '-mass', 3.446344036697244, 3.446344036697244, 3.446344036697244, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (6, 2, 1.5)
    ops.node(1622, 24.9, 10.0, 4.9, '-mass', 3.446344036697244, 3.446344036697244, 3.446344036697244, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (1, 2, 2.5)
    ops.node(1123, 5.0, 10.0, 7.9, '-mass', 3.393782874617738, 3.393782874617738, 3.393782874617738, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (2, 2, 2.5)
    ops.node(1223, 8.3, 10.0, 7.9, '-mass', 3.393782874617738, 3.393782874617738, 3.393782874617738, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (5, 2, 2.5)
    ops.node(1523, 21.6, 10.0, 7.9, '-mass', 3.3937828746177336, 3.3937828746177336, 3.3937828746177336, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (6, 2, 2.5)
    ops.node(1623, 24.9, 10.0, 7.9, '-mass', 3.3937828746177336, 3.3937828746177336, 3.3937828746177336, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (1, 2, 3.5)
    ops.node(1124, 5.0, 10.0, 10.9, '-mass', 3.3412217125382275, 3.3412217125382275, 3.3412217125382275, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (2, 2, 3.5)
    ops.node(1224, 8.3, 10.0, 10.9, '-mass', 3.3412217125382275, 3.3412217125382275, 3.3412217125382275, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (5, 2, 3.5)
    ops.node(1524, 21.6, 10.0, 10.9, '-mass', 3.3412217125382235, 3.3412217125382235, 3.3412217125382235, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (6, 2, 3.5)
    ops.node(1624, 24.9, 10.0, 10.9, '-mass', 3.3412217125382235, 3.3412217125382235, 3.3412217125382235, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (1, 2, 4.5)
    ops.node(1125, 5.0, 10.0, 13.9, '-mass', 3.236099388379206, 3.236099388379206, 3.236099388379206, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (2, 2, 4.5)
    ops.node(1225, 8.3, 10.0, 13.9, '-mass', 3.236099388379206, 3.236099388379206, 3.236099388379206, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (5, 2, 4.5)
    ops.node(1525, 21.6, 10.0, 13.9, '-mass', 3.236099388379202, 3.236099388379202, 3.236099388379202, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (6, 2, 4.5)
    ops.node(1625, 24.9, 10.0, 13.9, '-mass', 3.236099388379202, 3.236099388379202, 3.236099388379202, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (1, 2, 5.5)
    ops.node(1126, 5.0, 10.0, 16.9, '-mass', 3.2360993883792055, 3.2360993883792055, 3.2360993883792055, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (2, 2, 5.5)
    ops.node(1226, 8.3, 10.0, 16.9, '-mass', 3.2360993883792055, 3.2360993883792055, 3.2360993883792055, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (5, 2, 5.5)
    ops.node(1526, 21.6, 10.0, 16.9, '-mass', 3.2360993883792015, 3.2360993883792015, 3.2360993883792015, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (6, 2, 5.5)
    ops.node(1626, 24.9, 10.0, 16.9, '-mass', 3.2360993883792015, 3.2360993883792015, 3.2360993883792015, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (1, 2, 6.5)
    ops.node(1127, 5.0, 10.0, 19.9, '-mass', 3.236099388379206, 3.236099388379206, 3.236099388379206, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (2, 2, 6.5)
    ops.node(1227, 8.3, 10.0, 19.9, '-mass', 3.236099388379206, 3.236099388379206, 3.236099388379206, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (5, 2, 6.5)
    ops.node(1527, 21.6, 10.0, 19.9, '-mass', 3.236099388379202, 3.236099388379202, 3.236099388379202, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (6, 2, 6.5)
    ops.node(1627, 24.9, 10.0, 19.9, '-mass', 3.236099388379202, 3.236099388379202, 3.236099388379202, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (1, 2, 7.5)
    ops.node(1128, 5.0, 10.0, 22.9, '-mass', 3.236099388379206, 3.236099388379206, 3.236099388379206, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (2, 2, 7.5)
    ops.node(1228, 8.3, 10.0, 22.9, '-mass', 3.236099388379206, 3.236099388379206, 3.236099388379206, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (5, 2, 7.5)
    ops.node(1528, 21.6, 10.0, 22.9, '-mass', 3.236099388379202, 3.236099388379202, 3.236099388379202, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (6, 2, 7.5)
    ops.node(1628, 24.9, 10.0, 22.9, '-mass', 3.236099388379202, 3.236099388379202, 3.236099388379202, 0.0, 0.0, 0.0)

    # -------------------------------------------------
    # Add floor joints to ops domain
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 1)
    ops.node(1, 0.0, 0.0, 3.4, '-mass', 10.137640163098878, 10.137640163098878, 10.137640163098878, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 0, 1)
    ops.node(101, 5.0, 0.0, 3.4, '-mass', 15.397918705402649, 15.397918705402649, 15.397918705402649, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 0, 1)
    ops.node(201, 8.3, 0.0, 3.4, '-mass', 15.397918705402649, 15.397918705402649, 15.397918705402649, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 0, 1)
    ops.node(301, 13.3, 0.0, 3.4, '-mass', 15.238642456676859, 15.238642456676859, 15.238642456676859, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 0, 1)
    ops.node(401, 16.6, 0.0, 3.4, '-mass', 15.238642456676859, 15.238642456676859, 15.238642456676859, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 0, 1)
    ops.node(501, 21.6, 0.0, 3.4, '-mass', 15.397918705402647, 15.397918705402647, 15.397918705402647, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 0, 1)
    ops.node(601, 24.9, 0.0, 3.4, '-mass', 15.397918705402647, 15.397918705402647, 15.397918705402647, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 0, 1)
    ops.node(701, 29.9, 0.0, 3.4, '-mass', 10.137640163098878, 10.137640163098878, 10.137640163098878, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 1, 1)
    ops.node(11, 0.0, 5.0, 3.4, '-mass', 18.623241590214064, 18.623241590214064, 18.623241590214064, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 1, 1)
    ops.node(111, 5.0, 5.0, 3.4, '-mass', 27.026337920489297, 27.026337920489297, 27.026337920489297, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 1, 1)
    ops.node(211, 8.3, 5.0, 3.4, '-mass', 27.026337920489297, 27.026337920489297, 27.026337920489297, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 1, 1)
    ops.node(311, 13.3, 5.0, 3.4, '-mass', 26.72817278287462, 26.72817278287462, 26.72817278287462, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 1, 1)
    ops.node(411, 16.6, 5.0, 3.4, '-mass', 27.70676605504587, 27.70676605504587, 27.70676605504587, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 1, 1)
    ops.node(511, 21.6, 5.0, 3.4, '-mass', 27.026337920489294, 27.026337920489294, 27.026337920489294, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 1, 1)
    ops.node(611, 24.9, 5.0, 3.4, '-mass', 27.026337920489294, 27.026337920489294, 27.026337920489294, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 1, 1)
    ops.node(711, 29.9, 5.0, 3.4, '-mass', 18.623241590214064, 18.623241590214064, 18.623241590214064, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 2, 1)
    ops.node(21, 0.0, 10.0, 3.4, '-mass', 14.46455988786952, 14.46455988786952, 14.46455988786952, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 2, 1)
    ops.node(121, 5.0, 10.0, 3.4, '-mass', 18.38332364933741, 18.38332364933741, 18.38332364933741, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 2, 1)
    ops.node(221, 8.3, 10.0, 3.4, '-mass', 18.38332364933741, 18.38332364933741, 18.38332364933741, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 2, 1)
    ops.node(321, 13.3, 10.0, 3.4, '-mass', 20.969820336391432, 20.969820336391432, 20.969820336391432, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 2, 1)
    ops.node(421, 16.6, 10.0, 3.4, '-mass', 20.969820336391432, 20.969820336391432, 20.969820336391432, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 2, 1)
    ops.node(521, 21.6, 10.0, 3.4, '-mass', 18.38332364933741, 18.38332364933741, 18.38332364933741, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 2, 1)
    ops.node(621, 24.9, 10.0, 3.4, '-mass', 18.38332364933741, 18.38332364933741, 18.38332364933741, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 2, 1)
    ops.node(721, 29.9, 10.0, 3.4, '-mass', 14.46455988786952, 14.46455988786952, 14.46455988786952, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 3, 1)
    ops.node(31, 0.0, 13.3, 3.4, '-mass', 14.464559887869521, 14.464559887869521, 14.464559887869521, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 3, 1)
    ops.node(131, 5.0, 13.3, 3.4, '-mass', 21.08917125382263, 21.08917125382263, 21.08917125382263, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 3, 1)
    ops.node(231, 8.3, 13.3, 3.4, '-mass', 21.08917125382263, 21.08917125382263, 21.08917125382263, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 3, 1)
    ops.node(331, 13.3, 13.3, 3.4, '-mass', 20.969820336391436, 20.969820336391436, 20.969820336391436, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 3, 1)
    ops.node(431, 16.6, 13.3, 3.4, '-mass', 20.969820336391436, 20.969820336391436, 20.969820336391436, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 3, 1)
    ops.node(531, 21.6, 13.3, 3.4, '-mass', 21.089171253822624, 21.089171253822624, 21.089171253822624, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 3, 1)
    ops.node(631, 24.9, 13.3, 3.4, '-mass', 21.089171253822624, 21.089171253822624, 21.089171253822624, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 3, 1)
    ops.node(731, 29.9, 13.3, 3.4, '-mass', 14.464559887869521, 14.464559887869521, 14.464559887869521, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 4, 1)
    ops.node(41, 0.0, 18.3, 3.4, '-mass', 18.623241590214064, 18.623241590214064, 18.623241590214064, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 4, 1)
    ops.node(141, 5.0, 18.3, 3.4, '-mass', 27.026337920489297, 27.026337920489297, 27.026337920489297, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 4, 1)
    ops.node(241, 8.3, 18.3, 3.4, '-mass', 27.026337920489297, 27.026337920489297, 27.026337920489297, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 4, 1)
    ops.node(341, 13.3, 18.3, 3.4, '-mass', 26.72817278287462, 26.72817278287462, 26.72817278287462, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 4, 1)
    ops.node(441, 16.6, 18.3, 3.4, '-mass', 27.70676605504587, 27.70676605504587, 27.70676605504587, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 4, 1)
    ops.node(541, 21.6, 18.3, 3.4, '-mass', 27.026337920489294, 27.026337920489294, 27.026337920489294, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 4, 1)
    ops.node(641, 24.9, 18.3, 3.4, '-mass', 27.026337920489294, 27.026337920489294, 27.026337920489294, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 4, 1)
    ops.node(741, 29.9, 18.3, 3.4, '-mass', 18.623241590214064, 18.623241590214064, 18.623241590214064, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 5, 1)
    ops.node(51, 0.0, 23.3, 3.4, '-mass', 10.137640163098878, 10.137640163098878, 10.137640163098878, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 5, 1)
    ops.node(151, 5.0, 23.3, 3.4, '-mass', 15.397918705402649, 15.397918705402649, 15.397918705402649, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 5, 1)
    ops.node(251, 8.3, 23.3, 3.4, '-mass', 15.397918705402649, 15.397918705402649, 15.397918705402649, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 5, 1)
    ops.node(351, 13.3, 23.3, 3.4, '-mass', 15.238642456676859, 15.238642456676859, 15.238642456676859, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 5, 1)
    ops.node(451, 16.6, 23.3, 3.4, '-mass', 15.238642456676859, 15.238642456676859, 15.238642456676859, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 5, 1)
    ops.node(551, 21.6, 23.3, 3.4, '-mass', 15.397918705402647, 15.397918705402647, 15.397918705402647, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 5, 1)
    ops.node(651, 24.9, 23.3, 3.4, '-mass', 15.397918705402647, 15.397918705402647, 15.397918705402647, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 5, 1)
    ops.node(751, 29.9, 23.3, 3.4, '-mass', 10.137640163098878, 10.137640163098878, 10.137640163098878, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 0, 2)
    ops.node(2, 0.0, 0.0, 6.4, '-mass', 10.075203873598367, 10.075203873598367, 10.075203873598367, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 0, 2)
    ops.node(102, 5.0, 0.0, 6.4, '-mass', 15.377531345565748, 15.377531345565748, 15.377531345565748, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 0, 2)
    ops.node(202, 8.3, 0.0, 6.4, '-mass', 15.377531345565748, 15.377531345565748, 15.377531345565748, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 0, 2)
    ops.node(302, 13.3, 0.0, 6.4, '-mass', 15.281965596330274, 15.281965596330274, 15.281965596330274, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 0, 2)
    ops.node(402, 16.6, 0.0, 6.4, '-mass', 15.281965596330274, 15.281965596330274, 15.281965596330274, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 0, 2)
    ops.node(502, 21.6, 0.0, 6.4, '-mass', 15.377531345565746, 15.377531345565746, 15.377531345565746, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 0, 2)
    ops.node(602, 24.9, 0.0, 6.4, '-mass', 15.377531345565746, 15.377531345565746, 15.377531345565746, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 0, 2)
    ops.node(702, 29.9, 0.0, 6.4, '-mass', 10.075203873598367, 10.075203873598367, 10.075203873598367, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 1, 2)
    ops.node(12, 0.0, 5.0, 6.4, '-mass', 18.31615698267074, 18.31615698267074, 18.31615698267074, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 1, 2)
    ops.node(112, 5.0, 5.0, 6.4, '-mass', 26.74728593272171, 26.74728593272171, 26.74728593272171, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 1, 2)
    ops.node(212, 8.3, 5.0, 6.4, '-mass', 26.74728593272171, 26.74728593272171, 26.74728593272171, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 1, 2)
    ops.node(312, 13.3, 5.0, 6.4, '-mass', 26.575267584097855, 26.575267584097855, 26.575267584097855, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 1, 2)
    ops.node(412, 16.6, 5.0, 6.4, '-mass', 27.492698776758406, 27.492698776758406, 27.492698776758406, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 1, 2)
    ops.node(512, 21.6, 5.0, 6.4, '-mass', 26.747285932721706, 26.747285932721706, 26.747285932721706, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 1, 2)
    ops.node(612, 24.9, 5.0, 6.4, '-mass', 26.747285932721706, 26.747285932721706, 26.747285932721706, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 1, 2)
    ops.node(712, 29.9, 5.0, 6.4, '-mass', 18.31615698267074, 18.31615698267074, 18.31615698267074, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 2, 2)
    ops.node(22, 0.0, 10.0, 6.4, '-mass', 14.539738277268095, 14.539738277268095, 14.539738277268095, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 2, 2)
    ops.node(122, 5.0, 10.0, 6.4, '-mass', 18.743925076452598, 18.743925076452598, 18.743925076452598, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 2, 2)
    ops.node(222, 8.3, 10.0, 6.4, '-mass', 18.743925076452598, 18.743925076452598, 18.743925076452598, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 2, 2)
    ops.node(322, 13.3, 10.0, 6.4, '-mass', 21.371196483180427, 21.371196483180427, 21.371196483180427, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 2, 2)
    ops.node(422, 16.6, 10.0, 6.4, '-mass', 21.371196483180427, 21.371196483180427, 21.371196483180427, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 2, 2)
    ops.node(522, 21.6, 10.0, 6.4, '-mass', 18.743925076452598, 18.743925076452598, 18.743925076452598, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 2, 2)
    ops.node(622, 24.9, 10.0, 6.4, '-mass', 18.743925076452598, 18.743925076452598, 18.743925076452598, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 2, 2)
    ops.node(722, 29.9, 10.0, 6.4, '-mass', 14.539738277268095, 14.539738277268095, 14.539738277268095, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 3, 2)
    ops.node(32, 0.0, 13.3, 6.4, '-mass', 14.539738277268095, 14.539738277268095, 14.539738277268095, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 3, 2)
    ops.node(132, 5.0, 13.3, 6.4, '-mass', 21.38733639143731, 21.38733639143731, 21.38733639143731, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 3, 2)
    ops.node(232, 8.3, 13.3, 6.4, '-mass', 21.38733639143731, 21.38733639143731, 21.38733639143731, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 3, 2)
    ops.node(332, 13.3, 13.3, 6.4, '-mass', 21.371196483180423, 21.371196483180423, 21.371196483180423, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 3, 2)
    ops.node(432, 16.6, 13.3, 6.4, '-mass', 21.371196483180423, 21.371196483180423, 21.371196483180423, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 3, 2)
    ops.node(532, 21.6, 13.3, 6.4, '-mass', 21.387336391437305, 21.387336391437305, 21.387336391437305, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 3, 2)
    ops.node(632, 24.9, 13.3, 6.4, '-mass', 21.387336391437305, 21.387336391437305, 21.387336391437305, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 3, 2)
    ops.node(732, 29.9, 13.3, 6.4, '-mass', 14.539738277268095, 14.539738277268095, 14.539738277268095, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 4, 2)
    ops.node(42, 0.0, 18.3, 6.4, '-mass', 18.50728848114169, 18.50728848114169, 18.50728848114169, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 4, 2)
    ops.node(142, 5.0, 18.3, 6.4, '-mass', 27.064564220183485, 27.064564220183485, 27.064564220183485, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 4, 2)
    ops.node(242, 8.3, 18.3, 6.4, '-mass', 27.064564220183485, 27.064564220183485, 27.064564220183485, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 4, 2)
    ops.node(342, 13.3, 18.3, 6.4, '-mass', 26.89254587155963, 26.89254587155963, 26.89254587155963, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 4, 2)
    ops.node(442, 16.6, 18.3, 6.4, '-mass', 27.80997706422018, 27.80997706422018, 27.80997706422018, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 4, 2)
    ops.node(542, 21.6, 18.3, 6.4, '-mass', 27.06456422018348, 27.06456422018348, 27.06456422018348, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 4, 2)
    ops.node(642, 24.9, 18.3, 6.4, '-mass', 27.06456422018348, 27.06456422018348, 27.06456422018348, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 4, 2)
    ops.node(742, 29.9, 18.3, 6.4, '-mass', 18.50728848114169, 18.50728848114169, 18.50728848114169, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 5, 2)
    ops.node(52, 0.0, 23.3, 6.4, '-mass', 10.075203873598367, 10.075203873598367, 10.075203873598367, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 5, 2)
    ops.node(152, 5.0, 23.3, 6.4, '-mass', 15.377531345565748, 15.377531345565748, 15.377531345565748, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 5, 2)
    ops.node(252, 8.3, 23.3, 6.4, '-mass', 15.377531345565748, 15.377531345565748, 15.377531345565748, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 5, 2)
    ops.node(352, 13.3, 23.3, 6.4, '-mass', 15.281965596330274, 15.281965596330274, 15.281965596330274, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 5, 2)
    ops.node(452, 16.6, 23.3, 6.4, '-mass', 15.281965596330274, 15.281965596330274, 15.281965596330274, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 5, 2)
    ops.node(552, 21.6, 23.3, 6.4, '-mass', 15.377531345565746, 15.377531345565746, 15.377531345565746, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 5, 2)
    ops.node(652, 24.9, 23.3, 6.4, '-mass', 15.377531345565746, 15.377531345565746, 15.377531345565746, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 5, 2)
    ops.node(752, 29.9, 23.3, 6.4, '-mass', 10.075203873598367, 10.075203873598367, 10.075203873598367, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 0, 3)
    ops.node(3, 0.0, 0.0, 9.4, '-mass', 10.075203873598367, 10.075203873598367, 10.075203873598367, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 0, 3)
    ops.node(103, 5.0, 0.0, 9.4, '-mass', 15.281965596330274, 15.281965596330274, 15.281965596330274, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 0, 3)
    ops.node(203, 8.3, 0.0, 9.4, '-mass', 15.281965596330274, 15.281965596330274, 15.281965596330274, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 0, 3)
    ops.node(303, 13.3, 0.0, 9.4, '-mass', 15.122689347604483, 15.122689347604483, 15.122689347604483, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 0, 3)
    ops.node(403, 16.6, 0.0, 9.4, '-mass', 15.281965596330274, 15.281965596330274, 15.281965596330274, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 0, 3)
    ops.node(503, 21.6, 0.0, 9.4, '-mass', 15.281965596330272, 15.281965596330272, 15.281965596330272, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 0, 3)
    ops.node(603, 24.9, 0.0, 9.4, '-mass', 15.281965596330272, 15.281965596330272, 15.281965596330272, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 0, 3)
    ops.node(703, 29.9, 0.0, 9.4, '-mass', 10.075203873598367, 10.075203873598367, 10.075203873598367, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 1, 3)
    ops.node(13, 0.0, 5.0, 9.4, '-mass', 18.31615698267074, 18.31615698267074, 18.31615698267074, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 1, 3)
    ops.node(113, 5.0, 5.0, 9.4, '-mass', 26.55615443425076, 26.55615443425076, 26.55615443425076, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 1, 3)
    ops.node(213, 8.3, 5.0, 9.4, '-mass', 26.55615443425076, 26.55615443425076, 26.55615443425076, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 1, 3)
    ops.node(313, 13.3, 5.0, 9.4, '-mass', 26.256715086646278, 26.256715086646278, 26.256715086646278, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 1, 3)
    ops.node(413, 16.6, 5.0, 9.4, '-mass', 27.492698776758406, 27.492698776758406, 27.492698776758406, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 1, 3)
    ops.node(513, 21.6, 5.0, 9.4, '-mass', 26.55615443425076, 26.55615443425076, 26.55615443425076, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 1, 3)
    ops.node(613, 24.9, 5.0, 9.4, '-mass', 26.55615443425076, 26.55615443425076, 26.55615443425076, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 1, 3)
    ops.node(713, 29.9, 5.0, 9.4, '-mass', 18.31615698267074, 18.31615698267074, 18.31615698267074, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 2, 3)
    ops.node(23, 0.0, 10.0, 9.4, '-mass', 14.380462028542302, 14.380462028542302, 14.380462028542302, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 2, 3)
    ops.node(123, 5.0, 10.0, 9.4, '-mass', 18.3208873598369, 18.3208873598369, 18.3208873598369, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 2, 3)
    ops.node(223, 8.3, 10.0, 9.4, '-mass', 18.3208873598369, 18.3208873598369, 18.3208873598369, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 2, 3)
    ops.node(323, 13.3, 10.0, 9.4, '-mass', 20.8423993374108, 20.8423993374108, 20.8423993374108, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 2, 3)
    ops.node(423, 16.6, 10.0, 9.4, '-mass', 21.10679791029561, 21.10679791029561, 21.10679791029561, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 2, 3)
    ops.node(523, 21.6, 10.0, 9.4, '-mass', 18.3208873598369, 18.3208873598369, 18.3208873598369, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 2, 3)
    ops.node(623, 24.9, 10.0, 9.4, '-mass', 18.3208873598369, 18.3208873598369, 18.3208873598369, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 2, 3)
    ops.node(723, 29.9, 10.0, 9.4, '-mass', 14.380462028542302, 14.380462028542302, 14.380462028542302, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 3, 3)
    ops.node(33, 0.0, 13.3, 9.4, '-mass', 14.380462028542304, 14.380462028542304, 14.380462028542304, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 3, 3)
    ops.node(133, 5.0, 13.3, 9.4, '-mass', 20.96429867482161, 20.96429867482161, 20.96429867482161, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 3, 3)
    ops.node(233, 8.3, 13.3, 9.4, '-mass', 20.96429867482161, 20.96429867482161, 20.96429867482161, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 3, 3)
    ops.node(333, 13.3, 13.3, 9.4, '-mass', 20.842399337410804, 20.842399337410804, 20.842399337410804, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 3, 3)
    ops.node(433, 16.6, 13.3, 9.4, '-mass', 21.106797910295615, 21.106797910295615, 21.106797910295615, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 3, 3)
    ops.node(533, 21.6, 13.3, 9.4, '-mass', 20.964298674821602, 20.964298674821602, 20.964298674821602, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 3, 3)
    ops.node(633, 24.9, 13.3, 9.4, '-mass', 20.964298674821602, 20.964298674821602, 20.964298674821602, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 3, 3)
    ops.node(733, 29.9, 13.3, 9.4, '-mass', 14.380462028542304, 14.380462028542304, 14.380462028542304, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 4, 3)
    ops.node(43, 0.0, 18.3, 9.4, '-mass', 18.31615698267074, 18.31615698267074, 18.31615698267074, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 4, 3)
    ops.node(143, 5.0, 18.3, 9.4, '-mass', 26.55615443425076, 26.55615443425076, 26.55615443425076, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 4, 3)
    ops.node(243, 8.3, 18.3, 9.4, '-mass', 26.55615443425076, 26.55615443425076, 26.55615443425076, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 4, 3)
    ops.node(343, 13.3, 18.3, 9.4, '-mass', 26.256715086646278, 26.256715086646278, 26.256715086646278, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 4, 3)
    ops.node(443, 16.6, 18.3, 9.4, '-mass', 27.492698776758406, 27.492698776758406, 27.492698776758406, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 4, 3)
    ops.node(543, 21.6, 18.3, 9.4, '-mass', 26.55615443425076, 26.55615443425076, 26.55615443425076, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 4, 3)
    ops.node(643, 24.9, 18.3, 9.4, '-mass', 26.55615443425076, 26.55615443425076, 26.55615443425076, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 4, 3)
    ops.node(743, 29.9, 18.3, 9.4, '-mass', 18.31615698267074, 18.31615698267074, 18.31615698267074, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 5, 3)
    ops.node(53, 0.0, 23.3, 9.4, '-mass', 10.075203873598367, 10.075203873598367, 10.075203873598367, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 5, 3)
    ops.node(153, 5.0, 23.3, 9.4, '-mass', 15.281965596330274, 15.281965596330274, 15.281965596330274, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 5, 3)
    ops.node(253, 8.3, 23.3, 9.4, '-mass', 15.281965596330274, 15.281965596330274, 15.281965596330274, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 5, 3)
    ops.node(353, 13.3, 23.3, 9.4, '-mass', 15.122689347604483, 15.122689347604483, 15.122689347604483, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 5, 3)
    ops.node(453, 16.6, 23.3, 9.4, '-mass', 15.281965596330274, 15.281965596330274, 15.281965596330274, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 5, 3)
    ops.node(553, 21.6, 23.3, 9.4, '-mass', 15.281965596330272, 15.281965596330272, 15.281965596330272, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 5, 3)
    ops.node(653, 24.9, 23.3, 9.4, '-mass', 15.281965596330272, 15.281965596330272, 15.281965596330272, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 5, 3)
    ops.node(753, 29.9, 23.3, 9.4, '-mass', 10.075203873598367, 10.075203873598367, 10.075203873598367, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 0, 4)
    ops.node(4, 0.0, 0.0, 12.4, '-mass', 9.836289500509682, 9.836289500509682, 9.836289500509682, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 0, 4)
    ops.node(104, 5.0, 0.0, 12.4, '-mass', 14.885367737003056, 14.885367737003056, 14.885367737003056, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 0, 4)
    ops.node(204, 8.3, 0.0, 12.4, '-mass', 14.885367737003056, 14.885367737003056, 14.885367737003056, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 0, 4)
    ops.node(304, 13.3, 0.0, 12.4, '-mass', 14.726091488277268, 14.726091488277268, 14.726091488277268, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 0, 4)
    ops.node(404, 16.6, 0.0, 12.4, '-mass', 14.726091488277268, 14.726091488277268, 14.726091488277268, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 0, 4)
    ops.node(504, 21.6, 0.0, 12.4, '-mass', 14.885367737003056, 14.885367737003056, 14.885367737003056, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 0, 4)
    ops.node(604, 24.9, 0.0, 12.4, '-mass', 14.885367737003056, 14.885367737003056, 14.885367737003056, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 0, 4)
    ops.node(704, 29.9, 0.0, 12.4, '-mass', 9.836289500509682, 9.836289500509682, 9.836289500509682, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 1, 4)
    ops.node(14, 0.0, 5.0, 12.4, '-mass', 18.220591233435268, 18.220591233435268, 18.220591233435268, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 1, 4)
    ops.node(114, 5.0, 5.0, 12.4, '-mass', 26.397515290519873, 26.397515290519873, 26.397515290519873, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 1, 4)
    ops.node(214, 8.3, 5.0, 12.4, '-mass', 26.397515290519873, 26.397515290519873, 26.397515290519873, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 1, 4)
    ops.node(314, 13.3, 5.0, 12.4, '-mass', 26.09807594291539, 26.09807594291539, 26.09807594291539, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 1, 4)
    ops.node(414, 16.6, 5.0, 12.4, '-mass', 27.01550713557594, 27.01550713557594, 27.01550713557594, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 1, 4)
    ops.node(514, 21.6, 5.0, 12.4, '-mass', 26.397515290519873, 26.397515290519873, 26.397515290519873, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 1, 4)
    ops.node(614, 24.9, 5.0, 12.4, '-mass', 26.397515290519873, 26.397515290519873, 26.397515290519873, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 1, 4)
    ops.node(714, 29.9, 5.0, 12.4, '-mass', 18.220591233435268, 18.220591233435268, 18.220591233435268, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 2, 4)
    ops.node(24, 0.0, 10.0, 12.4, '-mass', 14.380462028542302, 14.380462028542302, 14.380462028542302, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 2, 4)
    ops.node(124, 5.0, 10.0, 12.4, '-mass', 18.3208873598369, 18.3208873598369, 18.3208873598369, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 2, 4)
    ops.node(224, 8.3, 10.0, 12.4, '-mass', 18.3208873598369, 18.3208873598369, 18.3208873598369, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 2, 4)
    ops.node(324, 13.3, 10.0, 12.4, '-mass', 20.8423993374108, 20.8423993374108, 20.8423993374108, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 2, 4)
    ops.node(424, 16.6, 10.0, 12.4, '-mass', 20.8423993374108, 20.8423993374108, 20.8423993374108, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 2, 4)
    ops.node(524, 21.6, 10.0, 12.4, '-mass', 18.3208873598369, 18.3208873598369, 18.3208873598369, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 2, 4)
    ops.node(624, 24.9, 10.0, 12.4, '-mass', 18.3208873598369, 18.3208873598369, 18.3208873598369, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 2, 4)
    ops.node(724, 29.9, 10.0, 12.4, '-mass', 14.380462028542302, 14.380462028542302, 14.380462028542302, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 3, 4)
    ops.node(34, 0.0, 13.3, 12.4, '-mass', 14.380462028542304, 14.380462028542304, 14.380462028542304, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 3, 4)
    ops.node(134, 5.0, 13.3, 12.4, '-mass', 20.96429867482161, 20.96429867482161, 20.96429867482161, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 3, 4)
    ops.node(234, 8.3, 13.3, 12.4, '-mass', 20.96429867482161, 20.96429867482161, 20.96429867482161, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 3, 4)
    ops.node(334, 13.3, 13.3, 12.4, '-mass', 20.842399337410804, 20.842399337410804, 20.842399337410804, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 3, 4)
    ops.node(434, 16.6, 13.3, 12.4, '-mass', 20.842399337410804, 20.842399337410804, 20.842399337410804, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 3, 4)
    ops.node(534, 21.6, 13.3, 12.4, '-mass', 20.964298674821602, 20.964298674821602, 20.964298674821602, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 3, 4)
    ops.node(634, 24.9, 13.3, 12.4, '-mass', 20.964298674821602, 20.964298674821602, 20.964298674821602, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 3, 4)
    ops.node(734, 29.9, 13.3, 12.4, '-mass', 14.380462028542304, 14.380462028542304, 14.380462028542304, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 4, 4)
    ops.node(44, 0.0, 18.3, 12.4, '-mass', 18.220591233435268, 18.220591233435268, 18.220591233435268, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 4, 4)
    ops.node(144, 5.0, 18.3, 12.4, '-mass', 26.397515290519873, 26.397515290519873, 26.397515290519873, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 4, 4)
    ops.node(244, 8.3, 18.3, 12.4, '-mass', 26.397515290519873, 26.397515290519873, 26.397515290519873, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 4, 4)
    ops.node(344, 13.3, 18.3, 12.4, '-mass', 26.09807594291539, 26.09807594291539, 26.09807594291539, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 4, 4)
    ops.node(444, 16.6, 18.3, 12.4, '-mass', 27.01550713557594, 27.01550713557594, 27.01550713557594, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 4, 4)
    ops.node(544, 21.6, 18.3, 12.4, '-mass', 26.397515290519873, 26.397515290519873, 26.397515290519873, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 4, 4)
    ops.node(644, 24.9, 18.3, 12.4, '-mass', 26.397515290519873, 26.397515290519873, 26.397515290519873, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 4, 4)
    ops.node(744, 29.9, 18.3, 12.4, '-mass', 18.220591233435268, 18.220591233435268, 18.220591233435268, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 5, 4)
    ops.node(54, 0.0, 23.3, 12.4, '-mass', 9.836289500509682, 9.836289500509682, 9.836289500509682, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 5, 4)
    ops.node(154, 5.0, 23.3, 12.4, '-mass', 14.885367737003056, 14.885367737003056, 14.885367737003056, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 5, 4)
    ops.node(254, 8.3, 23.3, 12.4, '-mass', 14.885367737003056, 14.885367737003056, 14.885367737003056, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 5, 4)
    ops.node(354, 13.3, 23.3, 12.4, '-mass', 14.726091488277268, 14.726091488277268, 14.726091488277268, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 5, 4)
    ops.node(454, 16.6, 23.3, 12.4, '-mass', 14.726091488277268, 14.726091488277268, 14.726091488277268, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 5, 4)
    ops.node(554, 21.6, 23.3, 12.4, '-mass', 14.885367737003056, 14.885367737003056, 14.885367737003056, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 5, 4)
    ops.node(654, 24.9, 23.3, 12.4, '-mass', 14.885367737003056, 14.885367737003056, 14.885367737003056, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 5, 4)
    ops.node(754, 29.9, 23.3, 12.4, '-mass', 9.836289500509682, 9.836289500509682, 9.836289500509682, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 0, 5)
    ops.node(5, 0.0, 0.0, 15.4, '-mass', 9.756651376146788, 9.756651376146788, 9.756651376146788, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 0, 5)
    ops.node(105, 5.0, 0.0, 15.4, '-mass', 14.726091488277268, 14.726091488277268, 14.726091488277268, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 0, 5)
    ops.node(205, 8.3, 0.0, 15.4, '-mass', 14.726091488277268, 14.726091488277268, 14.726091488277268, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 0, 5)
    ops.node(305, 13.3, 0.0, 15.4, '-mass', 14.646453363914372, 14.646453363914372, 14.646453363914372, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 0, 5)
    ops.node(405, 16.6, 0.0, 15.4, '-mass', 14.646453363914372, 14.646453363914372, 14.646453363914372, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 0, 5)
    ops.node(505, 21.6, 0.0, 15.4, '-mass', 14.726091488277266, 14.726091488277266, 14.726091488277266, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 0, 5)
    ops.node(605, 24.9, 0.0, 15.4, '-mass', 14.726091488277266, 14.726091488277266, 14.726091488277266, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 0, 5)
    ops.node(705, 29.9, 0.0, 15.4, '-mass', 9.756651376146788, 9.756651376146788, 9.756651376146788, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 1, 5)
    ops.node(15, 0.0, 5.0, 15.4, '-mass', 17.822400611620793, 17.822400611620793, 17.822400611620793, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 1, 5)
    ops.node(115, 5.0, 5.0, 15.4, '-mass', 25.682364933741077, 25.682364933741077, 25.682364933741077, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 1, 5)
    ops.node(215, 8.3, 5.0, 15.4, '-mass', 25.682364933741077, 25.682364933741077, 25.682364933741077, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 1, 5)
    ops.node(315, 13.3, 5.0, 15.4, '-mass', 25.542201834862382, 25.542201834862382, 25.542201834862382, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 1, 5)
    ops.node(415, 16.6, 5.0, 15.4, '-mass', 26.459633027522933, 26.459633027522933, 26.459633027522933, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 1, 5)
    ops.node(515, 21.6, 5.0, 15.4, '-mass', 25.682364933741077, 25.682364933741077, 25.682364933741077, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 1, 5)
    ops.node(615, 24.9, 5.0, 15.4, '-mass', 25.682364933741077, 25.682364933741077, 25.682364933741077, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 1, 5)
    ops.node(715, 29.9, 5.0, 15.4, '-mass', 17.822400611620793, 17.822400611620793, 17.822400611620793, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 2, 5)
    ops.node(25, 0.0, 10.0, 15.4, '-mass', 14.168624617737004, 14.168624617737004, 14.168624617737004, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 2, 5)
    ops.node(125, 5.0, 10.0, 15.4, '-mass', 17.924289500509683, 17.924289500509683, 17.924289500509683, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 2, 5)
    ops.node(225, 8.3, 10.0, 15.4, '-mass', 17.924289500509683, 17.924289500509683, 17.924289500509683, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 2, 5)
    ops.node(325, 13.3, 10.0, 15.4, '-mass', 20.578000764525992, 20.578000764525992, 20.578000764525992, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 2, 5)
    ops.node(425, 16.6, 10.0, 15.4, '-mass', 20.578000764525992, 20.578000764525992, 20.578000764525992, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 2, 5)
    ops.node(525, 21.6, 10.0, 15.4, '-mass', 17.92428950050968, 17.92428950050968, 17.92428950050968, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 2, 5)
    ops.node(625, 24.9, 10.0, 15.4, '-mass', 17.92428950050968, 17.92428950050968, 17.92428950050968, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 2, 5)
    ops.node(725, 29.9, 10.0, 15.4, '-mass', 14.168624617737004, 14.168624617737004, 14.168624617737004, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 3, 5)
    ops.node(35, 0.0, 13.3, 15.4, '-mass', 14.168624617737004, 14.168624617737004, 14.168624617737004, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 3, 5)
    ops.node(135, 5.0, 13.3, 15.4, '-mass', 20.567700815494394, 20.567700815494394, 20.567700815494394, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 3, 5)
    ops.node(235, 8.3, 13.3, 15.4, '-mass', 20.567700815494394, 20.567700815494394, 20.567700815494394, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 3, 5)
    ops.node(335, 13.3, 13.3, 15.4, '-mass', 20.578000764525992, 20.578000764525992, 20.578000764525992, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 3, 5)
    ops.node(435, 16.6, 13.3, 15.4, '-mass', 20.578000764525992, 20.578000764525992, 20.578000764525992, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 3, 5)
    ops.node(535, 21.6, 13.3, 15.4, '-mass', 20.567700815494387, 20.567700815494387, 20.567700815494387, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 3, 5)
    ops.node(635, 24.9, 13.3, 15.4, '-mass', 20.567700815494387, 20.567700815494387, 20.567700815494387, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 3, 5)
    ops.node(735, 29.9, 13.3, 15.4, '-mass', 14.168624617737004, 14.168624617737004, 14.168624617737004, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 4, 5)
    ops.node(45, 0.0, 18.3, 15.4, '-mass', 17.822400611620793, 17.822400611620793, 17.822400611620793, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 4, 5)
    ops.node(145, 5.0, 18.3, 15.4, '-mass', 25.682364933741077, 25.682364933741077, 25.682364933741077, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 4, 5)
    ops.node(245, 8.3, 18.3, 15.4, '-mass', 25.682364933741077, 25.682364933741077, 25.682364933741077, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 4, 5)
    ops.node(345, 13.3, 18.3, 15.4, '-mass', 25.542201834862382, 25.542201834862382, 25.542201834862382, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 4, 5)
    ops.node(445, 16.6, 18.3, 15.4, '-mass', 26.459633027522933, 26.459633027522933, 26.459633027522933, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 4, 5)
    ops.node(545, 21.6, 18.3, 15.4, '-mass', 25.682364933741077, 25.682364933741077, 25.682364933741077, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 4, 5)
    ops.node(645, 24.9, 18.3, 15.4, '-mass', 25.682364933741077, 25.682364933741077, 25.682364933741077, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 4, 5)
    ops.node(745, 29.9, 18.3, 15.4, '-mass', 17.822400611620793, 17.822400611620793, 17.822400611620793, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 5, 5)
    ops.node(55, 0.0, 23.3, 15.4, '-mass', 9.756651376146788, 9.756651376146788, 9.756651376146788, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 5, 5)
    ops.node(155, 5.0, 23.3, 15.4, '-mass', 14.726091488277268, 14.726091488277268, 14.726091488277268, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 5, 5)
    ops.node(255, 8.3, 23.3, 15.4, '-mass', 14.726091488277268, 14.726091488277268, 14.726091488277268, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 5, 5)
    ops.node(355, 13.3, 23.3, 15.4, '-mass', 14.646453363914372, 14.646453363914372, 14.646453363914372, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 5, 5)
    ops.node(455, 16.6, 23.3, 15.4, '-mass', 14.646453363914372, 14.646453363914372, 14.646453363914372, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 5, 5)
    ops.node(555, 21.6, 23.3, 15.4, '-mass', 14.726091488277266, 14.726091488277266, 14.726091488277266, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 5, 5)
    ops.node(655, 24.9, 23.3, 15.4, '-mass', 14.726091488277266, 14.726091488277266, 14.726091488277266, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 5, 5)
    ops.node(755, 29.9, 23.3, 15.4, '-mass', 9.756651376146788, 9.756651376146788, 9.756651376146788, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 0, 6)
    ops.node(6, 0.0, 0.0, 18.4, '-mass', 9.756651376146788, 9.756651376146788, 9.756651376146788, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 0, 6)
    ops.node(106, 5.0, 0.0, 18.4, '-mass', 14.646453363914372, 14.646453363914372, 14.646453363914372, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 0, 6)
    ops.node(206, 8.3, 0.0, 18.4, '-mass', 14.646453363914372, 14.646453363914372, 14.646453363914372, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 0, 6)
    ops.node(306, 13.3, 0.0, 18.4, '-mass', 14.646453363914372, 14.646453363914372, 14.646453363914372, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 0, 6)
    ops.node(406, 16.6, 0.0, 18.4, '-mass', 14.646453363914372, 14.646453363914372, 14.646453363914372, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 0, 6)
    ops.node(506, 21.6, 0.0, 18.4, '-mass', 14.64645336391437, 14.64645336391437, 14.64645336391437, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 0, 6)
    ops.node(606, 24.9, 0.0, 18.4, '-mass', 14.64645336391437, 14.64645336391437, 14.64645336391437, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 0, 6)
    ops.node(706, 29.9, 0.0, 18.4, '-mass', 9.756651376146788, 9.756651376146788, 9.756651376146788, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 1, 6)
    ops.node(16, 0.0, 5.0, 18.4, '-mass', 17.822400611620793, 17.822400611620793, 17.822400611620793, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 1, 6)
    ops.node(116, 5.0, 5.0, 18.4, '-mass', 25.52308868501529, 25.52308868501529, 25.52308868501529, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 1, 6)
    ops.node(216, 8.3, 5.0, 18.4, '-mass', 25.52308868501529, 25.52308868501529, 25.52308868501529, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 1, 6)
    ops.node(316, 13.3, 5.0, 18.4, '-mass', 25.542201834862382, 25.542201834862382, 25.542201834862382, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 1, 6)
    ops.node(416, 16.6, 5.0, 18.4, '-mass', 26.459633027522933, 26.459633027522933, 26.459633027522933, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 1, 6)
    ops.node(516, 21.6, 5.0, 18.4, '-mass', 25.523088685015285, 25.523088685015285, 25.523088685015285, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 1, 6)
    ops.node(616, 24.9, 5.0, 18.4, '-mass', 25.523088685015285, 25.523088685015285, 25.523088685015285, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 1, 6)
    ops.node(716, 29.9, 5.0, 18.4, '-mass', 17.822400611620793, 17.822400611620793, 17.822400611620793, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 2, 6)
    ops.node(26, 0.0, 10.0, 18.4, '-mass', 14.168624617737004, 14.168624617737004, 14.168624617737004, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 2, 6)
    ops.node(126, 5.0, 10.0, 18.4, '-mass', 17.79209021406728, 17.79209021406728, 17.79209021406728, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 2, 6)
    ops.node(226, 8.3, 10.0, 18.4, '-mass', 17.79209021406728, 17.79209021406728, 17.79209021406728, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 2, 6)
    ops.node(326, 13.3, 10.0, 18.4, '-mass', 20.578000764525992, 20.578000764525992, 20.578000764525992, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 2, 6)
    ops.node(426, 16.6, 10.0, 18.4, '-mass', 20.578000764525992, 20.578000764525992, 20.578000764525992, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 2, 6)
    ops.node(526, 21.6, 10.0, 18.4, '-mass', 17.792090214067276, 17.792090214067276, 17.792090214067276, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 2, 6)
    ops.node(626, 24.9, 10.0, 18.4, '-mass', 17.792090214067276, 17.792090214067276, 17.792090214067276, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 2, 6)
    ops.node(726, 29.9, 10.0, 18.4, '-mass', 14.168624617737004, 14.168624617737004, 14.168624617737004, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 3, 6)
    ops.node(36, 0.0, 13.3, 18.4, '-mass', 14.168624617737004, 14.168624617737004, 14.168624617737004, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 3, 6)
    ops.node(136, 5.0, 13.3, 18.4, '-mass', 20.435501529051987, 20.435501529051987, 20.435501529051987, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 3, 6)
    ops.node(236, 8.3, 13.3, 18.4, '-mass', 20.435501529051987, 20.435501529051987, 20.435501529051987, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 3, 6)
    ops.node(336, 13.3, 13.3, 18.4, '-mass', 20.578000764525992, 20.578000764525992, 20.578000764525992, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 3, 6)
    ops.node(436, 16.6, 13.3, 18.4, '-mass', 20.578000764525992, 20.578000764525992, 20.578000764525992, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 3, 6)
    ops.node(536, 21.6, 13.3, 18.4, '-mass', 20.435501529051983, 20.435501529051983, 20.435501529051983, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 3, 6)
    ops.node(636, 24.9, 13.3, 18.4, '-mass', 20.435501529051983, 20.435501529051983, 20.435501529051983, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 3, 6)
    ops.node(736, 29.9, 13.3, 18.4, '-mass', 14.168624617737004, 14.168624617737004, 14.168624617737004, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 4, 6)
    ops.node(46, 0.0, 18.3, 18.4, '-mass', 17.822400611620793, 17.822400611620793, 17.822400611620793, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 4, 6)
    ops.node(146, 5.0, 18.3, 18.4, '-mass', 25.52308868501529, 25.52308868501529, 25.52308868501529, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 4, 6)
    ops.node(246, 8.3, 18.3, 18.4, '-mass', 25.52308868501529, 25.52308868501529, 25.52308868501529, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 4, 6)
    ops.node(346, 13.3, 18.3, 18.4, '-mass', 25.542201834862382, 25.542201834862382, 25.542201834862382, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 4, 6)
    ops.node(446, 16.6, 18.3, 18.4, '-mass', 26.459633027522933, 26.459633027522933, 26.459633027522933, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 4, 6)
    ops.node(546, 21.6, 18.3, 18.4, '-mass', 25.523088685015285, 25.523088685015285, 25.523088685015285, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 4, 6)
    ops.node(646, 24.9, 18.3, 18.4, '-mass', 25.523088685015285, 25.523088685015285, 25.523088685015285, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 4, 6)
    ops.node(746, 29.9, 18.3, 18.4, '-mass', 17.822400611620793, 17.822400611620793, 17.822400611620793, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 5, 6)
    ops.node(56, 0.0, 23.3, 18.4, '-mass', 9.756651376146788, 9.756651376146788, 9.756651376146788, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 5, 6)
    ops.node(156, 5.0, 23.3, 18.4, '-mass', 14.646453363914372, 14.646453363914372, 14.646453363914372, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 5, 6)
    ops.node(256, 8.3, 23.3, 18.4, '-mass', 14.646453363914372, 14.646453363914372, 14.646453363914372, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 5, 6)
    ops.node(356, 13.3, 23.3, 18.4, '-mass', 14.646453363914372, 14.646453363914372, 14.646453363914372, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 5, 6)
    ops.node(456, 16.6, 23.3, 18.4, '-mass', 14.646453363914372, 14.646453363914372, 14.646453363914372, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 5, 6)
    ops.node(556, 21.6, 23.3, 18.4, '-mass', 14.64645336391437, 14.64645336391437, 14.64645336391437, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 5, 6)
    ops.node(656, 24.9, 23.3, 18.4, '-mass', 14.64645336391437, 14.64645336391437, 14.64645336391437, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 5, 6)
    ops.node(756, 29.9, 23.3, 18.4, '-mass', 9.756651376146788, 9.756651376146788, 9.756651376146788, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 0, 7)
    ops.node(7, 0.0, 0.0, 21.4, '-mass', 9.756651376146788, 9.756651376146788, 9.756651376146788, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 0, 7)
    ops.node(107, 5.0, 0.0, 21.4, '-mass', 14.646453363914372, 14.646453363914372, 14.646453363914372, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 0, 7)
    ops.node(207, 8.3, 0.0, 21.4, '-mass', 14.646453363914372, 14.646453363914372, 14.646453363914372, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 0, 7)
    ops.node(307, 13.3, 0.0, 21.4, '-mass', 14.646453363914372, 14.646453363914372, 14.646453363914372, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 0, 7)
    ops.node(407, 16.6, 0.0, 21.4, '-mass', 14.646453363914372, 14.646453363914372, 14.646453363914372, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 0, 7)
    ops.node(507, 21.6, 0.0, 21.4, '-mass', 14.64645336391437, 14.64645336391437, 14.64645336391437, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 0, 7)
    ops.node(607, 24.9, 0.0, 21.4, '-mass', 14.64645336391437, 14.64645336391437, 14.64645336391437, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 0, 7)
    ops.node(707, 29.9, 0.0, 21.4, '-mass', 9.756651376146788, 9.756651376146788, 9.756651376146788, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 1, 7)
    ops.node(17, 0.0, 5.0, 21.4, '-mass', 17.822400611620793, 17.822400611620793, 17.822400611620793, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 1, 7)
    ops.node(117, 5.0, 5.0, 21.4, '-mass', 25.52308868501529, 25.52308868501529, 25.52308868501529, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 1, 7)
    ops.node(217, 8.3, 5.0, 21.4, '-mass', 25.52308868501529, 25.52308868501529, 25.52308868501529, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 1, 7)
    ops.node(317, 13.3, 5.0, 21.4, '-mass', 25.542201834862382, 25.542201834862382, 25.542201834862382, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 1, 7)
    ops.node(417, 16.6, 5.0, 21.4, '-mass', 26.459633027522933, 26.459633027522933, 26.459633027522933, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 1, 7)
    ops.node(517, 21.6, 5.0, 21.4, '-mass', 25.523088685015285, 25.523088685015285, 25.523088685015285, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 1, 7)
    ops.node(617, 24.9, 5.0, 21.4, '-mass', 25.523088685015285, 25.523088685015285, 25.523088685015285, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 1, 7)
    ops.node(717, 29.9, 5.0, 21.4, '-mass', 17.822400611620793, 17.822400611620793, 17.822400611620793, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 2, 7)
    ops.node(27, 0.0, 10.0, 21.4, '-mass', 14.168624617737004, 14.168624617737004, 14.168624617737004, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 2, 7)
    ops.node(127, 5.0, 10.0, 21.4, '-mass', 17.79209021406728, 17.79209021406728, 17.79209021406728, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 2, 7)
    ops.node(227, 8.3, 10.0, 21.4, '-mass', 17.79209021406728, 17.79209021406728, 17.79209021406728, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 2, 7)
    ops.node(327, 13.3, 10.0, 21.4, '-mass', 20.578000764525992, 20.578000764525992, 20.578000764525992, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 2, 7)
    ops.node(427, 16.6, 10.0, 21.4, '-mass', 20.578000764525992, 20.578000764525992, 20.578000764525992, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 2, 7)
    ops.node(527, 21.6, 10.0, 21.4, '-mass', 17.792090214067276, 17.792090214067276, 17.792090214067276, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 2, 7)
    ops.node(627, 24.9, 10.0, 21.4, '-mass', 17.792090214067276, 17.792090214067276, 17.792090214067276, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 2, 7)
    ops.node(727, 29.9, 10.0, 21.4, '-mass', 14.168624617737004, 14.168624617737004, 14.168624617737004, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 3, 7)
    ops.node(37, 0.0, 13.3, 21.4, '-mass', 14.168624617737004, 14.168624617737004, 14.168624617737004, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 3, 7)
    ops.node(137, 5.0, 13.3, 21.4, '-mass', 20.435501529051987, 20.435501529051987, 20.435501529051987, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 3, 7)
    ops.node(237, 8.3, 13.3, 21.4, '-mass', 20.435501529051987, 20.435501529051987, 20.435501529051987, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 3, 7)
    ops.node(337, 13.3, 13.3, 21.4, '-mass', 20.578000764525992, 20.578000764525992, 20.578000764525992, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 3, 7)
    ops.node(437, 16.6, 13.3, 21.4, '-mass', 20.578000764525992, 20.578000764525992, 20.578000764525992, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 3, 7)
    ops.node(537, 21.6, 13.3, 21.4, '-mass', 20.435501529051983, 20.435501529051983, 20.435501529051983, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 3, 7)
    ops.node(637, 24.9, 13.3, 21.4, '-mass', 20.435501529051983, 20.435501529051983, 20.435501529051983, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 3, 7)
    ops.node(737, 29.9, 13.3, 21.4, '-mass', 14.168624617737004, 14.168624617737004, 14.168624617737004, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 4, 7)
    ops.node(47, 0.0, 18.3, 21.4, '-mass', 17.822400611620793, 17.822400611620793, 17.822400611620793, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 4, 7)
    ops.node(147, 5.0, 18.3, 21.4, '-mass', 25.52308868501529, 25.52308868501529, 25.52308868501529, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 4, 7)
    ops.node(247, 8.3, 18.3, 21.4, '-mass', 25.52308868501529, 25.52308868501529, 25.52308868501529, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 4, 7)
    ops.node(347, 13.3, 18.3, 21.4, '-mass', 25.542201834862382, 25.542201834862382, 25.542201834862382, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 4, 7)
    ops.node(447, 16.6, 18.3, 21.4, '-mass', 26.459633027522933, 26.459633027522933, 26.459633027522933, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 4, 7)
    ops.node(547, 21.6, 18.3, 21.4, '-mass', 25.523088685015285, 25.523088685015285, 25.523088685015285, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 4, 7)
    ops.node(647, 24.9, 18.3, 21.4, '-mass', 25.523088685015285, 25.523088685015285, 25.523088685015285, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 4, 7)
    ops.node(747, 29.9, 18.3, 21.4, '-mass', 17.822400611620793, 17.822400611620793, 17.822400611620793, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 5, 7)
    ops.node(57, 0.0, 23.3, 21.4, '-mass', 9.756651376146788, 9.756651376146788, 9.756651376146788, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 5, 7)
    ops.node(157, 5.0, 23.3, 21.4, '-mass', 14.646453363914372, 14.646453363914372, 14.646453363914372, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 5, 7)
    ops.node(257, 8.3, 23.3, 21.4, '-mass', 14.646453363914372, 14.646453363914372, 14.646453363914372, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 5, 7)
    ops.node(357, 13.3, 23.3, 21.4, '-mass', 14.646453363914372, 14.646453363914372, 14.646453363914372, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 5, 7)
    ops.node(457, 16.6, 23.3, 21.4, '-mass', 14.646453363914372, 14.646453363914372, 14.646453363914372, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 5, 7)
    ops.node(557, 21.6, 23.3, 21.4, '-mass', 14.64645336391437, 14.64645336391437, 14.64645336391437, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 5, 7)
    ops.node(657, 24.9, 23.3, 21.4, '-mass', 14.64645336391437, 14.64645336391437, 14.64645336391437, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 5, 7)
    ops.node(757, 29.9, 23.3, 21.4, '-mass', 9.756651376146788, 9.756651376146788, 9.756651376146788, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 0, 8)
    ops.node(8, 0.0, 0.0, 24.4, '-mass', 7.874617737003057, 7.874617737003057, 7.874617737003057, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 0, 8)
    ops.node(108, 5.0, 0.0, 24.4, '-mass', 12.084575688073393, 12.084575688073393, 12.084575688073393, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 0, 8)
    ops.node(208, 8.3, 0.0, 24.4, '-mass', 12.084575688073393, 12.084575688073393, 12.084575688073393, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 0, 8)
    ops.node(308, 13.3, 0.0, 24.4, '-mass', 12.084575688073393, 12.084575688073393, 12.084575688073393, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 0, 8)
    ops.node(408, 16.6, 0.0, 24.4, '-mass', 12.084575688073393, 12.084575688073393, 12.084575688073393, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 0, 8)
    ops.node(508, 21.6, 0.0, 24.4, '-mass', 12.084575688073393, 12.084575688073393, 12.084575688073393, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 0, 8)
    ops.node(608, 24.9, 0.0, 24.4, '-mass', 12.084575688073393, 12.084575688073393, 12.084575688073393, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 0, 8)
    ops.node(708, 29.9, 0.0, 24.4, '-mass', 7.874617737003057, 7.874617737003057, 7.874617737003057, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 1, 8)
    ops.node(18, 0.0, 5.0, 24.4, '-mass', 14.965596330275227, 14.965596330275227, 14.965596330275227, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 1, 8)
    ops.node(118, 5.0, 5.0, 24.4, '-mass', 22.386850152905197, 22.386850152905197, 22.386850152905197, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 1, 8)
    ops.node(218, 8.3, 5.0, 24.4, '-mass', 22.386850152905197, 22.386850152905197, 22.386850152905197, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 1, 8)
    ops.node(318, 13.3, 5.0, 24.4, '-mass', 22.396406727828744, 22.396406727828744, 22.396406727828744, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 1, 8)
    ops.node(418, 16.6, 5.0, 24.4, '-mass', 22.85512232415902, 22.85512232415902, 22.85512232415902, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 1, 8)
    ops.node(518, 21.6, 5.0, 24.4, '-mass', 22.386850152905193, 22.386850152905193, 22.386850152905193, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 1, 8)
    ops.node(618, 24.9, 5.0, 24.4, '-mass', 22.386850152905193, 22.386850152905193, 22.386850152905193, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 1, 8)
    ops.node(718, 29.9, 5.0, 24.4, '-mass', 14.965596330275227, 14.965596330275227, 14.965596330275227, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 2, 8)
    ops.node(28, 0.0, 10.0, 24.4, '-mass', 11.84566131498471, 11.84566131498471, 11.84566131498471, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 2, 8)
    ops.node(128, 5.0, 10.0, 24.4, '-mass', 15.49178134556575, 15.49178134556575, 15.49178134556575, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 2, 8)
    ops.node(228, 8.3, 10.0, 24.4, '-mass', 15.49178134556575, 15.49178134556575, 15.49178134556575, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 2, 8)
    ops.node(328, 13.3, 10.0, 24.4, '-mass', 17.95651758409786, 17.95651758409786, 17.95651758409786, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 2, 8)
    ops.node(428, 16.6, 10.0, 24.4, '-mass', 17.95651758409786, 17.95651758409786, 17.95651758409786, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 2, 8)
    ops.node(528, 21.6, 10.0, 24.4, '-mass', 15.491781345565748, 15.491781345565748, 15.491781345565748, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 2, 8)
    ops.node(628, 24.9, 10.0, 24.4, '-mass', 15.491781345565748, 15.491781345565748, 15.491781345565748, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 2, 8)
    ops.node(728, 29.9, 10.0, 24.4, '-mass', 11.84566131498471, 11.84566131498471, 11.84566131498471, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 3, 8)
    ops.node(38, 0.0, 13.3, 24.4, '-mass', 11.845661314984708, 11.845661314984708, 11.845661314984708, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 3, 8)
    ops.node(138, 5.0, 13.3, 24.4, '-mass', 17.805581039755353, 17.805581039755353, 17.805581039755353, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 3, 8)
    ops.node(238, 8.3, 13.3, 24.4, '-mass', 17.805581039755353, 17.805581039755353, 17.805581039755353, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 3, 8)
    ops.node(338, 13.3, 13.3, 24.4, '-mass', 17.95651758409786, 17.95651758409786, 17.95651758409786, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 3, 8)
    ops.node(438, 16.6, 13.3, 24.4, '-mass', 17.95651758409786, 17.95651758409786, 17.95651758409786, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 3, 8)
    ops.node(538, 21.6, 13.3, 24.4, '-mass', 17.80558103975535, 17.80558103975535, 17.80558103975535, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 3, 8)
    ops.node(638, 24.9, 13.3, 24.4, '-mass', 17.80558103975535, 17.80558103975535, 17.80558103975535, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 3, 8)
    ops.node(738, 29.9, 13.3, 24.4, '-mass', 11.845661314984708, 11.845661314984708, 11.845661314984708, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 4, 8)
    ops.node(48, 0.0, 18.3, 24.4, '-mass', 14.965596330275227, 14.965596330275227, 14.965596330275227, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 4, 8)
    ops.node(148, 5.0, 18.3, 24.4, '-mass', 22.386850152905197, 22.386850152905197, 22.386850152905197, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 4, 8)
    ops.node(248, 8.3, 18.3, 24.4, '-mass', 22.386850152905197, 22.386850152905197, 22.386850152905197, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 4, 8)
    ops.node(348, 13.3, 18.3, 24.4, '-mass', 22.396406727828744, 22.396406727828744, 22.396406727828744, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 4, 8)
    ops.node(448, 16.6, 18.3, 24.4, '-mass', 22.85512232415902, 22.85512232415902, 22.85512232415902, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 4, 8)
    ops.node(548, 21.6, 18.3, 24.4, '-mass', 22.386850152905193, 22.386850152905193, 22.386850152905193, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 4, 8)
    ops.node(648, 24.9, 18.3, 24.4, '-mass', 22.386850152905193, 22.386850152905193, 22.386850152905193, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 4, 8)
    ops.node(748, 29.9, 18.3, 24.4, '-mass', 14.965596330275227, 14.965596330275227, 14.965596330275227, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (0, 5, 8)
    ops.node(58, 0.0, 23.3, 24.4, '-mass', 7.874617737003057, 7.874617737003057, 7.874617737003057, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (1, 5, 8)
    ops.node(158, 5.0, 23.3, 24.4, '-mass', 12.084575688073393, 12.084575688073393, 12.084575688073393, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (2, 5, 8)
    ops.node(258, 8.3, 23.3, 24.4, '-mass', 12.084575688073393, 12.084575688073393, 12.084575688073393, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (3, 5, 8)
    ops.node(358, 13.3, 23.3, 24.4, '-mass', 12.084575688073393, 12.084575688073393, 12.084575688073393, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (4, 5, 8)
    ops.node(458, 16.6, 23.3, 24.4, '-mass', 12.084575688073393, 12.084575688073393, 12.084575688073393, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (5, 5, 8)
    ops.node(558, 21.6, 23.3, 24.4, '-mass', 12.084575688073393, 12.084575688073393, 12.084575688073393, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (6, 5, 8)
    ops.node(658, 24.9, 23.3, 24.4, '-mass', 12.084575688073393, 12.084575688073393, 12.084575688073393, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid

    # Joint grid ids (x, y, z): (7, 5, 8)
    ops.node(758, 29.9, 23.3, 24.4, '-mass', 7.874617737003057, 7.874617737003057, 7.874617737003057, 0.0, 0.0, 0.0)
    # Joint flexibility model: rigid
