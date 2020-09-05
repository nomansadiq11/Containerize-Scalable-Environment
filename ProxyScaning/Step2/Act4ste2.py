import sys
import urllib.request 
import ipaddress


# read the list of proxy IPs in proxyList
proxyList = ['140.82.61.218'] # there are two sample proxy ip

def is_bad_proxy(pip):    
    try:        
        proxy_handler = urllib.request.ProxyHandler({'http': pip})        
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)        
        sock=urllib.request.urlopen('http://www.google.com')  # change the url address here
        #sock=urllib.urlopen(req)
    except urllib.error.HTTPError as e:        
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:
        # print( "ERROR:", detail)
        return 1
    return 0

start_ip = ipaddress.IPv4Address(sys.argv[1])
end_ip = ipaddress.IPv4Address(sys.argv[2])
for ip_int in range(int(start_ip), int(end_ip)):
    if is_bad_proxy(ipaddress.IPv4Address(ip_int)):
        print ("Proxy is not working ", ipaddress.IPv4Address(ip_int))
    else:
        print (ipaddress.IPv4Address(ip_int), "proxy discovered")

    # print(ipaddress.IPv4Address(ip_int))


# for item in proxyList:
#     if is_bad_proxy(item):
#         print ("Proxy is not working ", item)
#     else:
#         print (item, "proxy discovered")