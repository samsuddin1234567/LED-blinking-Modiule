# blink_simulator.py
import time
import sys

ON_SEC = 0.5
OFF_SEC = 0.5

def led_on():
    # simple console "LED" indicator
    sys.stdout.write("\rLED: [●] ON ")
    sys.stdout.flush()

def led_off():
    sys.stdout.write("\rLED: [ ] OFF")
    sys.stdout.flush()

def main():
    print("Simulated LED blinking. Press Ctrl+C to stop.")
    try:
        while True:
            led_on()
            time.sleep(ON_SEC)
            led_off()
            time.sleep(OFF_SEC)
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    main()
