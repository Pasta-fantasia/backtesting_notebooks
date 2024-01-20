# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Range - BTC/USDT - Binance

- Experiment nickname: Range 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2022-06-19
- End date: 2023-03-12
- Timeframe: 1h

## Optimized parameters

- band_lenght=13
- band_mult=2
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=100
- buy_all_days=0
- lr_buy_longitude=4

## Results

- Return: **28.979307144275936%** over **15.943357391226895%** on buy and hold.
- Initial investment: 1600.0
- Final result: 2063.668914308415

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2022-06-19 00:00:00
End                       2023-03-12 23:00:00
Duration                    266 days 23:00:00
Exposure Time [%]                   94.366417
Equity Final [$]                  2063.668914
Equity Peak [$]                    2280.37347
Return [%]                          28.979307
Buy & Hold Return [%]               15.943357
Return (Ann.) [%]                   41.607236
Volatility (Ann.) [%]               69.159379
Sharpe Ratio                         0.601614
Sortino Ratio                        1.353332
Calmar Ratio                         1.449757
Max. Drawdown [%]                  -28.699457
Avg. Drawdown [%]                   -3.200812
Max. Drawdown Duration      156 days 14:00:00
Avg. Drawdown Duration        8 days 00:00:00
# Trades                                  196
Win Rate [%]                         88.77551
Best Trade [%]                      12.995857
Worst Trade [%]                     -13.38525
Avg. Trade [%]                       2.247934
Max. Trade Duration         184 days 10:00:00
Avg. Trade Duration          20 days 16:00:00
Profit Factor                        3.260334
Expectancy [%]                        2.38745
SQN                                  6.381714
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                        Size  Entry...
dtype: object
```

### Top 10 configurations

|     |   band_lenght |   band_mult |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|----:|--------------:|------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 552 |            13 |           2 |                               1.003 |          2 |          100 |              0 |                  4 |      28.9793 |
| 452 |            12 |           2 |                               1.003 |          2 |          100 |              0 |                  4 |      26.8249 |
| 352 |            11 |           2 |                               1.003 |          2 |          100 |              0 |                  4 |      25.7946 |
| 652 |            21 |           2 |                               1.003 |          2 |          100 |              0 |                  4 |      25.2878 |
| 650 |            21 |           2 |                               1.003 |          2 |          100 |              0 |                  2 |      24.5661 |
| 252 |            10 |           2 |                               1.003 |          2 |          100 |              0 |                  4 |      24.0678 |
| 550 |            13 |           2 |                               1.003 |          2 |          100 |              0 |                  2 |      23.9082 |
| 602 |            21 |           1 |                               1.003 |          2 |          100 |              0 |                  4 |      23.4843 |
| 450 |            12 |           2 |                               1.003 |          2 |          100 |              0 |                  2 |      23.398  |
| 350 |            11 |           2 |                               1.003 |          2 |          100 |              0 |                  2 |      23.3258 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)