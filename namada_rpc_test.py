from hyper import HTTP20Connection
from concurrent.futures import ThreadPoolExecutor, as_completed
import random

# Configuration
TARGET_URL = "your_rpc_server_address"  # Without "http://" or "https://"
ENDPOINT = "/tx_search"
NUM_REQUESTS = 2000
CONCURRENCY_LEVEL = 100  # Adjust based on your testing environment capabilities

def make_request(conn, tx_id):
    """
    Function to make a request to the RPC server
    """
    try:
        response = conn.request('GET', f'{ENDPOINT}?query=_&prove=_&page=_&per_page=_&order_by=_{tx_id}')
        # Uncomment the following line if you want to print response status for each request
        # print(f"Request {tx_id}: Response status: {response.status}")
    except Exception as e:
        print(f"Request {tx_id} failed: {e}")

def main():
    # Create a connection instance
    conn = HTTP20Connection(TARGET_URL, secure=False)

    # Use ThreadPoolExecutor to manage concurrent requests
    with ThreadPoolExecutor(max_workers=CONCURRENCY_LEVEL) as executor:
        futures = [executor.submit(make_request, conn, i) for i in range(NUM_REQUESTS)]
        
        # Wait for all futures to complete
        for future in as_completed(futures):
            pass  # You can handle results or exceptions here

    conn.close()

if __name__ == "__main__":
    main()
