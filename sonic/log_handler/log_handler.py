import os
import logging.config


def setup(log_file_path=None):

    if log_file_path is None:
        log_file_path = os.path.expanduser('~/sonic.log')

    config_default = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "simple",
                "stream": "ext://sys.stdout"
            },
            "error_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "simple",
                "filename": log_file_path,
                "maxBytes": 10485760,
                "backupCount": 20,
                "encoding": "utf8"
            },
        },
        "root": {
            "level": "DEBUG",
            "handlers": ["console", "error_file_handler"]
        }
    }

    logging.config.dictConfig(config_default)


class LogHandler:
    logger=None
    def __init__(self,*args, **kwargs):
        pass

    def create_logger(self,name):
        """
        Return a logger that will contextualize the logs with the name.
        """
        logger = logging.getLogger(name)
        self.logger=logger

    def logerror(self,sys_exec_info:Tuple,e):
        self.exc_type, self.exc_obj, self.exc_tb = sys_exec_info
        self.fname = os.path.split(self.exc_tb.tb_frame.f_code.co_filename)[1]
        self.error_message="{} {} {}\n {}".format(self.exc_type,self.fname,self.exc_tb.tb_lineno,e)
        self.logger.error(error_message)


# get a logger specific to this file
logger = LogHandler().get_logger(__name__)
logger.info('Logging configured and loaded.')


if __name__ == '__main__':
    print('run')
    logger.error('test')

