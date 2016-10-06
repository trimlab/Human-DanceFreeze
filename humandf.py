"""Usage: humandf.py SONG
          humandf.py (-h | --help)

Arguments:
    SONG    The short name of the song

Options:
    -h --help

"""

import logging
import logging.config
import datetime
from docopt import docopt

import playwav

songparts =    {'Berceuse': 5,
                'Twinkle': 5,
                'Tisket': 5, 
                'Waltz': 4}

def setuplogging():
    logger = logging.getLogger("humandf")
    logger.setLevel(logging.INFO)
 
    # create the logging file handler
    now = datetime.datetime.now()
    log_filename = "log\humandf_" + now.strftime('%Y_%m_%d_%H_%M_%S' + ".log") 
    fh = logging.FileHandler(log_filename)
 
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
 
    # add handler to logger object
    logger.addHandler(fh)

def main(song):
    """
    Play and log music for human Dance Freeze
    """

    setuplogging()

    # TODO Add logging and pauses
    for i in range(1, songparts[song]):
        songfile = "music\\" + song + str(i) + ".wav"
        playwav.playfile(songfile)
 
if __name__ == "__main__":
    arguments = docopt(__doc__)
    main(arguments['SONG'])
    