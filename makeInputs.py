#! usr/bin/env python
import math

# angular range: +- 0.15 degrees.
# G4Beamline scripts expect mrad

subBase = "mu2eg4bl --in={0} --tar=Geometry.tar --njobs=20 --events-per-job=50000 --jobname=angleEdge_{0} --g4bl-version=v2_16a --outstage=/pnfs/mu2e/scratch/outstage;\nsleep 1;\n"

degtomrad = 1000*math.pi/180

class SteerParams:
	def __init__(self):
		self.dxBeamAtTarget = 0.0
		self.dyBeamAtTarget = 0.0
		self.dxBendInPlane = 0.0
		self.dyBendInPlane = 0.0
		self.realAngle = 0.0

# middle
params0 = SteerParams()
params0.realAngle = 0.0
params0.dxBeamAtTarget = 3.125
params0.dyBeamAtTarget = 0.7056
params0.dxBendInPlane = -0.04405
params0.dyBendInPlane = 0.2542

# extrema
params1 = SteerParams()
params1.realAngle = 2.618
params1.dxBeamAtTarget = 3.458
params1.dyBeamAtTarget = 0.6790
params1.dxBendInPlane = 2.533
params1.dyBendInPlane = 0.5839

params2 = SteerParams()
params2.realAngle = -2.618
params2.dxBeamAtTarget = 2.792
params2.dyBeamAtTarget = 0.7322
params2.dxBendInPlane = -2.621
params2.dyBendInPlane = -0.07559

# halfway values
params3 = SteerParams()
params3.realAngle = 1.309
params3.dxBeamAtTarget = 3.291
params3.dyBeamAtTarget = 0.6923
params3.dxBendInPlane = 1.245
params3.dyBendInPlane = 0.4190

params4 = SteerParams()
params4.realAngle = -1.309
params4.dxBeamAtTarget = 2.958
params4.dyBeamAtTarget = 0.7189
params4.dxBendInPlane = -1.333
params4.dyBendInPlane = 0.08928

# quarter values
params5 = SteerParams()
params5.realAngle = 0.6545
params5.dxBeamAtTarget = 3.208
params5.dyBeamAtTarget = 0.6989
params5.dxBendInPlane = 0.6003
params5.dyBendInPlane = 0.3366

params6 = SteerParams()
params6.realAngle = -0.6545
params6.dxBeamAtTarget = 3.041
params6.dyBeamAtTarget = 0.7122
params6.dxBendInPlane = -0.6884
params6.dyBendInPlane = 0.1717

# three-quarter values
params7 = SteerParams()
params7.realAngle = 1.964
params7.dxBeamAtTarget = 3.374
params7.dyBeamAtTarget = 0.6857
params7.dxBendInPlane = 1.889
params7.dyBendInPlane = 0.5015

params8 = SteerParams()
params8.realAngle = -1.964
params8.dxBeamAtTarget = 2.875
params8.dyBeamAtTarget = 0.7255
params8.dxBendInPlane = -1.977
params8.dyBendInPlane = 0.006845




orig = open("minimalMu2E.in", 'r')
origTxt = orig.readlines()

subFile = open("submitAll.sh", 'w')
subFile.write("#! bin/bash\n\n")

for paramSet in [params0, params1, params2, params3, params4, params5, params6, params7, params8]:
	confFileName = "xAngle_{0}mrad.in".format(paramSet.realAngle)
	out = open(confFileName, 'w')
	for line0 in origTxt:
		line1 = line0.replace("dxBeamAtTarget=0", "dxBeamAtTarget={0} # mm".format(paramSet.dxBeamAtTarget))
		line2 = line1.replace("dyBeamAtTarget=0", "dyBeamAtTarget={0} # mm".format(paramSet.dyBeamAtTarget))
		line3 = line2.replace("dxBendInPlane=0", "dxBendInPlane={0} # mrad".format(paramSet.dxBendInPlane))
		line4 = line3.replace("dyBendInPlane=0", "dyBendInPlane={0} # mrad".format(paramSet.dyBendInPlane))
		out.write(line4)
	out.close()
	subLine = subBase.format(confFileName)
	subFile.write(subLine)
subFile.close()

