# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Up_and_down - BTC/USDT - Binance

- Experiment nickname: Up_and_down 
- Experiment timestamp: 2024-02-04_1939 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2019-11-01
- End date: 2022-01-23
- Timeframe: 1d
- Duration: 13.188374996185303s

## Optimized parameters

- band_length=34
- band_mult=2
- band_low_pct=3.0025190627892058
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=100
- buy_all_days=1
- lr_buy_longitude=10

## Results

- Return: **965.4840942441458%** over **292.6135311175407%** on buy and hold.
- Initial investment: 1000.0
- Final result: 10654.840942441459

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2019-11-01 00:00:00
End                       2022-01-23 00:00:00
Duration                    814 days 00:00:00
Exposure Time [%]                   94.110429
Equity Final [$]                 10654.840942
Equity Peak [$]                  13022.310489
Return [%]                         965.484094
Buy & Hold Return [%]              292.613531
Return (Ann.) [%]                  188.529184
Volatility (Ann.) [%]              156.671729
Sharpe Ratio                         1.203339
Sortino Ratio                        6.352132
Calmar Ratio                         7.490379
Max. Drawdown [%]                  -25.169512
Avg. Drawdown [%]                   -5.833637
Max. Drawdown Duration      146 days 00:00:00
Avg. Drawdown Duration       16 days 00:00:00
# Trades                                  185
Win Rate [%]                        78.918919
Best Trade [%]                      445.33703
Worst Trade [%]                    -48.114094
Avg. Trade [%]                      23.451009
Max. Trade Duration         280 days 00:00:00
Avg. Trade Duration          91 days 00:00:00
Profit Factor                         7.53917
Expectancy [%]                      52.666248
SQN                                   5.48119
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                         Size  Entr...
dtype: object
```

### Top 10 configurations

|      |   band_length |   band_mult |   band_low_pct |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|-----:|--------------:|------------:|---------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 1757 |            34 |           2 |        3.00252 |                               1.003 |          2 |          100 |              1 |                 10 |      965.484 |
| 1749 |            34 |           2 |        3.00252 |                               1.003 |          2 |          100 |              1 |                  2 |      958.571 |
| 1759 |            34 |           2 |        3.00252 |                               1.003 |          2 |          100 |              1 |                 12 |      954.594 |
| 1758 |            34 |           2 |        3.00252 |                               1.003 |          2 |          100 |              1 |                 11 |      953.122 |
| 1754 |            34 |           2 |        3.00252 |                               1.003 |          2 |          100 |              1 |                  7 |      945.571 |
| 1753 |            34 |           2 |        3.00252 |                               1.003 |          2 |          100 |              1 |                  6 |      940.126 |
| 1750 |            34 |           2 |        3.00252 |                               1.003 |          2 |          100 |              1 |                  3 |      936.27  |
| 1752 |            34 |           2 |        3.00252 |                               1.003 |          2 |          100 |              1 |                  5 |      932.841 |
| 1751 |            34 |           2 |        3.00252 |                               1.003 |          2 |          100 |              1 |                  4 |      929.114 |
| 1756 |            34 |           2 |        3.00252 |                               1.003 |          2 |          100 |              1 |                  9 |      922.762 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)

