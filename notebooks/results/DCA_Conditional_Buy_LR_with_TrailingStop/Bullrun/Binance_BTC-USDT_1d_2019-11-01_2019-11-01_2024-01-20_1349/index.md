# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Bullrun - BTC/USDT - Binance

- Experiment nickname: Bullrun 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2019-11-01
- End date: 2024-01-20
- Timeframe: 1d

## Optimized parameters

- band_lenght=34
- band_mult=2
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=100
- buy_all_days=1
- lr_buy_longitude=5

## Results

- Return: **1313.138142605717%** over **349.68277472726857%** on buy and hold.
- Initial investment: 1600.0
- Final result: 22610.21028169147

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2019-11-01 00:00:00
End                       2024-01-20 00:00:00
Duration                   1541 days 00:00:00
Exposure Time [%]                   96.822309
Equity Final [$]                 22610.210282
Equity Peak [$]                  24651.072201
Return [%]                        1313.138143
Buy & Hold Return [%]              349.682775
Return (Ann.) [%]                   87.178134
Volatility (Ann.) [%]               84.899078
Sharpe Ratio                         1.026844
Sortino Ratio                        3.302576
Calmar Ratio                         1.905118
Max. Drawdown [%]                  -45.759968
Avg. Drawdown [%]                   -5.927963
Max. Drawdown Duration      715 days 00:00:00
Avg. Drawdown Duration       28 days 00:00:00
# Trades                                  527
Win Rate [%]                        86.148008
Best Trade [%]                     445.503453
Worst Trade [%]                    -38.368149
Avg. Trade [%]                      25.435662
Max. Trade Duration         826 days 00:00:00
Avg. Trade Duration         222 days 00:00:00
Profit Factor                       18.924385
Expectancy [%]                      40.233809
SQN                                  9.587696
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                         Size  Entr...
dtype: object
```

### Top 10 configurations

|     |   band_lenght |   band_mult |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|----:|--------------:|------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 758 |            34 |           2 |                               1.003 |          2 |          100 |              1 |                  5 |     1313.14  |
| 757 |            34 |           2 |                               1.003 |          2 |          100 |              1 |                  4 |     1304.07  |
| 755 |            34 |           2 |                               1.003 |          2 |          100 |              1 |                  2 |     1300.83  |
| 759 |            34 |           2 |                               1.003 |          2 |          100 |              1 |                  6 |     1273.19  |
| 756 |            34 |           2 |                               1.003 |          2 |          100 |              1 |                  3 |     1271.24  |
| 766 |            34 |           2 |                               1.003 |          2 |          200 |              1 |                  3 |     1021.54  |
| 790 |            34 |           2 |                               1.003 |          2 |         1600 |              0 |                  2 |      973.952 |
| 765 |            34 |           2 |                               1.003 |          2 |          200 |              1 |                  2 |      972.223 |
| 769 |            34 |           2 |                               1.003 |          2 |          200 |              1 |                  6 |      971.571 |
| 774 |            34 |           2 |                               1.003 |          2 |          500 |              0 |                  6 |      962.489 |

### Files

- full: [heatmap.md](heatmap.md), [heatmap.xlsx](heatmap.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)