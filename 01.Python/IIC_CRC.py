import tkinter as tk

# CRC16_CCITT Calculation function
def CRC16_CCITT(data: bytes) -> int:
    """
    - Perform CRC16_CCITT algorithm on Bytes
    - POLY_Reverse = 0x8408 (reversed 0x1021)
    - Initialize CRC value to 0xFFFF

    Args:
        data (bytes): Input bytes, e.g., b'/x1234'

    Returns:
        int: Calculated 16-bit CRC value

    ## Remark
    >>> # C code from:
    >>> # MIPI® Alliance Specification for Camera Serial Interface 2 (CSI-2)
    >>> # Version 1.1 – 18 July 2012
    >>> #
    >>> # define POLY 0x8408 /* 1021H bit reversed */
    >>> # unsigned short crc16(char *data_p, unsigned short length)
    >>> #
    >>> #  {
    >>> #      unsigned char i;
    >>> #      unsigned int data;
    >>> #      unsigned int crc = 0xffff;
    >>> #      
    >>> #      if (length == 0)
    >>> #          return (unsigned short)(crc);
    >>> #      do
    >>> #      {
    >>> #          for (i=0, data=(unsigned int)0xff & *data_p++;
    >>> #          i < 8;i++, data >>= 1)
    >>> #      {
    >>> #          if ((crc & 0x0001) ^ (data & 0x0001))
    >>> #              crc = (crc >> 1) ^ POLY;
    >>> #          else
    >>> #              crc >>= 1;
    >>> #  }
    >>> #  }   while (--length);
    >>> #  
    >>> #  // Uncomment to change from little to big Endian
    >>> #  // crc = ((crc & 0xff) << 8) | ((crc & 0xff00) >> 8);
    >>> #
    >>> #    return (unsigned short)(crc);
    >>> #  }

    Example:
        >>> # MIPI® Alliance Specification GIVES F0(LSB) 00(MSB)
        >>> data_hex_1 = 0xFF000002B9DCF372BBD4B85AC875C27C81F805DFFF000001
        >>> #
        >>> # MIPI® Alliance Specification GIVES 69(LSB) E5(MSB) 
        >>> data_hex_2 = 0xFF0000001EF01EC74F8278C582E08C70D23C78E9FF000001
        >>> #
        >>> # 031 Application Note GIVES BF(MSB) D2(LSB)
        >>> data_hex_3 = 0x341E08AC0D 
        >>> #
        >>> data_bytes = data_hex_3.to_bytes((data_hex_3.bit_length() + 7) // 8, byteorder='big')
        >>> #
        >>> crc_result = CRC16_CCITT(data_bytes)
        >>> print(f"CRC16 result: {hex(crc_result)}")
    """
    # Polynomial used in CRC16_CCITT, 0x8408 is the reversed form of 0x1021 (standard CRC-16-CCITT)
    POLY_Reverse = 0x8408 

    crc = 0xFFFF  # Initialize CRC value to 0xFFFF (initial value)
    
    for byte in data:  # Process each byte of the data
        data_val = byte & 0xFF  # Ensure we are dealing with the least significant byte
        
        for _ in range(8):  # Process each bit of the byte (8 bits)
            if (crc & 0x0001) ^ (data_val & 0x0001):  # If the least significant bit of CRC differs from the data
                crc = (crc >> 1) ^ POLY_Reverse  # Shift CRC right and XOR with the polynomial
            else:
                crc >>= 1  # Otherwise, just shift CRC right
            data_val >>= 1  # Shift the byte right to process the next bit

    # Return the final CRC value, ensuring it's 16-bits (16-bit CRC)
    return crc & 0xFFFF  # Mask to ensure we return only the lower 16 bits of the CRC


# Function to convert a hexadecimal string to bytes
def hex_to_bytes(hex_str: str) -> bytes:
    """
    Converts a hexadecimal string into bytes.

    Args:
        hex_str (str): The hexadecimal string input (e.g., "34 1E 08 AC 0D").

    Returns:
        bytes: The corresponding byte array.

    Raises:
        ValueError: If the length of the hex string is odd or invalid characters are found.
    """
    # Remove any spaces, newlines, or tabs from the string
    hex_str = hex_str.replace(" ", "").replace("\n", "").replace("\t", "")
    
    # Ensure the hex string length is even (each pair of hex digits corresponds to one byte)
    if len(hex_str) % 2 != 0:
        raise ValueError("Hex string length must be even.")
    
    # Convert the hex string to bytes and return
    return bytes.fromhex(hex_str)


# Function to calculate CRC for each input field and update the corresponding labels
def calculate_crc():
    """
    Calculates the CRC16 for each of the input fields and updates the corresponding CRC label.
    """
    for i, entry in enumerate(text_entries):
        hex_str = entry.get().strip()  # Get the value from the input field
        if hex_str:  # If the input is not empty
            try:
                byte_data = hex_to_bytes(hex_str)  # Convert hex string to bytes
                crc_value = CRC16_CCITT(byte_data)  # Calculate the CRC16 value
                crc_labels[i].config(text=f"{crc_value:04X}")  # Update the label with the CRC value in hexadecimal format
            except ValueError as e:  # If there's an error (e.g., invalid hex input)
                crc_labels[i].config(text=f"Error: {str(e)}")  # Display the error message
        else:  # If the input is empty
            crc_labels[i].config(text="NULL")  # Indicate that no data was provided


# Function to clear all text entries and reset CRC labels
def clear_all():
    """
    Clears all text entries and resets CRC labels. The first input box will be set to a fixed value.
    """
    # Set the first input field to a fixed default value
    text_entries[0].delete(0, tk.END)  # Clear the first input box
    text_entries[0].insert(0, "34 1E 08 AC 0D")  # Insert default value into the first input box

    # Clear the remaining input boxes
    for entry in text_entries[1:]:
        entry.delete(0, tk.END)  # Clear all other input boxes
    
    # Reset all CRC labels to show "CRC16:"
    for label in crc_labels:
        label.config(text="CRC16: ")


# Create the main window using Tkinter
root = tk.Tk()
root.title("CRC Calculation Tool")

# Create the input text fields and corresponding CRC result labels
text_entries = []  # List to store the input text entry widgets
crc_labels = []  # List to store the corresponding CRC result labels

for i in range(10):
    # Create labels for each input field (e.g., "IIC command #1 0x:")
    label = tk.Label(root, text=f"IIC command #{i} 0x:")
    label.grid(row=i, column=0, padx=5, pady=5, sticky='e')  # Place the label in the grid

    # Create the text entry field for hexadecimal input
    entry = tk.Entry(root, width=30)
    entry.grid(row=i, column=1, padx=5, pady=5)  # Place the entry field in the grid
    if i == 0:
        entry.insert(0, "34 1E 08 AC 0D")  # Set a default value for the first input field
    text_entries.append(entry)  # Add the entry field to the list

    # Create the label to display the corresponding CRC16 result
    crc_label = tk.Label(root, text="CRC16: ", font=("Arial", 12))
    crc_label.grid(row=i, column=2, padx=5, pady=5)  # Place the CRC label in the grid
    crc_labels.append(crc_label)  # Add the label to the list

# Create the "Calculate" button to trigger CRC calculation
calc_button = tk.Button(root, text="Calculate", command=calculate_crc)
calc_button.grid(row=10, column=0, columnspan=3, pady=10)  # Place the button in the grid

# Create the "Clear" button to clear all inputs and CRC results
clear_button = tk.Button(root, text="Clear", command=clear_all)
clear_button.grid(row=11, column=0, columnspan=3, pady=10)  # Place the button in the grid

# Start the Tkinter event loop to display the window
root.mainloop()
