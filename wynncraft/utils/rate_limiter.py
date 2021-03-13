import time

import utils.constants


def limit(info):
    if utils.constants.RL_ENABLE:
        if info["RateLimit-Reset"] > info["RateLimit-Remaining"]:
            time.sleep(max([0, int(info["RateLimit-Reset"]) - int(info["RateLimit-Remaining"])]))