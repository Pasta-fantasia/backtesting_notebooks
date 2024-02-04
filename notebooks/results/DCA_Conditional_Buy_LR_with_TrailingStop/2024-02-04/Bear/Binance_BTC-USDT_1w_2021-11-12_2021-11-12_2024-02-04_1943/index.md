# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Bear - BTC/USDT - Binance

- Experiment nickname: Bear 
- Experiment timestamp: 2024-02-04_1943 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2021-11-12
- End date: 2022-11-12
- Timeframe: 1w
- Duration: 4.041464805603027s

## Optimized parameters

- band_length=34
- band_mult=1
- band_low_pct=8.070756896577578
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=1000
- buy_all_days=1
- lr_buy_longitude=12

## Results

- Return: **4.382045987030051%** over **-72.14382923004018%** on buy and hold.
- Initial investment: 1000.0
- Final result: 1043.8204598703005

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2021-11-15 00:00:00
End                       2022-11-07 00:00:00
Duration                    357 days 00:00:00
Exposure Time [%]                   19.230769
Equity Final [$]                   1043.82046
Equity Peak [$]                   1089.423394
Return [%]                           4.382046
Buy & Hold Return [%]              -72.143829
Return (Ann.) [%]                   23.101549
Volatility (Ann.) [%]               44.909364
Sharpe Ratio                         0.514404
Sortino Ratio                        0.910001
Calmar Ratio                         1.683867
Max. Drawdown [%]                  -13.719343
Avg. Drawdown [%]                  -13.719343
Max. Drawdown Duration       63 days 00:00:00
Avg. Drawdown Duration       63 days 00:00:00
# Trades                                    1
Win Rate [%]                            100.0
Best Trade [%]                        4.42191
Worst Trade [%]                       4.42191
Avg. Trade [%]                        4.42191
Max. Trade Duration          63 days 00:00:00
Avg. Trade Duration          63 days 00:00:00
Profit Factor                             NaN
Expectancy [%]                        4.42191
SQN                                       NaN
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
```

### Top 10 configurations

|      |   band_length |   band_mult |   band_low_pct |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|-----:|--------------:|------------:|---------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 1847 |            34 |           2 |        8.07076 |                               1.003 |          2 |         1000 |              1 |                 12 |     4.38205  |
| 1715 |            34 |           1 |        8.07076 |                               1.003 |          2 |         1000 |              1 |                 12 |     4.38205  |
| 1824 |            34 |           2 |        8.07076 |                               1.003 |          2 |          500 |              1 |                 11 |     1.9121   |
| 1692 |            34 |           1 |        8.07076 |                               1.003 |          2 |          500 |              1 |                 11 |     1.9121   |
| 1670 |            34 |           1 |        8.07076 |                               1.003 |          2 |          400 |              1 |                 11 |     1.52959  |
| 1802 |            34 |           2 |        8.07076 |                               1.003 |          2 |          400 |              1 |                 11 |     1.52959  |
| 1706 |            34 |           1 |        8.07076 |                               1.003 |          2 |         1000 |              1 |                  3 |     0.792077 |
| 1707 |            34 |           1 |        8.07076 |                               1.003 |          2 |         1000 |              1 |                  4 |     0.792077 |
| 1708 |            34 |           1 |        8.07076 |                               1.003 |          2 |         1000 |              1 |                  5 |     0.792077 |
| 1780 |            34 |           2 |        8.07076 |                               1.003 |          2 |          200 |              1 |                 11 |     0.765797 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)

