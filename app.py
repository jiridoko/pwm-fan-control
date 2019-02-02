#!/usr/bin/python3
import serial
import configparser
import time
from flask import Flask
from flask import request

app = Flask(__name__)
ser = serial.Serial('/dev/ttyUSB0')
config = configparser.ConfigParser()

def read_value():
    config.read('config.ini')
    return int(config['default']['pwm'])

def write_value(val):
    config['default'] = {'pwm': str(val)}
    with open('config.ini', 'w') as cfg:
        config.write(cfg)

def call_arduino(val):
    ser.write(str(str(val)+'\n').encode('utf-8'))
    line = ser.readline()
    print("Arduino says: "+line.decode('utf-8'))

time.sleep(2)
n = read_value()
call_arduino(n)

@app.route('/speed')
def speed_control():
    n = int(request.args['pwm'])
    print("PWM: "+str(n))
    call_arduino(n)
    write_value(n)
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=False, port=8080, host="0.0.0.0")
