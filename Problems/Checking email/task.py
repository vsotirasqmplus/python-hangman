def check_email(string):
    if string.find(" ") > - 1:
        return False
    at = string.find('@')
    if at > 0:
        if string[at + 2:].find('.') > - 1:
            return True
        else:
            return False
    else:
        return False
