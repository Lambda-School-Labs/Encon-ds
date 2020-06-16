# python script

#Function
def process_base64(img_string: str):
    """
    Converts a base64 image string to byte array.  
    Example: "data:image/png;base64,iVBORw0KGgoAAAANSUhE..."  
    becomes b'iVBORw0KGgoAAAANSUhE...'
    """
    # If base64 has metadata attached, get only data after comma
    if img_string.startswith("data"):
        img_string = img_string.split(",")[-1]
    return bytes(img_string,'utf-8')