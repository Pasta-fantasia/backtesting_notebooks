# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Range - BTC/USDT - Binance

- Experiment nickname: Range 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2022-06-19
- End date: 2023-03-12
- Timeframe: 1w

## Optimized parameters

- band_lenght=21
- band_mult=1
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=1600
- buy_all_days=1
- lr_buy_longitude=2

## Results

- Return: **36.065858451980034%** over **4.558593064858142%** on buy and hold.
- Initial investment: 1600.0
- Final result: 2177.0537352316805

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2022-06-20 00:00:00
End                       2023-03-06 00:00:00
Duration                    259 days 00:00:00
Exposure Time [%]                   39.473684
Equity Final [$]                  2177.053735
Equity Peak [$]                   2354.605728
Return [%]                          36.065858
Buy & Hold Return [%]                4.558593
Return (Ann.) [%]                  670.846941
Volatility (Ann.) [%]              639.695806
Sharpe Ratio                         1.048697
Sortino Ratio                       30.071468
Calmar Ratio                        81.826152
Max. Drawdown [%]                   -8.198442
Avg. Drawdown [%]                   -6.190899
Max. Drawdown Duration       35 days 00:00:00
Avg. Drawdown Duration       26 days 00:00:00
# Trades                                    1
Win Rate [%]                            100.0
Best Trade [%]                      36.393852
Worst Trade [%]                     36.393852
Avg. Trade [%]                      36.393852
Max. Trade Duration          98 days 00:00:00
Avg. Trade Duration          98 days 00:00:00
Profit Factor                             NaN
Expectancy [%]                      36.393852
SQN                                       NaN
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
```

### Top 10 configurations

|     |   band_lenght |   band_mult |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|----:|--------------:|------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 696 |            21 |           2 |                               1.003 |          2 |         1600 |              1 |                  3 |      36.0659 |
| 695 |            21 |           2 |                               1.003 |          2 |         1600 |              1 |                  2 |      36.0659 |
| 645 |            21 |           1 |                               1.003 |          2 |         1600 |              1 |                  2 |      36.0659 |
| 646 |            21 |           1 |                               1.003 |          2 |         1600 |              1 |                  3 |      36.0659 |
| 699 |            21 |           2 |                               1.003 |          2 |         1600 |              1 |                  6 |      33.5622 |
| 649 |            21 |           1 |                               1.003 |          2 |         1600 |              1 |                  6 |      33.5622 |
| 625 |            21 |           1 |                               1.003 |          2 |          500 |              1 |                  2 |      31.1261 |
| 675 |            21 |           2 |                               1.003 |          2 |          500 |              1 |                  2 |      31.1261 |
| 698 |            21 |           2 |                               1.003 |          2 |         1600 |              1 |                  5 |      30.8737 |
| 648 |            21 |           1 |                               1.003 |          2 |         1600 |              1 |                  5 |      30.8737 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)