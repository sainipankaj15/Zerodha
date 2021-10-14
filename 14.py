import webbrowser
#Coded by Pankaj Kumar Saini @IIIT Gwalior

url1 = " https://kite.zerodha.com/chart/ext/tvc/NSE/M&M/519937?theme=dark"
url2 = " https://kite.zerodha.com/chart/ext/tvc/NSE/MARUTI/2815745?theme=dark"
url3 = "https://kite.zerodha.com/chart/ext/tvc/NSE/NESTLEIND/4598529?theme=dark "
url4 = "https://kite.zerodha.com/chart/ext/tvc/NSE/NTPC/2977281?theme=dark "
url5 = " https://kite.zerodha.com/chart/ext/tvc/NSE/ONGC/633601?theme=dark"
url6 = " https://kite.zerodha.com/chart/ext/tvc/NSE/POWERGRID/3834113?theme=dark"
url7 = " https://kite.zerodha.com/chart/ext/tvc/NSE/RELIANCE/738561?theme=dark"
url8 = " https://kite.zerodha.com/chart/ext/tvc/NSE/SBILIFE/5582849?theme=dark"
url9 = " https://kite.zerodha.com/chart/ext/tvc/NSE/SBIN/779521?theme=dark"
url10 = " https://kite.zerodha.com/chart/ext/tvc/NSE/SHREECEM/794369?theme=dark"
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
