import webbrowser
#Coded by Pankaj Kumar Saini @IIIT Gwalior

url1 = " https://kite.zerodha.com/chart/ext/tvc/NSE/TORNTPHARM/900609?theme=dark"
url2 = "https://kite.zerodha.com/chart/ext/tvc/NSE/VEDL/784129?theme=dark "
url3 = " https://kite.zerodha.com/chart/ext/tvc/NSE/YESBANK/3050241?theme=dark"
url4 = " https://kite.zerodha.com/chart/ext/tvc/NSE/PETRONET/2905857?theme=dark"
url5 = " https://kite.zerodha.com/chart/ext/tvc/NSE/PIDILITIND/681985?theme=dark"
url6 = "https://kite.zerodha.com/chart/ext/tvc/NSE/PNB/2730497?theme=dark "
url7 = " https://kite.zerodha.com/chart/ext/tvc/NSE/SBICARD/4600577?theme=dark"
url8 = " https://kite.zerodha.com/chart/ext/tvc/NSE/SIEMENS/806401?theme=dark"
url9 = "https://kite.zerodha.com/chart/ext/tvc/NSE/UBL/4278529?theme=dark "
# url10 = " "
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
# webbrowser.get('chrome').open(url10)
