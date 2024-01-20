# Class: DCA_Conditional_Buy_LR_with_TrailingStop - Up_and_down - BTC/USDT - Binance

- Experiment nickname: Up_and_down 
- Symbol: BTC/USDT
- Exchange: Binance
- Start date: 2019-11-01
- End date: 2022-01-23
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

- Return: **752.6997816606998%** over **300.9587951506007%** on buy and hold.
- Initial investment: 1600.0
- Final result: 13643.196506571197

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
Start                     2019-11-04 00:00:00
End                       2022-01-17 00:00:00
Duration                    805 days 00:00:00
Exposure Time [%]                   81.034483
Equity Final [$]                 13643.196507
Equity Peak [$]                  18793.410208
Return [%]                         752.699782
Buy & Hold Return [%]              300.958795
Return (Ann.) [%]                10421.421001
Volatility (Ann.) [%]            20467.255577
Sharpe Ratio                         0.509175
Sortino Ratio                       154.35653
Calmar Ratio                       331.583358
Max. Drawdown [%]                  -31.429264
Avg. Drawdown [%]                  -11.060836
Max. Drawdown Duration      133 days 00:00:00
Avg. Drawdown Duration       38 days 00:00:00
# Trades                                   11
Win Rate [%]                        63.636364
Best Trade [%]                     603.004577
Worst Trade [%]                    -26.119474
Avg. Trade [%]                      33.014118
Max. Trade Duration         399 days 00:00:00
Avg. Trade Duration         148 days 00:00:00
Profit Factor                       14.682519
Expectancy [%]                      69.049267
SQN                                  1.280138
_strategy                 DCA_Conditional_...
_equity_curve                             ...
_trades                         Size  Entr...
dtype: object
```

### Top 10 configurations

|     |   band_lenght |   band_mult |   minimal_benefit_to_start_trailing |   reinvest |   dca_budget |   buy_all_days |   lr_buy_longitude |   Return [%] |
|----:|--------------:|------------:|------------------------------------:|-----------:|-------------:|---------------:|-------------------:|-------------:|
| 979 |            21 |           1 |                               1.003 |          2 |         1600 |              1 |                  2 |      752.7   |
| 980 |            21 |           1 |                               1.003 |          2 |         1600 |              1 |                  3 |      683.188 |
| 981 |            21 |           1 |                               1.003 |          2 |         1600 |              1 |                  4 |      640.202 |
| 982 |            21 |           1 |                               1.003 |          2 |         1600 |              1 |                  5 |      629.144 |
| 983 |            21 |           1 |                               1.003 |          2 |         1600 |              1 |                  6 |      611.893 |
| 429 |             9 |           2 |                               1.003 |          2 |         1600 |              1 |                  2 |      607.898 |
| 430 |             9 |           2 |                               1.003 |          2 |         1600 |              1 |                  3 |      597.482 |
| 433 |             9 |           2 |                               1.003 |          2 |         1600 |              1 |                  6 |      583.76  |
| 825 |            13 |           2 |                               1.003 |          2 |          200 |              1 |                  2 |      583.093 |
| 431 |             9 |           2 |                               1.003 |          2 |         1600 |              1 |                  4 |      580.056 |

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)