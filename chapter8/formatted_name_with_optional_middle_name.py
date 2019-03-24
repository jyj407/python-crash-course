def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a full name, neatly formated."""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
computer_scientist = get_formatted_name('james', 'jiang', 'xuan')
print(musician)
print(computer_scientist)
