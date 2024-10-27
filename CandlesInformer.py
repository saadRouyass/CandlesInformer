import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json
import datetime
import requests
import pywhatkit as kit


phone_number = "+212708271915"

redTrigger='\U0001F534'
orangeTrigger='\U0001F7E0'
yellowTrigger='\U0001F7E1'

#Bitstamp API
market_symbol='btcusd'
url=f'https://www.bitstamp.net/api/v2/ohlc/{market_symbol}/'
#############

#API parameters
params={
    'step':300,
    'limit':50,
    'end':1716483590,
    'exclude_current_candle':False
           }
#############
#Creating DataFrame
preData=requests.get(url,params=params)
dt=preData.json()['data']['ohlc']
Data=pd.DataFrame(dt)
#############

def is_bullish(x):
    return x['open']<x['close']

def is_bearish(x):
    return x['open']>x['close']

def upperTail(x):
    if is_bearish(x):
       return float( x['high'])-float(x['open'])
    if is_bullish(x):
        return float( x['high'])-float(x['close'])

def lowerTail(x):
    if is_bearish(x):
        return float(x['close'])-float( x['low'])
    if is_bullish(x):
        return float(x['open'])-float( x['low'])
    
def candleBody(x):
    return abs(float(x['open'])-float( x['close']))

################################################ Candles Patterns ############################################




############################################### Unicandle patterns ############################################
def Doji(x):
    name='DOJI PATTERN'
    time=datetime.datetime.fromtimestamp(int(x['timestamp']))
    a=True
    if x['high']==x['open'] or x['high']==x['close']:
        a=False
    
    if x['low']==x['open'] or x['low']==x['close']:
        a=False
    
    if upperTail(x)>3*lowerTail(x) or lowerTail(x)>3*upperTail(x):
        a=False
    
    if abs(float(x['open'])-float(x['close']))<=8 and a==True:
    
        msg=f'{redTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
        kit.sendwhatmsg_instantly(phone_number, msg)

    
    if abs(float(x['open'])-float(x['close']))>8 and abs(float(x['open'])-float(x['close']))<=12 and a==True:
        
        msg=f'{orangeTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
        kit.sendwhatmsg_instantly(phone_number, msg)
    
    if abs(float(x['open'])-float(x['close']))>12 and abs(float(x['open'])-float(x['close']))<=20 and a==True:
        msg=f'{yellowTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
        kit.sendwhatmsg_instantly(phone_number, msg)
        


def DragonFly(x):
    name='DRAGON FLY DOJI PATTERN'
    time=datetime.datetime.fromtimestamp(int(x['timestamp']))
    a=True
    if x['open']!=x['close'] and abs(float(x['open'])-float(x['close']))>5:
        a=False
    if upperTail(x)>1 or lowerTail(x)<3:
        a=False
    if a==True:
        if abs(float(x['open'])-float(x['close']))<=1:
            msg=f'{redTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
            kit.sendwhatmsg_instantly(phone_number, msg)
        else:
            msg=f'{orangeTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
            kit.sendwhatmsg_instantly(phone_number, msg)


def Gravestone(x):
    name='GRAVESTONE PATTERN'
    time=datetime.datetime.fromtimestamp(int(x['timestamp']))
    a=True
    if x['open']!=x['close'] and abs(float(x['open'])-float(x['close']))>5:
        a=False
    if lowerTail(x)>1 or upperTail(x)<3:
        a=False
    if a==True:
        if abs(float(x['open'])-float(x['close']))<=1:
            msg=f'{redTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
            kit.sendwhatmsg_instantly(phone_number, msg)
        else:
            msg=f'{orangeTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
            kit.sendwhatmsg_instantly(phone_number, msg)

def TheHammer(x):
    name='THE HAMMER PATTERN'
    time=datetime.datetime.fromtimestamp(int(x['timestamp']))
    a=True
    if x['open']!=x['close'] and abs(float(x['open'])-float(x['close']))>5:
        a=False
    if upperTail(x)>3 or lowerTail(x)<5:
        a=False
    if a==True:
        if lowerTail(x)>=3*upperTail(x):
            msg=f'{redTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
            kit.sendwhatmsg_instantly(phone_number, msg)
        else:
            msg=f'{orangeTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
            kit.sendwhatmsg_instantly(phone_number, msg)
            
def TheShootingStar(x):
    name='THE SHOOTING STAR PATTERN'
    time=datetime.datetime.fromtimestamp(int(x['timestamp']))
    a=True
    if x['open']!=x['close'] and abs(float(x['open'])-float(x['close']))>5:
        a=False
    if lowerTail(x)>3 or upperTail(x)<5:
        a=False
    if upperTail(x)<2*abs(float(x['open'])-float(x['close'])):
        a=False
    if a==True:
        if upperTail(x)>=3*lowerTail(x):
            msg=f'{redTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
            kit.sendwhatmsg_instantly(phone_number, msg)
        else:
            msg=f'{orangeTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
            kit.sendwhatmsg_instantly(phone_number, msg)

def TheBullishMarubozu(x):
    name='THE BULLISH MARUBOZU PATTERN'
    time=datetime.datetime.fromtimestamp(int(x['timestamp']))
    a=True
    if upperTail(x)>1 or lowerTail(x)>1:
        a=False
    if is_bearish(x):
        a=False
    if a==True:
        if candleBody(x)>=70:
            msg=f'{redTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
            kit.sendwhatmsg_instantly(phone_number, msg)
        else:
            msg=f'{orangeTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
            kit.sendwhatmsg_instantly(phone_number, msg)
            
def TheBearishMarubozu(x):
    name='THE BEARISH MARUBOZU PATTERN'
    time=datetime.datetime.fromtimestamp(int(x['timestamp']))
    a=True
    if upperTail(x)>1 or lowerTail(x)>1:
        a=False
    if is_bullish(x):
        a=False
    if a==True:
        if candleBody(x)>=70:
            msg=f'{redTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
            kit.sendwhatmsg_instantly(phone_number, msg)
        else:
            msg=f'{orangeTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
            kit.sendwhatmsg_instantly(phone_number, msg)
            
    



############################################# Bicandle Patterns ############################################

def BearishEngulfing(x,y):
    name='THE BEARISH ENGULFING PATTERN'
    time=datetime.datetime.fromtimestamp(int(x['timestamp']))
    a=True
    if is_bearish(x):
        a=False
    if is_bullish(y):
        a=False
    if x['open']<y['close'] or x['close']>y['open']:
        a=False
    if a==True:
        if x['high']<y['high'] and x['low']>y['low']:
            msg=f'{redTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
            kit.sendwhatmsg_instantly(phone_number, msg)
        else:
            msg=f'{orangeTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
            kit.sendwhatmsg_instantly(phone_number, msg)

def BullishEngulfing(x,y):
    name='THE BULLISH ENGULFING PATTERN'
    time=datetime.datetime.fromtimestamp(int(x['timestamp']))
    a=True
    if is_bullish(x):
        a=False
    if is_bearish(y):
        a=False
    if x['open']>y['close'] or x['close']<y['open']:
        a=False
    if a==True:
        if x['high']<y['high'] and x['low']>y['low']:
            msg=f'{redTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
            kit.sendwhatmsg_instantly(phone_number, msg)
        else:
            msg=f'{orangeTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
            kit.sendwhatmsg_instantly(phone_number, msg)       
    
def PiercingLine(x,y):
    name='THE PIERCING LINE PATTERN'
    time=datetime.datetime.fromtimestamp(int(x['timestamp']))
    a=True
    if is_bullish(x):
        a=False
    if is_bearish(y):
        a=False
    if y['open']>x['low']:
        a=False
    if y['close']<((float(x['open'])+float(x['close']))/2) or y['close']>x['open']:
        a=False
    if a==True:
        msg=f'{redTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
        kit.sendwhatmsg_instantly(phone_number, msg)
        
def theDarkCloudCover(x,y):
    name='THE DARK CLOUD PATTERN'
    time=datetime.datetime.fromtimestamp(int(x['timestamp']))
    a=True
    if is_bearish(x):
        a=False
    if y['open']<=x['high']:
        a=False
    if y['close']>((float(x['open'])+float(x['close']))/2):
        a=False
    if a==True:
        msg=f'{redTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
        kit.sendwhatmsg_instantly(phone_number, msg)
        
#def RisingWindow(x,y):
#    pass

#def FallingWindow(x,y):
#   pass

def BullishHarami(x,y):
    name='THE BULLISH HARAMI'
    time=datetime.datetime.fromtimestamp(int(x['timestamp']))
    a=True
    if is_bullish(x):
        a=False
    if a==True:
        if y['high']<x['open'] and y['low']>x['close']:
            msg=f'{redTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
            kit.sendwhatmsg_instantly(phone_number, msg)
            
    

def BearishHarami(x,y):
    name='THE BEARISH HARAMI'
    time=datetime.datetime.fromtimestamp(int(x['timestamp']))
    a=True
    if is_bearish(x):
        a=False
    if a==True:
        if y['high']<x['close'] and y['low']>x['open']:
            msg=f'{redTrigger}{name}\n\n\n   Timeframe: 5min\n   Time:{time}\n   Market: {market_symbol}'
            kit.sendwhatmsg_instantly(phone_number, msg)
            
    

        







########################################### TriCandles Pattern #############################################

def TheMorningStar(x,y,z):
    pass

def ThreeWhiteSoldiers(x,y,z):
    pass

def ThreeInsideUp(x,y,z):
    pass

def BullishAbandonedBaby(x,y,z):
    pass

def ThreeBlackCrows(x,y,z):
    pass

def ThreeInsideDown(x,y,z):
    pass

def BearishAbandonedBaby(x,y,z):
   pass

def EveningStar(x,y,z):
   pass
    

########################################### Testing ALL Candles #############################################
 
def testingUniPatterns(x):
    Doji(x)
    DragonFly(x)
    Gravestone(x)
    TheHammer(x)
    TheShootingStar(x)
    TheBullishMarubozu(x)
    TheBearishMarubozu(x)

def testingBiPatterns(x,y):
          
    BearishEngulfing(x,y)
    BullishEngulfing(x,y)       
    PiercingLine(x,y)
    theDarkCloudCover(x,y)
    BullishHarami(x,y)
    BearishHarami(x,y)
    
    

    

    
    
        
    
        
        
        
           