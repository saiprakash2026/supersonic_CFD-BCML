import tensorflow as tf
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt


# Normalization Parameters
VelocityNormalization = 2616.76359868
PressureNormalization = 500.00
TemperatureNormalization = 1000.00

# Input File of an Arbitrary problem/mesh
X = np.genfromtxt("InputFileWith16Generators_Validation.txt")

dia=1.0
X[:,0] /= dia; X[:,9] /= dia; X[:,18] /= dia; X[:,27] /= dia; X[:,36] /= dia; X[:,45] /= dia; 
X[:,54] /= dia; X[:,63] /= dia; X[:,72] /= dia; X[:,81] /= dia; X[:,90] /= dia; X[:,99] /= dia; 
X[:,108] /= dia; X[:,117] /= dia; X[:,126] /= dia; X[:,135] /= dia

# Calculate Distance function from the length of the generator
X[:,0] = np.exp((-X[:,0]**0.5)*2)
X[:,9] = np.exp((-X[:,9]**0.5)*2)
X[:,18] = np.exp((-X[:,18]**0.5)*2)
X[:,27] = np.exp((-X[:,27]**0.5)*2)
X[:,36] = np.exp((-X[:,36]**0.5)*2)
X[:,45] = np.exp((-X[:,45]**0.5)*2)
X[:,54] = np.exp((-X[:,54]**0.5)*2)
X[:,63] = np.exp((-X[:,63]**0.5)*2)
X[:,72] = np.exp((-X[:,72]**0.5)*2)
X[:,81] = np.exp((-X[:,81]**0.5)*2)
X[:,90] = np.exp((-X[:,90]**0.5)*2)
X[:,99] = np.exp((-X[:,99]**0.5)*2)
X[:,108] = np.exp((-X[:,108]**0.5)*2)
X[:,117] = np.exp((-X[:,117]**0.5)*2)
X[:,126] = np.exp((-X[:,126]**0.5)*2)
X[:,135] = np.exp((-X[:,135]**0.5)*2)


# 1st Generator Dirichlet Boundary Condition Normalization
X[:,1] /= VelocityNormalization
X[:,2] /= VelocityNormalization
X[:,3] /= PressureNormalization
X[:,4] /= TemperatureNormalization

# 2nd Generator Dirichlet Boundary Condition Normalization
X[:,10] /= VelocityNormalization
X[:,11] /= VelocityNormalization
X[:,12] /= PressureNormalization
X[:,13] /= TemperatureNormalization

# 3rd Generator Dirichlet Boundary Condition Normalization
X[:,19] /= VelocityNormalization
X[:,20] /= VelocityNormalization
X[:,21] /= PressureNormalization
X[:,22] /= TemperatureNormalization

#4th Generator Dirichlet Boundary Condition Normalization
X[:,28] /= VelocityNormalization
X[:,29] /= VelocityNormalization
X[:,30] /= PressureNormalization
X[:,31] /= TemperatureNormalization

#5th Generator Dirichlet Boundary Condition Normalization
X[:,37] /= VelocityNormalization
X[:,38] /= VelocityNormalization
X[:,39] /= PressureNormalization
X[:,40] /= TemperatureNormalization

#6th Generator Dirichlet Boundary Condition Normalization

X[:,46] /= VelocityNormalization
X[:,47] /= VelocityNormalization
X[:,48] /= PressureNormalization
X[:,49] /= TemperatureNormalization

#7th Generator Dirichlet Boundary Condition Normalization
X[:,55] /= VelocityNormalization
X[:,56] /= VelocityNormalization
X[:,57] /= PressureNormalization
X[:,58] /= TemperatureNormalization

#8th Generator Dirichlet Boundary Condition Normalization
X[:,64] /= VelocityNormalization
X[:,65] /= VelocityNormalization
X[:,66] /= PressureNormalization
X[:,67] /= TemperatureNormalization

#9th Generator Dirichlet Boundary Condition Normalization
X[:,73] /= VelocityNormalization
X[:,74] /= VelocityNormalization
X[:,75] /= PressureNormalization
X[:,76] /= TemperatureNormalization

#10th Generator Dirichlet Boundary Condition Normalization
X[:,82] /= VelocityNormalization
X[:,83] /= VelocityNormalization
X[:,84] /= PressureNormalization
X[:,85] /= TemperatureNormalization

#11th Generator Dirichlet Boundary Condition Normalization
X[:,91] /= VelocityNormalization
X[:,92] /= VelocityNormalization
X[:,93] /= PressureNormalization
X[:,94] /= TemperatureNormalization

#12th Generator Dirichlet Boundary Condition Normalization
X[:,100] /= VelocityNormalization
X[:,101] /= VelocityNormalization
X[:,102] /= PressureNormalization
X[:,103] /= TemperatureNormalization

#13th Generator Dirichlet Boundary Condition Normalization
X[:,109] /= VelocityNormalization
X[:,110] /= VelocityNormalization
X[:,111] /= PressureNormalization
X[:,112] /= TemperatureNormalization

#14th Generator Dirichlet Boundary Condition Normalization
X[:,118] /= VelocityNormalization
X[:,119] /= VelocityNormalization
X[:,120] /= PressureNormalization
X[:,121] /= TemperatureNormalization

#15th Generator Dirichlet Boundary Condition Normalization
X[:,127] /= VelocityNormalization
X[:,128] /= VelocityNormalization
X[:,129] /= PressureNormalization
X[:,130] /= TemperatureNormalization

#16th Generator Dirichlet Boundary Condition Normalization
X[:,136] /= VelocityNormalization
X[:,137] /= VelocityNormalization
X[:,138] /= PressureNormalization
X[:,139] /= TemperatureNormalization


# Running ML Model for the Input
model = tf.keras.models.load_model('model16GenObjC3012a.keras')
Ypred = model.predict(X)

# De-Normalization of the ML Predicted Values
Ypred[:,0] *= VelocityNormalization
Ypred[:,1] *= VelocityNormalization
Ypred[:,2] *= PressureNormalization
Ypred[:,3] *= TemperatureNormalization

# Writing data in OpenFOAM compatible form so that we can use Paraview.

# Writing the Pressure File
filePressure = open('p', 'w')
filePressure.write(""+'\n')

filePressure.write("/*--------------------------------*- C++ -*----------------------------------*\\"+'\n')
filePressure.write("| =========                 |                                                 |"+'\n')
filePressure.write("| \\      /  F ield         | foam-extend: Open Source CFD                    |"+'\n')
filePressure.write("|  \\    /   O peration     | Version:     4.1                                |"+'\n')
filePressure.write("|   \\  /    A nd           | Web:         http://www.foam-extend.org         |"+'\n')
filePressure.write("|    \\/     M anipulation  |                                                 |"+'\n')
filePressure.write("\\*---------------------------------------------------------------------------*/"+'\n')
filePressure.write("FoamFile"+'\n')
filePressure.write("{"+'\n')
filePressure.write("    version     2.0;"+'\n')
filePressure.write("    format      ascii;"+'\n')
filePressure.write("    class       volScalarField;"+'\n')
filePressure.write("    location    \"0.10\";"+'\n')
filePressure.write("    object      p;"+'\n')
filePressure.write("}"+'\n')
filePressure.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //"+'\n')
filePressure.write(""+'\n')
filePressure.write("dimensions      [1 -1 -2 0 0 0 0];"+'\n')
filePressure.write(""+'\n')
filePressure.write("internalField   nonuniform List<scalar> "+'\n')
filePressure.write("214244"+'\n')
filePressure.write("("+'\n')

for i in range(214244):
	filePressure.write(str(Ypred[i,2])+'\n')

filePressure.write(")"+'\n')
filePressure.write(";"+'\n')
filePressure.write(""+'\n')
filePressure.write("boundaryField"+'\n')
filePressure.write("{"+'\n')
filePressure.write("    inlet"+'\n')
filePressure.write("    {"+'\n')
filePressure.write("        type            supersonicInlet;"+'\n')
filePressure.write("        value           uniform 26.157;"+'\n')
filePressure.write("    }"+'\n')
filePressure.write("    outlet1"+'\n')
filePressure.write("    {"+'\n')
filePressure.write("        type            zeroGradient;"+'\n')
filePressure.write("    }"+'\n')
filePressure.write("    outlet2"+'\n')
filePressure.write("    {"+'\n')
filePressure.write("        type            zeroGradient;"+'\n')
filePressure.write("    }"+'\n')
filePressure.write("    outlet3"+'\n')
filePressure.write("    {"+'\n')
filePressure.write("        type            zeroGradient;"+'\n')
filePressure.write("    }"+'\n')
filePressure.write("    wall1"+'\n')
filePressure.write("    {"+'\n')
filePressure.write("        type            diffusedWall;"+'\n')
filePressure.write("        value           uniform 101325;"+'\n')
filePressure.write("    }"+'\n')
filePressure.write("    wall2"+'\n')
filePressure.write("    {"+'\n')
filePressure.write("        type            diffusedWall;"+'\n')
filePressure.write("        value           uniform 101325;"+'\n')
filePressure.write("    }"+'\n')
filePressure.write("    defaultFaces"+'\n')
filePressure.write("    {"+'\n')
filePressure.write("        type            empty;"+'\n')
filePressure.write("    }"+'\n')
filePressure.write("}"+'\n')
filePressure.write(""+'\n')
filePressure.write(""+'\n')
filePressure.write("// ************************************************************************* //"+'\n')
filePressure.write(""+'\n')
filePressure.close()


# Writing the Temperature File
fileTemperature = open('Ttrans', 'w')
fileTemperature.write(""+'\n')

fileTemperature.write("/*--------------------------------*- C++ -*----------------------------------*\\"+'\n')
fileTemperature.write("| =========                 |                                                 |"+'\n')
fileTemperature.write("| \\      /  F ield         | foam-extend: Open Source CFD                    |"+'\n')
fileTemperature.write("|  \\    /   O peration     | Version:     4.1                                |"+'\n')
fileTemperature.write("|   \\  /    A nd           | Web:         http://www.foam-extend.org         |"+'\n')
fileTemperature.write("|    \\/     M anipulation  |                                                 |"+'\n')
fileTemperature.write("\\*---------------------------------------------------------------------------*/"+'\n')
fileTemperature.write("FoamFile"+'\n')
fileTemperature.write("{"+'\n')
fileTemperature.write("    version     2.0;"+'\n')
fileTemperature.write("    format      ascii;"+'\n')
fileTemperature.write("    class       volScalarField;"+'\n')
fileTemperature.write("    location    \"0.10\";"+'\n')
fileTemperature.write("    object      Ttrans;"+'\n')
fileTemperature.write("}"+'\n')
fileTemperature.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //"+'\n')
fileTemperature.write(""+'\n')
fileTemperature.write("dimensions      [0 0 0 1 0 0 0];"+'\n')
fileTemperature.write(""+'\n')
fileTemperature.write("internalField   nonuniform List<scalar> "+'\n')
fileTemperature.write("214244"+'\n')
fileTemperature.write("("+'\n')

for i in range(214244):
	fileTemperature.write(str(Ypred[i,3])+'\n')

fileTemperature.write(")"+'\n')
fileTemperature.write(";"+'\n')
fileTemperature.write(""+'\n')
fileTemperature.write("boundaryField"+'\n')
fileTemperature.write("{"+'\n')
fileTemperature.write("    inlet"+'\n')
fileTemperature.write("    {"+'\n')
fileTemperature.write("        type            supersonicInlet;"+'\n')
fileTemperature.write("        value           uniform 245.1274;"+'\n')
fileTemperature.write("    }"+'\n')
fileTemperature.write("    outlet1"+'\n')
fileTemperature.write("    {"+'\n')
fileTemperature.write("        type            zeroGradient;"+'\n')
fileTemperature.write("    }"+'\n')
fileTemperature.write("    outlet2"+'\n')
fileTemperature.write("    {"+'\n')
fileTemperature.write("        type            zeroGradient;"+'\n')
fileTemperature.write("    }"+'\n')
fileTemperature.write("    outlet3"+'\n')
fileTemperature.write("    {"+'\n')
fileTemperature.write("        type            zeroGradient;"+'\n')
fileTemperature.write("    }"+'\n')
fileTemperature.write("    wall1"+'\n')
fileTemperature.write("    {"+'\n')
fileTemperature.write("        type            diffusedWall;"+'\n')
fileTemperature.write("        value           uniform 750;"+'\n')
fileTemperature.write("    }"+'\n')
fileTemperature.write("    wall2"+'\n')
fileTemperature.write("    {"+'\n')
fileTemperature.write("        type            diffusedWall;"+'\n')
fileTemperature.write("        value           uniform 750;"+'\n')
fileTemperature.write("    }"+'\n')
fileTemperature.write("    defaultFaces"+'\n')
fileTemperature.write("    {"+'\n')
fileTemperature.write("        type            empty;"+'\n')
fileTemperature.write("    }"+'\n')
fileTemperature.write("}"+'\n')
fileTemperature.write(""+'\n')
fileTemperature.write(""+'\n')
fileTemperature.write("// ************************************************************************* //"+'\n')
fileTemperature.write(""+'\n')
fileTemperature.close()


# Writing the Velocity File
fileVelocity = open('U', 'w')
fileVelocity.write(""+'\n')

fileVelocity.write("/*--------------------------------*- C++ -*----------------------------------*\\"+'\n')
fileVelocity.write("| =========                 |                                                 |"+'\n')
fileVelocity.write("| \\      /  F ield         | foam-extend: Open Source CFD                    |"+'\n')
fileVelocity.write("|  \\    /   O peration     | Version:     4.1                                |"+'\n')
fileVelocity.write("|   \\  /    A nd           | Web:         http://www.foam-extend.org         |"+'\n')
fileVelocity.write("|    \\/     M anipulation  |                                                 |"+'\n')
fileVelocity.write("\\*---------------------------------------------------------------------------*/"+'\n')
fileVelocity.write("FoamFile"+'\n')
fileVelocity.write("{"+'\n')
fileVelocity.write("    version     2.0;"+'\n')
fileVelocity.write("    format      ascii;"+'\n')
fileVelocity.write("    class       volVectorField;"+'\n')
fileVelocity.write("    location    \"0.10\";"+'\n')
fileVelocity.write("    object      U;"+'\n')
fileVelocity.write("}"+'\n')
fileVelocity.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //"+'\n')
fileVelocity.write(""+'\n')
fileVelocity.write("dimensions      [1 -1 0 0 0 0 0];"+'\n')
fileVelocity.write(""+'\n')
fileVelocity.write("internalField   nonuniform List<vector> "+'\n')
fileVelocity.write("214244"+'\n')
fileVelocity.write("("+'\n')

for i in range(214244):
	fileVelocity.write('('+str(Ypred[i,0])+'\t'+str(Ypred[i,1])+'\t 0)'+'\n')

fileVelocity.write(")"+'\n')
fileVelocity.write(";"+'\n')
fileVelocity.write(""+'\n')
fileVelocity.write("boundaryField"+'\n')
fileVelocity.write("{"+'\n')
fileVelocity.write("    inlet"+'\n')
fileVelocity.write("    {"+'\n')
fileVelocity.write("        type            supersonicInlet;"+'\n')
fileVelocity.write("        value           uniform (1862.5024 0 0);"+'\n')
fileVelocity.write("    }"+'\n')
fileVelocity.write("    outlet1"+'\n')
fileVelocity.write("    {"+'\n')
fileVelocity.write("        type            zeroGradient;"+'\n')
fileVelocity.write("    }"+'\n')
fileVelocity.write("    outlet2"+'\n')
fileVelocity.write("    {"+'\n')
fileVelocity.write("        type            zeroGradient;"+'\n')
fileVelocity.write("    }"+'\n')
fileVelocity.write("    outlet3"+'\n')
fileVelocity.write("    {"+'\n')
fileVelocity.write("        type            zeroGradient;"+'\n')
fileVelocity.write("    }"+'\n')
fileVelocity.write("    wall1"+'\n')
fileVelocity.write("    {"+'\n')
fileVelocity.write("        type            diffusedWall;"+'\n')
fileVelocity.write("        value           uniform (0 0 0);"+'\n')
fileVelocity.write("    }"+'\n')
fileVelocity.write("    wall2"+'\n')
fileVelocity.write("    {"+'\n')
fileVelocity.write("        type            diffusedWall;"+'\n')
fileVelocity.write("        value           uniform (0 0 0);"+'\n')
fileVelocity.write("    }"+'\n')
fileVelocity.write("    defaultFaces"+'\n')
fileVelocity.write("    {"+'\n')
fileVelocity.write("        type            empty;"+'\n')
fileVelocity.write("    }"+'\n')
fileVelocity.write("}"+'\n')
fileVelocity.write(""+'\n')
fileVelocity.write(""+'\n')
fileVelocity.write("// ************************************************************************* //"+'\n')
fileVelocity.write(""+'\n')
fileVelocity.close()


# Copy paste p Ttrans and U files into FVM Case folder.
