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
                "# 第一天：量化交易基础概念与环境准备\n",
                "\n",
                "在这个Notebook中，我们将学习如何使用Python获取股票数据，这是量化交易的第一步。\n",
                "\n",
                "## 学习目标\n",
                "- 了解如何使用yfinance库获取股票历史数据\n",
                "- 使用pandas处理股票数据\n",
                "- 使用matplotlib可视化股票价格走势"
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
                "import matplotlib.pyplot as plt\n",
                "from datetime import datetime, timedelta"
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
                "def get_stock_data(symbol='AAPL', days=10):\n",
                "    \"\"\"\n",
                "    获取指定股票的历史数据\n",
                "    \n",
                "    参数:\n",
                "        symbol (str): 股票代码\n",
                "        days (int): 获取最近多少天的数据\n",
                "    \"\"\"\n",
                "    # 计算起始日期\n",
                "    end_date = datetime.now()\n",
                "    start_date = end_date - timedelta(days=days)\n",
                "    \n",
                "    # 获取股票数据\n",
                "    stock = yf.Ticker(symbol)\n",
                "    hist = stock.history(start=start_date, end=end_date)\n",
                "    \n",
                "    return hist"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. 可视化股票价格\n",
                "\n",
                "接下来，我们定义一个函数，用于绘制股票收盘价走势图。"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "def plot_stock_price(data):\n",
                "    \"\"\"\n",
                "    绘制股票收盘价走势图\n",
                "    \n",
                "    参数:\n",
                "        data (pd.DataFrame): 股票历史数据\n",
                "    \"\"\"\n",
                "    plt.figure(figsize=(10, 6))\n",
                "    plt.plot(data.index, data['Close'], label='收盘价')\n",
                "    plt.title('股票收盘价走势图')\n",
                "    plt.xlabel('日期')\n",
                "    plt.ylabel('价格')\n",
                "    plt.legend()\n",
                "    plt.grid(True)\n",
                "    plt.xticks(rotation=45)\n",
                "    plt.tight_layout()\n",
                "    plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. 获取并分析股票数据\n",
                "\n",
                "现在，让我们使用上面定义的函数来获取苹果公司最近10天的股票数据，并进行可视化。"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# 获取苹果公司最近10天的股票数据\n",
                "stock_data = get_stock_data('AAPL', 10)\n",
                "\n",
                "# 打印数据\n",
                "print(\"\\n最近的股票数据:\")\n",
                "print(stock_data.tail())"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# 绘制走势图\n",
                "plot_stock_price(stock_data)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 小结\n",
                "\n",
                "在这个Notebook中，我们学习了：\n",
                "1. 如何使用yfinance库获取股票历史数据\n",
                "2. 如何处理和查看数据\n",
                "3. 如何绘制股票价格走势图\n",
                "\n",
                "这是量化交易的第一步，接下来我们将深入学习更多数据分析和处理技术。"
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
output_path = "../1_day1_stock_data.ipynb"
with open(output_path, 'w') as f:
    json.dump(notebook, f, indent=1)

print(f"Jupyter notebook创建成功: {output_path}") 