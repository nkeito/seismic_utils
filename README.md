# Introduction

seismic_utils is a set of codes to complement the docker container with the same name.

## Installation

# Docker image
Install docker as ussual, then execute to download the docker image
```
docker pull aneria/seismic_utils
```


## Ussage
Currently the code only handles the training and testing of a NN whose input data is a matrix in the form [X,Y]


## Test the code
```
cd seismic_utils/
# To train a NN
python3 run_training_testing.py -e ./test_data/settingsForTrainingAndTesting.txt
# To test a NN with the best model
python3 run_training_testing.py -p ./test_data/settingsForTrainingAndTesting.txt
```
The model weitghts are stored in the folder ./test_data/DNNRegressors

