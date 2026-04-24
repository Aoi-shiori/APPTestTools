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

# 运行
 `requirements.txt` 文件：

```txt
# 核心测试框架
airtest>=1.3.0
pocoui>=1.0.90          # POCO UI 自动化框架（Airtest 附带的可能版本较旧，单独指定）
pytest>=9.0.0
pytest-xdist>=3.5.0     # 并发执行
pytest-html>=4.1.0      # HTML 报告
allure-pytest>=2.13.0   # Allure 报告支持

# Airtest 依赖的图像处理库
opencv-python>=4.8.0
numpy>=1.24.0
Pillow>=10.0.0

# 辅助库
PyYAML>=6.0             # 如果配置文件使用 YAML（根据你的 config.settings 可能需要）
requests>=2.31.0        # 若 Nginx 或 Allure 服务涉及 HTTP 请求
```

### 📌 说明
- **`pocoui`**：POCO 的独立包，建议显式安装，比 Airtest 内置版本更新。
- **`opencv-python`**：Airtest 图像识别必需。
- **`pytest-xdist`**：`run.py` 中提到了 `-n` 参数。
- **`allure-pytest`**：生成 Allure 报告所需。
- **`PyYAML`** 和 **`requests`**：如果你的 `config.settings` 或 `nginx` 模块用到，可保留；否则可删除。

### ⚙️ 安装命令
```bash
pip install -r requirements.txt
```

### ⚠️ 注意事项
- 如果使用 Airtest 自带的 `poco`，可以不单独安装 `pocoui`，但建议独立安装以获得最新功能。
- 若在 macOS/Linux 上运行，确保系统已安装 `nginx` 并配置好路径（项目中的 `nginx-1.29.0` 目录）。
- 如果不需要并发或 HTML 报告，可移除 `pytest-xdist` 和 `pytest-html`。