# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Range - BTC/USDT - Binance

- Experiment nickname: Range 
- Experiment timestamp: 2024-02-04_1944 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2022-06-16
- End date: 2023-03-10
- Timeframe: 1w
- Duration: 4.043328046798706s

## Optimized parameters

- band_length=21
- band_mult=1
- band_low_pct=5.254349145416273
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=1000
- buy_all_days=1
- lr_buy_longitude=2

## Results

- Return: **36.065858451980034%** over **4.558593064858142%** on buy and hold.
- Initial investment: 1000.0
- Final result: 1360.6585845198003

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2022-06-20 00:00:00
End                       2023-03-06 00:00:00
Duration                    259 days 00:00:00
Exposure Time [%]                   39.473684
Equity Final [$]                  1360.658585
Equity Peak [$]                    1471.62858
Return [%]                          36.065858
Buy & Hold Return [%]                4.558593
Return (Ann.) [%]                  670.846941
Volatility (Ann.) [%]              639.695806
Sharpe Ratio                         1.048697
Sortino Ratio                       30.071468
Calmar Ratio                        81.826152
Max. Drawdown [%]                   -8.198442
Avg. Drawdown [%]                   -6.190899
Max. Drawdown Duration       35 days 00:00:00
Avg. Drawdown Duration       26 days 00:00:00
# Trades                                    1
Win Rate [%]                            100.0
Best Trade [%]                      36.393852
Worst Trade [%]                     36.393852
Avg. Trade [%]                      36.393852
Max. Trade Duration          98 days 00:00:00
Avg. Trade Duration          98 days 00:00:00
Profit Factor                             NaN
Expectancy [%]                      36.393852
SQN                                       NaN
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
```

### Top 10 configurations

|      |   band_length |   band_mult |   band_low_pct |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|-----:|--------------:|------------:|---------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 1441 |            21 |           1 |        5.25435 |                               1.003 |          2 |         1000 |              1 |                  2 |      36.0659 |
| 1574 |            21 |           2 |        5.25435 |                               1.003 |          2 |         1000 |              1 |                  3 |      36.0659 |
| 1573 |            21 |           2 |        5.25435 |                               1.003 |          2 |         1000 |              1 |                  2 |      36.0659 |
| 1442 |            21 |           1 |        5.25435 |                               1.003 |          2 |         1000 |              1 |                  3 |      36.0659 |
| 1579 |            21 |           2 |        5.25435 |                               1.003 |          2 |         1000 |              1 |                  8 |      34.5341 |
| 1447 |            21 |           1 |        5.25435 |                               1.003 |          2 |         1000 |              1 |                  8 |      34.5341 |
| 1424 |            21 |           1 |        5.25435 |                               1.003 |          2 |          500 |              1 |                  7 |      33.6805 |
| 1556 |            21 |           2 |        5.25435 |                               1.003 |          2 |          500 |              1 |                  7 |      33.6805 |
| 1577 |            21 |           2 |        5.25435 |                               1.003 |          2 |         1000 |              1 |                  6 |      33.5624 |
| 1445 |            21 |           1 |        5.25435 |                               1.003 |          2 |         1000 |              1 |                  6 |      33.5624 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)

