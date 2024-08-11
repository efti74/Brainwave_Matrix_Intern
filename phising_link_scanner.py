import tldextract
import pyfiglet

authentic_website = [
    "facebook.com", "twitter.com", "instagram.com", "linkedin.com", "tiktok.com", "snapchat.com", "pinterest.com", "reddit.com", "tumblr.com", "whatsapp.com", "google.com", "bing.com", "yahoo.com", "duckduckgo.com", "baidu.com", "amazon.com", "ebay.com", "alibaba.com", "walmart.com", "target.com", "bestbuy.com", "etsy.com", "shopify.com", "cnn.com", "bbc.com", "nytimes.com", "theguardian.com", "reuters.com", "aljazeera.com", "netflix.com", "hulu.com", "spotify.com", "youtube.com", "vimeo.com", "disneyplus.com", "apple.com", "microsoft.com", "adobe.com", "github.com", "salesforce.com", "dropbox.com", "paypal.com", "chase.com", "bankofamerica.com", "wellsfargo.com", "citi.com", "airbnb.com", "uber.com", "expedia.com", "booking.com"]

phishing_keywords = [
    "login", "verify", "account", "update", "secure", "password", "signin", "banking", "urgent", "confirm", "pay", "billing", "transaction", "support", "admin", "webmail", "reset", "unusual", "suspend", "locked", "alert", "activation", "deactivation", "refund", "win", "free", "prize", "offer", "claim", "limited", "access", "important", "notice", "safety", "security", "compliance", "notification", "attention", "warning", "review", "appeal", "confirm", "click", "here", "protection", "authenticate", "update", "verify", "service", "message", "secure_login"]

def url_extractor(url):
    extracted = tldextract.extract(url)
    return extracted.domain, extracted.suffix

def phishing_keyword_detection(url):
    url_portion = url.split(".")
    for url_partition in url_portion:
        if url_partition in phishing_keywords:
            print(f"🚨 Phishing alert! ⚠️ {url} is not a trusted website. 😕")
            return True
    return False

def phising_link_detection(url):
    domain, suffix = url_extractor(url)
    if f"{domain}.{suffix}" not in authentic_website:
        print(f"🚨 Phishing alert! ⚠️ {url} is not a trusted website. 😕")
    else:
        print(f"👍 You can go with the {url} It is safe. 😊")
        
def welcome_note():
    f = pyfiglet.Figlet(font='slant')
    print(f.renderText('URL Scanner'))
    print("This program will help you determine if a website is safe or not by scanning the URL for phishing keywords and checking if the domain is authentic.\n")

def main():
    welcome_note()
    while True:
        url = input("Enter the URL to scan 🔍 (or press 'e' to exit): ")
        if url == "e":
            print("Safe Exit. Goodbye. 👋")
            break
        
        keyword_detection = phishing_keyword_detection(url)
        if keyword_detection is not True:
            phising_link_detection(url)
        else:
            print("Phishing keyword detected. Please enter a new URL. 🔄\n")

if __name__ == "__main__":
    main()