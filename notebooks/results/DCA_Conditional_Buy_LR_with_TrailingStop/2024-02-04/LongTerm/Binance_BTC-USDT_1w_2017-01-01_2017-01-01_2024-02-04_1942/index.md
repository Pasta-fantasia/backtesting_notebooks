# Class: DCA_Conditional_Buy_LR_with_TrailingStop - LongTerm - BTC/USDT - Binance

- Experiment nickname: LongTerm 
- Experiment timestamp: 2024-02-04_1942 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2017-01-01
- End date: 2024-02-04
- Timeframe: 1w
- Duration: 6.9239301681518555s

## Optimized parameters

- band_length=5
- band_mult=2
- band_low_pct=7.147239576150882
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=500
- buy_all_days=1
- lr_buy_longitude=5

## Results

- Return: **1772.1409265665845%** over **954.2085738224648%** on buy and hold.
- Initial investment: 1000.0
- Final result: 18721.409265665843

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2017-08-14 00:00:00
End                       2024-01-29 00:00:00
Duration                   2359 days 00:00:00
Exposure Time [%]                    95.56213
Equity Final [$]                 18721.409266
Equity Peak [$]                  19604.053763
Return [%]                        1772.140927
Buy & Hold Return [%]              954.208574
Return (Ann.) [%]                   788.39771
Volatility (Ann.) [%]             1671.918947
Sharpe Ratio                         0.471553
Sortino Ratio                       10.773328
Calmar Ratio                        10.607751
Max. Drawdown [%]                  -74.322795
Avg. Drawdown [%]                  -16.493546
Max. Drawdown Duration     1071 days 00:00:00
Avg. Drawdown Duration      181 days 00:00:00
# Trades                                   71
Win Rate [%]                        84.507042
Best Trade [%]                     435.423602
Worst Trade [%]                    -35.913261
Avg. Trade [%]                      32.849819
Max. Trade Duration        1134 days 00:00:00
Avg. Trade Duration         289 days 00:00:00
Profit Factor                       17.359009
Expectancy [%]                        50.3793
SQN                                  4.158706
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                         Size  Entr...
dtype: object
```

### Top 10 configurations

|     |   band_length |   band_mult |   band_low_pct |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|----:|--------------:|------------:|---------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 498 |             5 |           2 |        7.14724 |                               1.003 |          2 |          500 |              1 |                  5 |      1772.14 |
| 497 |             5 |           2 |        7.14724 |                               1.003 |          2 |          500 |              1 |                  4 |      1741.64 |
| 496 |             5 |           2 |        7.14724 |                               1.003 |          2 |          500 |              1 |                  3 |      1660.59 |
| 495 |             5 |           2 |        7.14724 |                               1.003 |          2 |          500 |              1 |                  2 |      1618.84 |
| 475 |             5 |           2 |        7.14724 |                               1.003 |          2 |          400 |              1 |                  4 |      1609.72 |
| 474 |             5 |           2 |        7.14724 |                               1.003 |          2 |          400 |              1 |                  3 |      1577.73 |
| 476 |             5 |           2 |        7.14724 |                               1.003 |          2 |          400 |              1 |                  5 |      1437.76 |
| 451 |             5 |           2 |        7.14724 |                               1.003 |          2 |          200 |              1 |                  2 |      1415.9  |
| 453 |             5 |           2 |        7.14724 |                               1.003 |          2 |          200 |              1 |                  4 |      1395.33 |
| 520 |             5 |           2 |        7.14724 |                               1.003 |          2 |         1000 |              1 |                  5 |      1333.13 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)

