# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Range - ETH/USDT - Binance

- Experiment nickname: Range 
- Symbol: ETH/USDT
- Exchange: Binance
- Start date: 2022-06-16
- End date: 2023-03-10
- Timeframe: 1d

## Optimized parameters

- band_lenght=11
- band_mult=1
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=1600
- buy_all_days=0
- lr_buy_longitude=6

## Results

- Return: **81.8425920743399%** over **33.49928855895996%** on buy and hold.
- Initial investment: 1600.0
- Final result: 2909.4814731894385

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2022-06-16 00:00:00
End                       2023-03-10 00:00:00
Duration                    267 days 00:00:00
Exposure Time [%]                        50.0
Equity Final [$]                  2909.481473
Equity Peak [$]                   3002.655447
Return [%]                          81.842592
Buy & Hold Return [%]               33.499289
Return (Ann.) [%]                  125.782315
Volatility (Ann.) [%]               95.887183
Sharpe Ratio                         1.311774
Sortino Ratio                        6.169388
Calmar Ratio                         7.890869
Max. Drawdown [%]                  -15.940236
Avg. Drawdown [%]                   -5.238492
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
SQN                                  3.436569
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
```

### Top 10 configurations

|     |   band_lenght |   band_mult |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|----:|--------------:|------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 532 |            11 |           1 |                               1.003 |          2 |         1600 |              0 |                  6 |      81.8426 |
|  90 |             3 |           1 |                               1.003 |          2 |         1600 |              0 |                  4 |      79.6112 |
| 752 |            13 |           1 |                               1.003 |          2 |         1600 |              0 |                  6 |      72.0199 |
|  89 |             3 |           1 |                               1.003 |          2 |         1600 |              0 |                  3 |      63.1931 |
|  98 |             3 |           1 |                               1.003 |          2 |         1600 |              0 |                 12 |      62.0545 |
|  97 |             3 |           1 |                               1.003 |          2 |         1600 |              0 |                 11 |      62.0545 |
| 207 |             3 |           2 |                               1.003 |          2 |         1600 |              0 |                 11 |      57.3126 |
| 208 |             3 |           2 |                               1.003 |          2 |         1600 |              0 |                 12 |      57.3126 |
|  68 |             3 |           1 |                               1.003 |          2 |          500 |              0 |                  4 |      57.1937 |
| 867 |            13 |           2 |                               1.003 |          2 |         1600 |              0 |                 11 |      57.1087 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)