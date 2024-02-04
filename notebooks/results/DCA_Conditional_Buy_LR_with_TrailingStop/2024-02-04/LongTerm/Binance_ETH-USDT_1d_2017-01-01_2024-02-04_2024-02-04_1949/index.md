# Class: DCA_Conditional_Buy_LR_with_TrailingStop - LongTerm - ETH/USDT - Binance

- Experiment nickname: LongTerm 
- Experiment timestamp: 2024-02-04_1949 
- Symbol: ETH/USDT
- Exchange: Binance
- Start date: 2017-01-01
- End date: 2024-02-04
- Timeframe: 1d
- Duration: 46.68588852882385s

## Optimized parameters

- band_length=34
- band_mult=2
- band_low_pct=3.5976248
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=200
- buy_all_days=0
- lr_buy_longitude=12

## Results

- Return: **923.4731636863121%** over **665.6589508056641%** on buy and hold.
- Initial investment: 1000.0
- Final result: 10234.73163686312

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2017-08-17 00:00:00
End                       2024-02-03 00:00:00
Duration                   2361 days 00:00:00
Exposure Time [%]                   97.502117
Equity Final [$]                 10234.731637
Equity Peak [$]                  11064.728244
Return [%]                         923.473164
Buy & Hold Return [%]              665.658951
Return (Ann.) [%]                   43.247541
Volatility (Ann.) [%]               81.409829
Sharpe Ratio                         0.531232
Sortino Ratio                        1.236622
Calmar Ratio                         0.554252
Max. Drawdown [%]                  -78.028676
Avg. Drawdown [%]                  -11.035812
Max. Drawdown Duration      998 days 00:00:00
Avg. Drawdown Duration       88 days 00:00:00
# Trades                                  138
Win Rate [%]                        88.405797
Best Trade [%]                     193.557619
Worst Trade [%]                    -51.255233
Avg. Trade [%]                      25.084796
Max. Trade Duration        1098 days 00:00:00
Avg. Trade Duration         241 days 00:00:00
Profit Factor                        9.989083
Expectancy [%]                      33.748114
SQN                                  7.562442
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                         Size  Entr...
dtype: object
```

### Top 10 configurations

|      |   band_length |   band_mult |   band_low_pct |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|-----:|--------------:|------------:|---------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 1770 |            34 |           2 |        3.59762 |                               1.003 |          2 |          200 |              0 |                 12 |      923.473 |
| 1463 |            21 |           2 |        3.59762 |                               1.003 |          2 |           50 |              1 |                  2 |      915.873 |
| 1506 |            21 |           2 |        3.59762 |                               1.003 |          2 |          200 |              0 |                 12 |      913.368 |
| 1515 |            21 |           2 |        3.59762 |                               1.003 |          2 |          200 |              1 |                 10 |      875.375 |
| 1465 |            21 |           2 |        3.59762 |                               1.003 |          2 |           50 |              1 |                  4 |      875.113 |
| 1549 |            21 |           2 |        3.59762 |                               1.003 |          2 |          500 |              0 |                 11 |      862.357 |
| 1473 |            21 |           2 |        3.59762 |                               1.003 |          2 |           50 |              1 |                 12 |      853.218 |
| 1550 |            21 |           2 |        3.59762 |                               1.003 |          2 |          500 |              0 |                 12 |      851.35  |
| 1548 |            21 |           2 |        3.59762 |                               1.003 |          2 |          500 |              0 |                 10 |      849.141 |
| 1495 |            21 |           2 |        3.59762 |                               1.003 |          2 |          100 |              1 |                 12 |      842.87  |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)

