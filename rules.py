from stock import *

# These are stock selection rules

# --- Basic P/E and P/B Rules

# 1. Stock P/E should be less than its average historical value
def is_PE_less_hist_avg(stock):
    return stock.PE < stock.avgPE

# 2. Stock P/E should be less than industry average PE value
def is_PE_less_ind_avg_PE(stock):
    return stock.PE < stock.industry_avg_PE

# 3. Stock P/B should be less than its average historical value
def is_PB_less_hist_avg(stock):
    return stock.PB < stock.avgPB

# 4. Stock P/B should be less tthan industry average PB value
def is_PB_less_ind_avg_PB(stock):
    return stock.PB < stock.industry_avg_PB

# --- Dividents Rules

# 5. Stock should have divident yield > 0
def is_divident_yield(stock):
    return stock.divident_yield > 0
# 6. Dividents: Divident Growth Rate > 0
# TODO

# 7. № of consecutive years of dividents' increases
# TODO

# --- EBITDA Rules
# 8. EBITDA should grow for three years
# TODO: return EBITDA(today) > EBITDA(y-1) > EBITDA(y-2)