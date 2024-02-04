# Class: DCA_Conditional_Buy_LR_with_TrailingStop - LongTerm - BTC/USDT - Binance

- Experiment nickname: LongTerm 
- Experiment timestamp: 2024-02-04_1940 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2017-01-01
- End date: 2024-02-04
- Timeframe: 1d
- Duration: 34.96102833747864s

## Optimized parameters

- band_length=34
- band_mult=2
- band_low_pct=2.815263919591264
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=100
- buy_all_days=1
- lr_buy_longitude=7

## Results

- Return: **1487.0788390592738%** over **904.5432166669%** on buy and hold.
- Initial investment: 1000.0
- Final result: 15870.788390592737

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2017-08-17 00:00:00
End                       2024-02-03 00:00:00
Duration                   2361 days 00:00:00
Exposure Time [%]                   97.925487
Equity Final [$]                 15870.788391
Equity Peak [$]                  17050.990086
Return [%]                        1487.078839
Buy & Hold Return [%]              904.543217
Return (Ann.) [%]                     53.2952
Volatility (Ann.) [%]              100.723475
Sharpe Ratio                         0.529124
Sortino Ratio                         1.31845
Calmar Ratio                         0.694025
Max. Drawdown [%]                  -76.791423
Avg. Drawdown [%]                   -9.371515
Max. Drawdown Duration     1055 days 00:00:00
Avg. Drawdown Duration       59 days 00:00:00
# Trades                                  398
Win Rate [%]                        85.175879
Best Trade [%]                      445.33703
Worst Trade [%]                    -36.088398
Avg. Trade [%]                      23.491004
Max. Trade Duration        1176 days 00:00:00
Avg. Trade Duration         301 days 00:00:00
Profit Factor                       17.026069
Expectancy [%]                      37.708789
SQN                                  8.037344
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                         Size  Entr...
dtype: object
```

### Top 10 configurations

|      |   band_length |   band_mult |   band_low_pct |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|-----:|--------------:|------------:|---------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 1754 |            34 |           2 |        2.81526 |                               1.003 |          2 |          100 |              1 |                  7 |      1487.08 |
| 1753 |            34 |           2 |        2.81526 |                               1.003 |          2 |          100 |              1 |                  6 |      1456.31 |
| 1756 |            34 |           2 |        2.81526 |                               1.003 |          2 |          100 |              1 |                  9 |      1429.81 |
| 1727 |            34 |           2 |        2.81526 |                               1.003 |          2 |           50 |              1 |                  2 |      1426.08 |
| 1752 |            34 |           2 |        2.81526 |                               1.003 |          2 |          100 |              1 |                  5 |      1425.63 |
| 1731 |            34 |           2 |        2.81526 |                               1.003 |          2 |           50 |              1 |                  6 |      1412.1  |
| 1755 |            34 |           2 |        2.81526 |                               1.003 |          2 |          100 |              1 |                  8 |      1409.46 |
| 1732 |            34 |           2 |        2.81526 |                               1.003 |          2 |           50 |              1 |                  7 |      1404.29 |
| 1750 |            34 |           2 |        2.81526 |                               1.003 |          2 |          100 |              1 |                  3 |      1400.09 |
| 1730 |            34 |           2 |        2.81526 |                               1.003 |          2 |           50 |              1 |                  5 |      1386.12 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)

