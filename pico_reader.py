import serial

PORT = "/dev/ttyACM0"   # adjust for your system (COM3 on Windows, etc.)
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)

print("Listening for button presses...")

while True:
    line = ser.readline().decode("utf-8", errors="ignore").strip()
    if "BUTTON_PRESSED" in line:
        button_num = int(line[-2:])

        match button_num:
            case 14:
                print("button 14 was pressed!!!!")
            case 15:
                print("button 15 was pressed!!!")
            case 16:
                print("button 16 was pressed!!")
            case 17:
                print("button 17 was pressed!")
        