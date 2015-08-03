from collections import defaultdict

def dict_construct(levels, final_type):
    """Returns n level deep dictionary
    Keyword arguments:
    levels: the number of levels desired
    final_type: data type of the last level
    
    E.g.
    some_dict=dict_construct(3, list) 
     will create a 3 level deep (i.e. 3 sets of keys) dictionary
     with a list as the innermost value 
    """

    return(defaultdict(final_type) if levels<2 else
          defaultdict(lambda: dict_construct(levels-1,final_type)))

    
