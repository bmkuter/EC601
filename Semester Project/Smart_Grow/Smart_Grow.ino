/*
 Name:		Smart_Grow.ino
 Created:	10/7/2021 7:58:56 PM
 Author:	bmk

 Notes:
 Motor & MOSFET Wiring: https://www.youtube.com/watch?v=3PkpOeHTnfo


*/

#include "functions.h"


// the setup function runs once when you press reset or power the board

int PWM_Pump = 33;

void setup() {
	Serial.begin(9600);
	while (!Serial) {
		; // wait for serial port to connect. Needed for native USB
	}
	pinMode(13, OUTPUT);
	pinMode(PWM_Pump, OUTPUT);
	digitalWrite(13, HIGH);
}

// the loop function runs over and over again until power down or reset
void loop() {
	PWM_Test(PWM_Pump);
	/*
	Serial.println("HIGH");
	digitalWrite(PWM_Pump, HIGH);

	delay(1000);

	Serial.println("LOW");
	digitalWrite(PWM_Pump, LOW);

	delay(1000);
	*/
}
