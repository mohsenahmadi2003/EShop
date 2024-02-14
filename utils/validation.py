def validate_count(count):
    try:
        count = int(count)
        if count < 1:
            return False
        return True
    except ValueError as e:
        print(e)
        return False