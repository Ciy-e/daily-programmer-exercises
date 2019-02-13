#!/bin/python3

import math
import os
import random
import re
import sys

# returns ranks for each entered score using dense ranking
def climbingLeaderboard(scores, entered_scores):
    results = []
    for score in entered_scores:
        temp_scores = scores
        current_rank = 1
        temp_scores.append(score)
        previous_score = -1
        for hiscore in temp_scores:
            if hiscore == score or score > hiscore:
                results.append(current_rank)
                break
            elif previous_score == hiscore:
                continue
            else:
                current_rank += 1
                previous_score = hiscore
    return results