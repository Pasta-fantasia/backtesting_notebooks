# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Up_and_down - BTC/USDT - Binance

- Experiment nickname: Up_and_down 
- Experiment timestamp: 2024-02-04_2021 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2019-11-01
- End date: 2022-01-23
- Timeframe: 1h
- Duration: 217.86875700950623s

## Optimized parameters

- band_length=21
- band_mult=2
- band_low_pct=0.5821211500777452
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=100
- buy_all_days=1
- lr_buy_longitude=5

## Results

- Return: **274.74413911463773%** over **297.1779142448869%** on buy and hold.
- Initial investment: 1000.0
- Final result: 3747.441391146377

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2019-11-01 00:00:00
End                       2022-01-23 23:00:00
Duration                    814 days 23:00:00
Exposure Time [%]                   99.554417
Equity Final [$]                  3747.441391
Equity Peak [$]                   7003.449364
Return [%]                         274.744139
Buy & Hold Return [%]              297.177914
Return (Ann.) [%]                   80.698095
Volatility (Ann.) [%]              149.261255
Sharpe Ratio                          0.54065
Sortino Ratio                        1.621809
Calmar Ratio                         1.372352
Max. Drawdown [%]                  -58.802751
Avg. Drawdown [%]                   -3.574427
Max. Drawdown Duration      188 days 10:00:00
Avg. Drawdown Duration        5 days 16:00:00
# Trades                                 1113
Win Rate [%]                        93.890386
Best Trade [%]                      21.542263
Worst Trade [%]                    -48.316551
Avg. Trade [%]                       1.344216
Max. Trade Duration         209 days 04:00:00
Avg. Trade Duration          23 days 22:00:00
Profit Factor                        1.894569
Expectancy [%]                       2.489245
SQN                                  6.396732
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                          Size  Ent...
dtype: object
```

### Top 10 configurations

|      |   band_length |   band_mult |   band_low_pct |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|-----:|--------------:|------------:|---------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 1488 |            21 |           2 |       0.582121 |                               1.003 |          2 |          100 |              1 |                  5 |      274.744 |
| 1465 |            21 |           2 |       0.582121 |                               1.003 |          2 |           50 |              1 |                  4 |      272.079 |
| 1489 |            21 |           2 |       0.582121 |                               1.003 |          2 |          100 |              1 |                  6 |      271.583 |
| 1490 |            21 |           2 |       0.582121 |                               1.003 |          2 |          100 |              1 |                  7 |      270.73  |
| 1463 |            21 |           2 |       0.582121 |                               1.003 |          2 |           50 |              1 |                  2 |      270.69  |
| 1487 |            21 |           2 |       0.582121 |                               1.003 |          2 |          100 |              1 |                  4 |      268.647 |
| 1622 |            34 |           1 |       0.582121 |                               1.003 |          2 |          100 |              1 |                  7 |      265.846 |
| 1620 |            34 |           1 |       0.582121 |                               1.003 |          2 |          100 |              1 |                  5 |      265.683 |
| 1469 |            21 |           2 |       0.582121 |                               1.003 |          2 |           50 |              1 |                  8 |      265.513 |
| 1464 |            21 |           2 |       0.582121 |                               1.003 |          2 |           50 |              1 |                  3 |      265.176 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)

