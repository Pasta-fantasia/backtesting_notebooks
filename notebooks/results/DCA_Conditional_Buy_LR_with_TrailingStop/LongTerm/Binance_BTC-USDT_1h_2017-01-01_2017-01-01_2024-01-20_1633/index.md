# Class: DCA_Conditional_Buy_LR_with_TrailingStop - LongTerm - BTC/USDT - Binance

- Experiment nickname: LongTerm 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2017-01-01
- End date: 2024-01-20
- Timeframe: 1h

## Optimized parameters

- band_lenght=55
- band_mult=2
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=500
- buy_all_days=0
- lr_buy_longitude=3

## Results

- Return: **789.449399978015%** over **863.4392630946221%** on buy and hold.
- Initial investment: 1600.0
- Final result: 14231.19039964824

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2017-08-17 04:00:00
End                       2024-01-20 09:00:00
Duration                   2347 days 05:00:00
Exposure Time [%]                   98.407643
Equity Final [$]                   14231.1904
Equity Peak [$]                  19968.862023
Return [%]                           789.4494
Buy & Hold Return [%]              863.439263
Return (Ann.) [%]                   40.456639
Volatility (Ann.) [%]              101.584115
Sharpe Ratio                         0.398258
Sortino Ratio                        0.906677
Calmar Ratio                         0.506167
Max. Drawdown [%]                   -79.92743
Avg. Drawdown [%]                   -3.175166
Max. Drawdown Duration     1104 days 12:00:00
Avg. Drawdown Duration       11 days 07:00:00
# Trades                                  473
Win Rate [%]                        91.966173
Best Trade [%]                      34.640225
Worst Trade [%]                    -38.540779
Avg. Trade [%]                       4.638802
Max. Trade Duration        1081 days 09:00:00
Avg. Trade Duration         104 days 12:00:00
Profit Factor                        3.519673
Expectancy [%]                       5.389646
SQN                                  9.894541
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                          Size  Ent...
dtype: object
```

### Top 10 configurations

|      |   band_lenght |   band_mult |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|-----:|--------------:|------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 1497 |            55 |           2 |                               1.003 |          2 |          500 |              0 |                  3 |      789.449 |
| 1500 |            55 |           2 |                               1.003 |          2 |          500 |              0 |                  6 |      775.71  |
| 1499 |            55 |           2 |                               1.003 |          2 |          500 |              0 |                  5 |      773.381 |
| 1498 |            55 |           2 |                               1.003 |          2 |          500 |              0 |                  4 |      756.308 |
| 1496 |            55 |           2 |                               1.003 |          2 |          500 |              0 |                  2 |      753.389 |
| 1486 |            55 |           2 |                               1.003 |          2 |          200 |              1 |                  3 |      749.291 |
| 1487 |            55 |           2 |                               1.003 |          2 |          200 |              1 |                  4 |      747.114 |
| 1488 |            55 |           2 |                               1.003 |          2 |          200 |              1 |                  5 |      745.559 |
| 1485 |            55 |           2 |                               1.003 |          2 |          200 |              1 |                  2 |      738.141 |
| 1489 |            55 |           2 |                               1.003 |          2 |          200 |              1 |                  6 |      737.498 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)