"""Usage: humandf.py SONG
          humandf.py (-h | --help)

Arguments:
    SONG    Berceuse, Tisket, Twinkle, Waltz

Options:
    -h --help

"""

import logging
import logging.config
import datetime
from docopt import docopt
import time

import playwav

songparts =    {'Berceuse': 5,
                'Twinkle': 5,
                'Tisket': 5, 
                'Waltz': 4}

pauses =    {'Berceuse': [3, 2, 4, 2],
            'Twinkle': [2, 1, 3, 2],
            'Tisket': [3, 3, 2],
            'Waltz': [3, 2, 4]}

def setuplogging():
    logger = logging.getLogger("humandf")
    logger.setLevel(logging.INFO)
 
    # create the logging file handler
    now = datetime.datetime.now()
    log_filename = "log\humandf_" + now.strftime('%Y_%m_%d_%H_%M_%S') + ".log"
    fh = logging.FileHandler(log_filename)
 
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
 
    # add handler to logger object
    logger.addHandler(fh)

    return (logger)

def main(song):
    """
    Play and log music for human Dance Freeze
    """

    logger = setuplogging()

    for i in range(songparts[song]):
        songfile = "music\\" + song + str(i+1) + ".wav"
        logger.info("Start " + song + str(i+1))
        playwav.playfile(songfile)
        logger.info("End " + song + str(i+1))
        if (i < len(pauses[song])):
            time.sleep(pauses[song][i])
            logger.info("Pause of " + str(pauses[song][i]) + " secs")


if __name__ == "__main__": 
    arguments = docopt(__doc__)
    main(arguments['SONG'])