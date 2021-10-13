
import serial
from serial.tools import list_ports
import time
import matplotlib.pyplot as plt

devices = list(list_ports.comports())

print('select device:')
counter = 0
for d in devices:
    print(str(counter) + ': ' + d.name)
    counter += 1

try:
    selected_dev = int(input('Input:'))
except ValueError:
    print("Not a number")
    exit(0)

# print(devices[selected_dev])
# exit(0)

ser = serial.Serial(devices[selected_dev].device, 115200, timeout=1)
time.sleep(2)

while True:
    data = []
    for i in range(4096):
        line = ser.readline()   # read a byte string
        if line:

            string = line.decode().strip()
            if len(string) != 0:
                num = float(string)
                # print(num)
                data.append(num)

    plt.plot(data)
    plt.xlabel('Time')
    plt.ylabel('V')
    plt.title('Voltage vs. Time[' + str(min(data)) + '      ' + str(max(data)) + '     ' + str(sum(data) / len(data)) + ']')
    plt.draw()
    plt.pause(0.0001)
    plt.clf()


ser.close()
