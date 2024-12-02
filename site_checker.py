
import requests  # Import to make the HTTP requests.

# Dictionary to map HTTP status codes to their explanations.
STATUS_CODE_DESCRIPTIONS = {
    200: "OK: The request was successful, and the server returned the requested resource.",
    201: "Created: The request was successful, and a new resource was created.",
    202: "Accepted: The request was accepted for processing but is not yet completed.",
    204: "No Content: The server successfully processed the request, but no content is returned.",
    301: "Moved Permanently: The requested resource has been permanently moved to a new location.",
    302: "Found: The requested resource has been temporarily moved to a new location.",
    304: "Not Modified: The requested resource has not been modified since the last request.",
    400: "Bad Request: The server cannot or will not process the request due to something that is perceived to be a client error.",
    401: "Unauthorized: The request requires user authentication.",
    403: "Forbidden: The server understood the request, but is refusing to fulfill it.",
    404: "Not Found: The requested resource could not be found on the server.",
    500: "Internal Server Error: The server encountered an internal error and was unable to complete the request.",
    503: "Service Unavailable: The server is currently unable to handle the request due to a temporary overloading or maintenance of the server.",
}

def explaination_of_status_code(status_code):
   
    return STATUS_CODE_DESCRIPTIONS.get(
        status_code, "Unknown Status Code: The server returned a status code not in our list. Please refer to HTTP documentation for details."
    )

def website_connectivity_checker(url):
    try:
        # Send a GET request to the website with a timeout of 5 seconds.
        response = requests.get(url, timeout=5)
        # If the request is successful or returns a valid status, provide details.
        status_code = response.status_code
        explanation = explaination_of_status_code(status_code)
        return f"Status code {status_code}: {explanation}"
    except requests.exceptions.ConnectionError:
        return "Error: The website is unreachable. Connection error occurred."
    except requests.exceptions.Timeout:
        return "Error: The website is unreachable. Request timed out."
    except requests.exceptions.RequestException as e:
        return f"Error: The website is unreachable. An error occurred: {e}"

def main():
   
    print("Website Connectivity Checker")
    print("============================")
    print("")

    while True:
        # Use strip() to clean up any unnecessary whitespace when typing the URL.
        url = input("Enter the URL of the website you would like to check (or type 'exit' OR 'e' to quit): ").strip()
        if url.lower() in ('exit', 'e'): 
            break  # Exit the program.

        # If the URL does not start with "http://" or "https://", add "http://" by default.
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url

        # Call the function to check the website.
        output = website_connectivity_checker(url)
        print(output)


# Call the main function when the script is executed directly.

main()
