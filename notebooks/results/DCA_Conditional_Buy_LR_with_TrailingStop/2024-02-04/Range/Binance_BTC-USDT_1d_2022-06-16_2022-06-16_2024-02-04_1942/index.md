# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Range - BTC/USDT - Binance

- Experiment nickname: Range 
- Experiment timestamp: 2024-02-04_1942 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2022-06-16
- End date: 2023-03-10
- Timeframe: 1d
- Duration: 6.2838006019592285s

## Optimized parameters

- band_length=3
- band_mult=1
- band_low_pct=2.065553230602729
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=1000
- buy_all_days=0
- lr_buy_longitude=6

## Results

- Return: **36.37531513528706%** over **-1.2284505259711431%** on buy and hold.
- Initial investment: 1000.0
- Final result: 1363.7531513528706

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2022-06-16 00:00:00
End                       2023-03-10 00:00:00
Duration                    267 days 00:00:00
Exposure Time [%]                   62.686567
Equity Final [$]                  1363.753151
Equity Peak [$]                   1554.551142
Return [%]                          36.375315
Buy & Hold Return [%]               -1.228451
Return (Ann.) [%]                   52.581567
Volatility (Ann.) [%]               45.515393
Sharpe Ratio                         1.155248
Sortino Ratio                        3.249567
Calmar Ratio                         4.284151
Max. Drawdown [%]                   -12.27351
Avg. Drawdown [%]                   -3.700359
Max. Drawdown Duration       74 days 00:00:00
Avg. Drawdown Duration       16 days 00:00:00
# Trades                                    8
Win Rate [%]                             87.5
Best Trade [%]                       23.59091
Worst Trade [%]                    -16.804455
Avg. Trade [%]                       4.058713
Max. Trade Duration          54 days 00:00:00
Avg. Trade Duration          20 days 00:00:00
Profit Factor                        3.184311
Expectancy [%]                       4.588269
SQN                                  1.175232
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
```

### Top 10 configurations

|     |   band_length |   band_mult |   band_low_pct |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|----:|--------------:|------------:|---------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 114 |             3 |           1 |        2.06555 |                               1.003 |          2 |         1000 |              0 |                  6 |      36.3753 |
| 222 |             3 |           2 |        2.06555 |                               1.003 |          2 |          500 |              0 |                  4 |      34.727  |
|  93 |             3 |           1 |        2.06555 |                               1.003 |          2 |          500 |              0 |                  7 |      34.6732 |
| 115 |             3 |           1 |        2.06555 |                               1.003 |          2 |         1000 |              0 |                  7 |      34.3221 |
| 221 |             3 |           2 |        2.06555 |                               1.003 |          2 |          500 |              0 |                  3 |      34.191  |
| 354 |             5 |           1 |        2.06555 |                               1.003 |          2 |          500 |              0 |                  4 |      33.0356 |
|  92 |             3 |           1 |        2.06555 |                               1.003 |          2 |          500 |              0 |                  6 |      32.8915 |
|  90 |             3 |           1 |        2.06555 |                               1.003 |          2 |          500 |              0 |                  4 |      32.6934 |
| 353 |             5 |           1 |        2.06555 |                               1.003 |          2 |          500 |              0 |                  3 |      32.6701 |
|  89 |             3 |           1 |        2.06555 |                               1.003 |          2 |          500 |              0 |                  3 |      32.271  |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)

