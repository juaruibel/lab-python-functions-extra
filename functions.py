import string

def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.
    Parameters:
    lst (list): The input list.
    Returns:
    list: A new list with unique elements from the input list.
    """
    # your code goes here

    try:
        if type(lst) != list:
            raise TypeError("Argument is not a list.")
        if len(lst) == 0:
            raise ValueError("Argument is empty, please try again.")
        seen = set()
        finished_lst = []
        for elem in lst:
            if elem not in seen:
                seen.add(elem)
                finished_lst.append(elem)
    except TypeError as e:
        print(f"Error: {e}")
        return []
    except ValueError as e:
        print(f"Error: {e}")
        return []
    else:
        return finished_lst
    finally:
        print(
            """
Program finished successfully. Read the results and report any issue.
This program has been designed to iterate through a list and return another
list with just the unique elements of the first list.
            """
            )
        
def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    # your code goes here
    try:
        if len(string) == 0:
            raise ValueError("String is empty")
        string = string.strip().split()
        string = "".join(string)
        uppercase_letters = ""
        lowercase_letters = ""
        for char in string:
            if char.islower():
                lowercase_letters = char + lowercase_letters
            else:
                uppercase_letters = char + uppercase_letters
        solution = (len(uppercase_letters), len(lowercase_letters))
    except ValueError as e:
        print(f"Error: {e}")
        return (0, 0)
    except TypeError as e:
        print(f'Error: {e}')
        return (0, 0)
    except AttributeError as e:
        print(f'Error: this program works with strings, {e}.')
        return (0, 0)
    else:
        print(f'Uppercase count: {solution[0]}, Lowercase count: {solution[1]}'); return solution
    finally:
        print("This program run succesfully.")

def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    # your code goes here
    try:
        if len(sentence) == 0:
            raise ValueError("String is empty.")
        solution = sentence.replace(",", "").replace(".", "").replace("!", "").replace("¡", "").replace("?", "").replace("¿", "").replace(":", "")
    except AttributeError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        return solution
    finally: 
        print("remove_puntuation function ran succesfully.")

# your code goes here

def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    # your code goes here
    try:
        no_punctuation = remove_punctuation_f(sentence)
        solution = len(no_punctuation.split())
    except AttributeError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")
    else:
        print(f"In sentence provided: '{sentence}', there are: {solution} words."); return solution
    finally:
        print("Word_count function ran succesfully.")