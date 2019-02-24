# Reads temperature from an Arduino board and stores it into a csv file

import logging
import serial
import time
import configparser
import pyowm

# config file will have following sections
# Serial
#   SerialPort
#   SerialBaudRate
#   SerialTimeout
#   SleepTime
#
# Output
#   FilePath
#
# Logging
#   LoggerName
#
# OpenWeather
#   APIKey
#   Lat
#   Lon


CONFIG_PATH = "config.ini"



def set_up_logs(logfilepath):
    logger = logging.getLogger(logfilepath)
    logger.setLevel(logging.ERROR)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

def main():

    config = configparser.ConfigParser()
    try:
        config.read(CONFIG_PATH)
    except:
        exit()

    logger = set_up_logs(config['Logging']['LoggerName'])
    serial_port = config['Serial']['SerialPort']
    serial_baud_rate = int(config['Serial']['SerialBaudRate'])
    serial_timeout = int(config['Serial']['SerialTimeout'])
    sleep_time = int(config['Serial']['SleepTime'])
    output_file = config['Output']['FilePath']
    lat = float(config['OpenWeather']['Lat'])
    lon = float(config['OpenWeather']['Lon'])

    owm = pyowm.OWM(config['OpenWeather']['APIKey'], language='es')
    arduino = serial.Serial(serial_port, serial_baud_rate, timeout=serial_timeout)


    while True:
        try:
            a = arduino.readline()
            hour = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(hour)
            logger.debug ('Value read: ' + str(a) + ' at ' + hour)
            obs = owm.weather_at_coords(lat, lon)

            temp = float(a)
            try:
                logger.debug ('Opening ' + output_file)
                f = open(output_file, 'a')
                logger.debug ('Writing ' + str(temp) + ' to ' + output_file)
                f.write(hour + ';' + str(temp) + ';' + str (obs.get_humidity()) + ';' + str(w.get_temperature('celsius')['temp']) + '\n')
                logger.debug ('Closing ' + output_file)
                f.close()
            except IOError:
                logger.error('IOError dealing with file ' + output_file)
                    

            time.sleep(sleep_time)
        except:
            logger.error ('Exception not cached, exiting...')
            arduino.close()
            exit()
              
if __name__ == "__main__":
    main()
