def throwError(x):
    """ Simply throws an error.
    
        prints the error, then quits"""
    print(x)
    quit()

def throwErrorCode(y):
    """ Simply throws an error code.
    
        only integers work for this function. Prints the error code and then quits"""
    print(int(y))
    quit()

def throwErrorWithCode(x, y):
    """throws an error with an added error code"""
    print(f"{x}\nExiting with error code {y}")
    quit()
