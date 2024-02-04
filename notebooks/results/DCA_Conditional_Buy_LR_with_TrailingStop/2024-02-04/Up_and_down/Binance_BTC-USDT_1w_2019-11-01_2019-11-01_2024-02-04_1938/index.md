# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Up_and_down - BTC/USDT - Binance

- Experiment nickname: Up_and_down 
- Experiment timestamp: 2024-02-04_1938 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2019-11-01
- End date: 2022-01-23
- Timeframe: 1w
- Duration: 4.797983884811401s

## Optimized parameters

- band_length=5
- band_mult=2
- band_low_pct=7.490851841398112
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=1000
- buy_all_days=1
- lr_buy_longitude=3

## Results

- Return: **1034.2213565932507%** over **300.9587951506007%** on buy and hold.
- Initial investment: 1000.0
- Final result: 11342.213565932507

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2019-11-04 00:00:00
End                       2022-01-17 00:00:00
Duration                    805 days 00:00:00
Exposure Time [%]                   87.931034
Equity Final [$]                 11342.213566
Equity Peak [$]                  13933.273578
Return [%]                        1034.221357
Buy & Hold Return [%]              300.958795
Return (Ann.) [%]                19454.201799
Volatility (Ann.) [%]            30529.063543
Sharpe Ratio                         0.637235
Sortino Ratio                      370.901159
Calmar Ratio                       920.748505
Max. Drawdown [%]                  -21.128681
Avg. Drawdown [%]                   -8.065419
Max. Drawdown Duration      133 days 00:00:00
Avg. Drawdown Duration       38 days 00:00:00
# Trades                                   22
Win Rate [%]                        68.181818
Best Trade [%]                     430.074464
Worst Trade [%]                    -34.326594
Avg. Trade [%]                      21.962144
Max. Trade Duration         280 days 00:00:00
Avg. Trade Duration         104 days 00:00:00
Profit Factor                        7.055426
Expectancy [%]                       47.43821
SQN                                  1.762738
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                         Size  Entr...
dtype: object
```

### Top 10 configurations

|      |   band_length |   band_mult |   band_low_pct |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|-----:|--------------:|------------:|---------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
|  518 |             5 |           2 |        7.49085 |                               1.003 |          2 |         1000 |              1 |                  3 |     1034.22  |
| 1441 |            21 |           1 |        7.49085 |                               1.003 |          2 |         1000 |              1 |                  2 |      752.701 |
|  474 |             5 |           2 |        7.49085 |                               1.003 |          2 |          400 |              1 |                  3 |      743.136 |
|  496 |             5 |           2 |        7.49085 |                               1.003 |          2 |          500 |              1 |                  3 |      732.463 |
|  497 |             5 |           2 |        7.49085 |                               1.003 |          2 |          500 |              1 |                  4 |      702.416 |
| 1442 |            21 |           1 |        7.49085 |                               1.003 |          2 |         1000 |              1 |                  3 |      683.189 |
| 1419 |            21 |           1 |        7.49085 |                               1.003 |          2 |          500 |              1 |                  2 |      646.727 |
| 1443 |            21 |           1 |        7.49085 |                               1.003 |          2 |         1000 |              1 |                  4 |      640.201 |
| 1444 |            21 |           1 |        7.49085 |                               1.003 |          2 |         1000 |              1 |                  5 |      629.142 |
| 1445 |            21 |           1 |        7.49085 |                               1.003 |          2 |         1000 |              1 |                  6 |      611.893 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)

