Serin
=====
Transfer files with an air swipe
----------------------------

Transfers files from a PC to another when hand is moved from first PC to another.
Works on computer vision using webcams networking.

###Dependencies

* [Python 2.7.*](http://www.python.org)
* [Numpy](http://www.numpy.org)
* **OpenCV** Python : See setup instructions [here](https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_setup/py_table_of_contents_setup/py_table_of_contents_setup.html#table-of-content-setup).

###Setting up

* **Make sure the computers are connected to a network**
* Start the `server.py` script at any one of the networked PC
* **OPTIONAL** : *Tune the minimum and maximum HSV values in `serin.py` to filter out skin color. Use the included `hsv_filter.py`*
* Start `serin.py`
* Fill in your server's ip in the window that pops up (for localhost leave it blank or fill 127.0.0.1) and submit

###Using

* Move hand in air either left or right.
* If no one is sending files then a prompt will ask you to choose the file.
* Do the same gesture at receiver's end and file will be transferred.
*(File transfer speed depends entirely on the network speed)*

###Working

* The image is converted from BGR to HSV Space for better filtering.
* Using specific HSV range, skin is filtered out and binarized.
* Morphological transformations enhances the chances of detection of hand as compared to face.
* Contours are searched and a contour with a minimum threshold area is worked on. The centroid of it gives the position of hand, which then is tracked.

#####Made possible using [OpenCV](http://www.opencv.org)

###License

BSD Licensed

Copyright (C) 2013 NebulaX
