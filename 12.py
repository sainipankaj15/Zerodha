
#Coded by Pankaj Kumar Saini @IIIT Gwalior
import webbrowser


url1 = " https://kite.zerodha.com/chart/ext/tvc/NSE/COALINDIA/5215745?theme=dark"
url2 = "https://kite.zerodha.com/chart/ext/tvc/NSE/DIVISLAB/2800641?theme=dark "
url3 = "https://kite.zerodha.com/chart/ext/tvc/NSE/DRREDDY/225537?theme=dark"
url4 = "https://kite.zerodha.com/chart/ext/tvc/NSE/EICHERMOT/232961?theme=dark"
url5 = "https://kite.zerodha.com/chart/ext/tvc/NSE/GRASIM/315393?theme=dark "
url6 = "https://kite.zerodha.com/chart/ext/tvc/NSE/HCLTECH/1850625?theme=dark "
url7 = "https://kite.zerodha.com/chart/ext/tvc/NSE/HDFC/340481?theme=dark "
url8 = "https://kite.zerodha.com/chart/ext/tvc/NSE/HDFCBANK/341249?theme=dark "
url9 = "https://kite.zerodha.com/chart/ext/tvc/NSE/HDFCLIFE/119553?theme=dark "
url10 = "https://kite.zerodha.com/chart/ext/tvc/NSE/HEROMOTOCO/345089?theme=dark"

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
