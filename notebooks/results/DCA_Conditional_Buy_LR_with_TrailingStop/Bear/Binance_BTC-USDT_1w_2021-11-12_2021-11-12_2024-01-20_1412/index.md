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
- lr_buy_longitude=3

## Results

- Return: **0.7919908013832355%** over **-72.14382923004018%** on buy and hold.
- Initial investment: 1600.0
- Final result: 1612.6718528221318

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2021-11-15 00:00:00
End                       2022-11-07 00:00:00
Duration                    357 days 00:00:00
Exposure Time [%]                   32.692308
Equity Final [$]                  1612.671853
Equity Peak [$]                   1845.042013
Return [%]                           0.791991
Buy & Hold Return [%]              -72.143829
Return (Ann.) [%]                    3.897007
Volatility (Ann.) [%]               53.700448
Sharpe Ratio                         0.072569
Sortino Ratio                        0.105232
Calmar Ratio                         0.191337
Max. Drawdown [%]                  -20.367245
Avg. Drawdown [%]                  -10.436866
Max. Drawdown Duration       91 days 00:00:00
Avg. Drawdown Duration       53 days 00:00:00
# Trades                                    2
Win Rate [%]                             50.0
Best Trade [%]                      10.678779
Worst Trade [%]                      -9.88028
Avg. Trade [%]                       -0.12838
Max. Trade Duration          91 days 00:00:00
Avg. Trade Duration          56 days 00:00:00
Profit Factor                        1.080817
Expectancy [%]                       0.399249
SQN                                  0.038872
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
```

### Top 10 configurations

|     |   band_lenght |   band_mult |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|----:|--------------:|------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 748 |            34 |           1 |                               1.003 |          2 |         1600 |              1 |                  5 |     0.791991 |
| 747 |            34 |           1 |                               1.003 |          2 |         1600 |              1 |                  4 |     0.791991 |
| 746 |            34 |           1 |                               1.003 |          2 |         1600 |              1 |                  3 |     0.791991 |
| 738 |            34 |           1 |                               1.003 |          2 |         1000 |              1 |                  5 |     0.495048 |
| 736 |            34 |           1 |                               1.003 |          2 |         1000 |              1 |                  3 |     0.495048 |
| 737 |            34 |           1 |                               1.003 |          2 |         1000 |              1 |                  4 |     0.495048 |
| 647 |            21 |           1 |                               1.003 |          2 |         1600 |              1 |                  4 |     0.405554 |
| 697 |            21 |           2 |                               1.003 |          2 |         1600 |              1 |                  4 |     0.405554 |
| 648 |            21 |           1 |                               1.003 |          2 |         1600 |              1 |                  5 |     0.405554 |
| 698 |            21 |           2 |                               1.003 |          2 |         1600 |              1 |                  5 |     0.405554 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)