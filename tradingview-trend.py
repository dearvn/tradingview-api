import logging
import sys
import os
import time

#from flask import Flask, jsonify, request
from tradingview import get_multiple_analysis
import sys

if __name__ == "__main__":
    screener = 'america'
    symbol = sys.argv[1]
    interval = sys.argv[2]

    symbols = [symbol]
    analyse = get_multiple_analysis(
        screener, interval, symbols
    )

    while True:
        result = {}
        for symbol in symbols:
            symbolAnalyse = analyse[symbol]
            if not (symbolAnalyse is None):
                result[symbol] = {
                    'summary': symbolAnalyse.summary, 'time': symbolAnalyse.time.isoformat(),
                    'oscillators': symbolAnalyse.oscillators, 'moving_averages': symbolAnalyse.moving_averages,
                    'indicators': symbolAnalyse.indicators}
            else:
                result[symbol] = {}

        r = result[symbol]
        print(r['moving_averages']['RECOMMENDATION'], r['summary']['RECOMMENDATION'], r['oscillators']['RECOMMENDATION'])

        time.sleep(5)
