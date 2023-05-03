//What is HTTP?
//  HTTP stands for Hypertext transfer protocol and is used as a method to load pages by encoding and transporting info between a client and server.
//What is a URL?
//  URL stands for Uniform Resource Locator and is a reference address to find a resource such as a webpage on the internet.
//What is DNS?
//  DNS stands for Domain Name System and turns domain names that are readable by humans into IP addresses that are readable by computers.
//What is a query string?
//  The query string string provides extra information to the server at the end of the URL and is in the format of ?x=1&x=2 as an example.
//What are two HTTP verbs and how are they different?
//  GET is a HTTP verb that requests info from the server without side effects, and as such the arguments seen in terminal are passed in the query string.
//  POST is a HTTP verb that requests info with side effects, and as such the arguments are typically in the body of request.
//What is an HTTP request?
//  A request from a client(computer) to a server(webpage) which follows the HTTP protocol.
//What is an HTTP response?
//  A response from a server to a client which follws the HTTP protocol.
//What is an HTTP header? Give a couple examples of request and response headers you have seen.
//  A type of HTTP request/response that gives additional info about the request/response. 
//  Request: Host, User-Agent, Connection, Cache-Control
//  Response: Connection, Date, Server, Set-Cookie
//What are the processes that happen when you type “http://somesite.com/some/page.html” into a browser?
//  First your browser turns the name into an IP address using DNS.  The browser then sends a request to the IP adress with additional info about other stuff it needs such as info about the browser.
//  Then, the server sends a response, and if successful the browser makes a DOM from the HTML received, and gets the other resources it needs outlined in the HTML, all in separate asynchronous requests.
