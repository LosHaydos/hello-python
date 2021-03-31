def read_input():
    return"some input"

def do_calculate(data):
    return data + " " + data

def send_email(body, to):
    #some magic that send the email
    return True

def main():
    inputValue = read_input()
    result = do_calculation(inputValue)
    send_email(result, "hjmoxey@gmail.com")
