import socket
import threading
import logging
from collections import Counter

# Set up basic logging configuration
logging.basicConfig(filename='server_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Constants for the server configuration
HOST = 'localhost'
PORT = 12345

def handle_client(client_socket, client_address):
    """ Handle incoming client requests. """
    logging.info(f"Client {client_address} connected.")

    try:
        while True:
            request_data = client_socket.recv(1024).decode()
            if not request_data:  
                break  # Client closed connection
            
            logging.info(f"Received request from {client_address}: {request_data}")
            response = process_request(request_data)

            # Extract request type and input string for logging
            check_type, input_string = request_data.split('|')
            log_message = f"Client: {client_address}, Type: {check_type}, Input: '{input_string}', Response: {response}"
            logging.info(log_message)

            client_socket.send(response.encode())
            logging.info(f"Sent response to {client_address}: {response}")
    except Exception as e:
        logging.error(f"Error handling client {client_address}: {e}")
    finally:
        client_socket.close()
        logging.info(f"Closed connection with {client_address}")

def can_form_palindrome(input_string):
    """ Check if a string can be rearranged into a palindrome. """
    freq = Counter(input_string)
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    return odd_count <= 1

def min_swaps_to_palindrome(s):
    """ Calculate the minimum swaps needed to convert the string into a palindrome 
        by allowing swaps between any two characters.
    """
    s = list(s)  # Convert string to list for easy swapping
    n = len(s)
    swaps = 0

    # Identifying the positions of the characters
    char_positions = {}
    for i, char in enumerate(s):
        if char in char_positions:
            char_positions[char].append(i)
        else:
            char_positions[char] = [i]

    left, right = 0, n - 1

    while left < right:
        if s[left] == s[right]:  # Characters already match
            left += 1
            right -= 1
            continue

        # Find the closest matching character to swap
        match_idx = right
        while match_idx > left and s[match_idx] != s[left]:
            match_idx -= 1

        if match_idx == left:  # If no match is found, move it to the center
            s[left], s[left + 1] = s[left + 1], s[left]
            swaps += 1
        else:
            # Swap the matching character to the correct position
            s[match_idx], s[right] = s[right], s[match_idx]
            swaps += 1  # swap = swap + 1
        left += 1
        right -= 1

    return swaps


def process_request(request_data):
    """ Process the client's request and generate a response. """
    check_type, input_string = request_data.split('|')
    input_string = ''.join(e for e in input_string if e.isalnum()).lower()

    if check_type == 'simple':
        result = is_palindrome(input_string)
        return f"Is palindrome: {result}"
    
    elif check_type == 'complex':
        can_rearrange = can_form_palindrome(input_string)
        if not can_rearrange:
            return "Can form a palindrome: False"
        
        swaps = min_swaps_to_palindrome(input_string)
        return f"Can form a palindrome: True\nComplexity score: {swaps}"


def is_palindrome(input_string):
    """ Check if the given string is a palindrome. """
    return input_string == input_string[::-1]

def start_server():
    """ Start the server and listen for incoming connections. """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        logging.info(f"Server started and listening on {HOST}:{PORT}")
        
        while True:
            # Accept new client connections and start a thread for each client
            client_socket, client_address = server_socket.accept()
            threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

if __name__ == '__main__':
    start_server()
