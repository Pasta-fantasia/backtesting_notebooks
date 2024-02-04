# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Up - BTC/USDT - Binance

- Experiment nickname: Up 
- Experiment timestamp: 2024-02-04_1941 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2023-01-01
- End date: 2024-02-04
- Timeframe: 1d
- Duration: 7.898077487945557s

## Optimized parameters

- band_length=3
- band_mult=2
- band_low_pct=1.5664176609689902
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=200
- buy_all_days=1
- lr_buy_longitude=2

## Results

- Return: **145.22911394659332%** over **159.04873377014158%** on buy and hold.
- Initial investment: 1000.0
- Final result: 2452.291139465933

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2023-01-01 00:00:00
End                       2024-02-03 00:00:00
Duration                    398 days 00:00:00
Exposure Time [%]                   98.746867
Equity Final [$]                  2452.291139
Equity Peak [$]                   2480.569138
Return [%]                         145.229114
Buy & Hold Return [%]              159.048734
Return (Ann.) [%]                  127.182783
Volatility (Ann.) [%]               80.982755
Sharpe Ratio                         1.570492
Sortino Ratio                        7.032258
Calmar Ratio                         7.065159
Max. Drawdown [%]                  -18.001404
Avg. Drawdown [%]                   -3.027679
Max. Drawdown Duration      102 days 00:00:00
Avg. Drawdown Duration       12 days 00:00:00
# Trades                                   94
Win Rate [%]                        95.744681
Best Trade [%]                       35.78176
Worst Trade [%]                     -8.081199
Avg. Trade [%]                       7.565671
Max. Trade Duration         193 days 00:00:00
Avg. Trade Duration          27 days 00:00:00
Profit Factor                       46.760142
Expectancy [%]                       7.795746
SQN                                 10.439064
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                        Size  Entry...
dtype: object
```

### Top 10 configurations

|     |   band_length |   band_mult |   band_low_pct |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|----:|--------------:|------------:|---------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 187 |             3 |           2 |        1.56642 |                               1.003 |          2 |          200 |              1 |                  2 |      145.229 |
| 189 |             3 |           2 |        1.56642 |                               1.003 |          2 |          200 |              1 |                  4 |      143.866 |
| 451 |             5 |           2 |        1.56642 |                               1.003 |          2 |          200 |              1 |                  2 |      143.231 |
|  55 |             3 |           1 |        1.56642 |                               1.003 |          2 |          200 |              1 |                  2 |      138.409 |
| 319 |             5 |           1 |        1.56642 |                               1.003 |          2 |          200 |              1 |                  2 |      138.328 |
| 188 |             3 |           2 |        1.56642 |                               1.003 |          2 |          200 |              1 |                  3 |      138.131 |
| 190 |             3 |           2 |        1.56642 |                               1.003 |          2 |          200 |              1 |                  5 |      137.604 |
| 211 |             3 |           2 |        1.56642 |                               1.003 |          2 |          400 |              1 |                  4 |      135.145 |
| 192 |             3 |           2 |        1.56642 |                               1.003 |          2 |          200 |              1 |                  7 |      133.275 |
| 209 |             3 |           2 |        1.56642 |                               1.003 |          2 |          400 |              1 |                  2 |      132.72  |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)

