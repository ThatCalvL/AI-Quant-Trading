# AI量化交易学习计划

这个项目包含了七天量化交易入门学习计划的Jupyter notebooks和相关资源，专注于使用Python进行股票交易策略开发。

## 项目结构

```
.
├── README.md           # 项目说明文档
├── requirements.txt    # 项目依赖
├── venv/               # Python虚拟环境
└── examples/           # Jupyter notebooks和示例代码
    ├── 1_day1_stock_data.ipynb         # 第一天：基础股票数据获取
    └── 2_day2_stock_data_processing.ipynb  # 第二天：股票数据基础与Python处理
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

4. 安装并配置Jupyter：
```bash
# 确保已安装jupyter
pip install jupyter

# 注册虚拟环境到Jupyter
python -m ipykernel install --user --name=venv --display-name="Python (AI-Quant-Trading)"
```

## 使用方法

有两种方式运行Jupyter notebooks：

### 1. 启动Jupyter Lab（推荐）

```bash
jupyter lab
```

### 2. 启动Jupyter Notebook

```bash
jupyter notebook
```

启动后，在浏览器中导航到`examples`目录，点击对应的notebook文件（.ipynb）进行学习。

## 学习进度

- **第1天**：量化交易基础概念与环境准备
  - 理解量化交易的基本概念
  - 搭建Python开发环境
  - 使用yfinance获取股票数据
  
- **第2天**：股票数据基础与Python处理
  - 熟悉股票数据的基本构成
  - 使用pandas处理时间序列数据
  - 对股票数据进行基本统计分析与可视化

## 注意事项

- 本项目使用yfinance获取股票数据，仅用于学习目的
- 实际交易时需要考虑更多因素，如交易成本、滑点等
- 始终在虚拟环境中运行代码，避免依赖冲突
- 每次开始工作时记得激活虚拟环境