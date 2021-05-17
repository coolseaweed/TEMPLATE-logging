import logging

import os, sys

logging.basicConfig(
    format="[%(asctime)s][%(levelname)s]:%(name)s|%(message)s",
    stream=sys.stdout, 
    level=logging.INFO
    )
logger = logging.getLogger(__name__)





if __name__ == '__main__':

    for i in range(100):
        logger.info(f'{i}')

                
    logger.info('done!')

