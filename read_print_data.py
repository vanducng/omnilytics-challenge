import os

def is_float(obj):
    """
    Check if object is float datatype or not
    
    Args:
        obj: input object in string
    
    Returns:
        True if it is float, else False
    """
    try:
        float(obj)
    except ValueError:
        return False
    return True

if __name__=="__main__":

    base_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(base_path, "output.txt")
    
    with open(file_path, "r") as f:
        content = f.read()
        objs = [obj.strip() for obj in content.split(",")]

    for obj in objs:
        if obj.isnumeric():
            result = f"{obj} - integer"
        elif obj.isalpha():
            result = f"{obj} - alphabetical strings"
        elif obj.isalnum():
            result = f"{obj} - alphanumeric"
        elif is_float(obj):
            result = f"{obj} - real number"
        else:
            raise ValueError(f"Unknown object type: '{result}', please check your code.")

        print(result)