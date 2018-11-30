# Sonic the self driving car
- Building a raspberry pi self driving rc car, may take a while, but i hope to learn a lot of stuff on the way.


# Work Done
- [x] Create a handler for the PS3 bluetooth controller
- [ ] Stream video from the raspberry pi to a web interface

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


## Contribution
- Right now you can contribute by giving me ideas on how you think the neural network for the self driving car should be designed & necessary hardware too.

## Resources 
- The [donkey car](http://docs.donkeycar.com) project has been really helpful to me so far cant say more,**Note** that though most of the components design is similar, this project is a much more simpler version of the donkey car, not a donkey car project.

