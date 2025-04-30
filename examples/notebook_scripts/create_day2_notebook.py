#!/usr/bin/env python3
import json
import os

# 创建一个基本的notebook结构
notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# 第二天：股票数据基础与Python处理\n",
                "\n",
                "在这个Notebook中，我们将深入学习股票市场数据的基本结构与来源，以及使用Python处理历史行情数据的方法。\n",
                "\n",
                "## 学习目标\n",
                "- 了解股票数据的基本构成（日期、开盘价、收盘价、最高价、最低价、成交量等）\n",
                "- 获取和分析股票历史数据\n",
                "- 使用pandas处理时间序列数据\n",
                "- 对股票数据进行基本统计分析和可视化"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# 导入所需的库\n",
                "import yfinance as yf\n",
                "import pandas as pd\n",
                "import numpy as np\n",
                "import matplotlib.pyplot as plt\n",
                "import seaborn as sns\n",
                "from datetime import datetime, timedelta\n",
                "\n",
                "# 设置绘图风格\n",
                "sns.set_style(\"whitegrid\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 1. 获取股票数据\n",
                "\n",
                "首先，我们定义一个函数，用于获取指定股票的历史数据。"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "def get_stock_data(symbol='AAPL', period='3y'):\n",
                "    \"\"\"\n",
                "    获取指定股票的历史数据\n",
                "    \n",
                "    参数:\n",
                "        symbol (str): 股票代码\n",
                "        period (str): 获取数据的时间跨度，例如 '1d', '5d', '1mo', '3mo', '1y', '2y', '5y', '10y', 'ytd', 'max'\n",
                "    \n",
                "    返回:\n",
                "        pd.DataFrame: 包含股票历史数据的DataFrame\n",
                "    \"\"\"\n",
                "    # 获取股票数据\n",
                "    stock = yf.Ticker(symbol)\n",
                "    hist = stock.history(period=period)\n",
                "    \n",
                "    return hist\n",
                "\n",
                "# 设置要分析的股票代码\n",
                "stock_symbol = 'AAPL'\n",
                "\n",
                "# 获取过去3年的股票数据\n",
                "print(f\"正在获取 {stock_symbol} 过去3年的历史数据...\")\n",
                "stock_data = get_stock_data(stock_symbol, '3y')"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. 基本数据分析\n",
                "\n",
                "接下来，我们对获取的股票数据进行基本分析，了解数据的基本特征和统计信息。"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "def basic_data_analysis(data):\n",
                "    \"\"\"\n",
                "    对股票数据进行基本分析\n",
                "    \n",
                "    参数:\n",
                "        data (pd.DataFrame): 股票历史数据\n",
                "    \"\"\"\n",
                "    # 打印数据基本信息\n",
                "    print(\"\\n=== 数据基本信息 ===\")\n",
                "    print(f\"数据起始日期: {data.index.min().strftime('%Y-%m-%d')}\")\n",
                "    print(f\"数据结束日期: {data.index.max().strftime('%Y-%m-%d')}\")\n",
                "    print(f\"数据总天数: {len(data)}\")\n",
                "    print(f\"数据列: {', '.join(data.columns)}\")\n",
                "    \n",
                "    # 打印数据前5行\n",
                "    print(\"\\n=== 数据前5行 ===\")\n",
                "    display(data.head())\n",
                "    \n",
                "    # 计算基本统计值\n",
                "    print(\"\\n=== 收盘价基本统计值 ===\")\n",
                "    print(f\"均值: {data['Close'].mean():.2f}\")\n",
                "    print(f\"标准差: {data['Close'].std():.2f}\")\n",
                "    print(f\"最小值: {data['Close'].min():.2f}\")\n",
                "    print(f\"最大值: {data['Close'].max():.2f}\")\n",
                "    print(f\"中位数: {data['Close'].median():.2f}\")\n",
                "    \n",
                "    # 计算每日收益率\n",
                "    data['Daily_Return'] = data['Close'].pct_change() * 100\n",
                "    \n",
                "    print(\"\\n=== 日收益率基本统计值 ===\")\n",
                "    print(f\"均值: {data['Daily_Return'].mean():.2f}%\")\n",
                "    print(f\"标准差: {data['Daily_Return'].std():.2f}%\")\n",
                "    print(f\"最小值: {data['Daily_Return'].min():.2f}%\")\n",
                "    print(f\"最大值: {data['Daily_Return'].max():.2f}%\")\n",
                "    \n",
                "    return data\n",
                "\n",
                "# 进行基本数据分析\n",
                "print(f\"\\n对 {stock_symbol} 进行基本数据分析...\")\n",
                "stock_data = basic_data_analysis(stock_data)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. 数据可视化\n",
                "\n",
                "数据可视化是理解数据模式的重要工具。接下来，我们将通过多种图表来可视化股票数据。"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "def visualize_stock_data(data, symbol):\n",
                "    \"\"\"\n",
                "    可视化股票数据\n",
                "    \n",
                "    参数:\n",
                "        data (pd.DataFrame): 股票历史数据\n",
                "        symbol (str): 股票代码\n",
                "    \"\"\"\n",
                "    # 创建一个2x2的子图布局\n",
                "    fig, axes = plt.subplots(2, 2, figsize=(14, 10))\n",
                "    \n",
                "    # 1. 股票收盘价走势图\n",
                "    axes[0, 0].plot(data.index, data['Close'], color='blue')\n",
                "    axes[0, 0].set_title(f'{symbol} 收盘价走势')\n",
                "    axes[0, 0].set_ylabel('价格')\n",
                "    axes[0, 0].tick_params(axis='x', rotation=45)\n",
                "    \n",
                "    # 2. 成交量走势图\n",
                "    axes[0, 1].bar(data.index, data['Volume'], color='green', alpha=0.7)\n",
                "    axes[0, 1].set_title(f'{symbol} 成交量走势')\n",
                "    axes[0, 1].set_ylabel('成交量')\n",
                "    axes[0, 1].tick_params(axis='x', rotation=45)\n",
                "    \n",
                "    # 3. 收盘价的直方图\n",
                "    sns.histplot(data['Close'], bins=30, kde=True, ax=axes[1, 0], color='purple')\n",
                "    axes[1, 0].set_title(f'{symbol} 收盘价分布')\n",
                "    axes[1, 0].set_xlabel('价格')\n",
                "    \n",
                "    # 4. 日收益率的直方图\n",
                "    sns.histplot(data['Daily_Return'].dropna(), bins=50, kde=True, ax=axes[1, 1], color='red')\n",
                "    axes[1, 1].set_title(f'{symbol} 日收益率分布')\n",
                "    axes[1, 1].set_xlabel('日收益率 (%)')\n",
                "    \n",
                "    plt.tight_layout()\n",
                "    plt.show()\n",
                "\n",
                "# 数据可视化\n",
                "print(f\"\\n对 {stock_symbol} 进行数据可视化...\")\n",
                "visualize_stock_data(stock_data, stock_symbol)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4. 时间序列分析\n",
                "\n",
                "时间序列分析是量化交易中的重要工具，可以帮助我们发现价格趋势和模式。"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "def time_series_analysis(data, symbol):\n",
                "    \"\"\"\n",
                "    对股票数据进行时间序列分析\n",
                "    \n",
                "    参数:\n",
                "        data (pd.DataFrame): 股票历史数据\n",
                "        symbol (str): 股票代码\n",
                "    \"\"\"\n",
                "    # 创建一个图形\n",
                "    plt.figure(figsize=(14, 10))\n",
                "    \n",
                "    # 1. 计算不同周期的移动平均线\n",
                "    data['MA50'] = data['Close'].rolling(window=50).mean()\n",
                "    data['MA200'] = data['Close'].rolling(window=200).mean()\n",
                "    \n",
                "    # 绘制原始收盘价和移动平均线\n",
                "    plt.subplot(2, 1, 1)\n",
                "    plt.plot(data.index, data['Close'], label='收盘价', alpha=0.5)\n",
                "    plt.plot(data.index, data['MA50'], label='50日移动平均线', linewidth=1.5)\n",
                "    plt.plot(data.index, data['MA200'], label='200日移动平均线', linewidth=1.5)\n",
                "    plt.title(f'{symbol} 收盘价与移动平均线')\n",
                "    plt.ylabel('价格')\n",
                "    plt.legend()\n",
                "    plt.grid(True)\n",
                "    \n",
                "    # 2. 重采样按月计算\n",
                "    monthly_data = data['Close'].resample('M').last()\n",
                "    monthly_returns = monthly_data.pct_change() * 100\n",
                "    \n",
                "    plt.subplot(2, 1, 2)\n",
                "    monthly_returns.plot(kind='bar', color='blue', alpha=0.7)\n",
                "    plt.title(f'{symbol} 每月收益率')\n",
                "    plt.ylabel('收益率 (%)')\n",
                "    plt.grid(True)\n",
                "    plt.tight_layout()\n",
                "    \n",
                "    plt.show()\n",
                "\n",
                "# 时间序列分析\n",
                "print(f\"\\n对 {stock_symbol} 进行时间序列分析...\")\n",
                "time_series_analysis(stock_data, stock_symbol)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 5. 分析特定时间段的数据\n",
                "\n",
                "为了更深入地了解特定时间段的市场表现，我们可以截取数据的子集进行分析。"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "def analyze_specific_timeframe(data, symbol, start_date, end_date):\n",
                "    \"\"\"\n",
                "    分析特定时间段的股票数据\n",
                "    \n",
                "    参数:\n",
                "        data (pd.DataFrame): 股票历史数据\n",
                "        symbol (str): 股票代码\n",
                "        start_date (str): 开始日期，格式为'YYYY-MM-DD'\n",
                "        end_date (str): 结束日期，格式为'YYYY-MM-DD'\n",
                "    \"\"\"\n",
                "    # 截取特定时间段的数据\n",
                "    period_data = data.loc[start_date:end_date]\n",
                "    \n",
                "    print(f\"\\n=== {start_date} 至 {end_date} 期间 {symbol} 的表现 ===\")\n",
                "    print(f\"期间收盘价变化: {period_data['Close'].iloc[-1] - period_data['Close'].iloc[0]:.2f}\")\n",
                "    print(f\"期间收益率: {((period_data['Close'].iloc[-1] / period_data['Close'].iloc[0]) - 1) * 100:.2f}%\")\n",
                "    print(f\"期间平均成交量: {period_data['Volume'].mean():.0f}\")\n",
                "    print(f\"期间最高价: {period_data['High'].max():.2f}\")\n",
                "    print(f\"期间最低价: {period_data['Low'].min():.2f}\")\n",
                "    \n",
                "    # 绘制特定时间段的K线图\n",
                "    plt.figure(figsize=(12, 6))\n",
                "    \n",
                "    # 计算调整后的Open, High, Low, Close\n",
                "    period_data['Centered'] = (period_data['Open'] + period_data['Close']) / 2\n",
                "    period_data['Height'] = abs(period_data['Close'] - period_data['Open'])\n",
                "    \n",
                "    # 绘制K线图\n",
                "    for idx, row in period_data.iterrows():\n",
                "        color = 'green' if row['Close'] >= row['Open'] else 'red'\n",
                "        plt.plot([idx, idx], [row['Low'], row['High']], color=color)\n",
                "        plt.plot([idx, idx], [row['Open'], row['Close']], color=color, linewidth=4)\n",
                "    \n",
                "    plt.title(f'{symbol} 在 {start_date} 至 {end_date} 期间的价格走势')\n",
                "    plt.ylabel('价格')\n",
                "    plt.grid(True)\n",
                "    plt.xticks(rotation=45)\n",
                "    plt.tight_layout()\n",
                "    plt.show()\n",
                "\n",
                "# 分析最近一年的数据\n",
                "print(f\"\\n分析 {stock_symbol} 最近一年的数据...\")\n",
                "one_year_ago = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')\n",
                "today = datetime.now().strftime('%Y-%m-%d')\n",
                "analyze_specific_timeframe(stock_data, stock_symbol, one_year_ago, today)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 小结\n",
                "\n",
                "在这个Notebook中，我们学习了：\n",
                "1. 如何获取股票的长期历史数据\n",
                "2. 如何进行基本数据分析（计算统计值、显示数据特征）\n",
                "3. 如何通过多种图表可视化股票数据\n",
                "4. 如何进行时间序列分析（移动平均线、月度重采样）\n",
                "5. 如何分析特定时间段的股票表现\n",
                "\n",
                "这些知识和技能将为我们后续开发交易策略打下坚实的基础。"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.10"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# 写入notebook到文件
output_path = "../2_day2_stock_data_processing.ipynb"
with open(output_path, 'w') as f:
    json.dump(notebook, f, indent=1)

print(f"Jupyter notebook创建成功: {output_path}") 