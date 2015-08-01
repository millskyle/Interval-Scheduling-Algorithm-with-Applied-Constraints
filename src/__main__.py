#!/usr/bin/python

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

def file_read():
    """Reads course info from a text file into a dictionary 
    TEMPORARY FUNCTION
    """
    course_file_name = 'courses.txt'

    course_file = open(course_file_name, 'r')

    dict_list = []
    
    #Skip first line
    for _ in range(1):
        next(course_file)

    for line in course_file:
        #Add the info if the line is not blank 
        try:
            #Add the returned dictionary to the list of dicts
            dict_list.append(line_to_dict(line))
        except IndexError:
            pass

    course_file.close()

    return dict_list

def line_to_dict(line):
    """Puts the contents of the line into a dict that
    will be added to a list. 
    TEMPORARY FUNCTION
    """

    ls = line.split()
    
    #File format is CRN CTYPE CODE RSEAT STIME ETIME DAY SEM SUBJ
    dict_temp = {'CRN':ls[0], 'CTYPE':ls[1], 'CODE':ls[2],
                 'CINFO':[ls[3], ls[7], ls[8]], 
                 'TIMES':[ls[4], ls[5], ls[6]]}

    return dict_temp

def add_query_to_dict(course_dict, query_list):
    """Adds result of query to course dictionary
    Returns course_dict

    Keyword arguments:
    course_dict: the dictionary containing relevant courses
    query_list: the list of dicts obtained from the database query
    """
    
    #Loop over the queries
    for q in query_list:
        crn = q['CRN']
        ctype = q['CTYPE']
        code = q['CODE']
        cinfo = q['CINFO']
        times = q['TIMES']

        #Add the times list the course dictionary
        course_dict[code][ctype][crn]['TIMES'].append(times)
        #Add the course info to the dictionary
        #Contains number of available seats and subject
        if len(course_dict[code][ctype][crn]['CINFO']) == 0:
            course_dict[code][ctype][crn]['CINFO'].append(cinfo)
        else:
            course_dict[code][ctype][crn]['CINFO'][0] = cinfo

    return course_dict     

def print_course_dict(course_dict):
    """Prints course dict to the screen.
    TEMPORARY FUNCTION
    """
    
    for code in course_dict.keys():
        for ctype in course_dict[code].keys():
            for crn in course_dict[code][ctype].keys():
                print code, ctype, crn, course_dict[code][ctype][crn]['TIMES'], \
                      course_dict[code][ctype][crn]['CINFO']


def main():
    
    #Initialize the course dict
    course_dict = dict_construct(4, list)

    test_dict_list = file_read()
    
    course_dict = add_query_to_dict(course_dict, test_dict_list)

    #Uncomment if you want to print the contents of the course dictionary
    #print_course_dict(course_dict)

if __name__=="__main__":
    main()


