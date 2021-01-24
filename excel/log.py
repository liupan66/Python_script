import logging
import os
from logging.handlers import TimedRotatingFileHandler

from colorlog import ColoredFormatter


def init_logging(**kwargs):
    level = kwargs.pop('level', None)
    filename = kwargs.pop('filename', None)
    datefmt = kwargs.pop('datefmt', None)
    format = kwargs.pop('format', None)
    if level is None:
        level = logging.DEBUG
    if filename is None:
        filename = 'logs.log'
    if datefmt is None:
        datefmt = '%Y-%m-%d %H:%M:%S'
    if format is None:
        format = '%(asctime)s [%(levelname)8s]  %(message)s'

    log = logging.getLogger(__name__)

    sh = logging.StreamHandler()
    sh.setLevel(level)
    sh.setFormatter(ColoredFormatter('%(log_color)s%(message)s%(reset)s', log_colors={
        'DEBUG': 'cyan',
        'INFO': 'white',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }))
    log.addHandler(sh)

    if not os.path.exists('logs'):
        os.makedirs('logs')

    th = TimedRotatingFileHandler(filename='logs/' + filename, when='D', backupCount=7, encoding='utf-8')
    th.suffix = "%Y-%m-%d"
    th.setFormatter(logging.Formatter(format, datefmt))
    th.setLevel(level)
    log.addHandler(th)
    log.setLevel(level)
    return log
