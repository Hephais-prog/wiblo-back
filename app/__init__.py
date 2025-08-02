import os
import sys
import logging

# Configuration du logger
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter("%(asctime)s :: %(levelname)s ::  %(message)s")
stream_handler.setFormatter(log_formatter)
log.addHandler(stream_handler)

# Global path utile dans l'application
GLOBAL_PATH = os.getcwd()
GLOBAL_DATA_PATH = os.path.join(GLOBAL_PATH, "data")