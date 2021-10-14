import webbrowser

#Coded by Pankaj Kumar Saini @IIIT Gwalior
url1 = "https://kite.zerodha.com/chart/ext/tvc/NSE/BIOCON/2911489?theme=dark "
url2 = "https://kite.zerodha.com/chart/ext/tvc/NSE/BERGEPAINT/103425?theme=dark "
url3 = " https://kite.zerodha.com/chart/ext/tvc/NSE/BOSCHLTD/558337?theme=dark"
url4 = " https://kite.zerodha.com/chart/ext/tvc/NSE/CADILAHC/2029825?theme=dark"
url5 = "https://kite.zerodha.com/chart/ext/tvc/NSE/COLPAL/3876097?theme=dark "
url6 = " https://kite.zerodha.com/chart/ext/tvc/NSE/DABUR/197633?theme=dark"
url7 = " https://kite.zerodha.com/chart/ext/tvc/NSE/DLF/3771393?theme=dark"
url8 = " https://kite.zerodha.com/chart/ext/tvc/NSE/DMART/5097729?theme=dark"
url9 = "https://kite.zerodha.com/chart/ext/tvc/NSE/GAIL/1207553?theme=dark "
url10 = "https://kite.zerodha.com/chart/ext/tvc/NSE/GODREJCP/2585345?theme=dark "
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
