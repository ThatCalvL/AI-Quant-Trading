import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

def get_stock_data(symbol='AAPL', period='3y'):
    """
    获取指定股票的历史数据
    
    参数:
        symbol (str): 股票代码
        period (str): 获取数据的时间跨度，例如 '1d', '5d', '1mo', '3mo', '1y', '2y', '5y', '10y', 'ytd', 'max'
    
    返回:
        pd.DataFrame: 包含股票历史数据的DataFrame
    """
    # 获取股票数据
    stock = yf.Ticker(symbol)
    hist = stock.history(period=period)
    
    return hist

def basic_data_analysis(data):
    """
    对股票数据进行基本分析
    
    参数:
        data (pd.DataFrame): 股票历史数据
    """
    # 打印数据基本信息
    print("\n=== 数据基本信息 ===")
    print(f"数据起始日期: {data.index.min().strftime('%Y-%m-%d')}")
    print(f"数据结束日期: {data.index.max().strftime('%Y-%m-%d')}")
    print(f"数据总天数: {len(data)}")
    print(f"数据列: {', '.join(data.columns)}")
    
    # 打印数据前5行
    print("\n=== 数据前5行 ===")
    print(data.head())
    
    # 计算基本统计值
    print("\n=== 收盘价基本统计值 ===")
    print(f"均值: {data['Close'].mean():.2f}")
    print(f"标准差: {data['Close'].std():.2f}")
    print(f"最小值: {data['Close'].min():.2f}")
    print(f"最大值: {data['Close'].max():.2f}")
    print(f"中位数: {data['Close'].median():.2f}")
    
    # 计算每日收益率
    data['Daily_Return'] = data['Close'].pct_change() * 100
    
    print("\n=== 日收益率基本统计值 ===")
    print(f"均值: {data['Daily_Return'].mean():.2f}%")
    print(f"标准差: {data['Daily_Return'].std():.2f}%")
    print(f"最小值: {data['Daily_Return'].min():.2f}%")
    print(f"最大值: {data['Daily_Return'].max():.2f}%")
    
    return data

def visualize_stock_data(data, symbol):
    """
    可视化股票数据
    
    参数:
        data (pd.DataFrame): 股票历史数据
        symbol (str): 股票代码
    """
    # 设置绘图风格
    sns.set_style("whitegrid")
    
    # 创建一个2x2的子图布局
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # 1. 股票收盘价走势图
    axes[0, 0].plot(data.index, data['Close'], color='blue')
    axes[0, 0].set_title(f'{symbol} 收盘价走势')
    axes[0, 0].set_ylabel('价格')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # 2. 成交量走势图
    axes[0, 1].bar(data.index, data['Volume'], color='green', alpha=0.7)
    axes[0, 1].set_title(f'{symbol} 成交量走势')
    axes[0, 1].set_ylabel('成交量')
    axes[0, 1].tick_params(axis='x', rotation=45)
    
    # 3. 收盘价的直方图
    sns.histplot(data['Close'], bins=30, kde=True, ax=axes[1, 0], color='purple')
    axes[1, 0].set_title(f'{symbol} 收盘价分布')
    axes[1, 0].set_xlabel('价格')
    
    # 4. 日收益率的直方图
    sns.histplot(data['Daily_Return'].dropna(), bins=50, kde=True, ax=axes[1, 1], color='red')
    axes[1, 1].set_title(f'{symbol} 日收益率分布')
    axes[1, 1].set_xlabel('日收益率 (%)')
    
    plt.tight_layout()
    plt.show()

def time_series_analysis(data, symbol):
    """
    对股票数据进行时间序列分析
    
    参数:
        data (pd.DataFrame): 股票历史数据
        symbol (str): 股票代码
    """
    # 创建一个图形
    plt.figure(figsize=(14, 10))
    
    # 1. 计算不同周期的移动平均线
    data['MA50'] = data['Close'].rolling(window=50).mean()
    data['MA200'] = data['Close'].rolling(window=200).mean()
    
    # 绘制原始收盘价和移动平均线
    plt.subplot(2, 1, 1)
    plt.plot(data.index, data['Close'], label='收盘价', alpha=0.5)
    plt.plot(data.index, data['MA50'], label='50日移动平均线', linewidth=1.5)
    plt.plot(data.index, data['MA200'], label='200日移动平均线', linewidth=1.5)
    plt.title(f'{symbol} 收盘价与移动平均线')
    plt.ylabel('价格')
    plt.legend()
    plt.grid(True)
    
    # 2. 重采样按月计算
    monthly_data = data['Close'].resample('M').last()
    monthly_returns = monthly_data.pct_change() * 100
    
    plt.subplot(2, 1, 2)
    monthly_returns.plot(kind='bar', color='blue', alpha=0.7)
    plt.title(f'{symbol} 每月收益率')
    plt.ylabel('收益率 (%)')
    plt.grid(True)
    plt.tight_layout()
    
    plt.show()

def analyze_specific_timeframe(data, symbol, start_date, end_date):
    """
    分析特定时间段的股票数据
    
    参数:
        data (pd.DataFrame): 股票历史数据
        symbol (str): 股票代码
        start_date (str): 开始日期，格式为'YYYY-MM-DD'
        end_date (str): 结束日期，格式为'YYYY-MM-DD'
    """
    # 截取特定时间段的数据
    period_data = data.loc[start_date:end_date]
    
    print(f"\n=== {start_date} 至 {end_date} 期间 {symbol} 的表现 ===")
    print(f"期间收盘价变化: {period_data['Close'].iloc[-1] - period_data['Close'].iloc[0]:.2f}")
    print(f"期间收益率: {((period_data['Close'].iloc[-1] / period_data['Close'].iloc[0]) - 1) * 100:.2f}%")
    print(f"期间平均成交量: {period_data['Volume'].mean():.0f}")
    print(f"期间最高价: {period_data['High'].max():.2f}")
    print(f"期间最低价: {period_data['Low'].min():.2f}")
    
    # 绘制特定时间段的K线图
    plt.figure(figsize=(12, 6))
    
    # 计算调整后的Open, High, Low, Close
    period_data['Centered'] = (period_data['Open'] + period_data['Close']) / 2
    period_data['Height'] = abs(period_data['Close'] - period_data['Open'])
    
    # 绘制K线图
    for idx, row in period_data.iterrows():
        color = 'green' if row['Close'] >= row['Open'] else 'red'
        plt.plot([idx, idx], [row['Low'], row['High']], color=color)
        plt.plot([idx, idx], [row['Open'], row['Close']], color=color, linewidth=4)
    
    plt.title(f'{symbol} 在 {start_date} 至 {end_date} 期间的价格走势')
    plt.ylabel('价格')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # 设置要分析的股票代码
    stock_symbol = 'AAPL'
    
    # 1. 获取过去3年的股票数据
    print(f"正在获取 {stock_symbol} 过去3年的历史数据...")
    stock_data = get_stock_data(stock_symbol, '3y')
    
    # 2. 进行基本数据分析
    print(f"\n对 {stock_symbol} 进行基本数据分析...")
    stock_data = basic_data_analysis(stock_data)
    
    # 3. 数据可视化
    print(f"\n对 {stock_symbol} 进行数据可视化...")
    visualize_stock_data(stock_data, stock_symbol)
    
    # 4. 时间序列分析
    print(f"\n对 {stock_symbol} 进行时间序列分析...")
    time_series_analysis(stock_data, stock_symbol)
    
    # 5. 分析最近一年的数据
    print(f"\n分析 {stock_symbol} 最近一年的数据...")
    one_year_ago = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
    today = datetime.now().strftime('%Y-%m-%d')
    analyze_specific_timeframe(stock_data, stock_symbol, one_year_ago, today)
    
    print("\n分析完成！现在你已经了解了如何获取和分析股票数据的基本方法。") 