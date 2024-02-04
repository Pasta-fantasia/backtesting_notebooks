# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Up - BTC/USDT - Binance

- Experiment nickname: Up 
- Experiment timestamp: 2024-02-04_1943 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2023-01-01
- End date: 2024-02-04
- Timeframe: 1w
- Duration: 4.152129650115967s

## Optimized parameters

- band_length=5
- band_mult=2
- band_low_pct=3.740957850481536
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=400
- buy_all_days=1
- lr_buy_longitude=5

## Results

- Return: **80.54682796827296%** over **151.5089157893907%** on buy and hold.
- Initial investment: 1000.0
- Final result: 1805.4682796827296

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2023-01-02 00:00:00
End                       2024-01-29 00:00:00
Duration                    392 days 00:00:00
Exposure Time [%]                   89.473684
Equity Final [$]                   1805.46828
Equity Peak [$]                    1907.03843
Return [%]                          80.546828
Buy & Hold Return [%]              151.508916
Return (Ann.) [%]                 1262.690687
Volatility (Ann.) [%]              1252.93035
Sharpe Ratio                          1.00779
Sortino Ratio                       39.421316
Calmar Ratio                        96.126648
Max. Drawdown [%]                  -13.135699
Avg. Drawdown [%]                   -6.386773
Max. Drawdown Duration      189 days 00:00:00
Avg. Drawdown Duration       58 days 00:00:00
# Trades                                    8
Win Rate [%]                             87.5
Best Trade [%]                      59.549397
Worst Trade [%]                       -4.4161
Avg. Trade [%]                      23.299067
Max. Trade Duration         266 days 00:00:00
Avg. Trade Duration          91 days 00:00:00
Profit Factor                       47.015161
Expectancy [%]                      25.400945
SQN                                  2.902161
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
```

### Top 10 configurations

|     |   band_length |   band_mult |   band_low_pct |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|----:|--------------:|------------:|---------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 476 |             5 |           2 |        3.74096 |                               1.003 |          2 |          400 |              1 |                  5 |      80.5468 |
| 454 |             5 |           2 |        3.74096 |                               1.003 |          2 |          200 |              1 |                  5 |      75.9569 |
| 188 |             3 |           2 |        3.74096 |                               1.003 |          2 |          200 |              1 |                  3 |      75.5844 |
| 189 |             3 |           2 |        3.74096 |                               1.003 |          2 |          200 |              1 |                  4 |      74.2965 |
| 190 |             3 |           2 |        3.74096 |                               1.003 |          2 |          200 |              1 |                  5 |      72.9534 |
| 498 |             5 |           2 |        3.74096 |                               1.003 |          2 |          500 |              1 |                  5 |      71.1793 |
| 344 |             5 |           1 |        3.74096 |                               1.003 |          2 |          400 |              1 |                  5 |      71.005  |
| 346 |             5 |           1 |        3.74096 |                               1.003 |          2 |          400 |              1 |                  7 |      70.9243 |
| 256 |             3 |           2 |        3.74096 |                               1.003 |          2 |         1000 |              1 |                  5 |      70.3001 |
| 322 |             5 |           1 |        3.74096 |                               1.003 |          2 |          200 |              1 |                  5 |      70.0216 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)

