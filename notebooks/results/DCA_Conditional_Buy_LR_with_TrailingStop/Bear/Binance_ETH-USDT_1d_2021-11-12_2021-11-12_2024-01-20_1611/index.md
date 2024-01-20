# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Bear - ETH/USDT - Binance

- Experiment nickname: Bear 
- Symbol: ETH/USDT
- Exchange: Binance
- Start date: 2021-11-12
- End date: 2022-11-12
- Timeframe: 1d

## Optimized parameters

- band_lenght=11
- band_mult=2
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=50
- buy_all_days=0
- lr_buy_longitude=11

## Results

- Return: **-3.892227772909436%** over **-73.05195927619934%** on buy and hold.
- Initial investment: 1600.0
- Final result: 1537.724355633449

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2021-11-12 00:00:00
End                       2022-11-12 00:00:00
Duration                    365 days 00:00:00
Exposure Time [%]                   94.808743
Equity Final [$]                  1537.724356
Equity Peak [$]                   1663.607998
Return [%]                          -3.892228
Buy & Hold Return [%]              -73.051959
Return (Ann.) [%]                   -3.881802
Volatility (Ann.) [%]               11.556249
Sharpe Ratio                              0.0
Sortino Ratio                             0.0
Calmar Ratio                              0.0
Max. Drawdown [%]                   -9.836263
Avg. Drawdown [%]                   -4.949309
Max. Drawdown Duration      130 days 00:00:00
Avg. Drawdown Duration       69 days 00:00:00
# Trades                                   22
Win Rate [%]                        59.090909
Best Trade [%]                      68.065061
Worst Trade [%]                    -72.181591
Avg. Trade [%]                     -14.479048
Max. Trade Duration         346 days 00:00:00
Avg. Trade Duration          87 days 00:00:00
Profit Factor                        0.659665
Expectancy [%]                      -5.758152
SQN                                 -0.733259
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
```

### Top 10 configurations

|     |   band_lenght |   band_mult |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|----:|--------------:|------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 559 |            11 |           2 |                               1.003 |          2 |           50 |              0 |                 11 |     -3.89223 |
| 119 |             3 |           2 |                               1.003 |          2 |           50 |              0 |                 11 |     -3.97207 |
| 449 |            11 |           1 |                               1.003 |          2 |           50 |              0 |                 11 |     -4.16206 |
| 339 |             9 |           2 |                               1.003 |          2 |           50 |              0 |                 11 |     -4.28592 |
| 448 |            11 |           1 |                               1.003 |          2 |           50 |              0 |                 10 |     -4.51141 |
| 118 |             3 |           2 |                               1.003 |          2 |           50 |              0 |                 10 |     -4.52653 |
| 338 |             9 |           2 |                               1.003 |          2 |           50 |              0 |                 10 |     -4.58651 |
|   9 |             3 |           1 |                               1.003 |          2 |           50 |              0 |                 11 |     -4.62622 |
| 669 |            13 |           1 |                               1.003 |          2 |           50 |              0 |                 11 |     -4.6973  |
| 229 |             9 |           1 |                               1.003 |          2 |           50 |              0 |                 11 |     -4.7745  |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)