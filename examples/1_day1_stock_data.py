import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def get_stock_data(symbol='AAPL', days=10):
    """
    获取指定股票的历史数据
    
    参数:
        symbol (str): 股票代码
        days (int): 获取最近多少天的数据
    """
    # 计算起始日期
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    # 获取股票数据
    stock = yf.Ticker(symbol)
    hist = stock.history(start=start_date, end=end_date)
    
    return hist

def plot_stock_price(data):
    """
    绘制股票收盘价走势图
    
    参数:
        data (pd.DataFrame): 股票历史数据
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], label='收盘价')
    plt.title('股票收盘价走势图')
    plt.xlabel('日期')
    plt.ylabel('价格')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # 获取苹果公司最近10天的股票数据
    stock_data = get_stock_data('AAPL', 10)
    
    # 打印数据
    print("\n最近的股票数据:")
    print(stock_data.tail())
    
    # 绘制走势图
    plot_stock_price(stock_data) 