# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Range - ETH/USDT - Binance

- Experiment nickname: Range 
- Experiment timestamp: 2024-02-04_1951 
- Symbol: ETH/USDT
- Exchange: Binance
- Start date: 2022-06-16
- End date: 2023-03-10
- Timeframe: 1d
- Duration: 6.979151487350464s

## Optimized parameters

- band_length=11
- band_mult=1
- band_low_pct=2.8878767
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=1000
- buy_all_days=0
- lr_buy_longitude=6

## Results

- Return: **81.84214298247093%** over **33.49928855895996%** on buy and hold.
- Initial investment: 1000.0
- Final result: 1818.4214298247093

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2022-06-16 00:00:00
End                       2023-03-10 00:00:00
Duration                    267 days 00:00:00
Exposure Time [%]                        50.0
Equity Final [$]                   1818.42143
Equity Peak [$]                   1876.654019
Return [%]                          81.842143
Buy & Hold Return [%]               33.499289
Return (Ann.) [%]                  125.781555
Volatility (Ann.) [%]               95.885292
Sharpe Ratio                         1.311792
Sortino Ratio                        6.169422
Calmar Ratio                         7.891028
Max. Drawdown [%]                  -15.939818
Avg. Drawdown [%]                   -5.238467
Max. Drawdown Duration       68 days 00:00:00
Avg. Drawdown Duration       17 days 00:00:00
# Trades                                    6
Win Rate [%]                            100.0
Best Trade [%]                      27.513899
Worst Trade [%]                      3.499545
Avg. Trade [%]                      13.415768
Max. Trade Duration          41 days 00:00:00
Avg. Trade Duration          22 days 00:00:00
Profit Factor                             NaN
Expectancy [%]                      13.765177
SQN                                  3.436623
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                      Size  EntryBa...
dtype: object
```

### Top 10 configurations

|      |   band_length |   band_mult |   band_low_pct |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|-----:|--------------:|------------:|---------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
|  906 |            11 |           1 |        2.88788 |                               1.003 |          2 |         1000 |              0 |                  6 |      81.8421 |
|  112 |             3 |           1 |        2.88788 |                               1.003 |          2 |         1000 |              0 |                  4 |      77.3272 |
| 1170 |            13 |           1 |        2.88788 |                               1.003 |          2 |         1000 |              0 |                  6 |      72.2407 |
|  486 |             5 |           2 |        2.88788 |                               1.003 |          2 |          500 |              0 |                  4 |      68.3222 |
| 1021 |            11 |           2 |        2.88788 |                               1.003 |          2 |          500 |              0 |                 11 |      67.2305 |
| 1022 |            11 |           2 |        2.88788 |                               1.003 |          2 |          500 |              0 |                 12 |      67.2305 |
|  642 |             9 |           1 |        2.88788 |                               1.003 |          2 |         1000 |              0 |                  6 |      65.3347 |
|   90 |             3 |           1 |        2.88788 |                               1.003 |          2 |          500 |              0 |                  4 |      64.9099 |
|   68 |             3 |           1 |        2.88788 |                               1.003 |          2 |          400 |              0 |                  4 |      64.4606 |
|  464 |             5 |           2 |        2.88788 |                               1.003 |          2 |          400 |              0 |                  4 |      62.1478 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)

