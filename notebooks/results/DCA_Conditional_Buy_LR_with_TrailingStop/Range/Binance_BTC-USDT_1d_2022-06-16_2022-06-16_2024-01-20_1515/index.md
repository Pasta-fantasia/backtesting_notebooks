# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Range - BTC/USDT - Binance

- Experiment nickname: Range 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2022-06-16
- End date: 2023-03-10
- Timeframe: 1d

## Optimized parameters

- band_lenght=9
- band_mult=1
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=1600
- buy_all_days=0
- lr_buy_longitude=7

## Results

- Return: **43.3217598368181%** over **-1.2284505259711431%** on buy and hold.
- Initial investment: 1600.0
- Final result: 2293.1481573890896

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2022-06-16 00:00:00
End                       2023-03-10 00:00:00
Duration                    267 days 00:00:00
Exposure Time [%]                   66.044776
Equity Final [$]                  2293.148157
Equity Peak [$]                   2600.009552
Return [%]                           43.32176
Buy & Hold Return [%]               -1.228451
Return (Ann.) [%]                   63.263007
Volatility (Ann.) [%]               50.640967
Sharpe Ratio                         1.249246
Sortino Ratio                        3.826211
Calmar Ratio                         5.360219
Max. Drawdown [%]                  -11.802318
Avg. Drawdown [%]                   -3.934448
Max. Drawdown Duration      108 days 00:00:00
Avg. Drawdown Duration       16 days 00:00:00
# Trades                                    6
Win Rate [%]                        83.333333
Best Trade [%]                      39.962953
Worst Trade [%]                    -12.035659
Avg. Trade [%]                       6.205316
Max. Trade Duration          54 days 00:00:00
Avg. Trade Duration          29 days 00:00:00
Profit Factor                        4.632084
Expectancy [%]                       7.285755
SQN                                  1.023363
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
```

### Top 10 configurations

|     |   band_lenght |   band_mult |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|----:|--------------:|------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 313 |             9 |           1 |                               1.003 |          2 |         1600 |              0 |                  7 |      43.3218 |
| 533 |            11 |           1 |                               1.003 |          2 |         1600 |              0 |                  7 |      40.4555 |
| 312 |             9 |           1 |                               1.003 |          2 |         1600 |              0 |                  6 |      37.9379 |
|  93 |             3 |           1 |                               1.003 |          2 |         1600 |              0 |                  7 |      36.8684 |
| 532 |            11 |           1 |                               1.003 |          2 |         1600 |              0 |                  6 |      35.3705 |
|  68 |             3 |           1 |                               1.003 |          2 |          500 |              0 |                  4 |      30.8548 |
|  67 |             3 |           1 |                               1.003 |          2 |          500 |              0 |                  3 |      30.1626 |
|  66 |             3 |           1 |                               1.003 |          2 |          500 |              0 |                  2 |      30.0087 |
|  71 |             3 |           1 |                               1.003 |          2 |          500 |              0 |                  7 |      28.4917 |
| 310 |             9 |           1 |                               1.003 |          2 |         1600 |              0 |                  4 |      26.7167 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)