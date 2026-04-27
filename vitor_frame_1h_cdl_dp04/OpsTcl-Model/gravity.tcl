# Perform linear static analysis under gravity loads

# Add gravity time-series and load pattern to ops domain
timeSeries Linear 1
pattern Plain 1 1 {

    # Add beam gravity loads to ops domain
    eleLoad -ele 1001 -type -beamUniform -9.28 0.0
    eleLoad -ele 1101 -type -beamUniform -5.508 0.0
    eleLoad -ele 1201 -type -beamUniform -9.28 0.0
    eleLoad -ele 1011 -type -beamUniform -16.88 0.0
    eleLoad -ele 1111 -type -beamUniform -9.336 0.0
    eleLoad -ele 1211 -type -beamUniform -16.88 0.0
    eleLoad -ele 1021 -type -beamUniform -9.28 0.0
    eleLoad -ele 1121 -type -beamUniform -5.508 0.0
    eleLoad -ele 1221 -type -beamUniform -9.28 0.0
    eleLoad -ele 2001 -type -beamUniform -17.12 0.0
    eleLoad -ele 2101 -type -beamUniform -28.45904 0.0
    eleLoad -ele 2201 -type -beamUniform -28.45904 0.0
    eleLoad -ele 2301 -type -beamUniform -17.12 0.0
    eleLoad -ele 2011 -type -beamUniform -17.12 0.0
    eleLoad -ele 2111 -type -beamUniform -28.45904 0.0
    eleLoad -ele 2211 -type -beamUniform -28.45904 0.0
    eleLoad -ele 2311 -type -beamUniform -17.12 0.0

    # Add column gravity loads to ops domain
    load 70000 0.0 0.0 -2.25 0.0 0.0 0.0
    load 1 0.0 0.0 -2.25 0.0 0.0 0.0
    load 70100 0.0 0.0 -2.25 0.0 0.0 0.0
    load 101 0.0 0.0 -2.25 0.0 0.0 0.0
    load 70200 0.0 0.0 -2.25 0.0 0.0 0.0
    load 201 0.0 0.0 -2.25 0.0 0.0 0.0
    load 70300 0.0 0.0 -2.25 0.0 0.0 0.0
    load 301 0.0 0.0 -2.25 0.0 0.0 0.0
    load 70010 0.0 0.0 -2.25 0.0 0.0 0.0
    load 11 0.0 0.0 -2.25 0.0 0.0 0.0
    load 70110 0.0 0.0 -2.25 0.0 0.0 0.0
    load 111 0.0 0.0 -2.25 0.0 0.0 0.0
    load 70210 0.0 0.0 -2.25 0.0 0.0 0.0
    load 211 0.0 0.0 -2.25 0.0 0.0 0.0
    load 70310 0.0 0.0 -2.25 0.0 0.0 0.0
    load 311 0.0 0.0 -2.25 0.0 0.0 0.0
    load 70020 0.0 0.0 -2.25 0.0 0.0 0.0
    load 21 0.0 0.0 -2.25 0.0 0.0 0.0
    load 70120 0.0 0.0 -2.25 0.0 0.0 0.0
    load 121 0.0 0.0 -2.25 0.0 0.0 0.0
    load 70220 0.0 0.0 -2.25 0.0 0.0 0.0
    load 221 0.0 0.0 -2.25 0.0 0.0 0.0
    load 70320 0.0 0.0 -2.25 0.0 0.0 0.0
    load 321 0.0 0.0 -2.25 0.0 0.0 0.0
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
