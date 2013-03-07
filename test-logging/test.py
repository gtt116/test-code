import logging

logging.basicConfig(filename='log', level=logging.NOTSET)

LOG = logging.getLogger(__name__)
LOG.info("info")
LOG.debug("debug")
raise Exception("A exception raised.")
LOG.debug("debug2")
