# OctoROS
This projects aims to be a bridge between 3d printers and ROS. 
It uses OctoPrint to control the printer, and get the info that is sent to ROS topics. 


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

First you'll need to install OctoPrint, the instructions are available at https://github.com/foosel/OctoPrint. But the easiest way that I see is with the following instructions

1. Checkout OctoPrint:  ```$ git clone https://github.com/foosel/OctoPrint.git```
2. Change into the OctoPrint folder: ```$ cd OctoPrint```
3. Create a user-owned virtual environment therein: ```$ virtualenv venv```
4. Install OctoPrint into that virtual environment: ```$ ./venv/bin/pip install .```
5. After installing OctoPrint, you should run it using:```$ octoprint serve```   
6. Now you should verify your installation opening a web browser and going to http://localhost:5000
7. If everything went right you should see the OctoPrint home screen  

If the printer that you're using is a MakerBot, now it's time to install the GPX plug-in, that will enable us to to send gcode to octoprint, that will take care of the conversion to x3g. To that do the following:
1. In the octoPrint home screen go to configurations/Plugin manager/Get More
2. Search for GPX and click install 
3. Go to GPX settings and click enable GPX
4. Choose your machine, gcode flavor and other settings


### Installing

This project should be run from source, to do so just go to your ROS workspace and clone it with ```git clone https://github.com/ielson/octoROS.git```. After that you can't forget to make the file executable, or ROS won't find it.

### Usage
To use it, you need to have your octoprint server running, have a model uploaded to it, and then run the octoROS.py file, changing the file name in the 59th line to the uploaded file name. 

So it will start printing the model and outputting the progress and some printer measurements to the ```/printer3d``` ROS topic until finish printing. When it happens the file will send a boolean to ```printer3d/finishedPrinting```.

Example of usage:
```
$ roscore
# in another terminal run 
$ rosrun octoROS octoROS.py 


```
```
Give an example
```


## Authors

* **Daniel Mascarenhas** - *Initial work* - [ielson](https://github.com/ielson)

See also the list of [contributors](https://github.com/ielson/octoROS/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Many thank to the octoprint team, that made this awesome software