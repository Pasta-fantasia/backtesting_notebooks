# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Bear - BTC/USDT - Binance

- Experiment nickname: Bear 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2021-11-12
- End date: 2022-11-12
- Timeframe: 1d

## Optimized parameters

- band_lenght=3
- band_mult=1
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=50
- buy_all_days=0
- lr_buy_longitude=11

## Results

- Return: **-4.829400051103121%** over **-73.78119881357838%** on buy and hold.
- Initial investment: 1600.0
- Final result: 1522.72959918235

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2021-11-12 00:00:00
End                       2022-11-12 00:00:00
Duration                    365 days 00:00:00
Exposure Time [%]                    87.15847
Equity Final [$]                  1522.729599
Equity Peak [$]                   1630.509927
Return [%]                            -4.8294
Buy & Hold Return [%]              -73.781199
Return (Ann.) [%]                   -4.816528
Volatility (Ann.) [%]                5.960401
Sharpe Ratio                              0.0
Sortino Ratio                             0.0
Calmar Ratio                              0.0
Max. Drawdown [%]                   -7.294158
Avg. Drawdown [%]                   -2.312442
Max. Drawdown Duration      228 days 00:00:00
Avg. Drawdown Duration       63 days 00:00:00
# Trades                                   22
Win Rate [%]                        72.727273
Best Trade [%]                      12.618233
Worst Trade [%]                     -64.13213
Avg. Trade [%]                     -11.734403
Max. Trade Duration         318 days 00:00:00
Avg. Trade Duration          61 days 00:00:00
Profit Factor                        0.411466
Expectancy [%]                      -7.090042
SQN                                  -1.31943
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
```

### Top 10 configurations

|     |   band_lenght |   band_mult |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|----:|--------------:|------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
|   9 |             3 |           1 |                               1.003 |          2 |           50 |              0 |                 11 |     -4.8294  |
|   8 |             3 |           1 |                               1.003 |          2 |           50 |              0 |                 10 |     -5.18036 |
|   1 |             3 |           1 |                               1.003 |          2 |           50 |              0 |                  3 |     -5.53969 |
| 229 |             9 |           1 |                               1.003 |          2 |           50 |              0 |                 11 |     -6.80449 |
|  10 |             3 |           1 |                               1.003 |          2 |           50 |              0 |                 12 |     -6.88604 |
| 228 |             9 |           1 |                               1.003 |          2 |           50 |              0 |                 10 |     -6.97225 |
| 449 |            11 |           1 |                               1.003 |          2 |           50 |              0 |                 11 |     -7.0057  |
| 448 |            11 |           1 |                               1.003 |          2 |           50 |              0 |                 10 |     -7.18859 |
| 119 |             3 |           2 |                               1.003 |          2 |           50 |              0 |                 11 |     -7.25128 |
| 111 |             3 |           2 |                               1.003 |          2 |           50 |              0 |                  3 |     -7.3229  |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)