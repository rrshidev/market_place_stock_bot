import base64

def generate_callback_data(item_name):
    encoded_item_name = base64.b64encode(item_name.encode()).decode()
    # print('------->>>>>', encoded_item_name)
    return encoded_item_name