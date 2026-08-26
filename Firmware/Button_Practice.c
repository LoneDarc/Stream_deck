#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"

#define NUM_BUTTONS 4
const uint BUTTON_PINS[NUM_BUTTONS] = {14, 15, 16, 17};

int main()
{
    stdio_init_all();
    for(int i =  0; i < NUM_BUTTONS; i++){
        gpio_init(BUTTON_PINS[i]);
        gpio_set_dir(BUTTON_PINS[i], GPIO_IN);
        gpio_pull_up(BUTTON_PINS[i]);
    }

    bool last_state[NUM_BUTTONS];
    for(int i = 0; i< NUM_BUTTONS; i++){
        last_state[i] = true;
    }

    while(true){
        for (int i = 0; i < NUM_BUTTONS; i++){
            bool current_state = gpio_get(BUTTON_PINS[i]);

            if  (last_state[i] && !current_state){
                printf("BUTTON_PRESSED: %d\n", BUTTON_PINS[i]);
            }
        }
        sleep_ms(250);
    }

}
