# Class: DCA_Conditional_Buy_LR_with_TrailingStop - LongTerm - BTC/USDT - Binance

- Experiment nickname: LongTerm 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2017-01-01
- End date: 2024-01-20
- Timeframe: 1w

## Optimized parameters

- band_lenght=55
- band_mult=1
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=500
- buy_all_days=1
- lr_buy_longitude=7

## Results

- Return: **1199.6557743688004%** over **915.9083178139584%** on buy and hold.
- Initial investment: 1600.0
- Final result: 20794.492389900806

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2017-08-14 00:00:00
End                       2024-01-15 00:00:00
Duration                   2345 days 00:00:00
Exposure Time [%]                   78.869048
Equity Final [$]                  20794.49239
Equity Peak [$]                  21870.034742
Return [%]                        1199.655774
Buy & Hold Return [%]              915.908318
Return (Ann.) [%]                  584.496537
Volatility (Ann.) [%]             1064.808019
Sharpe Ratio                         0.548922
Sortino Ratio                        8.589331
Calmar Ratio                        12.468515
Max. Drawdown [%]                    -46.8778
Avg. Drawdown [%]                  -16.027464
Max. Drawdown Duration      735 days 00:00:00
Avg. Drawdown Duration      113 days 00:00:00
# Trades                                   29
Win Rate [%]                        89.655172
Best Trade [%]                     553.784343
Worst Trade [%]                    -10.970204
Avg. Trade [%]                      98.702109
Max. Trade Duration        1162 days 00:00:00
Avg. Trade Duration         502 days 00:00:00
Profit Factor                      175.150672
Expectancy [%]                     133.582178
SQN                                  4.451495
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                         Size  Entr...
dtype: object
```

### Top 10 configurations

|      |   band_lenght |   band_mult |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|-----:|--------------:|------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 1402 |            55 |           1 |                               1.003 |          2 |          500 |              1 |                  7 |      1199.66 |
|  300 |             9 |           1 |                               1.003 |          2 |          500 |              1 |                  5 |      1139.01 |
| 1375 |            55 |           1 |                               1.003 |          2 |          200 |              1 |                  2 |      1098.26 |
|  299 |             9 |           1 |                               1.003 |          2 |          500 |              1 |                  4 |      1096.63 |
|  301 |             9 |           1 |                               1.003 |          2 |          500 |              1 |                  6 |      1083.62 |
| 1406 |            55 |           1 |                               1.003 |          2 |          500 |              1 |                 11 |      1074.7  |
| 1377 |            55 |           1 |                               1.003 |          2 |          200 |              1 |                  4 |      1072.05 |
| 1403 |            55 |           1 |                               1.003 |          2 |          500 |              1 |                  8 |      1071.23 |
| 1376 |            55 |           1 |                               1.003 |          2 |          200 |              1 |                  3 |      1069.85 |
|  302 |             9 |           1 |                               1.003 |          2 |          500 |              1 |                  7 |      1041.77 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)