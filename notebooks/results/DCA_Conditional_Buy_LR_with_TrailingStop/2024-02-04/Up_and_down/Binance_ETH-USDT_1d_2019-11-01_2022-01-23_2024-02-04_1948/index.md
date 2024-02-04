# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Up_and_down - ETH/USDT - Binance

- Experiment nickname: Up_and_down 
- Experiment timestamp: 2024-02-04_1948 
- Symbol: ETH/USDT
- Exchange: Binance
- Start date: 2019-11-01
- End date: 2022-01-23
- Timeframe: 1d
- Duration: 19.38255548477173s

## Optimized parameters

- band_length=21
- band_mult=2
- band_low_pct=3.8906393
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=500
- buy_all_days=1
- lr_buy_longitude=12

## Results

- Return: **1734.846979884518%** over **1288.575267791748%** on buy and hold.
- Initial investment: 1000.0
- Final result: 18348.46979884518

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2019-11-01 00:00:00
End                       2022-01-23 00:00:00
Duration                    814 days 00:00:00
Exposure Time [%]                   93.251534
Equity Final [$]                 18348.469799
Equity Peak [$]                  24356.900137
Return [%]                         1734.84698
Buy & Hold Return [%]             1288.575268
Return (Ann.) [%]                  268.049881
Volatility (Ann.) [%]              318.068292
Sharpe Ratio                         0.842743
Sortino Ratio                        5.625764
Calmar Ratio                         5.841737
Max. Drawdown [%]                  -45.885303
Avg. Drawdown [%]                    -9.16283
Max. Drawdown Duration      162 days 00:00:00
Avg. Drawdown Duration       19 days 00:00:00
# Trades                                  119
Win Rate [%]                         84.87395
Best Trade [%]                     184.111011
Worst Trade [%]                     -47.95594
Avg. Trade [%]                      21.857992
Max. Trade Duration         166 days 00:00:00
Avg. Trade Duration          58 days 00:00:00
Profit Factor                         5.87608
Expectancy [%]                      29.426315
SQN                                   7.30593
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                         Size  Entr...
dtype: object
```

### Top 10 configurations

|      |   band_length |   band_mult |   band_low_pct |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|-----:|--------------:|------------:|---------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 1561 |            21 |           2 |        3.89064 |                               1.003 |          2 |          500 |              1 |                 12 |      1734.85 |
| 1296 |            13 |           2 |        3.89064 |                               1.003 |          2 |          500 |              1 |                 11 |      1683.71 |
| 1274 |            13 |           2 |        3.89064 |                               1.003 |          2 |          400 |              1 |                 11 |      1677.18 |
| 1560 |            21 |           2 |        3.89064 |                               1.003 |          2 |          500 |              1 |                 11 |      1645.87 |
| 1252 |            13 |           2 |        3.89064 |                               1.003 |          2 |          200 |              1 |                 11 |      1587.41 |
| 1253 |            13 |           2 |        3.89064 |                               1.003 |          2 |          200 |              1 |                 12 |      1578.34 |
| 1539 |            21 |           2 |        3.89064 |                               1.003 |          2 |          400 |              1 |                 12 |      1535.12 |
| 1429 |            21 |           1 |        3.89064 |                               1.003 |          2 |          500 |              1 |                 12 |      1510.53 |
| 1551 |            21 |           2 |        3.89064 |                               1.003 |          2 |          500 |              1 |                  2 |      1500.85 |
| 1692 |            34 |           1 |        3.89064 |                               1.003 |          2 |          500 |              1 |                 11 |      1499.25 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)

