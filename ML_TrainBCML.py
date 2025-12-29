import tensorflow as tf
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt

# Function to read the large file
def iter_loadtxt(filename, delimiter=',', skiprows=0, dtype=float):
    print('File Reading Start')
    def iter_func():
        with open(filename, 'r') as infile:
            for _ in range(skiprows):
                next(infile)
            for line in infile:
                line = line.rstrip().split(delimiter)
                for item in line:
                    yield dtype(item)
        iter_loadtxt.rowlength = len(line)

    data = np.fromiter(iter_func(), dtype=dtype)
    data = data.reshape((-1, iter_loadtxt.rowlength))
    return data
    
VelocityNormalization = 2616.76359868
PressureNormalization = 76.104
TemperatureNormalization = 245.1274

# Replace the InputFile.txt with actual data file
X = iter_loadtxt("InputFile.txt", delimiter=' ',skiprows=0,dtype=float)

print('File reading done')

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

	

# Normalization of the input Dirichlet Boundary condition values
X[:,1] /= VelocityNormalization
X[:,2] /= VelocityNormalization
X[:,3] /= PressureNormalization
X[:,4] /= TemperatureNormalization

X[:,10] /= VelocityNormalization
X[:,11] /= VelocityNormalization
X[:,12] /= PressureNormalization
X[:,13] /= TemperatureNormalization

X[:,19] /= VelocityNormalization
X[:,20] /= VelocityNormalization
X[:,21] /= PressureNormalization
X[:,22] /= TemperatureNormalization

X[:,28] /= VelocityNormalization
X[:,29] /= VelocityNormalization
X[:,30] /= PressureNormalization
X[:,31] /= TemperatureNormalization

X[:,37] /= VelocityNormalization
X[:,38] /= VelocityNormalization
X[:,39] /= PressureNormalization
X[:,40] /= TemperatureNormalization

X[:,46] /= VelocityNormalization
X[:,47] /= VelocityNormalization
X[:,48] /= PressureNormalization
X[:,49] /= TemperatureNormalization

X[:,55] /= VelocityNormalization
X[:,56] /= VelocityNormalization
X[:,57] /= PressureNormalization
X[:,58] /= TemperatureNormalization

X[:,64] /= VelocityNormalization
X[:,65] /= VelocityNormalization
X[:,66] /= PressureNormalization
X[:,67] /= TemperatureNormalization

X[:,73] /= VelocityNormalization
X[:,74] /= VelocityNormalization
X[:,75] /= PressureNormalization
X[:,76] /= TemperatureNormalization

X[:,82] /= VelocityNormalization
X[:,83] /= VelocityNormalization
X[:,84] /= PressureNormalization
X[:,85] /= TemperatureNormalization

X[:,91] /= VelocityNormalization
X[:,92] /= VelocityNormalization
X[:,93] /= PressureNormalization
X[:,94] /= TemperatureNormalization

X[:,100] /= VelocityNormalization
X[:,101] /= VelocityNormalization
X[:,102] /= PressureNormalization
X[:,103] /= TemperatureNormalization

X[:,109] /= VelocityNormalization
X[:,110] /= VelocityNormalization
X[:,111] /= PressureNormalization
X[:,112] /= TemperatureNormalization

X[:,118] /= VelocityNormalization
X[:,119] /= VelocityNormalization
X[:,120] /= PressureNormalization
X[:,121] /= TemperatureNormalization

X[:,127] /= VelocityNormalization
X[:,128] /= VelocityNormalization
X[:,129] /= PressureNormalization
X[:,130] /= TemperatureNormalization

X[:,136] /= VelocityNormalization
X[:,137] /= VelocityNormalization
X[:,138] /= PressureNormalization
X[:,139] /= TemperatureNormalization



# Replace the OutputFile.txt with actual data file
Y = iter_loadtxt("OutputFile.txt", delimiter=' ',skiprows=0,dtype=float)

# Normalization of the output values
Y[:,0] /= VelocityNormalization
Y[:,1] /= VelocityNormalization
Y[:,2] /= PressureNormalization
Y[:,3] /= TemperatureNormalization

# Testing Data
Xreal = X[5::1000,:]
Yreal = Y[5::1000,:]

# BCML DNN Model
model = Sequential()
model.add(Dense(144, input_dim=144, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(4, activation='linear'))

# Training and compiling the BCML Model
model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])
nepoch = 500
nbatch = 32768
model.fit(X, Y, epochs=nepoch, batch_size=nbatch)
Ylearn = model.predict(Xreal)
score = model.evaluate(Xreal, Yreal, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# Generation of the final BCML model and saving in keras format 
model.save('model16GenObjC2802a.keras')


