import time

import utils.constants


def limit(info):
    if utils.constants.RL_ENABLE:
        if info["RateLimit-Reset"] > info["RateLimit-Remaining"]:
            time.sleep(max([0, info["RateLimit-Reset"] - info["RateLimit-Remaining"]]))