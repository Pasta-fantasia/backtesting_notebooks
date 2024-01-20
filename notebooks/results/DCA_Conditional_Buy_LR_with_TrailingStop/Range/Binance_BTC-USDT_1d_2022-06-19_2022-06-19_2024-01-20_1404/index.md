# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Range - BTC/USDT - Binance

- Experiment nickname: Range 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2022-06-19
- End date: 2023-03-12
- Timeframe: 1d

## Optimized parameters

- band_lenght=9
- band_mult=1
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=1600
- buy_all_days=0
- lr_buy_longitude=6

## Results

- Return: **38.33137059349767%** over **6.917031204432789%** on buy and hold.
- Initial investment: 1600.0
- Final result: 2213.3019294959627

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2022-06-19 00:00:00
End                       2023-03-12 00:00:00
Duration                    266 days 00:00:00
Exposure Time [%]                   65.917603
Equity Final [$]                  2213.301929
Equity Peak [$]                   2513.757579
Return [%]                          38.331371
Buy & Hold Return [%]                6.917031
Return (Ann.) [%]                   55.827598
Volatility (Ann.) [%]               48.186159
Sharpe Ratio                         1.158582
Sortino Ratio                        3.331087
Calmar Ratio                         4.367113
Max. Drawdown [%]                  -12.783638
Avg. Drawdown [%]                   -4.005411
Max. Drawdown Duration      108 days 00:00:00
Avg. Drawdown Duration       16 days 00:00:00
# Trades                                    5
Win Rate [%]                             80.0
Best Trade [%]                      36.577839
Worst Trade [%]                    -11.631655
Avg. Trade [%]                       6.630558
Max. Trade Duration          54 days 00:00:00
Avg. Trade Duration          35 days 00:00:00
Profit Factor                        4.325395
Expectancy [%]                        7.73597
SQN                                   0.97199
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
```

### Top 10 configurations

|     |   band_lenght |   band_mult |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|----:|--------------:|------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 144 |             9 |           1 |                               1.003 |          2 |         1600 |              0 |                  6 |      38.3314 |
| 244 |            10 |           1 |                               1.003 |          2 |         1600 |              0 |                  6 |      38.0651 |
| 344 |            11 |           1 |                               1.003 |          2 |         1600 |              0 |                  6 |      35.7375 |
| 444 |            12 |           1 |                               1.003 |          2 |         1600 |              0 |                  6 |      33.5831 |
| 134 |             9 |           1 |                               1.003 |          2 |         1000 |              0 |                  6 |      28.2394 |
|  22 |             3 |           1 |                               1.003 |          2 |          500 |              0 |                  4 |      27.8098 |
| 234 |            10 |           1 |                               1.003 |          2 |         1000 |              0 |                  6 |      27.8006 |
|  21 |             3 |           1 |                               1.003 |          2 |          500 |              0 |                  3 |      27.1176 |
|  20 |             3 |           1 |                               1.003 |          2 |          500 |              0 |                  2 |      26.8454 |
| 142 |             9 |           1 |                               1.003 |          2 |         1600 |              0 |                  4 |      26.7098 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)