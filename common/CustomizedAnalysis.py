# Awesome Oscillator
def ao_call(row):
    if row['ao_shift'] < 0 and row['ao'] > 0: 
        return 1 
    elif row['ao_shift'] > 0 and row['ao'] < 0: 
        return -1 
    else: 
        return 0
def ao_signal_call(row):
    if row['ao_ao_signal_diff_shift'] < 0 and row['ao_ao_signal_diff'] > 0: 
        return 1 
    elif row['ao_ao_signal_diff_shift'] > 0 and row['ao_ao_signal_diff'] < 0: 
        return -1 
    else: 
        return 0
    
# KAMA (Kaufman’s Adaptive Moving Average)
def kama_call(row):
    if row['kama_close_kama_diff_shift'] < 0 and row['kama_close_kama_diff'] > 0: 
        return 1 
    elif row['kama_close_kama_diff_shift'] > 0 and row['kama_close_kama_diff'] < 0: 
        return -1 
    else: 
        return 0
def kama_ema_call(row):
    if row['kama_kama_ema_diff_shift'] < 0 and row['kama_kama_ema_diff'] > 0: 
        return 1 
    elif row['kama_kama_ema_diff_shift'] > 0 and row['kama_kama_ema_diff'] < 0: 
        return -1 
    else: 
        return 0
def kama_signal_call(row):
    if row['kama_kama_signal_diff_shift'] < 0 and row['kama_kama_signal_diff'] > 0: 
        return 1 
    elif row['kama_kama_signal_diff_shift'] > 0 and row['kama_kama_signal_diff'] < 0: 
        return -1 
    else: 
        return 0
    
# PPO (Percentage Price Oscillator)
def ppo_signal_call(row):
    if row['ppo_hist_shift'] < 0 and row['ppo_hist'] > 0: 
        return 1 
    elif row['ppo_hist_shift'] > 0 and row['ppo_hist'] < 0: 
        return -1 
    else: 
        return 0

# PVO (Percentage Volume Oscillator)
def pvo_signal_call(row):
    if row['pvo_hist_shift'] < 0 and row['pvo_hist'] > 0: 
        return 1 
    elif row['pvo_hist_shift'] > 0 and row['pvo_hist'] < 0: 
        return -1 
    else: 
        return 0
    
# RSI (Relative Strength Index)
def rsi_indicator(row):
    if row['rsi_shift'] < 30 and row['rsi'] > 30: 
        return 1 
    elif row['rsi_shift'] > 70 and row['rsi'] < 70: 
        return -1 
    else: 
        return 0
    
# Stochastic RSI Oscillator
def stochrsi_call(row):
    if row['stochrsi_fast_k_shift'] < 0.2 and row['stochrsi_fast_k'] > 0.2: 
        return 1 
    elif row['stochrsi_fast_k_shift'] > 0.2 and row['stochrsi_fast_k'] < 0.2: 
        return -1 
    elif row['stochrsi_fast_k_shift'] < 0.8 and row['stochrsi_fast_k'] > 0.8: 
        return 1 
    elif row['stochrsi_fast_k_shift'] > 0.8 and row['stochrsi_fast_k'] < 0.8: 
        return -1 
    else: 
        return 0
def stochrsi_fast_d_call(row):
    if row['stochrsi_fast_d_diff_shift'] < 0 and row['stochrsi_fast_d_diff'] > 0: 
        return 1 
    elif row['stochrsi_fast_d_diff_shift'] > 0 and row['stochrsi_fast_d_diff'] < 0: 
        return -1 
    else: 
        return 0
    
# Stochastic Oscillator
def stoch_call(row):
    if row['stoch_k_shift'] < 20 and row['stoch_k'] > 20: 
        return 1 
    elif row['stoch_k_shift'] > 20 and row['stoch_k'] < 20: 
        return -1 
    elif row['stoch_k_shift'] < 80 and row['stoch_k'] > 80: 
        return 1 
    elif row['stoch_k_shift'] > 80 and row['stoch_k'] < 80: 
        return -1 
    else: 
        return 0
def stoch_k_d_call(row):
    if row['stoch_k_d_diff_shift'] < 0 and row['stoch_k_d_diff'] > 0: 
        return 1 
    elif row['stoch_k_d_diff_shift'] > 0 and row['stoch_k_d_diff'] < 0: 
        return -1 
    else: 
        return 0
    
# TSI (True Strength Index)
def tsi_call(row):
    if row['tsi_shift'] < 0 and row['tsi'] > 0: 
        return 1 
    elif row['tsi_shift'] > 0 and row['tsi'] < 0: 
        return -1 
    else: 
        return 0
def tsi_signal_call(row):
    if row['tsi_tsi_signal_diff_shift'] < 0 and row['tsi_tsi_signal_diff'] > 0: 
        return 1 
    elif row['tsi_tsi_signal_diff_shift'] > 0 and row['tsi_tsi_signal_diff'] < 0: 
        return -1 
    else: 
        return 0

# Ultimate Oscillator
def uo_call(row):
    if row['uo_shift'] < 30 and row['uo'] > 30:
        return 1 
    elif row['uo_shift'] > 30 and row['uo'] < 30: 
        return -1 
    elif row['uo_shift'] < 70 and row['uo'] > 70:
        return 1 
    elif row['uo_shift'] > 70 and row['uo'] < 70: 
        return -1 
    else: 
        return 0
def uo_signal_call(row):
    if row['uo_uo_signal_diff_shift'] < 0 and row['uo_uo_signal_diff'] > 0: 
        return 1 
    elif row['uo_uo_signal_diff_shift'] > 0 and row['uo_uo_signal_diff'] < 0: 
        return -1 
    else: 
        return 0

# Williams %R
def williams_r_call(row):
    if row['williams_r_shift'] < -80 and row['williams_r'] > -80:
        return 1 
    elif row['williams_r_shift'] > -80 and row['williams_r'] < -80: 
        return -1 
    elif row['williams_r_shift'] < -20 and row['williams_r'] > -20:
        return 1 
    elif row['williams_r_shift'] > -20 and row['williams_r'] < -20: 
        return -1 
    else: 
        return 0
def williams_r_signal_call(row):
    if row['williams_r_r_signal_diff_shift'] < 0 and row['williams_r_r_signal_diff'] > 0: 
        return 1 
    elif row['williams_r_r_signal_diff_shift'] > 0 and row['williams_r_r_signal_diff'] < 0: 
        return -1 
    else: 
        return 0
    
# ADI (Accumulation/Distribution Index)
def adi_signal_call(row):
    if row['adi_adi_signal_diff_shift'] < 0 and row['adi_adi_signal_diff'] > 0: 
        return 1 
    elif row['adi_adi_signal_diff_shift'] > 0 and row['adi_adi_signal_diff'] < 0: 
        return -1 
    else: 
        return 0
    
# CMF (Chaikin Money Flow)
def cmf_call(row):
    if row['cmf_shift'] < 0 and row['cmf'] > 0: 
        return 1 
    elif row['cmf_shift'] > 0 and row['cmf'] < 0: 
        return -1 
    else: 
        return 0
def cmf_signal_call(row):
    if row['cmf_cmf_signal_diff_shift'] < 0 and row['cmf_cmf_signal_diff'] > 0: 
        return 1 
    elif row['cmf_cmf_signal_diff_shift'] > 0 and row['cmf_cmf_signal_diff'] < 0: 
        return -1 
    else: 
        return 0
    
# EoM, EMV (Ease of movement)
def eom_sma_indicator(row):
    if row['eom_sma_shift'] < 0 and row['eom_sma'] > 0: 
        return 1 
    elif row['eom_sma_shift'] > 0 and row['eom_sma'] < 0: 
        return -1 
    else: 
        return 0
    
# FI (Force Index)
def fi_signal_call(row):
    if row['fi_fi_signal_diff_shift'] < 0 and row['fi_fi_signal_diff'] > 0: 
        return 1 
    elif row['fi_fi_signal_diff_shift'] > 0 and row['fi_fi_signal_diff'] < 0: 
        return -1 
    else: 
        return 0
    
# MFI (Money Flow Index)
def mfi_call(row):
    if row['mfi_shift'] < 20 and row['mfi'] > 20: 
        return 1 
    elif row['mfi_shift'] > 20 and row['mfi'] < 20: 
        return -1 
    elif row['mfi_shift'] < 80 and row['mfi'] > 80: 
        return 1 
    elif row['mfi_shift'] > 80 and row['mfi'] < 80: 
        return -1 
    else: 
        return 0
def mfi_signal_call(row):
    if row['mfi_mfi_signal_diff_shift'] < 0 and row['mfi_mfi_signal_diff'] > 0: 
        return 1 
    elif row['mfi_mfi_signal_diff_shift'] > 0 and row['mfi_mfi_signal_diff'] < 0: 
        return -1 
    else: 
        return 0

    
# NVI (Negative Volume Index)
def nvi_short_long_call(row):
    if row['nvi_short_long_diff_shift'] < 0 and row['nvi_short_long_diff'] > 0: 
        return 1 
    elif row['nvi_short_long_diff_shift'] > 0 and row['nvi_short_long_diff'] < 0: 
        return -1 
    else: 
        return 0

# OBV (On-Balance Volume)
def obv_signal_call(row):
    if row['obv_obv_signal_diff_shift'] < 0 and row['obv_obv_signal_diff'] > 0: 
        return 1 
    elif row['obv_obv_signal_diff_shift'] > 0 and row['obv_obv_signal_diff'] < 0: 
        return -1 
    else: 
        return 0
    
# VPT (Volume-price trend)
def vpt_signal_call(row):
    if row['vpt_vpt_signal_diff_shift'] < 0 and row['vpt_vpt_signal_diff'] > 0: 
        return 1 
    elif row['vpt_vpt_signal_diff_shift'] > 0 and row['vpt_vpt_signal_diff'] < 0: 
        return -1 
    else: 
        return 0
    
# VWAP (Volume Weighted Average Price)
def vwap_call(row):
    if row['vwap_close_vwap_diff_shift'] < 0 and row['vwap_close_vwap_diff'] > 0: 
        return 1 
    elif row['vwap_close_vwap_diff_shift'] > 0 and row['vwap_close_vwap_diff'] < 0: 
        return -1 
    else: 
        return 0
def vwap_signal_call(row):
    if row['vwap_vwap_signal_diff_shift'] < 0 and row['vwap_vwap_signal_diff'] > 0: 
        return 1 
    elif row['vwap_vwap_signal_diff_shift'] > 0 and row['vwap_vwap_signal_diff'] < 0: 
        return -1 
    else: 
        return 0

# Bollinger Bands
def bollinger_pband_call(row):
    if row['bollinger_pband_shift'] < 0.2 and row['bollinger_pband'] > 0.2: 
        return 1 
    elif row['bollinger_pband_shift'] > 0.2 and row['bollinger_pband'] < 0.2: 
        return -1 
    elif row['bollinger_pband_shift'] < 0.8 and row['bollinger_pband'] > 0.8: 
        return 1 
    elif row['bollinger_pband_shift'] > 0.8 and row['bollinger_pband'] < 0.8: 
        return -1 
    else: 
        return 0
def bollinger_pband_signal_call(row):
    if row['bollinger_pband_signal_diff_shift'] < 0 and row['bollinger_pband_signal_diff'] > 0: 
        return 1 
    elif row['bollinger_pband_signal_diff_shift'] > 0 and row['bollinger_pband_signal_diff'] < 0: 
        return -1 
    else: 
        return 0
    
# Donchian Channels
def donchian_channel_pband_call(row):
    if row['donchian_channel_pband_shift'] < 0.2 and row['donchian_channel_pband'] > 0.2: 
        return 1 
    elif row['donchian_channel_pband_shift'] > 0.2 and row['donchian_channel_pband'] < 0.2: 
        return -1 
    elif row['donchian_channel_pband_shift'] < 0.8 and row['donchian_channel_pband'] > 0.8: 
        return 1 
    elif row['donchian_channel_pband_shift'] > 0.8 and row['donchian_channel_pband'] < 0.8: 
        return -1 
    else: 
        return 0
def donchian_channel_pband_signal_call(row):
    if row['donchian_channel_pband_signal_diff_shift'] < 0 and row['donchian_channel_pband_signal_diff'] > 0: 
        return 1 
    elif row['donchian_channel_pband_signal_diff_shift'] > 0 and row['donchian_channel_pband_signal_diff'] < 0: 
        return -1 
    else: 
        return 0

    
# Keltner Channel
def keltner_channel_pband_call(row):
    if row['keltner_channel_pband_shift'] < 0.2 and row['keltner_channel_pband'] > 0.2: 
        return 1 
    elif row['keltner_channel_pband_shift'] > 0.2 and row['keltner_channel_pband'] < 0.2: 
        return -1 
    elif row['keltner_channel_pband_shift'] < 0.8 and row['keltner_channel_pband'] > 0.8: 
        return 1 
    elif row['keltner_channel_pband_shift'] > 0.8 and row['keltner_channel_pband'] < 0.8: 
        return -1 
    else: 
        return 0
def keltner_channel_pband_signal_call(row):
    if row['keltner_channel_pband_signal_diff_shift'] < 0 and row['keltner_channel_pband_signal_diff'] > 0: 
        return 1 
    elif row['keltner_channel_pband_signal_diff_shift'] > 0 and row['keltner_channel_pband_signal_diff'] < 0: 
        return -1 
    else: 
        return 0


# ADX (Average Directional Movement Index)
def adx_pos_neg_call(row):
    if row['adx_pos_neg_diff_shift'] < 0 and row['adx_pos_neg_diff'] > 0: 
        return 1 
    elif row['adx_pos_neg_diff_shift'] > 0 and row['adx_pos_neg_diff'] < 0: 
        return -1 
    else: 
        return 0

# Aroon Indicator
def aroon_up_down_call(row):
    if row['aroon_up_down_diff_shift'] < 0 and row['aroon_up_down_diff'] > 0: 
        return 1 
    elif row['aroon_up_down_diff_shift'] > 0 and row['aroon_up_down_diff'] < 0: 
        return -1 
    else: 
        return 0

# CCI (Commodity Channel Index)
def cci_call(row):
    if row['cci_shift'] < -100 and row['cci'] > -100: 
        return 1 
    elif row['cci_shift'] > -100 and row['cci'] < -100: 
        return -1 
    elif row['cci_shift'] < 100 and row['cci'] > 100: 
        return 1 
    elif row['cci_shift'] > 100 and row['cci'] < 100: 
        return -1 
    else: 
        return 0
def cci_signal_call(row):
    if row['cci_cci_signal_diff_shift'] < 0 and row['cci_cci_signal_diff'] > 0: 
        return 1 
    elif row['cci_cci_signal_diff_shift'] > 0 and row['cci_cci_signal_diff'] < 0: 
        return -1 
    else: 
        return 0

# DPO (Detrended Price Oscillator)
def dpo_indicator(row):
    if row['dpo_shift'] < 0 and row['dpo'] > 0: 
        return 1 
    elif row['dpo_shift'] > 0 and row['dpo'] < 0: 
        return -1 
    else: 
        return 0
    
# 일목균형표 (Ichimoku Kinkō Hyō, Ichimoku)
def ichimoku_close_position(row):
    ichimoku_a = row['ichimoku_a']
    ichimoku_b = row['ichimoku_b']
    close = row['close']
    
    min_ichimoku = min(ichimoku_a, ichimoku_b)
    max_ichimoku = max(ichimoku_a, ichimoku_b)
    
    if close > max_ichimoku:
        return 1  # 구름 위에 있음
    elif close < min_ichimoku:
        return -1  # 구름 아래에 있음
    else:
        return 0  # 구름 안에 있음
def ichimoku_conversion_base_call(row):
    if row['ichimoku_conversion_base_diff_shift'] < 0 and row['ichimoku_conversion_base_diff'] > 0: 
        return 1 
    elif row['ichimoku_conversion_base_diff_shift'] > 0 and row['ichimoku_conversion_base_diff'] < 0: 
        return -1 
    else: 
        return 0
def ichimoku_a_b_call(row):
    if row['ichimoku_close_a_diff_shift'] < 0 and row['ichimoku_close_a_diff'] > 0: 
        return 1 
    elif row['ichimoku_close_a_diff_shift'] > 0 and row['ichimoku_close_a_diff'] < 0: 
        return -1 
    elif row['ichimoku_close_b_diff_shift'] < 0 and row['ichimoku_close_b_diff'] > 0: 
        return 1 
    elif row['ichimoku_close_b_diff_shift'] > 0 and row['ichimoku_close_b_diff'] < 0: 
        return -1 
    else: 
        return 0

    
# KST Oscillator (KST Signal)
def kst_call(row):
    if row['kst_shift'] < 0 and row['kst'] > 0: 
        return 1 
    elif row['kst_shift'] > 0 and row['kst'] < 0: 
        return -1 
    else: 
        return 0
def kst_signal_call(row):
    if row['kst_kst_signal_diff_shift'] < 0 and row['kst_kst_signal_diff'] > 0: 
        return 1 
    elif row['kst_kst_signal_diff_shift'] > 0 and row['kst_kst_signal_diff'] < 0: 
        return -1 
    else: 
        return 0
    
# MACD (Moving Average Convergence Divergence)
def macd_call(row):
    if row['macd_shift'] < 0 and row['macd'] > 0: 
        return 1 
    elif row['macd_shift'] > 0 and row['macd'] < 0: 
        return -1 
    else: 
        return 0
def macd_signal_call(row):
    if row['macd_signal_diff_shift'] < 0 and row['macd_signal_diff'] > 0: 
        return 1 
    elif row['macd_signal_diff_shift'] > 0 and row['macd_signal_diff'] < 0: 
        return -1 
    else: 
        return 0
    
# Parabolic SAR (Parabolic Stop and Reverse)
def psar_call(row):
    # if row['psar_up_indicator'] == 1.0:
    #     return 1
    # elif row['psar_down_indicator'] == 1.0:
    #     return -1
    # else:
    #     return 0
    if row['psar_close_psar_diff_shift'] < 0 and row['psar_close_psar_diff'] > 0: 
        return 1 
    elif row['psar_close_psar_diff_shift'] > 0 and row['psar_close_psar_diff'] < 0: 
        return -1 
    else: 
        return 0

# STC (Schaff Trend Cycle)
def stc_indicator(row):
    if row['stc_shift'] < 25 and row['stc'] > 25: 
        return 1 
    elif row['stc_shift'] > 25 and row['stc'] < 25: 
        return -1 
    elif row['stc_shift'] < 75 and row['stc'] > 75: 
        return 1 
    elif row['stc_shift'] > 75 and row['stc'] < 75: 
        return -1 
    else: 
        return 0

# TRIX (Triple Exponential Average)
def trix_call(row):
    if row['trix_shift'] < 0 and row['trix'] > 0: 
        return 1 
    elif row['trix_shift'] > 0 and row['trix'] < 0: 
        return -1 
    else: 
        return 0
def trix_signal_call(row):
    if row['trix_trix_signal_diff_shift'] < 0 and row['trix_trix_signal_diff'] > 0: 
        return 1 
    elif row['trix_trix_signal_diff_shift'] > 0 and row['trix_trix_signal_diff'] < 0: 
        return -1 
    else: 
        return 0
    
# VI (Vortex Indicator)
def vi_call(row):
    if row['vi_pos_neg_diff_shift'] < 0 and row['vi_pos_neg_diff'] > 0: 
        return 1 
    elif row['vi_pos_neg_diff_shift'] > 0 and row['vi_pos_neg_diff'] < 0: 
        return -1 
    else: 
        return 0

# Chande Momentum Oscillator (CMO)
def cmo(close, window=14):
    delta = close.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    sum_gain = gain.rolling(window=window).sum()
    sum_loss = loss.rolling(window=window).sum()

    cmo = 100 * (sum_gain - sum_loss) / (sum_gain + sum_loss)
    return cmo
def cmo_call(row):
    if row['cmo_shift'] < 0 and row['cmo'] > 0: 
        return 1 
    elif row['cmo_shift'] > 0 and row['cmo'] < 0: 
        return -1 
    else: 
        return 0
def cmo_signal_call(row):
    if row['cmo_cmo_signal_diff_shift'] < 0 and row['cmo_cmo_signal_diff'] > 0: 
        return 1 
    elif row['cmo_cmo_signal_diff_shift'] > 0 and row['cmo_cmo_signal_diff'] < 0: 
        return -1 
    else: 
        return 0
    
# Pivot Point
def pp1_call(row):
    if row['pp1_close_pp1_diff_shift'] < 0 and row['pp1_close_pp1_diff'] > 0: 
        return 1 
    elif row['pp1_close_pp1_diff_shift'] > 0 and row['pp1_close_pp1_diff'] < 0: 
        return -1 
    else: 
        return 0
def pp2_call(row):
    if row['pp2_close_pp2_diff_shift'] < 0 and row['pp2_close_pp2_diff'] > 0: 
        return 1 
    elif row['pp2_close_pp2_diff_shift'] > 0 and row['pp2_close_pp2_diff'] < 0: 
        return -1 
    else: 
        return 0

''' 캔들스틱 차트 (Candlestick chart) '''
# 도지 (Doji)
def is_doji(row, threshold=0.01):
    if (row['high'] - row['low']) == 0:
        return False
    return abs(row['close'] - row['open']) / (row['high'] - row['low']) <= threshold

# 해머 (Hammer)
def is_hammer(row):
    body = abs(row['close'] - row['open'])
    upper_shadow = row['high'] - max(row['close'], row['open'])
    lower_shadow = min(row['close'], row['open']) - row['low']
    return lower_shadow > 2 * body and upper_shadow < body * 0.2

# 역해머 (Inverted Hammer)
def is_inverted_hammer(row):
    body = abs(row['close'] - row['open'])
    upper_shadow = row['high'] - max(row['close'], row['open'])
    lower_shadow = min(row['close'], row['open']) - row['low']
    return upper_shadow > 2 * body and lower_shadow < body * 0.2

# 유성형 (Morning Star)
def is_morning_star(data, i):
    if i < 2:
        return False
    first = data.iloc[i-2]
    second = data.iloc[i-1]
    third = data.iloc[i]
    
    first_condition = first['close'] < first['open']
    second_condition = abs(second['close'] - second['open']) <= (first['high'] - first['low']) * 0.5
    third_condition = third['close'] > third['open'] and third['close'] > (first['close'] + first['open']) / 2
    
    return first_condition and second_condition and third_condition

# 삼중천장 (Triple Top)
def is_triple_top(data, i):
    if i < 4:
        return False
    first_top = data.iloc[i-4]['high']
    second_top = data.iloc[i-2]['high']
    third_top = data.iloc[i]['high']
    
    return abs(first_top - second_top) <= first_top * 0.02 and abs(second_top - third_top) <= second_top * 0.02

# 삼중바닥 (Triple Bottom)
def is_triple_bottom(data, i):
    if i < 4:
        return False
    first_bottom = data.iloc[i-4]['low']
    second_bottom = data.iloc[i-2]['low']
    third_bottom = data.iloc[i]['low']
    
    return abs(first_bottom - second_bottom) <= first_bottom * 0.02 and abs(second_bottom - third_bottom) <= second_bottom * 0.02

# 붉은색 마루보즈 (Red Marubozu)
def is_red_marubozu(row):
    return row['close'] < row['open'] and row['open'] == row['high'] and row['close'] == row['low']

# 녹색 마루보즈 (Green Marubozu)
def is_green_marubozu(row):
    return row['close'] > row['open'] and row['open'] == row['low'] and row['close'] == row['high']

# 흑삼병 (Three Black Crows)
def is_three_black_crows(data, i):
    if i < 2:
        return False
    return (
        data.iloc[i-2]['close'] < data.iloc[i-2]['open'] and
        data.iloc[i-1]['close'] < data.iloc[i-1]['open'] and
        data.iloc[i]['close'] < data.iloc[i]['open']
    )

# 적삼병 (Three White Soldiers)
def is_three_white_soldiers(data, i):
    if i < 2:
        return False
    return (
        data.iloc[i-2]['close'] > data.iloc[i-2]['open'] and
        data.iloc[i-1]['close'] > data.iloc[i-1]['open'] and
        data.iloc[i]['close'] > data.iloc[i]['open']
    )