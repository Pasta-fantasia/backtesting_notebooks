# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Bear - ETH/USDT - Binance

- Experiment nickname: Bear 
- Experiment timestamp: 2024-02-04_1951 
- Symbol: ETH/USDT
- Exchange: Binance
- Start date: 2021-11-12
- End date: 2022-11-12
- Timeframe: 1d
- Duration: 7.323721647262573s

## Optimized parameters

- band_length=5
- band_mult=1
- band_low_pct=3.6983202
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=50
- buy_all_days=0
- lr_buy_longitude=11

## Results

- Return: **-4.599458516273751%** over **-73.05195927619934%** on buy and hold.
- Initial investment: 1000.0
- Final result: 954.0054148372625

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2021-11-12 00:00:00
End                       2022-11-12 00:00:00
Duration                    365 days 00:00:00
Exposure Time [%]                   94.808743
Equity Final [$]                   954.005415
Equity Peak [$]                   1009.213855
Return [%]                          -4.599459
Buy & Hold Return [%]              -73.051959
Return (Ann.) [%]                   -4.587184
Volatility (Ann.) [%]               13.110221
Sharpe Ratio                              0.0
Sortino Ratio                             0.0
Calmar Ratio                              0.0
Max. Drawdown [%]                  -13.363689
Avg. Drawdown [%]                   -9.831925
Max. Drawdown Duration      228 days 00:00:00
Avg. Drawdown Duration      173 days 00:00:00
# Trades                                   22
Win Rate [%]                        68.181818
Best Trade [%]                      50.959144
Worst Trade [%]                    -72.181591
Avg. Trade [%]                     -12.580272
Max. Trade Duration         346 days 00:00:00
Avg. Trade Duration          71 days 00:00:00
Profit Factor                        0.716327
Expectancy [%]                      -4.261359
SQN                                 -0.582023
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
```

### Top 10 configurations

|     |   band_length |   band_mult |   band_low_pct |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|----:|--------------:|------------:|---------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 273 |             5 |           1 |        3.69832 |                               1.003 |          2 |           50 |              0 |                 11 |     -4.59946 |
| 405 |             5 |           2 |        3.69832 |                               1.003 |          2 |           50 |              0 |                 11 |     -6.19401 |
| 933 |            11 |           2 |        3.69832 |                               1.003 |          2 |           50 |              0 |                 11 |     -6.22756 |
| 537 |             9 |           1 |        3.69832 |                               1.003 |          2 |           50 |              0 |                 11 |     -6.26612 |
| 141 |             3 |           2 |        3.69832 |                               1.003 |          2 |           50 |              0 |                 11 |     -6.51805 |
| 801 |            11 |           1 |        3.69832 |                               1.003 |          2 |           50 |              0 |                 11 |     -6.54782 |
| 272 |             5 |           1 |        3.69832 |                               1.003 |          2 |           50 |              0 |                 10 |     -6.80304 |
| 669 |             9 |           2 |        3.69832 |                               1.003 |          2 |           50 |              0 |                 11 |     -6.85748 |
| 800 |            11 |           1 |        3.69832 |                               1.003 |          2 |           50 |              0 |                 10 |     -7.10678 |
|   9 |             3 |           1 |        3.69832 |                               1.003 |          2 |           50 |              0 |                 11 |     -7.26143 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)

