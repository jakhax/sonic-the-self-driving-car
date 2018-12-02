# Sonic the self driving car
- Building a raspberry pi self driving rc car, may take a while, but i hope to learn a lot of stuff on the way.

## Work Done this weekend
- [x] Create a handler to control sonic with a PS3 bluetooth controller(see donkey car ps3 controller).
- [x] Use tornado to create a controller stream for sonic.
- [x] Stream video from sonic's pi cam to the web interface.
- [x] create PWM actuators for controlling sonic i.e steering the MG996R servo motor and throttling the DC motor via L298N motor board with speed control.
- [x] Succesfully drive sonic via the web interface with the pi cam, fucking awesome.

## Next-time: start working on the self drving part
- [ ] Lane detection with a CNN.

## Usage
### Parts
- A part is a class that represents a functional unit of the car (physical or logical) such as cameras, web interface and motor contollers.
### Anatomy of a part
- All parts share a common structure so that they can all be run by the vehicles drive loop.
    - `part.run`: function that runs the part
    - `part.update`: funtion that runs the part in a thread loop
    - `part.run_threaded` : threaded function
    - `part.shutdown`
- For a vehicle to perform well the drive loop must execute 10-30 times per second so slow parts should be threaded to avoid holding up the drive loop.
- A threaded part needs to define the function that runs in the separate thread and the function to call that will return the most recent values quickly.

### List of current parts
- Pi camera
- Web interface
- PWM Actuators - MG996R servo motor and L298N to control the 12v DC motor
- Joystick - am using an X-box 360 pad , the controls for the PS3 dualshock were difficult to use in my case( R2 for steering !!)
- Tub - datastrore to store sensor data in a key, value format e.g speed,steering angle & images from the pi cam.

## Contribution
- Right now you can contribute by giving me ideas on how you think the neural network for the self driving car should be designed & necessary hardware too.

## Resources 
- The [donkey car](http://docs.donkeycar.com) project has been really helpful to me so far cant say more,**Note** that though most of the components design is similar, this project is a much more simpler version of the donkey car, not a donkey car project.

