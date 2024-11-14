# IIC_CRC_Checker

## General Description:
This script provides a tool for calculating the **16-bit CRC (Cyclic Redundancy Check)** value for data transmitted over **I2C communication**. It implements the **CRC16-CCITT** algorithm, which is commonly used in communication protocols like I2C, ensuring data integrity by verifying the accuracy of transmitted data.

To understand IIC better, it is advisable to refer to the following two documents:

1. [The I2C Bus Specification and User Manual (NXP Semiconductors)](https://www.nxp.com/docs/en/user-guide/UM10204.pdf)
   
2. [Understanding the I2C Bus (Texas Instruments)](https://www.ti.com/lit/an/slva704/slva704.pdf)

### Key Features:
- **CRC Calculation**: The script calculates the CRC16 value for each input data string (represented in hexadecimal format).
- **Hexadecimal Input**: Users can input hexadecimal values representing I2C commands or data.
- **Real-time CRC Display**: As users input hexadecimal data, the corresponding CRC16 value is calculated and displayed in real-time.
- **Error Handling**: If an invalid input is detected (e.g., incorrect hex format), an error message is displayed.
- **Clear Function**: The "Clear" button resets all input fields and CRC results, with the first input field set to a default value.
- **Graphical User Interface (GUI)**: A simple, user-friendly **Tkinter** interface allows users to easily interact with the tool by entering data, calculating CRC, and viewing results.

## Code Explanation:

### CRC16_CCITT function:
This function implements the **CRC16-CCITT** algorithm, which is often used in protocols like **I2C** and **MIPI**.  
The polynomial used here is `0x8408`, which is the reversed version of `0x1021`.

- The function loops through the input data **byte-by-byte** and **bit-by-bit**, calculating the CRC value using the polynomial.
- It returns the final CRC value, ensuring it is limited to **16 bits** (`crc & 0xFFFF`).

### hex_to_bytes function:
This function converts a hexadecimal string (e.g., `"34 1E 08 AC 0D"`) into a corresponding `bytes` object.  

- It ensures that the input string is valid and has **even-length** (since each pair of hex digits corresponds to one byte).

### calculate_crc function:
This function loops through all input text fields, retrieves the hexadecimal values, converts them to bytes, and calculates the CRC for each one.

- It updates the **CRC label** next to each input field with the computed CRC16 value in **hexadecimal format**.
- If the input is invalid or empty, an error message or `"NULL"` is displayed.

### clear_all function:
This function resets the input fields and CRC labels.

- The first input field is set to a fixed default value (`"34 1E 08 AC 0D"`).
- All other input fields are cleared, and the CRC labels are reset to `"CRC16: "`.

### Tkinter GUI:
A simple **Tkinter** interface is created with 10 input fields (`text_entries`), each with a label (`crc_labels`) showing the corresponding CRC16 value.

- The **"Calculate"** and **"Clear"** buttons allow users to trigger CRC calculation and reset the inputs respectively.

## How to Use:
1. **Enter hexadecimal values** into the input fields.
2. Click **"Calculate"** to compute the CRC16 value for each input.
3. Click **"Clear"** to reset all inputs and CRC values, with the first input field set to a default value.

## Author:
Mr. Bingtao (Robert) Liu  
FAE of Sony Semicon (SH) Automotive Division  
- **Working Email**: Bingtao.Liu@sony.com  
- **Alternative Email**: Liubingtao0513@Gmail.com
