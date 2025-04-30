# AI量化交易学习项目

这是一个为期7天的量化交易入门学习项目，专注于使用Python进行股票交易策略开发。

## 项目结构
```
.
├── README.md           # 项目说明文档
├── requirements.txt    # 项目依赖
├── venv/              # Python虚拟环境
└── examples/          # 示例代码
    └── day1_stock_data.py  # 第一天：基础股票数据获取示例
```

## 环境配置
1. 确保已安装Python 3.8+

2. 设置虚拟环境：
```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
# 在macOS/Linux上：
source venv/bin/activate
# 在Windows上：
# .\venv\Scripts\activate

# 当看到命令行前面出现(venv)前缀时，说明虚拟环境已经激活
```

3. 在虚拟环境中安装依赖包：
```bash
pip install -r requirements.txt
```

4. 退出虚拟环境（当完成工作后）：
```bash
conda deactivate
```

## 快速开始
确保虚拟环境已激活，然后运行第一天的示例代码：
```bash
python examples/day1_stock_data.py
```

这将获取苹果公司(AAPL)最近10天的股票数据并绘制走势图。

## 学习计划
- 第1天：量化交易基础概念与环境准备
  - 理解量化交易的基本概念
  - 搭建Python开发环境
  - 实现第一个数据获取示例

## 注意事项
- 本项目使用yfinance获取股票数据，仅用于学习目的
- 实际交易时需要考虑更多因素，如交易成本、滑点等
- 始终在虚拟环境中运行代码，避免依赖冲突
- 每次开始工作时记得激活虚拟环境