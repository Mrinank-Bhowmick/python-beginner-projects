# Link Shortener by Vaibhav Agrawal in Python
import pyshorteners
long_link = input("Enter The Link :  ")
shortener = pyshorteners.Shortener()
short_link = shortener.tinyurl.short(long_link)
print(f"Shortened Link:  {short_link}")
