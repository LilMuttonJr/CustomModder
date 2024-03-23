import wmi
import time

# Connect to the OpenHardwareMonitor WMI namespace
w = wmi.WMI(namespace="root\OpenHardwareMonitor")

def set_fan_speed(device_id, speed):
    # Find the fan device by its ID
    fan = None
    for sensor in w.Sensor():
        if sensor.SensorType == 'Fan' and sensor.Identifier == device_id:
            fan = sensor
            break
    
    if fan:
        # Set the fan speed
        fan.SetControlSpeed(speed)

try:
    while True:
        # Example: Set fan speed to 50%
        set_fan_speed("Fan/1", 50)
        time.sleep(5)  # Wait for 5 seconds
        # Example: Set fan speed to 100%
        set_fan_speed("Fan/1", 100)
        time.sleep(5)  # Wait for 5 seconds
        # Repeat as needed
except KeyboardInterrupt:
    pass  # Handle Ctrl+C if necessary
