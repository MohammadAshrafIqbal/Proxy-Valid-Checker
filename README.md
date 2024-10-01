Proxy Checker
This is a Python script designed to test a list of proxies for validity by sending requests to the http://ipinfo.io/json endpoint. The script identifies and collects valid proxies for further use.

Features
Multi-threaded Testing: The script uses threading to concurrently test multiple proxies, improving efficiency and speed.
Output of Valid Proxies: Valid proxies are printed to the console and stored in a list for further use.
Error Handling: The script handles exceptions to ensure that invalid proxies do not crash the program.
Requirements
Python 3.x
requests library
Installation
Clone the Repository:

bash
Copy code
git clone <repository-url>
cd <repository-directory>
Install Required Packages: You may need to install the requests library if you haven't already. You can do this via pip:

bash
Copy code
pip install requests
Prepare Proxy List: Create a file named proxy_list.txt in the same directory as the script. List each proxy on a new line in the following format:

perl
Copy code
http://username:password@proxyserver:port
http://proxyserver:port
Usage
Run the Script: Execute the script using Python:

bash
Copy code
python proxy_checker.py
Output:

The script will print each valid proxy found during testing.
After completion, a list of valid proxies will be displayed in the console.
Customization
Number of Threads: You can adjust the number of concurrent threads in the following line:
python
Copy code
for _ in range(20):  # Adjust this number to change the level of concurrency
Example Output
javascript
Copy code
Valid proxy found: http://username:password@proxyserver:port
Valid proxy found: http://proxyserver:port
Issue with proxy: http://invalidproxy:port ...
Proxy check complete.
Valid proxies: ['http://username:password@proxyserver:port', 'http://proxyserver:port']
Contributing
Feel free to submit issues or pull requests for any enhancements or bug fixes.
