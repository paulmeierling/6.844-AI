# MIT 6.034 Lab 0: Getting Started
# Written by jb16, jmn, dxh, and past 6.034 staff

from point_api import Point

#### Multiple Choice ###########################################################

# These are multiple choice questions. You answer by replacing
# the symbol 'None' with a letter (or True or False), corresponding 
# to your answer.

# True or False: Our code supports both Python 2 and Python 3
# Fill in your answer in the next line of code (True or False):
ANSWER_1 = False

# What version(s) of Python do we *recommend* for this course?
#   A. Python v2.3
#   B. Python V2.5 through v2.7
#   C. Python v3.2 or v3.3
#   D. Python v3.4 or higher
# Fill in your answer in the next line of code ("A", "B", "C", or "D"):
ANSWER_2 = "D"


################################################################################
# Note: Each function we require you to fill in has brief documentation        # 
# describing what the function should input and output. For more detailed      # 
# instructions, check out the lab 0 wiki page!                                 #
################################################################################


#### Warmup ####################################################################

def is_even(x):
    """If x is even, returns True; otherwise returns False"""
    return (x%2 == 0)

def decrement(x):
    """Given a number x, returns x - 1 unless that would be less than
    zero, in which case returns 0."""
    if x -1 < 0: return 0
    else: return x - 1

def cube(x):
    """Given a number x, returns its cube (x^3)"""
    return x**3

#### Iteration #################################################################

def is_prime(x):
    """Given a number x, returns True if it is prime; otherwise returns False"""
    for i in range(2,int(x)):
        if x%i == 0:
            return False
    
    return x >= 2

def primes_up_to(x):
    """Given a number x, returns an in-order list of all primes up to and including x"""
    primes = []
    for i in range(2,int(x)+1):
        if(is_prime(i)):
            primes.append(i)
    return primes
#### Recursion #################################################################

def fibonacci(n):
    """Given a positive int n, uses recursion to return the nth Fibonacci number."""
    #TODO: add exception handling
    if n == 0 or n== 1: return n 
    return fibonacci(n-1) + fibonacci(n-2)

def expression_depth(expr):
    """Given an expression expressed as Python lists, uses recursion to return
    the depth of the expression, where depth is defined by the maximum number of
    nested operations."""
    depths = []
    if not isinstance(expr,list): return 0
    for e in expr:
            depths.append(expression_depth(e) + 1)
    return max(depths)

#### Built-in data types #######################################################

def remove_from_string(string, letters):
    """Given an original string and a string of letters, returns a new string
    which is the same as the old one except all occurrences of those letters
    have been removed from it."""
    new_string = []
    for c in string:
        if c not in letters:
            new_string.append(c)
    return ''.join(new_string)

def compute_string_properties(string):
    """Given a string of lowercase letters, returns a tuple containing the
    following three elements:
        0. The length of the string
        1. A list of all the characters in the string (including duplicates, if
           any), sorted in REVERSE alphabetical order
        2. The number of distinct characters in the string (hint: use a set)
    """
    len_str = len(string)
    reverse = sorted(list(string),reverse=True)
    distinct = len(set(string))
    return (len_str, reverse, distinct)

def tally_letters(string):
    """Given a string of lowercase letters, returns a dictionary mapping each
    letter to the number of times it occurs in the string."""
    dic = {}
    for c in string:
        if c in dic: dic[c] = dic[c] + 1 
        else: dic[c] = 1
    return dic

#### Functions that return functions ###########################################

def create_multiplier_function(m):
    """Given a multiplier m, returns a function that multiplies its input by m."""
    return lambda x: x*m


def create_length_comparer_function(check_equal):
    """Returns a function that takes as input two lists. If check_equal == True,
    this function will check if the lists are of equal lengths. If
    check_equal == False, this function will check if the lists are of different
    lengths."""
    if check_equal: return lambda x,y: len(x) == len(y)
    return lambda x,y: len(x) != len(y)


#### Objects and APIs: Copying and modifying objects ############################

def sum_of_coordinates(point):
    """Given a 2D point (represented as a Point object), returns the sum
    of its X- and Y-coordinates."""
    return point.getX() + point.getY()
 
def get_neighbors(point):
    """Given a 2D point (represented as a Point object), returns a list of the
    four points that neighbor it in the four coordinate directions. Uses the
    "copy" method to avoid modifying the original point."""
    x = point.getX()
    y = point.getY()
    points = []

    points.append(point.copy().setX(x+1))
    points.append(point.copy().setX(x-1))
    points.append(point.copy().setY(y+1))
    points.append(point.copy().setY(y-1))

    return points

#### Using the "key" argument ##################################################

def sort_points_by_Y(list_of_points):
    """Given a list of 2D points (represented as Point objects), uses "sorted"
    with the "key" argument to create and return a list of the SAME (not copied)
    points sorted in decreasing order based on their Y coordinates, without
    modifying the original list."""
    return sorted(list_of_points, key=lambda p: p.getY(), reverse=True)

def furthest_right_point(list_of_points):
    """Given a list of 2D points (represented as Point objects), uses "max" with
    the "key" argument to return the point that is furthest to the right (that
    is, the point with the largest X coordinate)."""
    return max(list_of_points, key=lambda p: p.getX())

#### SURVEY ####################################################################

# How much programming experience do you have, in any language?
#     A. No experience (never programmed before this lab)
#     B. Beginner (just started learning to program, e.g. took one programming class)
#     C. Intermediate (have written programs for a couple classes/projects)
#     D. Proficient (have been programming for multiple years, or wrote programs for many classes/projects)
#     E. Expert (could teach a class on programming, either in a specific language or in general)

PROGRAMMING_EXPERIENCE = "B"


# How much experience do you have with Python?
#     A. No experience (never used Python before this lab)
#     B. Beginner (just started learning, e.g. took 6.0001)
#     C. Intermediate (have used Python in a couple classes/projects)
#     D. Proficient (have used Python for multiple years or in many classes/projects)
#     E. Expert (could teach a class on Python)

PYTHON_EXPERIENCE = "B"


# Finally, the following questions will appear at the end of every lab.
# The first three are required in order to receive full credit for your lab.

NAME = "Paul Meierling"
COLLABORATORS = ""
HOW_MANY_HOURS_THIS_LAB_TOOK = 6
SUGGESTIONS = None #optional
