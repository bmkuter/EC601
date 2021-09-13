**Benjamin Kuter**
**Project 1**
**Fall 2021**

**Resources:**


- https://www.stupid-projects.com/tensorflow-2-1-0-for-microcontrollers-benchmarks-on-teensy-4-0/
- https://journals.sagepub.com/doi/full/10.1177/1178622121995819
- https://towardsdatascience.com/plant-ai-plant-disease-detection-using-convolutional-neural-network-9b58a96f2289
- https://forum.pjrc.com/threads/57433-Teensy-4-0-Image-Classification-w-CMSIS-NN
- https://www.tensorflow.org/lite/microcontrollers/get_started_low_level
- http://l0ner.github.io/2020-08-24_teensy-the-hard-way-blink/
- https://embedded.fm/blog/2017/2/27/dma-examples
- Garden Database: https://garden.org/plants/

**Project 1**
User Stories
Consumer
Competition
Open-Source Resources (Libraries, APIs, off-the-shelf components
Problem Space & Solution Set (What is the issue & how can it be resolved?)
MVP

**Automated Agricultural Grow System:**

**Problem statement**

Many resources are wasted in the process of bringing agricultural goods from where they are grown to where they are consumed. For smaller crops with shorter and grow times this process seems ridiculous. Things such as basil, Rosemary, or other herbs can readily be grown in doors locally to where they will be consumed. However in a many regions and in cities in particular available light comes in issue. On top of this of the modern world has many time requirements that put horticulture out of reach for many busy people. To correct this I propose a low-cost space efficient automated ways of growing commonly used agricultural goods within one’s own home or even apartment. 

**Area of focus within topic**

Within the scope of this project, my main area of interest is in the actual interaction in interfacing of sensors in actuators with the micro controller for automated tasks. I am very interested in using computers to remove the human element of redundant tasks. Specifically I want to interact with the GPIO pins on my MCU to establish a cyber physical system. The primary task is to make a system that can monitor and correct for base growth conditions with the reach goal of adding image recognition to automatically set those growth conditions. 

This project stems from my interests in sustainability through food localization, optimisation, and automation. I am considering off the shelf components for easier open sourcing and to minimise replicated work. I am interested in making products and open-source devices that are easy to DIY using readily available parts. It will be developed on a Teensy 4.1 running an ARM Cortex M7 @ 1.008 GHz. This board is programmable on the Arduino framework, but has many highly optimized native libraries (termed Teensyduino). Direct bare-metal programming is also available if/when needed, leveraging the full power of the fastest member of the ARM Cortex-M processor family. Building upon the Arduino framework additionally allows for many pre existing components to be readily deployed in the system. 

I would like to make an automated, indoors agricultural grow system for use in anyone's home. I think it's silly to get my tomatoes, herbs, etc shipped from around the country when I can get them much fresher here, potentially save gas money, and increase biodiversity. It would be able to self-regulate grow conditions (lighting intensity by grow period, water pH, feed schedules) automatically, perhaps supported by computer vision via TensorFlow Lite for Microcontrollers. 

The current design would be modular grow chambers which make up the grow system, which can act independently if needed. Modular units could be grouped, and each follower would be able to communicate with a central leader via ethernet or other local networking. 

A literature review of previous attempts at smart grow systems reveals the types of sensors typically needed as well as specific model numbers for the parts. These are typically well integrated into the Arduino environment and include things such as relays, lights, water sensors, humidity sensors, and temperature probes. most reviewed Arduino based projects that are limited in their processing powers because of the ATmega328P 8 bit architecture. The proposed MCU for my own project is instead based off of the current arm cortex M7 processor line which will afford me far more computational power, enabling more complicated tasks such as image recognition. 

Growing conditions, such as temperature, humidity, luminosity, water pH, and water temperature could be monitored and adjusted through a microcontroller. Sensors required (so far) are a humidity/temperature sensor (DHT22), light sensor (VEML7700), and a pH meter. Actuators required (so far) are servos, a peristaltic liquid pump, and relays (Adafruit). Some HVAC systems may also be needed as will irrigation & hydroponics systems. Lighting requirements will be met through a 12v LED bulb optimised for the growth spectrum running through a relay. 

Structurally, each module will be constructed with aluminium extrusions (Makerbeam) and 3D printed components (PLA during R&D, probably Nylon during production). Foam board insulation will be used to construct walls with advantageous thermal properties, with the internal sides covered in reflective material to increase light efficiency. The entire module will need to be enclosed to prevent light pollution & preserve proper growth periods. Simple HVAC systems using cheap, efficient, readily available computer fans will be used to supply fresh air and exhaust. These fans can be driven & monitored through the Teensy 4.1 lying at the heart of each module. 

**Duplicate results**
To duplicate research on this topic I have taken sample sensors and connected them to my MCU Without consideration for the final physical enclosure nor the total number of sensors and actuators eventually needed. This was done to ensure library compatibility as well as see in general power requirements and layout for the project. 

