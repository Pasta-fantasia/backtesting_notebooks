# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Range - BTC/USDT - Binance

- Experiment nickname: Range 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2022-06-16
- End date: 2023-03-10
- Timeframe: 1h

## Optimized parameters

- band_lenght=21
- band_mult=2
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=50
- buy_all_days=0
- lr_buy_longitude=12

## Results

- Return: **44.837709332268275%** over **-11.15216049382716%** on buy and hold.
- Initial investment: 1600.0
- Final result: 2317.4033493162924

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2022-06-16 00:00:00
End                       2023-03-10 23:00:00
Duration                    267 days 23:00:00
Exposure Time [%]                   94.558458
Equity Final [$]                  2317.403349
Equity Peak [$]                   2528.942818
Return [%]                          44.837709
Buy & Hold Return [%]               -11.15216
Return (Ann.) [%]                   65.619397
Volatility (Ann.) [%]               46.608402
Sharpe Ratio                         1.407888
Sortino Ratio                        4.843605
Calmar Ratio                         5.791663
Max. Drawdown [%]                  -11.329976
Avg. Drawdown [%]                   -1.731004
Max. Drawdown Duration       42 days 23:00:00
Avg. Drawdown Duration        4 days 16:00:00
# Trades                                  414
Win Rate [%]                        94.202899
Best Trade [%]                      20.104184
Worst Trade [%]                     -19.79732
Avg. Trade [%]                       3.301659
Max. Trade Duration         183 days 20:00:00
Avg. Trade Duration          11 days 16:00:00
Profit Factor                        5.028031
Expectancy [%]                       3.497993
SQN                                 11.417069
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                        Size  Entry...
dtype: object
```

### Top 10 configurations

|      |   band_lenght |   band_mult |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|-----:|--------------:|------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 1000 |            21 |           2 |                               1.003 |          2 |           50 |              0 |                 12 |      44.8377 |
| 1440 |            55 |           2 |                               1.003 |          2 |           50 |              0 |                 12 |      44.7639 |
|  999 |            21 |           2 |                               1.003 |          2 |           50 |              0 |                 11 |      43.3258 |
| 1439 |            55 |           2 |                               1.003 |          2 |           50 |              0 |                 11 |      42.0242 |
|  802 |            13 |           2 |                               1.003 |          2 |          100 |              0 |                 12 |      40.202  |
| 1110 |            34 |           1 |                               1.003 |          2 |           50 |              0 |                 12 |      39.3448 |
|  998 |            21 |           2 |                               1.003 |          2 |           50 |              0 |                 10 |      38.4833 |
| 1109 |            34 |           1 |                               1.003 |          2 |           50 |              0 |                 11 |      38.1169 |
| 1220 |            34 |           2 |                               1.003 |          2 |           50 |              0 |                 12 |      38.0321 |
| 1438 |            55 |           2 |                               1.003 |          2 |           50 |              0 |                 10 |      37.604  |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)