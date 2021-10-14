import webbrowser
#Coded by Pankaj Kumar Saini @IIIT Gwalior

url1 = "https://kite.zerodha.com/chart/ext/tvc/NSE/MUTHOOTFIN/6054401?theme=dark "
url2 = "https://kite.zerodha.com/chart/ext/tvc/NSE/NMDC/3924993?theme=dark "
url3 = "https://kite.zerodha.com/chart/ext/tvc/NSE/PEL/617473?theme=dark "
url4 = "https://kite.zerodha.com/chart/ext/tvc/NSE/PGHH/648961?theme=dark "
url5 = "https://kite.zerodha.com/chart/ext/tvc/NSE/NAUKRI/3520257?theme=dark "
url6 = " https://kite.zerodha.com/chart/ext/tvc/NSE/LUPIN/2672641?theme=dark"
url7 = " https://kite.zerodha.com/chart/ext/tvc/NSE/MARICO/1041153?theme=dark"
url8 = " https://kite.zerodha.com/chart/ext/tvc/NSE/MCDOWELL-N/2674433?theme=dark"
url9 = " https://kite.zerodha.com/chart/ext/tvc/NSE/MOTHERSUMI/1076225?theme=dark"
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
