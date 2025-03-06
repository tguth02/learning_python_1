
def convert_age_to_int(age_in_str):
    try:
        my_age_in_integer = int(age_in_str)
        return my_age_in_integer
    except ValueError:
        print("Could not convert.")

