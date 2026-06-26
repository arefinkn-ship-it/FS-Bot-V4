# ==========================================
# TELEGRAM
# ==========================================

TELEGRAM_TOKEN = "8722459635:AAF8VAN9xnjaZ8zXnBESZKc4dalA9S6JMWo"
CHAT_ID = "8310319714"

# ==========================================
# MT5 SYMBOLS
# ==========================================

PAIRS = [
    "XAUUSD",
    "EURUSD",
    "GBPUSD",
    "USDJPY",
    "GBPJPY"
]

# ==========================================
# TIMEFRAMES
# ==========================================

H1_TIMEFRAME = "H1"
H4_TIMEFRAME = "H4"

# ==========================================
# SCANNER SETTINGS
# ==========================================

SCAN_INTERVAL_MINUTES = 15

# ==========================================
# INDICATOR SETTINGS
# ==========================================

RSI_LENGTH = 14

PIVOT_LEFT = 5
PIVOT_RIGHT = 5

ATR_LENGTH = 14

# ==========================================
# FIBONACCI SETTINGS
# ==========================================

FIB_RETRACEMENTS = [
    0.382,
    0.618,
    0.786,
    0.886
]

FIB_EXTENSIONS = [
    1.272,
    1.414,
    1.618
]

FIB_TOLERANCE = 0.002   # 0.2%

# ==========================================
# RISK MANAGEMENT
# ==========================================

ATR_SL_MULTIPLIER = 1.5

TP1_R_MULTIPLIER = 1.0
TP2_R_MULTIPLIER = 2.0

RISK_PER_TRADE = 0.01

# ==========================================
# SIGNAL SCORING
# ==========================================

GRADE_A_PLUS = 95
GRADE_A = 85
GRADE_B = 75

MINIMUM_SCORE = 75

# ==========================================
# BACKTEST SETTINGS
# ==========================================

BACKTEST_BARS = 10000

MAX_HOLDING_BARS = 100

MOVE_SL_TO_BREAKEVEN_AT_TP1 = True

# ==========================================
# GMMA SETTINGS
# ==========================================

GMMA_FAST = [
    3,
    5,
    8,
    10,
    12,
    15
]

GMMA_SLOW = [
    30,
    35,
    40,
    45,
    50,
    60
]