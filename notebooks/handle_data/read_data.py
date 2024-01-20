import os
import pandas as pd

# simple cache
last_read_filename = ""
last_read_candles = None


def get_dir_file_names(symbol, timeframe, exchange_name):
    if timeframe == '1m':
        timeframe = '1min'
    directory = '../data/' + symbol.replace('/', '-') + '/' + timeframe
    filename = directory + '/' + symbol.replace('/', '-') + '_' + timeframe + '_' + exchange_name + '.pickle'
    return directory, filename


def load_candles(exchange_name, symbol, timeframe='1d', factor=1, start_date=None, end_date=None, path='../data/'):
    global last_read_filename
    global last_read_candles
    candles_slice = None

    # if end_date<start_date:
    #    print("Error invalid dates")
    #    return

    directory, filename = get_dir_file_names(symbol, timeframe, exchange_name)

    if filename != last_read_filename:
        print("reading", filename)
        last_read_filename = filename
        candles_from_disk = pd.read_pickle(filename)

        candles_from_disk['Open time'] = pd.to_datetime(candles_from_disk['Open time'], unit='ms')
        candles_from_disk = candles_from_disk.set_index('Open time')
        last_read_candles = candles_from_disk
    else:
        candles_from_disk = last_read_candles

    candles_slice = candles_from_disk[start_date:end_date].copy(deep=True)  # ensure candles_slice is a copy

    if factor != 1:
        candles_slice.Open /= factor
        candles_slice.High /= factor
        candles_slice.Low /= factor
        candles_slice.Close /= factor
        candles_slice.Volume *= factor

    return candles_slice
