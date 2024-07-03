[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# HID Device Scanner

This application scans the computer for Human Interface Devices (HID) and checks for any issues that might be present.

## Features

- **Scan for HID Devices:** Quickly find all HID devices connected to your computer.
- **Issue Detection:** Automatically detect and report any issues found with the devices.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- Access to a terminal or command prompt.

### Installation

1. Clone the repository to your local machine:

git clone https://github.com/yourusername/hid-device-scanner.git

2. Navigate to the cloned repository:

cd hid-device-scanner

3. Install the required Python packages:

pip install -r requirements.txt


### Building the Application

To build the application into a standalone executable, run the following command:

pyinstaller --onefile --windowed --icon=icon.ico hid_gui.py


This will generate an executable in the `dist` directory.

## Usage

After building the application, you can run the executable directly. The GUI will guide you through scanning your computer for HID devices and identifying any issues.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any improvements or find any bugs.

## License

This project is licensed under the MIT License - see the LICENSE file for details.