**Benjamin Kuter**  
**Project 1**  
**Fall 2021**  

<h1>Automated Agricultural Grow System:</h1>

*<h3>Table of Contents</h3>*  
- Problem Statement  
- Area of focus within topic  
- Users  
- User Stories  
- Open Source Resources  
- Previous Implementations  
- Preliminary Technical Approach
- Duplicating Results


<h3>Problem statement</h3>

Many resources are wasted in the process of bringing agricultural goods from where they are grown to where they are consumed. For smaller crops with shorter and grow times this process seems ridiculous. Things such as basil, Rosemary, or other herbs can readily be grown in doors locally to where they will be consumed. However in a many regions and in cities in particular available light comes in issue. On top of this of the modern world has many time requirements that put horticulture out of reach for many busy people. I think it is unfortunate that much of my produce, such as tomatoes, herbs, etc.,  are shipped from around the country when I can produce them much fresher in my own abode. This has the added benefit of reducing carbon emissions produced by the transportation process, as well as increasing national agricultural biodiversity. The system would be able to automatically self-regulate grow conditions (lighting intensity by grow period, water pH, feed schedules). I propose a low-cost, space-efficient, automated device for growing commonly used agricultural goods within one’s own home or even apartment.

This project stems from my interests in sustainability through food localization, optimisation, and automation. I am considering off the shelf components for easier open sourcing and to minimise replicated work. I am interested in making products and open-source devices that are easy to DIY using readily available parts. It will be developed on a Teensy 4.1 running an ARM Cortex M7 @ 1.008 GHz. This board is programmable on the Arduino framework, but has many highly optimized native libraries (termed Teensyduino). Direct bare-metal programming is also available if/when needed, leveraging the full power of the fastest member of the ARM Cortex-M processor family. Building upon the Arduino framework additionally allows for many pre existing components to be readily deployed in the system.



<h3>Area of focus within topic</h3>

Within the scope of this project, my main area of interest is in the actual interaction in interfacing of sensors in actuators with the micro controller for automated tasks. I am very interested in using computers to remove the human element of redundant tasks. Specifically I want to interact with the GPIO pins on my MCU to establish a cyber physical system. The primary task is to make a system that can monitor and correct for base growth conditions with a stretch goal of adding image recognition to automatically set those growth conditions, most likely via TensorFlow Lite for Microcontrollers and open source plant databases such the Pl@ntNet dataset.  



<h3>Users</h3>   

There are two primary groups of users for this modular grow system: individual households, and larger-scale community farms:  
The first & primary audience for the device's initial conception would be individual households with either limited outdoor growing space or inclement weather. This group can be further subdivided into limited space users, such as those living in apartments, and those with larges spaces like homes but with poor growing conditions. For such users a compact, modular grow system could provide basic herbs and produce year-round.

The second target audience would be communities, akin to community gardens. Scalability through networked modules is inherent to the initial design. This scalability can be increased from several modules within one household to many modules residing inside some communal building. As renewable infrastructures become more common place (fingers-crossed), this system could be readily adjusted to using said renewable resources for power.  



<h3>User Stories</h3>  

-As an apartment user, I want to be able to grow my own herbs in my basement apartment that has limited lighting.  
-As a household user in northern Minnesota, I want to have fresh tomatoes, lettuce, & other produce for my family readily available.  
-As a community manager, I want to supply my coop with low-cost exotic produce that normally can't be found locally, or is normally prohibitively expensive.  



<h3>Open Source Resources</h3>

Arduino itself is licensed under GNU General Public License Version 2, which allows for commercial development and use<sup>10</sup>. According to Paul Stoffregen of Teensy, the Teensy board itself is closed source but usable in commercial projects without any additional licensing fees<sup>11</sup>. The Teensyduino code itself is open source, primarily under the MIT license<sup>11</sup>. Specific modules and components to be used are still under investigation, but preliminary research into products through Adafruit seem to be under the BSD License, which imposes minimal restrictions on the use and distribution of the specified libraries<sup>12</sup>.

The image-recognition portion of the project will probably utilise the open-source plant database Pl@ntNet<sup>9</sup>. According to their GitLab page there is no license, but further work is needed to see if commercial use is permitted. They have published an API allowing up to 500 identification requests per day<sup>13</sup> which may be utilised, but more research is needed to verify this use.



<h3>Duplicate results</h3>

This project will utilise open-source libraries developed by the Arduino foundation and supplemented by libraries written by Adafruit & Sparkfun for specific sensor modules. Additionally libraries developed by Paul Stoffregen (father of Teensyduino and massive contributor to the Arduino Foundation) will be used for their incredible optisiation for the Teensy platform. To duplicate research on this topic I have taken sample sensors and connected them to my MCU without consideration for the final physical enclosure nor the total number of sensors and actuators eventually needed. This was done to ensure library compatibility as well as see in general power requirements and layout for the project. To learn the requisite libraries, I will examine demo codes provided through each libraries GitHub. These will be referenced when used with all appropriate licenses attached to the final repository.



<h3>Technical Approach & Previous Implementations</h3>

The current design would be modular grow chambers which make up the grow system, which can act independently if needed. Modular units could be grouped, and each follower would be able to communicate with a central leader via ethernet or other local networking.

A literature review of previous attempts at smart grow systems reveals the types of sensors typically needed as well as specific model numbers for the parts. These are typically well integrated into the Arduino environment and include things such as relays, lights, water sensors, humidity sensors, and temperature probes. most reviewed Arduino based projects that are limited in their processing powers because of the ATmega328P 8 bit architecture. The proposed MCU for my own project is instead based off of the current arm cortex M7 processor line which will afford me far more computational power, enabling more complicated tasks such as image recognition.

Growing conditions, such as temperature, humidity, luminosity, water pH, and water temperature could be monitored and adjusted through a microcontroller. Sensors required (so far) are a humidity/temperature sensor (DHT22), light sensor (VEML7700), and a pH meter. Actuators required (so far) are servos, a peristaltic liquid pump, and relays (Adafruit). Some HVAC systems may also be needed as will irrigation & hydroponics systems. Lighting requirements will be met through a 12v LED bulb optimised for the growth spectrum running through a relay.

Structurally, each module will be constructed with aluminium extrusions (Makerbeam) and 3D printed components (PLA during R&D, probably Nylon during production). Foam board insulation will be used to construct walls with advantageous thermal properties, with the internal sides covered in reflective material to increase light efficiency. The entire module will need to be enclosed to prevent light pollution & preserve proper growth periods. Simple HVAC systems using cheap, efficient, readily available computer fans will be used to supply fresh air and exhaust. These fans can be driven & monitored through the Teensy 4.1 lying at the heart of each module.



<h3>Resources:</h3>

1. https://www.stupid-projects.com/tensorflow-2-1-0-for-microcontrollers-benchmarks-on-teensy-4-0/
2. https://journals.sagepub.com/doi/full/10.1177/1178622121995819
3. https://towardsdatascience.com/plant-ai-plant-disease-detection-using-convolutional-neural-network-9b58a96f2289
4. https://forum.pjrc.com/threads/57433-Teensy-4-0-Image-Classification-w-CMSIS-NN
5. https://www.tensorflow.org/lite/microcontrollers/get_started_low_level
6. http://l0ner.github.io/2020-08-24_teensy-the-hard-way-blink/
7. https://embedded.fm/blog/2017/2/27/dma-examples
8. Garden Database: https://garden.org/plants/
9. Garden Database: https://plantnet.org/en/2021/03/30/a-plntnet-dataset-for-machine-learning-researchers/
10. https://github.com/arduino/Arduino/blob/master/license.txt
11. https://forum.pjrc.com/threads/47851-Doing-business?p=159647&viewfull=1#post159647, post 4
12. https://github.com/adafruit/Adafruit_VEML7700/blob/master/license.txt
13. https://my.plantnet.org/usage
