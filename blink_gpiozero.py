# blink_gpiozero.py
from gpiozero import LED
from time import sleep

LED_PIN = 18         # change to the GPIO pin you use
ON_SEC = 0.5
OFF_SEC = 0.5

def main():
    led = LED(LED_PIN)
    try:
        print(f"Blinking LED on GPIO {LED_PIN}. Press Ctrl+C to stop.")
        while True:
            led.on()
            sleep(ON_SEC)
            led.off()
            sleep(OFF_SEC)
    except KeyboardInterrupt:
        led.off()
        print("\nStopped. LED turned off.")

if __name__ == "__main__":
    main()
