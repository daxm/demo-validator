def set_password(password=''):
    # SSH over to oob-server and update guacamole password for dcloud user.
    # TODO Actually write in the code to set up password.
    worked = True
    if worked:
        return "Guacamole password {} is set.".format(password)
    else:
        return "Setting guacamole password failed."
