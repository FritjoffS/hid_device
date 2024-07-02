import wmi
import os
import ctypes
import tkinter as tk
from tkinter import messagebox, Scrollbar

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
    # Replace this with actual update functionality if available
    messagebox.showinfo("Update Driver", f"Please update the driver for device: {device.Name}\n\n"
                                         "You can do this via Device Manager or by visiting the manufacturer's website.")

def reset_device(device):
    try:
        os.system(f"devcon restart {device.DeviceID}")
        return True
    except Exception as e:
        messagebox.showerror("Reset Device", f"Failed to reset device: {device.Name}. Error: {e}")
        return False

def check_devices():
    hid_devices = list_hid_devices()
    if not hid_devices:
        result_text.insert(tk.END, "No HID devices found.\n")
    else:
        for device in hid_devices:
            status, error_code = check_driver_status(device)
            result_text.insert(tk.END, f"Device: {device.Name}\n")
            if not status:
                result_text.insert(tk.END, f"Issue found. Error code: {error_code}\n")
                result_text.insert(tk.END, f"Updating driver for {device.Name}...\n")
                update_driver(device)
                result_text.insert(tk.END, f"Resetting {device.Name}...\n")
                reset_device(device)
                result_text.insert(tk.END, f"{device.Name} reset successfully.\n")
            else:
                result_text.insert(tk.END, "No issues found.\n")
            result_text.insert(tk.END, "\n")

def main():
    root = tk.Tk()
    root.title("HID Device Manager")

    label = tk.Label(root, text="Click 'Check Devices' to scan HID devices and check status.")
    label.pack(pady=10)

    check_button = tk.Button(root, text="Check Devices", command=check_devices)
    check_button.pack(pady=10)

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    global result_text
    result_text = tk.Text(root, height=20, width=80, wrap=tk.WORD, yscrollcommand=scrollbar.set)
    result_text.pack(pady=10)

    scrollbar.config(command=result_text.yview)

    if not ctypes.windll.shell32.IsUserAnAdmin():
        messagebox.showerror("Admin Privileges", "Please run this script as an administrator.")
        root.destroy()
        return

    root.mainloop()

if __name__ == "__main__":
    main()
