# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Up - ETH/USDT - Binance

- Experiment nickname: Up 
- Experiment timestamp: 2024-02-04_1950 
- Symbol: ETH/USDT
- Exchange: Binance
- Start date: 2023-01-01
- End date: 2024-02-04
- Timeframe: 1d
- Duration: 8.508580923080444s

## Optimized parameters

- band_length=3
- band_mult=2
- band_low_pct=1.7821342
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=200
- buy_all_days=1
- lr_buy_longitude=3

## Results

- Return: **91.2884459499544%** over **92.6362693309784%** on buy and hold.
- Initial investment: 1000.0
- Final result: 1912.884459499544

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2023-01-01 00:00:00
End                       2024-02-03 00:00:00
Duration                    398 days 00:00:00
Exposure Time [%]                   97.493734
Equity Final [$]                  1912.884459
Equity Peak [$]                   2061.645813
Return [%]                          91.288446
Buy & Hold Return [%]               92.636269
Return (Ann.) [%]                   81.002756
Volatility (Ann.) [%]               73.994225
Sharpe Ratio                         1.094717
Sortino Ratio                         3.49947
Calmar Ratio                         3.814234
Max. Drawdown [%]                  -21.236964
Avg. Drawdown [%]                   -5.768817
Max. Drawdown Duration      119 days 00:00:00
Avg. Drawdown Duration       19 days 00:00:00
# Trades                                   63
Win Rate [%]                         90.47619
Best Trade [%]                      24.006363
Worst Trade [%]                    -10.846623
Avg. Trade [%]                       7.089829
Max. Trade Duration         237 days 00:00:00
Avg. Trade Duration          37 days 00:00:00
Profit Factor                       17.179823
Expectancy [%]                       7.313539
SQN                                  8.294545
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
```

### Top 10 configurations

|     |   band_length |   band_mult |   band_low_pct |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|----:|--------------:|------------:|---------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 188 |             3 |           2 |        1.78213 |                               1.003 |          2 |          200 |              1 |                  3 |      91.2884 |
| 189 |             3 |           2 |        1.78213 |                               1.003 |          2 |          200 |              1 |                  4 |      86.1173 |
| 190 |             3 |           2 |        1.78213 |                               1.003 |          2 |          200 |              1 |                  5 |      83.0149 |
| 191 |             3 |           2 |        1.78213 |                               1.003 |          2 |          200 |              1 |                  6 |      81.2036 |
| 232 |             3 |           2 |        1.78213 |                               1.003 |          2 |          500 |              1 |                  3 |      80.9732 |
| 454 |             5 |           2 |        1.78213 |                               1.003 |          2 |          200 |              1 |                  5 |      80.1007 |
| 451 |             5 |           2 |        1.78213 |                               1.003 |          2 |          200 |              1 |                  2 |      79.9773 |
| 452 |             5 |           2 |        1.78213 |                               1.003 |          2 |          200 |              1 |                  3 |      78.7424 |
| 192 |             3 |           2 |        1.78213 |                               1.003 |          2 |          200 |              1 |                  7 |      78.4891 |
| 211 |             3 |           2 |        1.78213 |                               1.003 |          2 |          400 |              1 |                  4 |      78.1763 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)

