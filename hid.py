import wmi
import os
import ctypes

# Initialize WMI
c = wmi.WMI()

def list_hid_devices():
    hid_devices = []
    for device in c.Win32_PnPEntity():
        if device.Name is not None and "HID" in device.Name:
            hid_devices.append(device)
    return hid_devices

def check_driver_status(device):
    if device.ConfigManagerErrorCode != 0:
        return False, device.ConfigManagerErrorCode
    return True, None

def update_driver(device):
    # This function will prompt the user to update the driver manually
    print(f"Please update the driver for device: {device.Name}")
    print("You can do this via Device Manager or by visiting the manufacturer's website.")

def reset_device(device):
    try:
        os.system(f"devcon restart {device.DeviceID}")
        return True
    except Exception as e:
        print(f"Failed to reset device: {device.Name}. Error: {e}")
        return False

def main():
    print("Listing HID devices...")
    hid_devices = list_hid_devices()
    
    if not hid_devices:
        print("No HID devices found.")
        return
    
    for device in hid_devices:
        print(f"Checking device: {device.Name}")
        status, error_code = check_driver_status(device)
        
        if not status:
            print(f"Issue found with device: {device.Name}. Error code: {error_code}")
            update_driver(device)
            if reset_device(device):
                print(f"Device {device.Name} reset successfully.")
            else:
                print(f"Failed to reset device {device.Name}.")
        else:
            print(f"No issues found with device: {device.Name}")

if __name__ == "__main__":
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("Please run this script as an administrator.")
    else:
        main()
