# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Up - BTC/USDT - Binance

- Experiment nickname: Up 
- Experiment timestamp: 2024-02-04_1946 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2023-01-01
- End date: 2024-02-04
- Timeframe: 1h
- Duration: 90.63754105567932s

## Optimized parameters

- band_length=5
- band_mult=1
- band_low_pct=0.3022449542863991
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=100
- buy_all_days=1
- lr_buy_longitude=3

## Results

- Return: **166.43827242676338%** over **160.41342911715722%** on buy and hold.
- Initial investment: 1000.0
- Final result: 2664.382724267634

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2023-01-01 00:00:00
End                       2024-02-03 08:00:00
Duration                    398 days 08:00:00
Exposure Time [%]                   99.843096
Equity Final [$]                  2664.382724
Equity Peak [$]                   2811.765928
Return [%]                         166.438272
Buy & Hold Return [%]              160.413429
Return (Ann.) [%]                  144.611135
Volatility (Ann.) [%]              103.040489
Sharpe Ratio                          1.40344
Sortino Ratio                        6.194643
Calmar Ratio                         6.987503
Max. Drawdown [%]                  -20.695682
Avg. Drawdown [%]                   -1.888299
Max. Drawdown Duration      102 days 01:00:00
Avg. Drawdown Duration        3 days 12:00:00
# Trades                                  867
Win Rate [%]                        96.885813
Best Trade [%]                      11.257664
Worst Trade [%]                    -11.449519
Avg. Trade [%]                       1.910152
Max. Trade Duration         112 days 09:00:00
Avg. Trade Duration           7 days 21:00:00
Profit Factor                       17.832269
Expectancy [%]                       1.937465
SQN                                 24.060597
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                        Size  Entry...
dtype: object
```

### Top 10 configurations

|     |   band_length |   band_mult |   band_low_pct |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|----:|--------------:|------------:|---------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 298 |             5 |           1 |       0.302245 |                               1.003 |          2 |          100 |              1 |                  3 |      166.438 |
|  43 |             3 |           1 |       0.302245 |                               1.003 |          2 |          100 |              1 |                 12 |      166.422 |
|  42 |             3 |           1 |       0.302245 |                               1.003 |          2 |          100 |              1 |                 11 |      165.228 |
| 297 |             5 |           1 |       0.302245 |                               1.003 |          2 |          100 |              1 |                  2 |      165.042 |
| 299 |             5 |           1 |       0.302245 |                               1.003 |          2 |          100 |              1 |                  4 |      164.11  |
| 306 |             5 |           1 |       0.302245 |                               1.003 |          2 |          100 |              1 |                 11 |      163.715 |
|  37 |             3 |           1 |       0.302245 |                               1.003 |          2 |          100 |              1 |                  6 |      162.989 |
|  34 |             3 |           1 |       0.302245 |                               1.003 |          2 |          100 |              1 |                  3 |      162.936 |
| 307 |             5 |           1 |       0.302245 |                               1.003 |          2 |          100 |              1 |                 12 |      162.111 |
|  38 |             3 |           1 |       0.302245 |                               1.003 |          2 |          100 |              1 |                  7 |      161.657 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)

