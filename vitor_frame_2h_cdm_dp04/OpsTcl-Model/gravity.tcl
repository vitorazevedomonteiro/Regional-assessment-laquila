# Perform linear static analysis under gravity loads

# Add gravity time-series and load pattern to ops domain
timeSeries Linear 1
pattern Plain 1 1 {

    # Add beam gravity loads to ops domain
    eleLoad -ele 1001 -type -beamUniform -13.0238 0.0
    eleLoad -ele 1101 -type -beamUniform -3.6369 0.0
    eleLoad -ele 1201 -type -beamUniform -13.0238 0.0
    eleLoad -ele 1011 -type -beamUniform -19.9375 0.0
    eleLoad -ele 1111 -type -beamUniform -23.85125 0.0
    eleLoad -ele 1211 -type -beamUniform -19.9375 0.0
    eleLoad -ele 1021 -type -beamUniform -13.0238 0.0
    eleLoad -ele 1121 -type -beamUniform -8.87505 0.0
    eleLoad -ele 1221 -type -beamUniform -13.0238 0.0
    eleLoad -ele 1002 -type -beamUniform -10.625 0.0
    eleLoad -ele 1102 -type -beamUniform -2.8125 0.0
    eleLoad -ele 1202 -type -beamUniform -10.625 0.0
    eleLoad -ele 1012 -type -beamUniform -18.4375 0.0
    eleLoad -ele 1112 -type -beamUniform -23.35625 0.0
    eleLoad -ele 1212 -type -beamUniform -18.4375 0.0
    eleLoad -ele 1022 -type -beamUniform -10.625 0.0
    eleLoad -ele 1122 -type -beamUniform -6.73125 0.0
    eleLoad -ele 1222 -type -beamUniform -10.625 0.0
    eleLoad -ele 6200 -type -beamUniform -19.3244 0.0
    eleLoad -ele 6201 -type -beamUniform -19.3244 0.0
    eleLoad -ele 2001 -type -beamUniform -21.5863 0.0
    eleLoad -ele 2101 -type -beamUniform -19.9375 0.0
    eleLoad -ele 2201 -type -beamUniform -19.9375 0.0
    eleLoad -ele 2301 -type -beamUniform -21.5863 0.0
    eleLoad -ele 2011 -type -beamUniform -21.5863 0.0
    eleLoad -ele 2111 -type -beamUniform -31.76635 0.0
    eleLoad -ele 2211 -type -beamUniform -31.76635 0.0
    eleLoad -ele 2311 -type -beamUniform -21.5863 0.0
    eleLoad -ele 2002 -type -beamUniform -18.4375 0.0
    eleLoad -ele 2102 -type -beamUniform -18.4375 0.0
    eleLoad -ele 2202 -type -beamUniform -18.4375 0.0
    eleLoad -ele 2302 -type -beamUniform -18.4375 0.0
    eleLoad -ele 2012 -type -beamUniform -18.4375 0.0
    eleLoad -ele 2112 -type -beamUniform -28.93975 0.0
    eleLoad -ele 2212 -type -beamUniform -28.93975 0.0
    eleLoad -ele 2312 -type -beamUniform -18.4375 0.0

    # Add column gravity loads to ops domain
    load 70000 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 1 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 70300 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 301 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 70010 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 11 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 70110 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 111 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 70210 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 211 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 70310 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 311 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 70020 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 21 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 70120 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 121 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 70220 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 221 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 70320 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 321 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 1 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 2 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 301 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 302 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 11 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 12 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 111 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 112 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 211 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 212 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 311 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 312 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 21 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 22 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 121 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 122 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 221 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 222 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 321 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 322 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 70100 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 1101 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 1101 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 101 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 70200 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 1201 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 1201 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 201 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 101 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 1102 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 1102 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 102 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 201 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 1202 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 1202 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 202 0.0 0.0 -1.171875 0.0 0.0 0.0
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
