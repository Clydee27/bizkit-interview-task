import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):
    """Determine if the list of favorite numbers match
    
    :param fave_numbers_1: list - first list of favorite numbers
    :param fave_numbers_2: list - second list of favorite numbers
    :return: bool -  do the first set of favorite numbers contain the second
                    set of favorite numbers or vice versa?
    """
    #Converting lists to set to make sure every member is unique
    set_1 = set(fave_numbers_1)
    set_2 = set(fave_numbers_2)

    #If the first set contains the the whole second set or vice versa, 
    #return True. If both conditions doesn't apply, return false
    return set_1.issuperset(set_2) or set_2.issuperset(set_1)
