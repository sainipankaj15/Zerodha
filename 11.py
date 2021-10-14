#Coded by Pankaj Kumar Saini @IIIT Gwalior
import webbrowser


url1 = "https://kite.zerodha.com/chart/ext/tvc/NSE/AXISBANK/1510401?theme=dark"
url2 = "https://kite.zerodha.com/chart/ext/tvc/NSE/ADANIPORTS/3861249?theme=dark "
url3 = " https://kite.zerodha.com/chart/ext/tvc/NSE/ASIANPAINT/60417?theme=dark"
url4 = "https://kite.zerodha.com/chart/ext/tvc/NSE/BAJFINANCE/81153?theme=dark"
url5 = " https://kite.zerodha.com/chart/ext/tvc/NSE/BAJAJFINSV/4268801?theme=dark"
url6 = " https://kite.zerodha.com/chart/ext/tvc/NSE/BAJAJ-AUTO/4267265?theme=dark"
url7 = " https://kite.zerodha.com/chart/ext/tvc/NSE/BHARTIARTL/2714625?theme=dark"
url8 = " https://kite.zerodha.com/chart/ext/tvc/NSE/BPCL/134657?theme=dark"
url9 = "https://kite.zerodha.com/chart/ext/tvc/NSE/BRITANNIA/140033?theme=dark "
url10 = " https://kite.zerodha.com/chart/ext/tvc/NSE/CIPLA/177665?theme=dark"

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
