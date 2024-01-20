# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Up_and_down - BTC/USDT - Binance

- Experiment nickname: Up_and_down 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2019-11-01
- End date: 2022-01-23
- Timeframe: 1d

## Optimized parameters

- band_lenght=34
- band_mult=2
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=200
- buy_all_days=1
- lr_buy_longitude=7

## Results

- Return: **942.0295578414548%** over **292.6135311175407%** on buy and hold.
- Initial investment: 1600.0
- Final result: 16672.472925463277

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2019-11-01 00:00:00
End                       2022-01-23 00:00:00
Duration                    814 days 00:00:00
Exposure Time [%]                   94.601227
Equity Final [$]                 16672.472925
Equity Peak [$]                  21015.704423
Return [%]                         942.029558
Buy & Hold Return [%]              292.613531
Return (Ann.) [%]                  185.667205
Volatility (Ann.) [%]              163.872118
Sharpe Ratio                         1.133001
Sortino Ratio                        5.776911
Calmar Ratio                          6.26696
Max. Drawdown [%]                   -29.62636
Avg. Drawdown [%]                   -6.152195
Max. Drawdown Duration      129 days 00:00:00
Avg. Drawdown Duration       15 days 00:00:00
# Trades                                  170
Win Rate [%]                        78.823529
Best Trade [%]                      445.33703
Worst Trade [%]                    -48.114094
Avg. Trade [%]                      19.966363
Max. Trade Duration         280 days 00:00:00
Avg. Trade Duration          91 days 00:00:00
Profit Factor                        6.633184
Expectancy [%]                      44.735517
SQN                                  4.863153
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                         Size  Entr...
dtype: object
```

### Top 10 configurations

|      |   band_lenght |   band_mult |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|-----:|--------------:|------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 1270 |            34 |           2 |                               1.003 |          2 |          200 |              1 |                  7 |      942.03  |
| 1266 |            34 |           2 |                               1.003 |          2 |          200 |              1 |                  3 |      928.224 |
| 1243 |            34 |           2 |                               1.003 |          2 |          100 |              1 |                  2 |      927.986 |
| 1246 |            34 |           2 |                               1.003 |          2 |          100 |              1 |                  5 |      921.685 |
| 1245 |            34 |           2 |                               1.003 |          2 |          100 |              1 |                  4 |      917.887 |
| 1275 |            34 |           2 |                               1.003 |          2 |          200 |              1 |                 12 |      914.619 |
| 1273 |            34 |           2 |                               1.003 |          2 |          200 |              1 |                 10 |      914.174 |
| 1272 |            34 |           2 |                               1.003 |          2 |          200 |              1 |                  9 |      912.497 |
| 1274 |            34 |           2 |                               1.003 |          2 |          200 |              1 |                 11 |      902.752 |
| 1244 |            34 |           2 |                               1.003 |          2 |          100 |              1 |                  3 |      900.9   |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)