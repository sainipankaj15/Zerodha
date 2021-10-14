import webbrowser
#Coded by Pankaj Kumar Saini @IIIT Gwalior

url1 = " https://kite.zerodha.com/chart/ext/tvc/NSE/SUNPHARMA/857857?theme=dark"
url2 = "https://kite.zerodha.com/chart/ext/tvc/NSE/TATACONSUM/878593?theme=dark "
url3 = " https://kite.zerodha.com/chart/ext/tvc/NSE/TATAMOTORS/884737?theme=dark"
url4 = "https://kite.zerodha.com/chart/ext/tvc/NSE/TATASTEEL/895745?theme=dark "
url5 = " https://kite.zerodha.com/chart/ext/tvc/NSE/TCS/2953217?theme=dark"
url6 = " https://kite.zerodha.com/chart/ext/tvc/NSE/TECHM/3465729?theme=dark"
url7 = "https://kite.zerodha.com/chart/ext/tvc/NSE/TITAN/897537?theme=dark"
url8 = " https://kite.zerodha.com/chart/ext/tvc/NSE/UPL/2889473?theme=dark"
url9 = " https://kite.zerodha.com/chart/ext/tvc/NSE/ULTRACEMCO/2952193?theme=dark"
url10 = " https://kite.zerodha.com/chart/ext/tvc/NSE/WIPRO/969473?theme=dark"

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
