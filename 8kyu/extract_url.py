import re
def domain_name(url):
        x = re.findall("[/]{2}|[.]+.*[.]", url)
        
        print(x)
if __name__ == "__main__":
        domain_name("http://www.zombie-bites.com")
