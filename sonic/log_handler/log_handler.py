import os
import logging.config


class LogHandler:
    def get_logger(self,name,log_file_path=None,*args, **kwargs):
        if log_file_path is None:
            log_file_path=os.path.expanduser("~/sonic.log")
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
        return logging.getLogger(name)


if __name__ == '__main__':
    logger = LogHandler().get_logger(__name__)
    try:
        s=100/0
    except Exception as e:
        logger.exception(e)


