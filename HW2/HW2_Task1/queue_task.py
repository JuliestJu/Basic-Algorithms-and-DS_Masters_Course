import time
import threading
import queue

# Create a queue for requests
request_queue = queue.Queue()
continue_generating = True

def generate_request():
    """Generate new requests and add them to the queue."""
    request_id = 0  # Start request IDs from 0
    global continue_generating
    while continue_generating:
        print(f"Generated request with ID: {request_id} \n")
        request_queue.put(request_id)  # Add the request to the queue
        request_id += 1  # Increment the request ID
        time.sleep(0.5)  # Simulate shorter time to generate a request
        if request_id % 20 == 1 and request_id > 1:  # Adjust condition to ask after every 20 requests
            user_input = input("Do you want to continue generating new requests? (yes/no): \n")
            if user_input.lower() != 'yes':
                continue_generating = False

def process_request():
    """Process requests by removing them from the queue."""
    while continue_generating or not request_queue.empty():
        if not request_queue.empty():
            request_id = request_queue.get()
            print(f"Processed request with ID: {request_id} \n")
            time.sleep(1)  # Simulate longer time to process a request
        else:
            time.sleep(0.1)  # Short sleep to avoid busy waiting

def main():
    """Main program to handle generation and processing of requests using threads."""
    generator_thread = threading.Thread(target=generate_request)
    processor_thread = threading.Thread(target=process_request)

    generator_thread.start()
    processor_thread.start()

    # Wait for both threads to finish
    generator_thread.join()
    processor_thread.join()

    print("Bank department finish work.")

if __name__ == "__main__":
    main()