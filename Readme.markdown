``` text
airtest_framework/
│
├── config/                      # 配置模块
│   ├── __init__.py
│   └── settings.py              # 全局配置（设备参数、超时、路径等）
│
├── core/                        # 核心封装层（强手负责）
│   ├── __init__.py
│   ├── device_manager.py        # 设备连接与管理
│   ├── base_page.py             # Page Object 基类
│   └── report_utils.py          # 报告增强工具（截图、日志）
│
├── pages/                       # 页面对象层（强手封装，弱手调用）
│   ├── __init__.py
│   └── calculator_page.py       # 示例：计算器页面
│
├── tests/                       # 测试用例层（弱手主要工作区）
│   ├── __init__.py
│   └── test_calculator.py       # 计算器功能测试
│
├── utils/                       # 辅助工具
│   ├── __init__.py
│   └── logger.py                # 日志记录器
│
├── logs/                        # 运行时日志目录（自动生成）
├── reports/                     # 测试报告目录（自动生成）
├── screenshots/                 # 失败截图目录（自动生成）
│
├── requirements.txt             # 依赖列表
├── conftest.py                  # pytest 全局 fixture
├── pytest.ini                   # pytest 配置
└── run.py                       # 运行入口（可选）'
```
