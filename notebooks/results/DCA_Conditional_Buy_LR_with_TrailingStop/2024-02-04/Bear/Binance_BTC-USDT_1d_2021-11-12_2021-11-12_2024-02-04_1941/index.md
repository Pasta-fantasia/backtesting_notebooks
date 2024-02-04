# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Bear - BTC/USDT - Binance

- Experiment nickname: Bear 
- Experiment timestamp: 2024-02-04_1941 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2021-11-12
- End date: 2022-11-12
- Timeframe: 1d
- Duration: 6.545968770980835s

## Optimized parameters

- band_length=3
- band_mult=1
- band_low_pct=2.8111930348691905
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=50
- buy_all_days=0
- lr_buy_longitude=11

## Results

- Return: **-9.49249976588443%** over **-73.78119881357838%** on buy and hold.
- Initial investment: 1000.0
- Final result: 905.0750023411557

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2021-11-12 00:00:00
End                       2022-11-12 00:00:00
Duration                    365 days 00:00:00
Exposure Time [%]                    87.15847
Equity Final [$]                   905.075002
Equity Peak [$]                   1024.931401
Return [%]                            -9.4925
Buy & Hold Return [%]              -73.781199
Return (Ann.) [%]                   -9.467833
Volatility (Ann.) [%]                9.095637
Sharpe Ratio                              0.0
Sortino Ratio                             0.0
Calmar Ratio                              0.0
Max. Drawdown [%]                  -13.054445
Avg. Drawdown [%]                   -3.767063
Max. Drawdown Duration      228 days 00:00:00
Avg. Drawdown Duration       63 days 00:00:00
# Trades                                   22
Win Rate [%]                        68.181818
Best Trade [%]                      11.499928
Worst Trade [%]                     -64.13213
Avg. Trade [%]                     -13.151987
Max. Trade Duration         318 days 00:00:00
Avg. Trade Duration          59 days 00:00:00
Profit Factor                        0.318507
Expectancy [%]                      -8.710241
SQN                                 -1.660402
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
```

### Top 10 configurations

|     |   band_length |   band_mult |   band_low_pct |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|----:|--------------:|------------:|---------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
|   9 |             3 |           1 |        2.81119 |                               1.003 |          2 |           50 |              0 |                 11 |      -9.4925 |
|   8 |             3 |           1 |        2.81119 |                               1.003 |          2 |           50 |              0 |                 10 |     -10.054  |
| 141 |             3 |           2 |        2.81119 |                               1.003 |          2 |           50 |              0 |                 11 |     -10.4277 |
| 273 |             5 |           1 |        2.81119 |                               1.003 |          2 |           50 |              0 |                 11 |     -10.6003 |
|   1 |             3 |           1 |        2.81119 |                               1.003 |          2 |           50 |              0 |                  3 |     -10.7228 |
| 140 |             3 |           2 |        2.81119 |                               1.003 |          2 |           50 |              0 |                 10 |     -11.0005 |
| 272 |             5 |           1 |        2.81119 |                               1.003 |          2 |           50 |              0 |                 10 |     -11.0342 |
| 537 |             9 |           1 |        2.81119 |                               1.003 |          2 |           50 |              0 |                 11 |     -12.5013 |
|  10 |             3 |           1 |        2.81119 |                               1.003 |          2 |           50 |              0 |                 12 |     -12.7831 |
| 133 |             3 |           2 |        2.81119 |                               1.003 |          2 |           50 |              0 |                  3 |     -13.5443 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)

