import webbrowser
#Coded by Pankaj Kumar Saini @IIIT Gwalior

url1 = "https://kite.zerodha.com/chart/ext/tvc/NSE/ABBOTINDIA/4583169?theme=dark "
url2 = " https://kite.zerodha.com/chart/ext/tvc/NSE/ACC/5633?theme=dark"
url3 = " https://kite.zerodha.com/chart/ext/tvc/NSE/ADANIENT/6401?theme=dark"
url4 = "https://kite.zerodha.com/chart/ext/tvc/NSE/ADANIGREEN/912129?theme=dark "
url5 = " https://kite.zerodha.com/chart/ext/tvc/NSE/ALKEM/2995969?theme=dark"
url6 = " https://kite.zerodha.com/chart/ext/tvc/NSE/ALKEM/2995969?theme=dark"
url7 = " https://kite.zerodha.com/chart/ext/tvc/NSE/APOLLOHOSP/40193?theme=dark"
url8 = " https://kite.zerodha.com/chart/ext/tvc/NSE/AUROPHARMA/70401?theme=dark"
url9 = " https://kite.zerodha.com/chart/ext/tvc/NSE/BAJAJHLDNG/78081?theme=dark"
url10 = " https://kite.zerodha.com/chart/ext/tvc/NSE/BANDHANBNK/579329?theme=dark"

chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

webbrowser.get('chrome').open(url1)

webbrowser.get('chrome').open(url2)
webbrowser.get('chrome').open(url3)
webbrowser.get('chrome').open(url4)
webbrowser.get('chrome').open(url5)

webbrowser.get('chrome').open(url6)

webbrowser.get('chrome').open(url7)
webbrowser.get('chrome').open(url8)
webbrowser.get('chrome').open(url9)
webbrowser.get('chrome').open(url10)
