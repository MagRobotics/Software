# MagRobot: An Open Simulation Platform for Magnetically Navigated Robots

# Overall
The major purpose of the proposed simulator is to facilitate the design and development of magnetic navigation systems for miniature medical robots. The simulator is built with physical models of magnetic systems and robot dynamics to accurately compute the behavior of magnetic navigation of various small-scale medical robots. 
     ![figure1](https://github.com/MagRobotics/software/assets/161809470/dce1c66f-0430-4126-bff3-49cb26c60ee3)


# Dependencies and Installation
Download the software package and decompress it. The download path does not contain Chinese

For Windows7 or later, ```python3.8``` can be installed

When installing ```python3.8```, select Add python to environment variables

If multiple python versions exist in the system, set 3.8 to the highest priority

If you are creating a python3.8 environment in conda, you need to set the ```PYTHONHOME``` environment variable

Install two third-party libraries for python
```
$ pip install numpy
$ pip install scipy
```
If you need other functions in the application software, install the corresponding third-party python library

# Running
Double-click the software to start using: ```bin/Release/MNSS.exe```

Please refer to the manual for details: ```manual.docx```

# Note
```Qt5WebEngineCore.dll``` in the bin\Release path needs to be downloaded with LFS to replace the pointer
