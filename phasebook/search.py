from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    # Implement search here!
    #Checks if the args is empty
    if args:
        to_filter=[]
        user_data = USERS

        #A loop going all through the keys from args to know their
        #value and know which values to search for in the list
        for key in args.keys():
            to_search = args[key]
            for item in user_data:
                if key=='id':
                    if item[key]==to_search:
                        to_filter.append(item)
                elif key=='name':
                    #Converted the string to lowercase and
                    #check if the searched item is a substring
                    if to_search.lower() in item[key].lower():
                        to_filter.append(item)
                elif key=='age':
                    #Casting string to integer to know the range of age
                    #to be filtered
                    minimum = int(to_search)-1
                    maximum = int(to_search)+1
                    if minimum<=item[key]<=maximum:
                        to_filter.append(item)
                elif key=='occupation':
                    #Checking if the searched item is a substring
                    if to_search in item[key]:
                        to_filter.append(item)
                        
        #Remove duplicate entries by checking every record
        #if it is already in the new list. If not, then it is
        #going to be added.
        new_list = []

        for dictionary in to_filter:
            if dictionary not in new_list:
                new_list.append(dictionary)

        return new_list
    #If args is empty, it'll return USERS data
    else:
        return USERS
