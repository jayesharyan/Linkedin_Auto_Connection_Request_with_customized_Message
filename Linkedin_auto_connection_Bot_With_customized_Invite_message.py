from linkedin_api import Linkedin
import time

# Enter your LinkedIn username and password
username = 'Your Email Id'
password = 'Your Password'

# Initialize LinkedIn API
print("Initializing LinkedIn API...")
linkedin = Linkedin(username, password)

# Define search parameters
search_query = 'azure cloud'
search_filters = {
    'keywords': search_query,
    #'network_depths': ['F', 'S', 'O'],  # First, Second, and Third+ connections
    'regions': ['101452733'],  # India location code
    #'limit': 50  # Number of results per page
}

# Send connection requests
def send_connection_requests(profiles):
    for profile in profiles:
        try:
            # Customize invitation message
            message = f"Hi {profile['name']}, I am actively looking for roles in Azure Cloud and I am an immediate joiner. Let's connect!"
            if len(message) > 300:
                message = message[:297] + "..."
            linkedin.add_connection(profile_public_id=profile['urn_id'], message=message)
            print(f"Sent connection request to {profile['name']}.")
        except Exception as e:
            print(f"Failed to send connection request to {profile['name']}: {e}")

# Perform search and send connection requests
try:
    print("Starting search and connection requests...")
    page_num = 1
    while True:
        print(f"Processing page {page_num}...")
        search_results = linkedin.search_people(**search_filters)
        print(search_results)
        if search_results:
            send_connection_requests(search_results)
            page_num += 1
            time.sleep(2)  # Add a delay to avoid being rate-limited
        else:
            print("No more search results found.")
            break
except Exception as e:
    print("An error occurred: ", e)
