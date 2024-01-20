# Class: {{ str_strategy_name }} - {{ experiment_nickname }} - {{ symbol }} - {{ exchange }}

- Experiment nickname: {{ experiment_nickname }} 
- Symbol: {{ symbol }}
- Exchange: {{ exchange }}
- Start date: {{ start_date }}
- End date: {{ end_date }}
- Timeframe: {{ timeframe }}

## Optimized parameters
{% for parameter in parameters %}
- {{ parameter }}{% endfor %}

## Results

- Return: **{{ strat_return }}%** over **{{ buy_and_hold }}%** on buy and hold.
- Initial investment: {{ equity_init }}
- Final result: {{ equity_final }}

Interactive simulation graph: [bt_interactive_plot.html](bt_interactive_plot.html)

## Details 
### Backtesting stats:

```
{{ str_stats }}
```

### Top 10 configurations

{{ heatmap_md }}

### Files

- full: [heatmap.md](heatmap_df.md), [heatmap.xlsx](heatmap_df.xlsx) 
- trades: [trades.md](trades.md) [trades.xlsx](trades.xlsx)
- equity: [equity_curve.md](equity_curve.md) [equity_curve.xlsx](equity_curve.xlsx)
