import logging
import logging.config

LOGGING_CONFIG = {
    "version": 1,  # 필수, 항상 1
    "disable_existing_loggers": False,  # 기존 로거 비활성화 여부

    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
            "stream": "ext://sys.stdout"
        },
        "file_handler": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "filename": "app.log",
            "encoding": "utf8"
        }
    },

    "loggers": {
        "yyhome": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False
        }
    },

    "root": {
        "level": "WARNING",
        "handlers": ["console"]
    }
}


logging.config.dictConfig(LOGGING_CONFIG)

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
