# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Bear - BTC/USDT - Binance

- Experiment nickname: Bear 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2021-11-12
- End date: 2022-11-12
- Timeframe: 1h

## Optimized parameters

- band_lenght=21
- band_mult=1
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=1000
- buy_all_days=1
- lr_buy_longitude=5

## Results

- Return: **-43.76917585800206%** over **-74.05869077557232%** on buy and hold.
- Initial investment: 1600.0
- Final result: 899.6931862719671

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2021-11-12 00:00:00
End                       2022-11-12 23:00:00
Duration                    365 days 23:00:00
Exposure Time [%]                   99.487705
Equity Final [$]                   899.693186
Equity Peak [$]                   1628.437557
Return [%]                         -43.769176
Buy & Hold Return [%]              -74.058691
Return (Ann.) [%]                   -43.67393
Volatility (Ann.) [%]               17.360267
Sharpe Ratio                              0.0
Sortino Ratio                             0.0
Calmar Ratio                              0.0
Max. Drawdown [%]                  -45.840277
Avg. Drawdown [%]                   -8.197434
Max. Drawdown Duration      362 days 14:00:00
Avg. Drawdown Duration       60 days 20:00:00
# Trades                                    2
Win Rate [%]                             50.0
Best Trade [%]                       1.547363
Worst Trade [%]                    -72.216128
Avg. Trade [%]                     -46.883346
Max. Trade Duration         361 days 09:00:00
Avg. Trade Duration         182 days 01:00:00
Profit Factor                        0.021427
Expectancy [%]                     -35.334383
SQN                                 -0.958046
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
```

### Top 10 configurations

|     |   band_lenght |   band_mult |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|----:|--------------:|------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 638 |            21 |           1 |                               1.003 |          2 |         1000 |              1 |                  5 |     -43.7692 |
| 639 |            21 |           1 |                               1.003 |          2 |         1000 |              1 |                  6 |     -43.8725 |
| 285 |            10 |           2 |                               1.003 |          2 |         1000 |              1 |                  2 |     -43.9533 |
| 385 |            11 |           2 |                               1.003 |          2 |         1000 |              1 |                  2 |     -43.9634 |
| 587 |            13 |           2 |                               1.003 |          2 |         1000 |              1 |                  4 |     -44.0497 |
| 485 |            12 |           2 |                               1.003 |          2 |         1000 |              1 |                  2 |     -44.0716 |
| 585 |            13 |           2 |                               1.003 |          2 |         1000 |              1 |                  2 |     -44.1398 |
| 586 |            13 |           2 |                               1.003 |          2 |         1000 |              1 |                  3 |     -44.1398 |
| 788 |            34 |           2 |                               1.003 |          2 |         1000 |              1 |                  5 |     -44.1807 |
| 435 |            12 |           1 |                               1.003 |          2 |         1000 |              1 |                  2 |     -44.2045 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)