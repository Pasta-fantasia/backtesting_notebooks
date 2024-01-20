# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Up_and_down - BTC/USDT - Binance

- Experiment nickname: Up_and_down 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2019-11-01
- End date: 2022-01-23
- Timeframe: 1h

## Optimized parameters

- band_lenght=34
- band_mult=1
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=100
- buy_all_days=1
- lr_buy_longitude=7

## Results

- Return: **279.19010153141335%** over **297.1779142448869%** on buy and hold.
- Initial investment: 1600.0
- Final result: 6067.041624502614

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2019-11-01 00:00:00
End                       2022-01-23 23:00:00
Duration                    814 days 23:00:00
Exposure Time [%]                   99.605634
Equity Final [$]                  6067.041625
Equity Peak [$]                  10674.606431
Return [%]                         279.190102
Buy & Hold Return [%]              297.177914
Return (Ann.) [%]                   81.653053
Volatility (Ann.) [%]              148.389418
Sharpe Ratio                         0.550262
Sortino Ratio                        1.645697
Calmar Ratio                         1.360532
Max. Drawdown [%]                  -60.015527
Avg. Drawdown [%]                   -3.481006
Max. Drawdown Duration      184 days 10:00:00
Avg. Drawdown Duration        5 days 20:00:00
# Trades                                 1956
Win Rate [%]                        94.580777
Best Trade [%]                      19.829327
Worst Trade [%]                    -48.316551
Avg. Trade [%]                        1.41094
Max. Trade Duration         190 days 16:00:00
Avg. Trade Duration          19 days 21:00:00
Profit Factor                        1.992787
Expectancy [%]                       2.303722
SQN                                  8.780164
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                          Size  Ent...
dtype: object
```

### Top 10 configurations

|      |   band_lenght |   band_mult |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|-----:|--------------:|------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 1138 |            34 |           1 |                               1.003 |          2 |          100 |              1 |                  7 |      279.19  |
| 1025 |            21 |           2 |                               1.003 |          2 |          100 |              1 |                  4 |      277.826 |
| 1135 |            34 |           1 |                               1.003 |          2 |          100 |              1 |                  4 |      276.568 |
| 1136 |            34 |           1 |                               1.003 |          2 |          100 |              1 |                  5 |      276.109 |
| 1026 |            21 |           2 |                               1.003 |          2 |          100 |              1 |                  5 |      275.56  |
| 1028 |            21 |           2 |                               1.003 |          2 |          100 |              1 |                  7 |      275.485 |
| 1027 |            21 |           2 |                               1.003 |          2 |          100 |              1 |                  6 |      274.676 |
| 1050 |            21 |           2 |                               1.003 |          2 |          200 |              1 |                  7 |      274.192 |
| 1137 |            34 |           1 |                               1.003 |          2 |          100 |              1 |                  6 |      273.027 |
| 1048 |            21 |           2 |                               1.003 |          2 |          200 |              1 |                  5 |      272.245 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)