# intruderdet

This is a simple intrusion detection system that uses OpenCV.
In this version, the script is comparing consecutive frames by simply subtracting them. Any movement will create a large amplitude variation on the pixel values and the program will save the frame along with a timestamp.
