# Perform linear static analysis under gravity loads

# Add gravity time-series and load pattern to ops domain
timeSeries Linear 1
pattern Plain 1 1 {

    # Add beam gravity loads to ops domain
    eleLoad -ele 1001 -type -beamUniform -11.6788 0.0
    eleLoad -ele 1101 -type -beamUniform -2.5044 0.0
    eleLoad -ele 1201 -type -beamUniform -11.6788 0.0
    eleLoad -ele 1011 -type -beamUniform -19.1 0.0
    eleLoad -ele 1111 -type -beamUniform -22.973 0.0
    eleLoad -ele 1211 -type -beamUniform -19.1 0.0
    eleLoad -ele 1021 -type -beamUniform -11.6788 0.0
    eleLoad -ele 1121 -type -beamUniform -7.6518 0.0
    eleLoad -ele 1221 -type -beamUniform -11.6788 0.0
    eleLoad -ele 1002 -type -beamUniform -9.28 0.0
    eleLoad -ele 1102 -type -beamUniform -1.68 0.0
    eleLoad -ele 1202 -type -beamUniform -9.28 0.0
    eleLoad -ele 1012 -type -beamUniform -17.12 0.0
    eleLoad -ele 1112 -type -beamUniform -21.998 0.0
    eleLoad -ele 1212 -type -beamUniform -17.12 0.0
    eleLoad -ele 1022 -type -beamUniform -9.28 0.0
    eleLoad -ele 1122 -type -beamUniform -5.508 0.0
    eleLoad -ele 1222 -type -beamUniform -9.28 0.0
    eleLoad -ele 6200 -type -beamUniform -18.7544 0.0
    eleLoad -ele 6201 -type -beamUniform -18.5144 0.0
    eleLoad -ele 2001 -type -beamUniform -20.7488 0.0
    eleLoad -ele 2101 -type -beamUniform -19.7 0.0
    eleLoad -ele 2201 -type -beamUniform -19.7 0.0
    eleLoad -ele 2301 -type -beamUniform -20.7488 0.0
    eleLoad -ele 2011 -type -beamUniform -20.7488 0.0
    eleLoad -ele 2111 -type -beamUniform -31.28564 0.0
    eleLoad -ele 2211 -type -beamUniform -31.28564 0.0
    eleLoad -ele 2311 -type -beamUniform -20.7488 0.0
    eleLoad -ele 2002 -type -beamUniform -17.12 0.0
    eleLoad -ele 2102 -type -beamUniform -17.9 0.0
    eleLoad -ele 2202 -type -beamUniform -17.9 0.0
    eleLoad -ele 2302 -type -beamUniform -17.12 0.0
    eleLoad -ele 2012 -type -beamUniform -17.12 0.0
    eleLoad -ele 2112 -type -beamUniform -28.15904 0.0
    eleLoad -ele 2212 -type -beamUniform -28.15904 0.0
    eleLoad -ele 2312 -type -beamUniform -17.12 0.0

    # Add column gravity loads to ops domain
    load 70000 0.0 0.0 -2.25 0.0 0.0 0.0
    load 1 0.0 0.0 -2.25 0.0 0.0 0.0
    load 70300 0.0 0.0 -2.25 0.0 0.0 0.0
    load 301 0.0 0.0 -2.25 0.0 0.0 0.0
    load 70010 0.0 0.0 -2.25 0.0 0.0 0.0
    load 11 0.0 0.0 -2.25 0.0 0.0 0.0
    load 70110 0.0 0.0 -4.41 0.0 0.0 0.0
    load 111 0.0 0.0 -4.41 0.0 0.0 0.0
    load 70210 0.0 0.0 -4.41 0.0 0.0 0.0
    load 211 0.0 0.0 -4.41 0.0 0.0 0.0
    load 70310 0.0 0.0 -2.25 0.0 0.0 0.0
    load 311 0.0 0.0 -2.25 0.0 0.0 0.0
    load 70020 0.0 0.0 -2.25 0.0 0.0 0.0
    load 21 0.0 0.0 -2.25 0.0 0.0 0.0
    load 70120 0.0 0.0 -3.24 0.0 0.0 0.0
    load 121 0.0 0.0 -3.24 0.0 0.0 0.0
    load 70220 0.0 0.0 -3.24 0.0 0.0 0.0
    load 221 0.0 0.0 -3.24 0.0 0.0 0.0
    load 70320 0.0 0.0 -2.25 0.0 0.0 0.0
    load 321 0.0 0.0 -2.25 0.0 0.0 0.0
    load 1 0.0 0.0 -2.25 0.0 0.0 0.0
    load 2 0.0 0.0 -2.25 0.0 0.0 0.0
    load 301 0.0 0.0 -2.25 0.0 0.0 0.0
    load 302 0.0 0.0 -2.25 0.0 0.0 0.0
    load 11 0.0 0.0 -2.25 0.0 0.0 0.0
    load 12 0.0 0.0 -2.25 0.0 0.0 0.0
    load 111 0.0 0.0 -4.41 0.0 0.0 0.0
    load 112 0.0 0.0 -4.41 0.0 0.0 0.0
    load 211 0.0 0.0 -4.41 0.0 0.0 0.0
    load 212 0.0 0.0 -4.41 0.0 0.0 0.0
    load 311 0.0 0.0 -2.25 0.0 0.0 0.0
    load 312 0.0 0.0 -2.25 0.0 0.0 0.0
    load 21 0.0 0.0 -2.25 0.0 0.0 0.0
    load 22 0.0 0.0 -2.25 0.0 0.0 0.0
    load 121 0.0 0.0 -3.24 0.0 0.0 0.0
    load 122 0.0 0.0 -3.24 0.0 0.0 0.0
    load 221 0.0 0.0 -3.24 0.0 0.0 0.0
    load 222 0.0 0.0 -3.24 0.0 0.0 0.0
    load 321 0.0 0.0 -2.25 0.0 0.0 0.0
    load 322 0.0 0.0 -2.25 0.0 0.0 0.0
    load 70100 0.0 0.0 -1.125 0.0 0.0 0.0
    load 1101 0.0 0.0 -1.125 0.0 0.0 0.0
    load 1101 0.0 0.0 -1.125 0.0 0.0 0.0
    load 101 0.0 0.0 -1.125 0.0 0.0 0.0
    load 70200 0.0 0.0 -1.125 0.0 0.0 0.0
    load 1201 0.0 0.0 -1.125 0.0 0.0 0.0
    load 1201 0.0 0.0 -1.125 0.0 0.0 0.0
    load 201 0.0 0.0 -1.125 0.0 0.0 0.0
    load 101 0.0 0.0 -1.125 0.0 0.0 0.0
    load 1102 0.0 0.0 -1.125 0.0 0.0 0.0
    load 1102 0.0 0.0 -1.125 0.0 0.0 0.0
    load 102 0.0 0.0 -1.125 0.0 0.0 0.0
    load 201 0.0 0.0 -1.125 0.0 0.0 0.0
    load 1202 0.0 0.0 -1.125 0.0 0.0 0.0
    load 1202 0.0 0.0 -1.125 0.0 0.0 0.0
    load 202 0.0 0.0 -1.125 0.0 0.0 0.0
}

# Perform gravity analysis and save the model state
system UmfPack
numberer RCM
constraints Transformation
test NormDispIncr 1e-08 10 3
integrator LoadControl 0.1
algorithm Newton
analysis Static
analyze 10
loadConst -time 0.0
wipeAnalysis
