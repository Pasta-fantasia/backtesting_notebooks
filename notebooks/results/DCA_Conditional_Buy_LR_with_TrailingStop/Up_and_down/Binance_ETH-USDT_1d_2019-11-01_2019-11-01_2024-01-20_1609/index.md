# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Up_and_down - ETH/USDT - Binance

- Experiment nickname: Up_and_down 
- Symbol: ETH/USDT
- Exchange: Binance
- Start date: 2019-11-01
- End date: 2022-01-23
- Timeframe: 1d

## Optimized parameters

- band_lenght=55
- band_mult=2
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=500
- buy_all_days=1
- lr_buy_longitude=2

## Results

- Return: **1847.8581851160022%** over **1288.575267791748%** on buy and hold.
- Initial investment: 1600.0
- Final result: 31165.730961856036

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2019-11-01 00:00:00
End                       2022-01-23 00:00:00
Duration                    814 days 00:00:00
Exposure Time [%]                   92.883436
Equity Final [$]                 31165.730962
Equity Peak [$]                  64730.100786
Return [%]                        1847.858185
Buy & Hold Return [%]             1288.575268
Return (Ann.) [%]                  278.034828
Volatility (Ann.) [%]               376.61535
Sharpe Ratio                         0.738246
Sortino Ratio                        5.027494
Calmar Ratio                         4.964543
Max. Drawdown [%]                  -56.004116
Avg. Drawdown [%]                   -9.526198
Max. Drawdown Duration      257 days 00:00:00
Avg. Drawdown Duration       19 days 00:00:00
# Trades                                  143
Win Rate [%]                        65.034965
Best Trade [%]                      504.38809
Worst Trade [%]                    -49.879782
Avg. Trade [%]                      10.475443
Max. Trade Duration         238 days 00:00:00
Avg. Trade Duration          95 days 00:00:00
Profit Factor                         3.95892
Expectancy [%]                      41.689598
SQN                                  3.664743
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                         Size  Entr...
dtype: object
```

### Top 10 configurations

|      |   band_lenght |   band_mult |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|-----:|--------------:|------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 1507 |            55 |           2 |                               1.003 |          2 |          500 |              1 |                  2 |      1847.86 |
| 1397 |            55 |           1 |                               1.003 |          2 |          500 |              1 |                  2 |      1841    |
|  856 |            13 |           2 |                               1.003 |          2 |          500 |              1 |                 11 |      1757.07 |
|  857 |            13 |           2 |                               1.003 |          2 |          500 |              1 |                 12 |      1734.38 |
| 1516 |            55 |           2 |                               1.003 |          2 |          500 |              1 |                 11 |      1697.47 |
|  966 |            21 |           1 |                               1.003 |          2 |          500 |              1 |                 11 |      1691.49 |
| 1485 |            55 |           2 |                               1.003 |          2 |          200 |              1 |                  2 |      1688.26 |
|  967 |            21 |           1 |                               1.003 |          2 |          500 |              1 |                 12 |      1683.68 |
| 1509 |            55 |           2 |                               1.003 |          2 |          500 |              1 |                  4 |      1682.22 |
| 1531 |            55 |           2 |                               1.003 |          2 |         1600 |              1 |                  4 |      1664.56 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)