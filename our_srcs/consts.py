from honeybadgerbft.core.honeybadger import HoneyBadgerBFT, ImprovedHoneyBadgerBFT

LOG_DIR = './logs'


LOG_PATH = LOG_DIR + '/honeybadger_test_{}_{}_{}_{}_{}_{}.log'
LOGGER_NAME = 'honeybadger_test_logger'
NUM_OF_NODE_OPTIONS = [4, 6]
NUM_OF_IDENTICAL_INPUTS_OPTIONS = [0, 2, 4]
NUM_OF_INPUTS_IN_ITERATION = 3
INPUT_SIZES = [2, 1024, 1024*1024]
DEFAULT_NUM_OF_NODES = NUM_OF_NODE_OPTIONS[-1]
DEFAULT_NUM_OF_IDENTICAL_INPUTS_OPTIONS = NUM_OF_IDENTICAL_INPUTS_OPTIONS[-1]
DEFAULT_INPUT_SIZE = INPUT_SIZES[-1]
HONEYBADGERS = [("Regular Honeybadger", HoneyBadgerBFT), ("Parity Honeybadger", ImprovedHoneyBadgerBFT)]
