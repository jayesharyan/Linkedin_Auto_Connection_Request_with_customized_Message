# LinkedIn Connection Request Automator

## Overview

This script automates the process of sending connection requests on LinkedIn based on specified search criteria. It utilizes the LinkedIn API to perform searches for profiles matching the defined parameters and sends connection requests to them with a customized message.

## Prerequisites

- Python 3.x installed on your system
- Installation of the `linkedin_api` library (`pip install linkedin-api`)

## Usage

1. **LinkedIn Credentials**: Replace `'Your Email Id'` and `'Your Password'` with your LinkedIn username and password in the script.

2. **Define Search Parameters**: Adjust the `search_query` and `search_filters` variables according to your preferences. These parameters include keywords, regions, and optionally, network depths and result limits.

3. **Customize Invitation Message**: Customize the invitation message in the `send_connection_requests()` function. Ensure it's concise and relevant to increase the likelihood of connections accepting your request.

4. **Run the Script**: Execute the script by running `python linkedin_connection_request.py`. Ensure you are in the directory containing the script file.

## Important Notes

- **API Limitations**: Be mindful of LinkedIn's API usage limitations and potential rate limits. Adjust the script's sleep time (`time.sleep()`) accordingly to avoid being rate-limited.

- **Error Handling**: The script includes basic error handling to handle exceptions gracefully. However, if encountering persistent issues, review the error messages and consult the LinkedIn API documentation for troubleshooting.

- **Legal and Ethical Considerations**: Ensure compliance with LinkedIn's terms of service and respect the platform's usage policies. Automating actions on LinkedIn should be done responsibly and ethically, avoiding spammy or unsolicited behavior.

## Contributions and Feedback

Contributions, suggestions, and feedback are welcome! If you encounter any bugs or have ideas for improvements, feel free to open an issue or submit a pull request.
