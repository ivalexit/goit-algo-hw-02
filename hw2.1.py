import queue
import time
import random

# Creating a new request
def generate_request (request_queue, request_id):
    request_info = f"Request number{request_id}"
    request_queue.put(request_info)
    print(f"New request added: {request_info}")

# Processing requests
def process_request(request_queue):
    if not request_queue.empty():
        request_info = request_queue.get()
        print(f"Processing of the request: {request_info}")

        time.sleep(random.uniform(0.5, 2.5))
        print(f"{request_info} is processed.")
    else: print("There are no new requests. Have a coffee.")

def main():
    request_queue = queue.Queue()
    request_id = 0


 # *Option with limited amount of requests*
 #   processed_requests = 0   (requests counter)
 #   max_requests = 1000      (max amount of requests)
 #   try:
 #     while processed_requests < max_requests:
 #         time.sleep(1)


    try:
        while True:
            time.sleep(1)
            # 50% chance of adding a new request
            if random.choice([True, False]):
                request_id += 1
                generate_request(request_queue, request_id)

            #50% chance of processing a request
            if random.choice([True, False]):
                process_request(request_queue)
#          *    processed_requests += 1    (for requests counter)  *
            

    except KeyboardInterrupt:
        print("\nThe program was finished by user.")


# * if processed_requests >= max_requests:
#       print("\nMax requests amount was reached.")

#   print(f"Program completed after processing {processed_requests} requests.") *


if __name__ == "__main__":
    main()