import webbrowser
#Coded by Pankaj Kumar Saini @IIIT Gwalior

url1 = "https://kite.zerodha.com/chart/ext/tvc/NSE/HAVELLS/2513665?theme=dark "
url2 = " https://kite.zerodha.com/chart/ext/tvc/NSE/HDFCAMC/1086465?theme=dark"
url3 = " https://kite.zerodha.com/chart/ext/tvc/NSE/HINDPETRO/359937?theme=dark"
url4 = " https://kite.zerodha.com/chart/ext/tvc/NSE/ICICIGI/5573121?theme=dark"
url5 = " https://kite.zerodha.com/chart/ext/tvc/NSE/IGL/2883073?theme=dark"
url6 = "https://kite.zerodha.com/chart/ext/tvc/NSE/ICICIPRULI/4774913?theme=dark "
url7 = " https://kite.zerodha.com/chart/ext/tvc/NSE/INDIGO/2865921?theme=dark"
url8 = " https://kite.zerodha.com/chart/ext/tvc/NSE/INDUSTOWER/7458561?theme=dark"
url9 = "https://kite.zerodha.com/chart/ext/tvc/NSE/JUBLFOOD/4632577?theme=dark "
url10 = " https://kite.zerodha.com/chart/ext/tvc/NSE/LTI/4561409?theme=dark"

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
