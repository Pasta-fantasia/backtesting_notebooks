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
- dca_budget=100
- buy_all_days=0
- lr_buy_longitude=3

## Results

- Return: **-11.08321657262475%** over **-73.78119881357838%** on buy and hold.
- Initial investment: 1600.0
- Final result: 1422.668534838004

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2021-11-12 00:00:00
End                       2022-11-12 00:00:00
Duration                    365 days 00:00:00
Exposure Time [%]                   92.896175
Equity Final [$]                  1422.668535
Equity Peak [$]                   1677.617515
Return [%]                         -11.083217
Buy & Hold Return [%]              -73.781199
Return (Ann.) [%]                  -11.054674
Volatility (Ann.) [%]               12.621369
Sharpe Ratio                              0.0
Sortino Ratio                             0.0
Calmar Ratio                              0.0
Max. Drawdown [%]                  -16.381375
Avg. Drawdown [%]                   -5.131056
Max. Drawdown Duration      228 days 00:00:00
Avg. Drawdown Duration       67 days 00:00:00
# Trades                                   24
Win Rate [%]                             75.0
Best Trade [%]                      13.070653
Worst Trade [%]                    -66.291202
Avg. Trade [%]                     -12.774741
Max. Trade Duration         339 days 00:00:00
Avg. Trade Duration          65 days 00:00:00
Profit Factor                        0.406578
Expectancy [%]                      -7.457887
SQN                                 -1.372414
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
```

### Top 10 configurations

|     |   band_lenght |   band_mult |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|----:|--------------:|------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
|   1 |             3 |           1 |                               1.003 |          2 |          100 |              0 |                  3 |     -11.0832 |
|  51 |             3 |           2 |                               1.003 |          2 |          100 |              0 |                  3 |     -14.6503 |
|   3 |             3 |           1 |                               1.003 |          2 |          100 |              0 |                  5 |     -17.6747 |
| 101 |             9 |           1 |                               1.003 |          2 |          100 |              0 |                  3 |     -18.5578 |
| 401 |            12 |           1 |                               1.003 |          2 |          100 |              0 |                  3 |     -18.8818 |
|   2 |             3 |           1 |                               1.003 |          2 |          100 |              0 |                  4 |     -18.9878 |
| 301 |            11 |           1 |                               1.003 |          2 |          100 |              0 |                  3 |     -19.0014 |
| 201 |            10 |           1 |                               1.003 |          2 |          100 |              0 |                  3 |     -19.0181 |
|   4 |             3 |           1 |                               1.003 |          2 |          100 |              0 |                  6 |     -19.8411 |
|  53 |             3 |           2 |                               1.003 |          2 |          100 |              0 |                  5 |     -21.0425 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)