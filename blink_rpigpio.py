# blink_rpigpio.py
import RPi.GPIO as GPIO
from time import sleep

LED_PIN = 18       # BCM numbering
ON_SEC = 0.5
OFF_SEC = 0.5

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    try:
        print(f"Blinking LED on GPIO {LED_PIN}. Press Ctrl+C to stop.")
        while True:
            GPIO.output(LED_PIN, GPIO.HIGH)
            sleep(ON_SEC)
            GPIO.output(LED_PIN, GPIO.LOW)
            sleep(OFF_SEC)
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.cleanup()
        print("GPIO cleaned up. LED off.")

if __name__ == "__main__":
    main()
