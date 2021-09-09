import logging

log = logging.getLogger(__name__)

log.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
#formatter = logging.Formatter('[%(asctime)s %(levelname)s %(filename)s:%(lineno)d:%(funcName)s] %(message)s')
formatter = logging.Formatter('[%(levelname)s %(filename)s:%(lineno)d] %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
log.addHandler(ch)
