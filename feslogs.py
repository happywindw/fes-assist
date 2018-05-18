import datetime
import logging
import os


class FesLogger(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level=logging.DEBUG)

        current_dir = os.getcwd()
        log_dir = current_dir + '/logs'
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)

        log_file = log_dir + '/' + datetime.date.today().strftime('%Y%m%d') + '_fes_assist_log.txt'
        handler = logging.FileHandler(log_file)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger
