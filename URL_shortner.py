import pyshorteners
import validators

def shorten_url(long_url):
    if not validators.url(long_url):
        print("Invalid URL. Please enter a valid URL.")
        return None

    s = pyshorteners.Shortener()
    try:
        short_url = s.tinyurl.short(long_url)
        return short_url
    except Exception as e:
        print(f"Error shortening URL: {e}")
        return None

def main():
    print("URL Shortener")
    long_url = input("Enter the URL to shorten: ")
    short_url = shorten_url(long_url)
    if short_url:
        print(f"Shortened URL: {short_url}")

if __name__ == "__main__":
    main()
