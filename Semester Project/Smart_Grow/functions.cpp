// 
// 
// 

#include "functions.h"

void PWM_Test(uint8_t gpio_pin)
{
	for (int i = 70; i <= 255; i += 5) {
		analogWrite(gpio_pin, i);
		delay(100);
	}
	for (int i = 255; i >= 70; i -= 5) {
		analogWrite(gpio_pin, i);
		delay(100);
	}
}0



