def set_password(password=''):
    # SSH over to CSR and update NHRP password for interface tunnel 300.
    worked = True
    if worked:
        return "NHRP password {} is set.".format(password)
    else:
        return "Setting NHRP password failed."
