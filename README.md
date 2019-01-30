# rpi-pmsensor-tw
Python 3 scripts to send pm 2.5 and pm 10 sensors values to twitter

  
Sensor abstraction library
https://github.com/ikalchev/py-sds011

    cd py-sds011/
    pip install .
    apt install libatlas3-base python3
    update-alternatives --list python
    update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
    update-alternatives --install /usr/bin/python python /usr/bin/python3 1
    update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
    update-alternatives --install /usr/bin/python python /usr/bin/python3 2
    update-alternatives --install /usr/bin/python python /usr/bin/python3.5 3
    update-alternatives --install /usr/bin/python python /usr/bin/python2 4
    update-alternatives --config python
    pip install matplotlib
    pip install -U numpy
    pip install tweepy
