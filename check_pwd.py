def check_pwd(pwd):
    symbols = '~`!@#$%^&*()_+-='
    if len(pwd) < 8 or len(pwd) > 20:
        return False
    if not any(char.isupper() for char in pwd):
        return False
    return True
