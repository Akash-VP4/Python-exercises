his is a short introduction to requests, a Python module that make grabbing content from the web quite easy.

Requests is NOT in the python distribution, but is installed in Genepy.

To install it on your machine, use: python3 -m pip install requests.

Now, your exercice will just have to GET the content of the page https://api.github.com/users/python, and print it.

In case your computer is not connected to the internet, your program should simply print No internet connectivity. on the standard output.

Beware: requests will raise an exception if there's no internet connectivity, and I will test this case!


Example

$ python solution.py
{
  "login": "python",
  "id": 1525981,
  ...
Oh Damn ! The Wi-Fi is down !

$ python solution.py
No internet connectivity.
