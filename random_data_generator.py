import random
import string
import os

def get_random_object(max_obj_length = 15):
    """
    Get the random objects from the supported list including: integer, float, alphabet and alphanumeric.
    
    Args:
        max_obj_length: the length of objects (note: integer part of float & excluding spaces in alphanumeric)
    
    Return:
        random_obj: random object
    """
    
    obj_type = random.choice(["integer", "float", "alphabet", "alphanumeric"])
    obj_length = random.randint(2, max_obj_length)
    random_number = random.random()
    
    if obj_type == "integer":
        rand_obj = int(random_number*(10**obj_length))
    
    elif obj_type == "float":
        rand_obj = round(random_number*(10**obj_length), 5)
        
    elif obj_type == "alphabet":
        rand_obj = "".join(random.choices(string.ascii_letters, k = obj_length))
        
    elif obj_type == "alphanumeric":
        rand_obj = "".join(random.choices(string.ascii_letters + string.digits, k = obj_length-2))
        rand_obj += random.choice(string.ascii_letters)
        rand_obj += random.choice(string.digits)
        
        # Add random spaces before and after the alphanumeric object, total spaces <= 10
        n_before = random.randint(0, 10)
        n_after = random.randint(0, 10 - n_before)
        rand_obj = n_before*" " + rand_obj + n_after*" "
    else:
        raise ValueError(f"Not supported object type: '{obj_type}'")
    
    return rand_obj

def write_file(content, file_path):
    """
    Write the content to file. If file is not exsited, it uses 'w' mode else 'a' (append) mode.
    
    Args:
        content: content to write
        file_path: path to store the file
    
    Returns:
        None
    """
    write_mode = "a" if os.path.exists(file_path) else "w"
    with open(file_path, write_mode) as f:
        if write_mode == "w":
            f.write(content)
        else:
            f.write(", " + content)

if __name__=="__main__":
    # Write object by batch of N objects (N=500 inthis case), so it can scale to write the large file
    # to prevent out of memory

    obj_cnt = 0
    batch = 500
    one_mb = int(1<<20)
    rand_objs = []

    base_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(base_path, "output.txt")
    file_size = os.path.getsize(file_path) if os.path.exists(file_path) else 0

    print("Script started...")
    while file_size < 10*one_mb:
        
        rand_objs.append(str(get_random_object()))
        obj_cnt += 1
        
        if obj_cnt % batch == 0:
            content = ", ".join(rand_objs)
            write_file(content, file_path)
            file_size = os.path.getsize(file_path)
            rand_objs = []

    print(f"Total generated objects: {obj_cnt}")
    print(f"File size: {round(file_size/one_mb, 3)} MB")