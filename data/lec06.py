
def cookie_message(num):
    if num == 1:
        message = "You have 1 cookie."
        return message
    elif num >= 0:
        message = "You have " + str(num) + " cookies."
        return message
    else:
        message = "Invalid amount of cookies."
        return message

def questionize(message):
    '''Convert given message into a question
    by adding a ? if it does not already end in one.

    Parameters:
        message - a str
    Return Value
        string that is now a question
    '''
    # how to find last letter of a string?
    


def main():
    m = cookie_message(-4)
    print(m)







if __name__ == '__main__':
    main()
