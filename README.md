# IIC_CRC_Checker
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

