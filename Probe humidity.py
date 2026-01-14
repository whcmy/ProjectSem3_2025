import PCF8591 as ADC
import time
import RPi.GPIO as GPIO

# Initialize hardware
ADC.setup(0x48)  # Default I2C address of PCF8591
GPIO.setmode(GPIO.BCM)
# FC-28 digital pin (optional, for auxiliary judgment)
D0_PIN = 21
GPIO.setup(D0_PIN, GPIO.IN)

# Calibration parameters (adjust after actual testing for accuracy)
DRY_VALUE = 220  # Analog value in completely dry soil (typical: 200-250)
WET_VALUE = 30   # Analog value in fully wet soil (typical: 20-50)

def calculate_humidity(analog_val):
    """Convert FC-28 analog value to relative humidity (0-100%)"""
    if analog_val >= DRY_VALUE:
        return 0.0
    elif analog_val <= WET_VALUE:
        return 100.0
    else:
        # Linear mapping: smaller analog value = higher humidity
        return round(((DRY_VALUE - analog_val) / (DRY_VALUE - WET_VALUE)) * 100, 2)

try:
    print("FC-28 Soil Moisture Monitoring Started (Press CTRL+C to stop)")
    while True:
        # Read analog value from FC-28 A0 pin (via PCF8591 AIN0)
        analog_value = ADC.read(0)
        humidity = calculate_humidity(analog_value)
        # Read digital pin state (HIGH = dry, LOW = wet)
        digital_state = "Dry" if GPIO.input(D0_PIN) else "Wet"
        
        # Output data
        print(f"Analog Value: {analog_value:3d} | Relative Humidity: {humidity:5.1f}% | Digital State: {digital_state}")
        time.sleep(1)  # Read data every 1 second

except KeyboardInterrupt:
    print("\nProgram Terminated")
finally:
    GPIO.cleanup()  # Clean up GPIO resources to avoid pin occupation
