import logging


def create(name: str, level: int) -> object:
    """
    Wrapper to create a logger
    """

    # create logger
    logger = logging.getLogger(name=name)
    logger.setLevel(level=level)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(level=level)

    # create formatter
    formatter = logging.Formatter("[%(levelname)s] %(asctime)s: %(message)s")

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    return logger
