# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Bear - BTC/USDT - Binance

- Experiment nickname: Bear 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2021-11-12
- End date: 2022-11-12
- Timeframe: 1w

## Optimized parameters

- band_lenght=34
- band_mult=1
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=1600
- buy_all_days=1
- lr_buy_longitude=12

## Results

- Return: **4.382023855037545%** over **-72.14382923004018%** on buy and hold.
- Initial investment: 1600.0
- Final result: 1670.1123816806007

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2021-11-15 00:00:00
End                       2022-11-07 00:00:00
Duration                    357 days 00:00:00
Exposure Time [%]                   19.230769
Equity Final [$]                  1670.112382
Equity Peak [$]                   1743.076707
Return [%]                           4.382024
Buy & Hold Return [%]              -72.143829
Return (Ann.) [%]                   23.101422
Volatility (Ann.) [%]               44.909085
Sharpe Ratio                         0.514404
Sortino Ratio                            0.91
Calmar Ratio                         1.683866
Max. Drawdown [%]                   -13.71928
Avg. Drawdown [%]                   -13.71928
Max. Drawdown Duration       63 days 00:00:00
Avg. Drawdown Duration       63 days 00:00:00
# Trades                                    1
Win Rate [%]                            100.0
Best Trade [%]                        4.42191
Worst Trade [%]                       4.42191
Avg. Trade [%]                        4.42191
Max. Trade Duration          63 days 00:00:00
Avg. Trade Duration          63 days 00:00:00
Profit Factor                             NaN
Expectancy [%]                        4.42191
SQN                                       NaN
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
```

### Top 10 configurations

|      |   band_lenght |   band_mult |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|-----:|--------------:|------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 1319 |            34 |           2 |                               1.003 |          2 |         1600 |              1 |                 12 |     4.38202  |
| 1209 |            34 |           1 |                               1.003 |          2 |         1600 |              1 |                 12 |     4.38202  |
| 1296 |            34 |           2 |                               1.003 |          2 |          500 |              1 |                 11 |     2.56442  |
| 1186 |            34 |           1 |                               1.003 |          2 |          500 |              1 |                 11 |     2.56442  |
| 1202 |            34 |           1 |                               1.003 |          2 |         1600 |              1 |                  5 |     0.791991 |
| 1201 |            34 |           1 |                               1.003 |          2 |         1600 |              1 |                  4 |     0.791991 |
| 1200 |            34 |           1 |                               1.003 |          2 |         1600 |              1 |                  3 |     0.791991 |
| 1274 |            34 |           2 |                               1.003 |          2 |          200 |              1 |                 11 |     0.478623 |
| 1164 |            34 |           1 |                               1.003 |          2 |          200 |              1 |                 11 |     0.478623 |
| 1311 |            34 |           2 |                               1.003 |          2 |         1600 |              1 |                  4 |     0.405554 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)