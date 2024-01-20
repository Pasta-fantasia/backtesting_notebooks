# Class: DCA_Conditional_Buy_LR_with_TrailingStop - LongTerm - ETH/USDT - Binance

- Experiment nickname: LongTerm 
- Symbol: ETH/USDT
- Exchange: Binance
- Start date: 2017-01-01
- End date: 2024-01-20
- Timeframe: 1d

## Optimized parameters

- band_lenght=21
- band_mult=2
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=100
- buy_all_days=1
- lr_buy_longitude=2

## Results

- Return: **1029.3874857202793%** over **717.3178672790527%** on buy and hold.
- Initial investment: 1600.0
- Final result: 18070.19977152447

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2017-08-17 00:00:00
End                       2024-01-20 00:00:00
Duration                   2347 days 00:00:00
Exposure Time [%]                   98.764906
Equity Final [$]                 18070.199772
Equity Peak [$]                   18823.31328
Return [%]                        1029.387486
Buy & Hold Return [%]              717.317867
Return (Ann.) [%]                   45.769265
Volatility (Ann.) [%]              122.969309
Sharpe Ratio                         0.372201
Sortino Ratio                        0.903589
Calmar Ratio                          0.50081
Max. Drawdown [%]                  -91.390464
Avg. Drawdown [%]                  -11.022759
Max. Drawdown Duration     1089 days 00:00:00
Avg. Drawdown Duration       74 days 00:00:00
# Trades                                  600
Win Rate [%]                        86.333333
Best Trade [%]                      193.32435
Worst Trade [%]                    -48.221488
Avg. Trade [%]                      21.250947
Max. Trade Duration        1129 days 00:00:00
Avg. Trade Duration         257 days 00:00:00
Profit Factor                         8.52871
Expectancy [%]                      27.708852
SQN                                 15.307616
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                        Size  Entry...
dtype: object
```

### Top 10 configurations

|      |   band_lenght |   band_mult |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|-----:|--------------:|------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 1023 |            21 |           2 |                               1.003 |          2 |          100 |              1 |                  2 |     1029.39  |
| 1033 |            21 |           2 |                               1.003 |          2 |          100 |              1 |                 12 |      964.481 |
| 1025 |            21 |           2 |                               1.003 |          2 |          100 |              1 |                  4 |      957.25  |
| 1028 |            21 |           2 |                               1.003 |          2 |          100 |              1 |                  7 |      933.473 |
| 1055 |            21 |           2 |                               1.003 |          2 |          200 |              1 |                 12 |      916.689 |
| 1032 |            21 |           2 |                               1.003 |          2 |          100 |              1 |                 11 |      910.184 |
| 1024 |            21 |           2 |                               1.003 |          2 |          100 |              1 |                  3 |      908.859 |
| 1031 |            21 |           2 |                               1.003 |          2 |          100 |              1 |                 10 |      906.537 |
| 1479 |            55 |           2 |                               1.003 |          2 |          200 |              0 |                  7 |      902.494 |
| 1030 |            21 |           2 |                               1.003 |          2 |          100 |              1 |                  9 |      900.194 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)