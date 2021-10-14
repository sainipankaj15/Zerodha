import webbrowser
#Coded by Pankaj Kumar Saini @IIIT Gwalior

url1 = "https://kite.zerodha.com/chart/ext/tvc/NSE/HINDALCO/348929?theme=dark"
url2 = " https://kite.zerodha.com/chart/ext/tvc/NSE/HINDUNILVR/356865?theme=dark"
url3 = " https://kite.zerodha.com/chart/ext/tvc/NSE/ICICIBANK/1270529?theme=dark"
url4 = " https://kite.zerodha.com/chart/ext/tvc/NSE/INDUSINDBK/1346049?theme=dark"
url5 = " https://kite.zerodha.com/chart/ext/tvc/NSE/INFY/408065?theme=dark"
url6 = " https://kite.zerodha.com/chart/ext/tvc/NSE/IOC/415745?theme=dark"
url7 = "https://kite.zerodha.com/chart/ext/tvc/NSE/ITC/424961?theme=dark "
url8 = "https://kite.zerodha.com/chart/ext/tvc/NSE/JSWSTEEL/3001089?theme=dark "
url9 = "https://kite.zerodha.com/chart/ext/tvc/NSE/KOTAKBANK/492033?theme=dark"
url10 = " https://kite.zerodha.com/chart/ext/tvc/NSE/LT/2939649?theme=dark"
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
