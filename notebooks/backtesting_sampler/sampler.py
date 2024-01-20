import time
import os

from datetime import date
from datetime import timedelta
from datetime import datetime

import pickle

import json

import pandas as pd
import random

from handle_data.read_data import load_candles

from backtesting import Backtest


def process_heatmap(heatmap,take_slice=0):
    hm = heatmap.reset_index()
    target_opt = hm.columns[-1]
    if take_slice>0:
        opt_slice_rows = int(hm.shape[0]/10)
        hm_opt_slice = hm.sort_values(target_opt, ascending=False)[:opt_slice_rows]
        return hm_opt_slice
    else:
        return hm.sort_values(target_opt, ascending=False)


def opt_asset_factor(stats):
    trades = stats._trades
    if len(trades)>0:
        last_trade = trades["ExitTime"].max()
        final_holding = trades[trades["ExitTime"] == last_trade]["Size"].sum()
        final_open = trades[trades["ExitTime"] == last_trade]["Size"].count()
        return final_holding / ( trades['Size'][0] * final_open )
    else:
        return 1

class MultiSampleSimulator:
    def __init__(self, p_class_to_simulate, p_optimization_function,
                 sim_symbol='BTC/USDT', asset_factor=1_000_000, exchange='Binance',
                 p_sim_start_date="2020-01-01",
                 p_history_days_simulate=0, p_sim_end_date=None, base_days=5, time_frame='1h'):

        # configure simulation
        self.sim_samples_results = None
        self.time_run_simulation_samples = None
        self.full_cycle_samples = None

        self.df_sim_strategies_ranking = None
        self.df_sim_samples_results = None
        self.df_final_sim_results = None

        self.class_to_simulate = p_class_to_simulate
        self.optimization_function = p_optimization_function

        # Start ----------
        if p_history_days_simulate > 0:
            self.sim_start_date = (date.today() - timedelta(days=p_history_days_simulate))
        else:
            self.sim_start_date = datetime.strptime(p_sim_start_date, '%Y-%m-%d')

            # Jump ----------
        self.sim_window_days = base_days * 3  # 1 base of data, 2 of min optimization
        self.sim_window_plus_rnd_day = base_days * 3

        self.sim_jump_min_days = base_days
        self.sim_jump_plus_rnd_days = base_days * 2

        # End ----------
        if p_sim_end_date is None:
            #self.sim_end_date = date.today() - timedelta(days=(self.sim_window_days + self.sim_window_plus_rnd_day))
            self.sim_end_date = date.today() 
        else:
            self.sim_end_date = datetime.strptime(p_sim_end_date, '%Y-%m-%d')

        self.time_frame = time_frame

        # optimization targets, not a parameter by now
        #self.optimization_targets = [opt_asset_factor]  # ,opt_asset_factor]: # ["Return [%]", "Win Rate [%]", "SQN"]:
        #self.optimization_targets = [opt_asset_factor,"Equity Final [$]"]  # ,opt_asset_factor]: # ["Return [%]", "Win Rate [%]", "SQN"]:
        self.optimization_targets = ["Equity Final [$]"]  # ,opt_asset_factor]: # ["Return [%]", "Win Rate [%]", "SQN"]:
        
        # a single symbol on v1
        self.sim_symbol = sim_symbol
        # make sure the asset is a fraction of 1
        self.asset_factor = asset_factor
        self.exchange = exchange

        self.file_name_instance_id = self.class_to_simulate.__name__ + '_' + datetime.now().strftime('%Y-%m-%d_%H%M')
        


    def run_simulation_samples(self, fast_test_samples=0, full_cycle_samples=1):
        start_time = time.time()
        sim_results = []

        self.full_cycle_samples = full_cycle_samples

        for sample in range(full_cycle_samples):
            print(f"Sample: {sample + 1} of {full_cycle_samples}.")
            i = 0
            sim_start_date = self.sim_start_date

            while sim_start_date.strftime('%Y-%m-%d') <= self.sim_end_date.strftime('%Y-%m-%d'):
                start_date = sim_start_date.strftime('%Y-%m-%d')
                windows_plus_days = int(self.sim_window_plus_rnd_day * random.random())
                end_date = (sim_start_date + timedelta(days=(self.sim_window_days + windows_plus_days))).strftime(
                    '%Y-%m-%d')

                print(start_date,end_date)
                time_frame = load_candles(self.exchange, self.sim_symbol, timeframe=self.time_frame, factor=self.asset_factor,
                                          start_date=start_date, end_date=end_date)

                # for each strategy to test and/or symbol
                for optimize_target in self.optimization_targets:
                    try:
                        results, heatmap = self.optimization_function(time_frame, optimize_target)
                        results["symbol"] = self.sim_symbol
                        results["optimize_target"] = optimize_target
                        sim_results.append(results)
                        hm_opt_slice = self.process_heatmap(heatmap)
                        # TODO for hm_opt_slice run simulation and add to sim_results... maybe the first is already in
                    except Exception as err:
                        print(f"time frame error {self.sim_symbol}, start_date={start_date}, end_date={end_date}")
                        print(f"Unexpected {err=}, {type(err)=}")

                jump_plus_days = int(self.sim_jump_plus_rnd_days * random.random())
                sim_start_date = sim_start_date + timedelta(days=(self.sim_jump_min_days + jump_plus_days))
                i = i + 1
                if fast_test_samples and i >= fast_test_samples:  # number of test samples for testing. 0 = all possible samples.
                    print("end of samples")
                    break

            # pickle_file_name = self.sim_symbol + "_" + self.file_name_instance_id  + ".pickle"
            # with open(pickle_file_name, 'wb') as f:
            #    pickle.dump(sim_results, f)

        self.time_run_simulation_samples = time.time() - start_time
        self.sim_samples_results = sim_results

        return

    @staticmethod
    def __df_from_sim_result(sim_results):
        win = 0
        loss = 0

        asset_win = 0
        asset_loss = 0

        df_sim_results = pd.DataFrame()

        for sim_result in sim_results:

            if sim_result["# Trades"] > 0:
                trades = sim_result._trades
                asset_result = trades['Size'][len(trades['Size']) - 1] / trades['Size'][0]
                if (sim_result["Return [%]"] - sim_result["Buy & Hold Return [%]"]) > 0:
                    win = win + 1
                else:
                    loss = loss + 1

                if asset_result > 1:
                    asset_win = asset_win + 1
                else:
                    asset_loss = asset_loss + 1
            else:
                asset_result = 1
                

            # Using pandas.concat() to append a row
            new_row = pd.DataFrame({'Symbol': sim_result["symbol"],
                                    'Optimize Target': sim_result["optimize_target"],
                                    '_strategy': str(sim_result._strategy),
                                    'Start': sim_result["Start"],
                                    'End': sim_result["End"],
                                    'Duration': sim_result["Duration"],
                                    'Exposure Time [%]': sim_result["Exposure Time [%]"],
                                    'Equity Final [$]': sim_result["Equity Final [$]"],
                                    '# Trades': sim_result["# Trades"],
                                    'SQN': sim_result["SQN"],
                                    "Win Rate [%]": sim_result["Win Rate [%]"],
                                    "Return [%]": sim_result["Return [%]"],
                                    "Return (Ann.) [%]:": sim_result["Return (Ann.) [%]"],
                                    "Sharpe Ratio": sim_result["Sharpe Ratio"],
                                    "Sortino Ratio": sim_result["Sortino Ratio"],
                                    "Buy & Hold Return [%]": sim_result["Buy & Hold Return [%]"],
                                    "Return - Hold": sim_result["Return [%]"] - sim_result["Buy & Hold Return [%]"],
                                    "asset_result": asset_result},
                                   index=[0])
            df_sim_results = pd.concat([new_row, df_sim_results.loc[:]]).reset_index(drop=True)

        # print("Normal $:", win,loss)
        # print("Asset:", asset_win, asset_loss)

        # pickle_file_name = self.sim_symbol + "_" + self.file_name_instance_id  + "_df.pickle"
        # with open(pickle_file_name, 'wb') as f:
        #    pickle.dump(df_sim_results, f)
        return df_sim_results

    def __df_add_base_ranking(self, df_sim_results, ranking_slots=None):
        def is_good(Retrun, Retund_Hold):
            if Retund_Hold>0:
                return 2
            else:
                if Retrun>0:
                    return 1
            return -1
        
        if ranking_slots is None:
            ranking_slots = 10 * self.full_cycle_samples * len(self.optimization_targets)
        print("ranking_slots:", ranking_slots)
        
        #df_sim_results['is_good'] = df_sim_results["Return - Hold"].apply(lambda x: 1 if x >= 0 else -1)
        #df_sim_results['is_good'] = df_sim_results["asset_result"].apply(lambda x: 1 if x > 1 else -1)
        #df_sim_results['is_good'] = df_sim_results["Return [%]"].apply(lambda x: 1 if x >= 0 else -1)
        df_sim_results['is_good'] = df_sim_results.apply(lambda x: is_good(x["Return [%]"],x["Return - Hold"]), axis=1)

        df_sim_results["ranking_eqf"] = 0
        index = df_sim_results[df_sim_results["is_good"] > 0].sort_values("Equity Final [$]", ascending=False)[
                0:ranking_slots].index
        df_sim_results.loc[index, 'ranking_eqf'] = 1

        df_sim_results["ranking_wr"] = 0
        index = df_sim_results[df_sim_results["is_good"] > 0].sort_values("Win Rate [%]", ascending=False)[
                0:ranking_slots].index
        df_sim_results.loc[index, 'ranking_wr'] = 1

        df_sim_results["ranking_rh"] = 0
        index = df_sim_results[df_sim_results["is_good"] > 0].sort_values("Return - Hold", ascending=False)[
                0:ranking_slots].index
        df_sim_results.loc[index, 'ranking_rh'] = 1

        df_sim_results["ranking_ass"] = 0
        index = df_sim_results[df_sim_results["is_good"] > 0].sort_values("asset_result", ascending=False)[
                0:ranking_slots].index
        df_sim_results.loc[index, 'ranking_ass'] = 1

        df_sim_results["ranking_from_samples"] = df_sim_results["ranking_eqf"] + df_sim_results["ranking_wr"] + \
                                                 df_sim_results["ranking_rh"] + df_sim_results["ranking_ass"]

        return df_sim_results

    @staticmethod
    def __df_sim_ranking(df_sim_results):
        def ret_mult(Return, Retund_Hold):
            return Retund_Hold if Retund_Hold > Return else Return
        
        #df_sim_results_stats
        df_sim_results_by_is_good = df_sim_results.groupby('is_good', as_index=False)['_strategy'].value_counts()
        df_sim_results_by_is_good['is_good_count'] = df_sim_results_by_is_good[df_sim_results_by_is_good["is_good"] > 0]["count"]
        df_sim_results_by_is_good['is_bad_count'] = df_sim_results_by_is_good[df_sim_results_by_is_good["is_good"] <= 0]["count"]
        
        # how many time this confguration was better than doing nothing?
        df_sim_results_by_is_good['strategies_samples_success_ranking'] = df_sim_results_by_is_good['count'] * df_sim_results_by_is_good['is_good']
        
        df_sim_results_stats_sum = df_sim_results_by_is_good.groupby('_strategy', as_index=False).agg(
                        {'strategies_samples_success_ranking':'sum', 
                         'is_good_count': 'sum', 
                         'is_bad_count': 'sum'})
        
        # how many time this confguration was choosed?
        df_sim_results_stats_sum['samples_count'] = df_sim_results_stats_sum['is_good_count'] + df_sim_results_stats_sum['is_bad_count']
        df_sim_results_stats_sum['efficiency'] = df_sim_results_stats_sum['is_good_count'] / df_sim_results_stats_sum['samples_count']
        df_sim_results_stats_sum['samples_count_represetativity'] = df_sim_results_stats_sum['samples_count'] / df_sim_results_stats_sum['samples_count'].sum()

        
        df_sim_results_by_strategy = df_sim_results.groupby('_strategy', as_index=False).agg(
                            Avg_Return=('Return [%]','mean') ,
                            Avg_Return_Hold=('Return - Hold','mean') , 
                            Avg_Equity_Final=('Equity Final [$]', 'mean'), 
                            Avg_Trades=('# Trades', 'mean'))
        
        df_sim_results_stats_sum = df_sim_results_stats_sum.merge(df_sim_results_by_strategy, on=['_strategy'])
        
        # df_sim_results_ranking_stats
        df_sim_results_ranking_stats = df_sim_results.groupby('ranking_from_samples', as_index=False)['_strategy'].value_counts()
        df_sim_results_ranking_stats['strategies_ranking'] = df_sim_results_ranking_stats['count'] * df_sim_results_ranking_stats['ranking_from_samples']
        df_sim_results_ranking_stats = df_sim_results_ranking_stats.groupby('_strategy', as_index=False)['strategies_ranking'].sum()
    

        # df_sim_ranking
        df_sim_ranking = df_sim_results_ranking_stats.merge(df_sim_results_stats_sum, on=['_strategy'])
        df_sim_ranking['Return_mult'] = df_sim_ranking.apply(lambda x: ret_mult(x["Avg_Return"],x["Avg_Return_Hold"]), axis=1)
        df_sim_ranking['ranking'] =  (df_sim_ranking['strategies_ranking'] + df_sim_ranking['strategies_samples_success_ranking']) * df_sim_ranking['efficiency'] * df_sim_ranking['Return_mult'] * df_sim_ranking['samples_count_represetativity']

        return df_sim_ranking

    def generate_ranking(self):
        self.df_sim_samples_results = self.__df_from_sim_result(self.sim_samples_results)
        self.df_sim_samples_results = self.__df_add_base_ranking(self.df_sim_samples_results)
        self.df_sim_strategies_ranking = self.__df_sim_ranking(self.df_sim_samples_results)

    def evaluate_ranked_strategies_on_period(self, start_date="2022-01-11", end_date=None, p_cash=1_000,
                                             run_period_optimization=True, p_minimal_samples_count=None):
        final_sim_results = []

        # improve using "symbol+_strategy" as primary key
        # maybe loop by simbols and filter byt it
        time_frame = load_candles(self.exchange, self.sim_symbol, timeframe=self.time_frame, factor=self.asset_factor,
                                          start_date=start_date, end_date=end_date)

        if p_minimal_samples_count is None:
            minimal_samples_count = self.full_cycle_samples  # * 2
        else:
            minimal_samples_count = p_minimal_samples_count    
        print("minimal_samples_count:", minimal_samples_count)
        
        for row in self.df_sim_strategies_ranking[self.df_sim_strategies_ranking["samples_count"] >= minimal_samples_count][
            '_strategy'].unique():
            print(row)
            strategy_class = row[:row.find("(")]
            strategy_parameters = row[row.find("(") + 1:-1]

            try:
                bt = Backtest(time_frame, self.class_to_simulate, cash=p_cash, commission=.002)
                results = eval("bt.run(" + strategy_parameters + ")")
                results["symbol"] = self.sim_symbol
                results["optimize_target"] = "final simulation"
                final_sim_results.append(results)
            except Exception as err:
                print(f"time frame error {self.sim_symbol}, start_date={start_date}, end_date={end_date}")
                print(f"Unexpected {err=}, {type(err)=}")
                excel_file_name = self.sim_symbol + "_" + self.file_name_instance_id + "_error.xlsx"
                with pd.ExcelWriter(excel_file_name, engine='xlsxwriter') as writer:
                    time_frame.to_excel(writer, index=True)

        if run_period_optimization:
            # optimize for the full time_frame

            for optimize_target in self.optimization_targets:
                results = self.optimization_function(time_frame, optimize_target)
                results["symbol"] = self.sim_symbol
                results["optimize_target"] = optimize_target
                final_sim_results.append(results)

        if len(final_sim_results) > 0:
            df_final_sim_results = self.__df_from_sim_result(final_sim_results)
            df_final_sim_results = self.__df_add_base_ranking(df_final_sim_results, 3)

            df_final_sim_results = df_final_sim_results.merge(self.df_sim_strategies_ranking, on=['_strategy'])
            self.df_final_sim_results = df_final_sim_results
        else:
            self.df_final_sim_results = pd.DataFrame()

    def save_excels(self):
        directory = "xlxs/"
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        excel_file_name = directory + self.sim_symbol.replace('/','-') + "_" + self.file_name_instance_id + "_01_samples.xlsx"    
        with pd.ExcelWriter(excel_file_name, engine='xlsxwriter') as writer:
            self.df_sim_samples_results.to_excel(writer, index=False)

        excel_file_name = directory + self.sim_symbol.replace('/','-') + "_" + self.file_name_instance_id + "_02_strategies_ranking.xlsx"
        with pd.ExcelWriter(excel_file_name, engine='xlsxwriter') as writer:
            self.df_sim_strategies_ranking.to_excel(writer, index=False)

        excel_file_name = directory + self.sim_symbol.replace('/','-') + "_" + self.file_name_instance_id + "_03_final.xlsx"

        with pd.ExcelWriter(excel_file_name, engine='xlsxwriter') as writer:
            self.df_final_sim_results.to_excel(writer, index=False)
