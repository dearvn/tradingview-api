# tradingview-api

Monitoring trend BUY, SELL or NEUTRAL

**CMD**
```python -m tradingview-trend CME_MINI:NQ1! 1m```

![Alt text](https://github.com/dearvn/tradingview-api/raw/main/summary.png?raw=true "Summary")


**Run**
```
python -m tradingview-api
```

**Call url from postman**
```http://0.0.0.0:8080?symbols=NASDAQ:TSLA&screener=america&interval=5m```

**Result**

```
{
    "request": {
        "interval": "5m",
        "screener": "america",
        "symbols": [
            "NASDAQ:TSLA"
        ]
    },
    "result": {
        "NASDAQ:TSLA": {
            "indicators": {
                "ADX": 22.31301913,
                "ADX+DI": 15.08406627,
                "ADX+DI[1]": 15.60000389,
                "ADX-DI": 25.17832606,
                "ADX-DI[1]": 26.03952922,
                "AO": 0.26278265,
                "AO[1]": 0.19807676,
                "AO[2]": 0.12945353,
                "BB.lower": 306.06645037,
                "BB.upper": 309.77798963,
                "BBPower": -1.13945662,
                "CCI20": -107.83940321,
                "CCI20[1]": -102.58664606,
                "EMA10": 307.32425543,
                "EMA100": 305.97228733,
                "EMA20": 307.44295623,
                "EMA200": 304.40554456,
                "EMA30": 307.36467617,
                "EMA5": 307.09075568,
                "EMA50": 307.03960634,
                "HullMA9": 307.3485237,
                "Ichimoku.BLine": 307.46955,
                "MACD.macd": -0.02686322,
                "MACD.signal": 0.16025286,
                "Mom": -2.5766,
                "Mom[1]": -2.2924,
                "P.SAR": 308.62,
                "Pivot.M.Camarilla.Middle": 305.61333333,
                "Pivot.M.Camarilla.R1": 310.30366667,
                "Pivot.M.Camarilla.R2": 311.40733333,
                "Pivot.M.Camarilla.R3": 312.511,
                "Pivot.M.Camarilla.S1": 308.09633333,
                "Pivot.M.Camarilla.S2": 306.99266667,
                "Pivot.M.Camarilla.S3": 305.889,
                "Pivot.M.Classic.Middle": 305.61333333,
                "Pivot.M.Classic.R1": 313.42666667,
                "Pivot.M.Classic.R2": 317.65333333,
                "Pivot.M.Classic.R3": 329.69333333,
                "Pivot.M.Classic.S1": 301.38666667,
                "Pivot.M.Classic.S2": 293.57333333,
                "Pivot.M.Classic.S3": 281.53333333,
                "Pivot.M.Demark.Middle": 306.67,
                "Pivot.M.Demark.R1": 315.54,
                "Pivot.M.Demark.S1": 303.5,
                "Pivot.M.Fibonacci.Middle": 305.61333333,
                "Pivot.M.Fibonacci.R1": 310.21261333,
                "Pivot.M.Fibonacci.R2": 313.05405333,
                "Pivot.M.Fibonacci.R3": 317.65333333,
                "Pivot.M.Fibonacci.S1": 301.01405333,
                "Pivot.M.Fibonacci.S2": 298.17261333,
                "Pivot.M.Fibonacci.S3": 293.57333333,
                "Pivot.M.Woodie.Middle": 305.365,
                "Pivot.M.Woodie.R1": 312.93,
                "Pivot.M.Woodie.R2": 317.405,
                "Pivot.M.Woodie.R3": 324.97,
                "Pivot.M.Woodie.S1": 300.89,
                "Pivot.M.Woodie.S2": 293.325,
                "Pivot.M.Woodie.S3": 288.85,
                "RSI": 44.18184909,
                "RSI[1]": 44.64454229,
                "Rec.BBPower": 0,
                "Rec.HullMA9": -1,
                "Rec.Ichimoku": 0,
                "Rec.Stoch.RSI": 0,
                "Rec.UO": 0,
                "Rec.VWMA": -1,
                "Rec.WR": 0,
                "Recommend.All": -0.29090909,
                "Recommend.MA": -0.4,
                "Recommend.Other": -0.18181818,
                "SMA10": 307.23268,
                "SMA100": 306.189289,
                "SMA20": 307.92222,
                "SMA200": 303.630597,
                "SMA30": 307.46698,
                "SMA5": 307.3952,
                "SMA50": 307.007484,
                "Stoch.D": 50.66932456,
                "Stoch.D[1]": 54.88549596,
                "Stoch.K": 38.68645974,
                "Stoch.K[1]": 52.32815573,
                "Stoch.RSI.D": 40.02108194,
                "Stoch.RSI.K": 27.37594829,
                "UO": 48.3121806,
                "VWMA": 307.97323852,
                "W.R": -72.39025165,
                "change": -0.02419321,
                "close": 306.6234,
                "high": 307.11,
                "low": 306.55,
                "open": 306.6956,
                "volume": 74715
            },
            "moving_averages": {
                "BUY": 4,
                "COMPUTE": {
                    "EMA10": "SELL",
                    "EMA100": "BUY",
                    "EMA20": "SELL",
                    "EMA200": "BUY",
                    "EMA30": "SELL",
                    "EMA50": "SELL",
                    "HullMA": "SELL",
                    "Ichimoku": "NEUTRAL",
                    "SMA10": "SELL",
                    "SMA100": "BUY",
                    "SMA20": "SELL",
                    "SMA200": "BUY",
                    "SMA30": "SELL",
                    "SMA50": "SELL",
                    "VWMA": "SELL"
                },
                "NEUTRAL": 1,
                "RECOMMENDATION": "SELL",
                "SELL": 10
            },
            "oscillators": {
                "BUY": 0,
                "COMPUTE": {
                    "ADX": "NEUTRAL",
                    "AO": "NEUTRAL",
                    "BBP": "NEUTRAL",
                    "CCI": "NEUTRAL",
                    "MACD": "SELL",
                    "Mom": "SELL",
                    "RSI": "NEUTRAL",
                    "STOCH.K": "NEUTRAL",
                    "Stoch.RSI": "NEUTRAL",
                    "UO": "NEUTRAL",
                    "W%R": "NEUTRAL"
                },
                "NEUTRAL": 9,
                "RECOMMENDATION": "SELL",
                "SELL": 2
            },
            "summary": {
                "BUY": 4,
                "NEUTRAL": 10,
                "RECOMMENDATION": "SELL",
                "SELL": 12
            },
            "time": "2022-09-20T21:31:18.086086"
        }
    }
}
```
