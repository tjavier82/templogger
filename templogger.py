#/usr/bin/env python3

import logging
import serial
import time

#Serial config
SERIAL_PORT = '/dev/ttyACM0'
SERIAL_BAUD_RATE = 9600
SERIAL_TIMEOUT = 4

#File config
PATH = '/home/pi/Arduino/TempLogger/temp.csv'


#Log config
LOGGER_NAME = '/home/pi/Arduino/TempLogger/templogger.log'


def set_up_logs():
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.ERROR)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

def main():

    logger = set_up_logs()
    arduino = serial.Serial (SERIAL_PORT, SERIAL_BAUD_RATE, timeout=SERIAL_TIMEOUT)

    while True:
        try:
            a = arduino.readline()
            hour = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            logger.debug ('Value read: ' + str(a) + ' at ' + hour)
            try:
                temp = float(a)
                try:
                    logger.debug ('Opening ' + PATH)
                    f = open(PATH, 'a')
                    logger.debug ('Writing ' + str(temp) + ' to ' + PATH)
                    f.write(hour + ';' + str(temp) +'\n')
                    logger.debug ('Closing ' + PATH)
                    f.close()
                except IOError:
                    logger.error('IOError dealing with file ' + PATH)
                    
            except ValueError:
                logger.error('ValueError converting ' + str(temp) + ' to float')
            time.sleep(60)
        except:
            logger.error ('Exception not cached, exiting...')
            arduino.close()
            exit()
              
if __name__ == "__main__":
    main()
