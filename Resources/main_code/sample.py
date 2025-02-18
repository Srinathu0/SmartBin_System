# import serial
#
# ser = serial.Serial('COM3',9600)
# ser.close()
# ser.open()
#
# while True:
#     data = ser.readline()
#     print(data.decode())

import serial.tools.list_ports
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portsList = []
for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))

#val = input("Select Port: COM")
for x in range(0,len(portsList)):
    if portsList[x].startswith("COM3"):
        portsVar = "COM3"
        print(portsVar)

serialInst.baudrate = 9600
serialInst.port = portsVar
serialInst.open()

while True:
    command = input("Arduino Command: (Wet/Dry/Mixed: ")
    serialInst.write(command.encode('utf-8'))
    if command == "exit":
        exit()