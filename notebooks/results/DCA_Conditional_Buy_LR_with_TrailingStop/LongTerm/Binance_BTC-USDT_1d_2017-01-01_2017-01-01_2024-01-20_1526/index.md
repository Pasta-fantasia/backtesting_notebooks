# Class: DCA_Conditional_Buy_LR_with_TrailingStop - LongTerm - BTC/USDT - Binance

- Experiment nickname: LongTerm 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2017-01-01
- End date: 2024-01-20
- Timeframe: 1d

## Optimized parameters

- band_lenght=34
- band_mult=2
- minimal_benefit_to_start_trailing=1.003
- reinvest=2
- dca_budget=100
- buy_all_days=1
- lr_buy_longitude=2

## Results

- Return: **1426.2876041527215%** over **868.7791126420045%** on buy and hold.
- Initial investment: 1600.0
- Final result: 24420.601666443545

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2017-08-17 00:00:00
End                       2024-01-20 00:00:00
Duration                   2347 days 00:00:00
Exposure Time [%]                   98.296422
Equity Final [$]                 24420.601666
Equity Peak [$]                    26565.0719
Return [%]                        1426.287604
Buy & Hold Return [%]              868.779113
Return (Ann.) [%]                   52.755898
Volatility (Ann.) [%]               98.319095
Sharpe Ratio                         0.536578
Sortino Ratio                        1.329192
Calmar Ratio                         0.668116
Max. Drawdown [%]                  -78.962133
Avg. Drawdown [%]                   -8.138571
Max. Drawdown Duration     1055 days 00:00:00
Avg. Drawdown Duration       56 days 00:00:00
# Trades                                  555
Win Rate [%]                        83.243243
Best Trade [%]                     451.564727
Worst Trade [%]                    -38.368149
Avg. Trade [%]                      26.176131
Max. Trade Duration        1193 days 00:00:00
Avg. Trade Duration         277 days 00:00:00
Profit Factor                       19.707418
Expectancy [%]                      41.494654
SQN                                 10.089358
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                         Size  Entr...
dtype: object
```

### Top 10 configurations

|      |   band_lenght |   band_mult |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|-----:|--------------:|------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 1243 |            34 |           2 |                               1.003 |          2 |          100 |              1 |                  2 |      1426.29 |
| 1270 |            34 |           2 |                               1.003 |          2 |          200 |              1 |                  7 |      1405.88 |
| 1272 |            34 |           2 |                               1.003 |          2 |          200 |              1 |                  9 |      1390.63 |
| 1266 |            34 |           2 |                               1.003 |          2 |          200 |              1 |                  3 |      1367.22 |
| 1269 |            34 |           2 |                               1.003 |          2 |          200 |              1 |                  6 |      1360.83 |
| 1247 |            34 |           2 |                               1.003 |          2 |          100 |              1 |                  6 |      1356.98 |
| 1267 |            34 |           2 |                               1.003 |          2 |          200 |              1 |                  4 |      1354.84 |
| 1273 |            34 |           2 |                               1.003 |          2 |          200 |              1 |                 10 |      1350.47 |
| 1276 |            34 |           2 |                               1.003 |          2 |          500 |              0 |                  2 |      1344.01 |
| 1294 |            34 |           2 |                               1.003 |          2 |          500 |              1 |                  9 |      1343.38 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)