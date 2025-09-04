# 🕵️‍♂️ CheckIPs v1.0 - 高级 IP 地址智能检测工具

![image-20250820110610691](https://s1.vika.cn/space/2025/08/20/b6feb84bd00044629e53edeefbdd1077)

<div align="center"><p>🔍 精准、高效的IP地址信息探测与分析解决方案 🔍</p><div><img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python版本"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="许可证"><img src="https://img.shields.io/badge/Version-1.0.0-orange.svg" alt="版本号"><img src="https://img.shields.io/badge/Status-Active-brightgreen.svg" alt="项目状态"></div></div>

------

## 👨‍💻 作者信息

- **作者**：一只鱼（Bifish）
- **GitHub**：https://github.com/Bifishone
- **工具名称**：CheckIPs v1.0

------

## 📖 工具简介

CheckIPs 是一款基于 Python 和 Selenium 开发的高级 IP 地址检测工具，专为网络管理员、安全分析师和开发者设计。它能够批量查询 IP 地址的地理位置信息和使用类型，以直观的方式呈现结果并生成详细报告。

无论是安全审计、服务器监控还是网络分析，CheckIPs 都能为您提供精准、全面的 IP 信息，帮助您更好地理解和管理网络资源。

------

## ✨ 核心功能

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 2rem 0;"><div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"><h3>📦 批量IP处理</h3><p>支持大规模IP地址批量检测，轻松处理上百个IP，兼容标准IP和IP:端口格式</p></div>




<div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"><h3>🌍 地理定位识别</h3><p>精准识别IP所属国家/地区信息，提供详细的地理位置解析</p></div>



<div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"><h3>🏢 IP类型判断</h3><p>智能识别IP使用类型：原生IP、家庭带宽、IDC机房、广播IP等</p></div>



<div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"><h3>📊 专业报告生成</h3><p>自动生成美观的Excel报告，包含所有检测结果和分析信息</p></div>



<div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"><h3>🌈 彩色终端输出</h3><p>检测结果以彩色方式在终端显示，不同类型IP一目了然</p></div>



<div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"><h3>🕵️‍♂️ 无头浏览器模式</h3><p>支持无界面运行模式，资源占用更低，适合服务器环境</p></div>



<div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"><h3>🔄 智能错误处理</h3><p>内置重试机制和多元素定位备份，提高页面解析稳定性</p></div>



<div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"><h3>⚡ 自动过滤无效IP</h3><p>自动识别并过滤格式无效的IP地址，提高检测效率</p></div></div>

------

## 🎨 检测结果说明

CheckIPs 能识别多种 IP 类型，并以不同颜色编码直观展示：

| IP 类型     | 详细描述                         | 显示颜色 |
| ----------- | -------------------------------- | -------- |
| 原生 IP     | 直接分配给终端用户的原始 IP 地址 | 绿色     |
| 家庭带宽 IP | 家庭网络服务提供商分配的 IP      | 绿色     |
| IDC 机房 IP | 数据中心或服务器集群使用的 IP    | 黄色     |
| 广播 IP     | 用于网络广播服务的特殊 IP        | 黄色     |
| 未知类型    | 无法识别的 IP 类型               | 灰色     |

------

## 📥 安装指南

### 📋 前提条件

- Python 3.x 环境
- Google Chrome 浏览器（推荐最新版本）
- 与 Chrome 版本匹配的 ChromeDriver

### 🔧 安装步骤

1. **获取项目代码**

   ```bash
   # 克隆仓库（如果有）
   git clone https://github.com/Bifish0/CheckIPs.git
   cd CheckIPs
   
   # 或直接下载代码并解压
   ```

2. **安装依赖包**

   ```bash
   # 使用pip安装所需依赖
   pip install selenium colorama openpyxl
   
   # 对于Python3用户
   pip3 install selenium colorama openpyxl
   ```

3. **配置 ChromeDriver**

   - 根据您的 Chrome 浏览器版本下载对应版本的 ChromeDriver

   - 下载地址: [ChromeDriver 官方网站](https://sites.google.com/chromium.org/driver/)

   - 将下载的 ChromeDriver 可执行文件放在项目根目录下

   - 确保 ChromeDriver 具有可执行权限（Linux/macOS 用户）:

     ```bash
     chmod +x chromedriver
     ```

------

## 🛠️ 参数配置

CheckIPs 提供了灵活的参数配置，可根据实际需求调整检测行为：

![image-20250820110212000](https://s1.vika.cn/space/2025/08/20/5d87e3ff60d34a4ead3371f2af29c9e2)

| 参数         | 缩写  | 描述                             | 默认值               |
| ------------ | ----- | -------------------------------- | -------------------- |
| `--file`     | `-f`  | 指定 IP 列表文件路径             | `ip.txt`             |
| `--headless` | `-hl` | 启用无头浏览器模式（无界面运行） | `False`              |
| `--timeout`  | `-t`  | 页面加载超时时间（秒）           | `15`                 |
| `--retry`    | `-r`  | 失败重试次数                     | `3`                  |
| `--output`   | `-o`  | 自定义输出报告文件名             | 自动生成（含时间戳） |
| `--interval` | `-i`  | 检测间隔时间（秒）               | `2`                  |
| `--help`     | `-h`  | 显示帮助信息                     | -                    |

### 参数使用示例：

```bash
# 使用自定义IP文件并启用无头模式
python CheckIPs.py -f my_ips.txt -hl

# 设置超时时间为10秒，重试次数为5次
python CheckIPs.py -t 10 -r 5

# 自定义输出文件名
python CheckIPs.py -o my_report.xlsx
```

------



## 📝 使用教程

### 1. 准备 IP 列表

创建一个包含待检测 IP 地址的文本文件，命名为`ip.txt`：

```plaintext
# ip.txt示例内容
8.8.8.8
114.114.114.114:8080
203.0.113.1
198.51.100.7
```



> 💡 提示：每行一个 IP 地址，可以包含端口号（格式为 IP: 端口）

### 2. 运行 CheckIPs

```bash
# 基本运行方式
python CheckIPs.py
```

运行后，您将看到精美的工具横幅和实时检测进度：

```plaintext
  ____  _                  _     ___  ____        _  _  _ 
 / ___|| |__    ___   ___ | | __|_ _||  _ \  ___ | || || |
| |    | '_ \  / _ \ / __|| |/ / | | | |_) |/ __|| || || |
| |___ | | | ||  __/| (__ |   <  | | |  __/ \__ \|_||_||_|
\____||_| |_| \___| \___||_|\_\|___||_|    |___/(_)(_)(_)

==========================================================

                  Author: 一只鱼（Bifish）
                    Name: CheckIPs v1.0
                  Github: https://github.com/Bifish0

==========================================================

IP 地址检测工具 v1.0
=======================
检测网站: https://ipip.la/
开始时间: 2023-09-01 12:34:56

成功加载 4 个有效IP地址

正在检测 [1/4]: 8.8.8.8
国家/地区: 美国
类型: 原生IP ✅
...
```

![image-20250820101333227](https://s1.vika.cn/space/2025/08/20/ab30e0e774fe48799c749a19f20b005b)

### 3. 查看检测结果

- 程序运行时会在控制台实时显示检测进度和结果
- 检测完成后，会自动生成 Excel 格式的报告文件
- 报告文件命名格式：`ip_result_YYYYMMDD_HHMMSS.xlsx`
- 报告包含详细的 IP 信息和统计数据

![image-20250820101710530](https://s1.vika.cn/space/2025/08/20/b094814ede9d4179bcfd1e823522eb2c)

------

## 📝 详细使用方法

### 1. 基础使用流程

1. **准备 IP 列表**
   创建文本文件（默认`ip.txt`），每行填写一个 IP 地址：

   ```plaintext
   # 支持格式示例
   8.8.8.8
   114.114.114.114:8080
   203.0.113.1
   ```

2. **运行检测工具**

   ```bash
   # 基础命令（使用默认配置）
   python CheckIPs.py
   
   # 查看所有可用参数
   python CheckIPs.py --help
   ```

3. **查看检测结果**

   - 终端实时显示检测进度和结果（彩色区分 IP 类型）
   - 自动生成 Excel 报告（默认路径：当前目录）
   - 报告包含：IP 地址、国家 / 地区、使用类型、检测时间、状态

### 2. 高级使用场景

- **批量检测大量 IP**

  ```bash
  # 启用无头模式并延长间隔时间，避免触发限制
  python CheckIPs.py -f large_ip_list.txt -hl -i 3
  ```

- **自定义报告输出**

  ```bash
  # 指定输出路径和文件名
  python CheckIPs.py -o ./reports/2025_q3_ip_check.xlsx
  ```

- **调试模式运行**

  ```bash
  # 禁用无头模式，显示浏览器窗口便于调试
  python CheckIPs.py  # 默认不启用无头模式
  ```

## 📂 项目结构

```plaintext
CheckIPs/
├── CheckIPs.py          # 主程序文件
├── ip.txt                # IP列表文件（用户创建）
├── chromedriver.exe      # Chrome驱动（Windows）
├── chromedriver          # Chrome驱动（Linux/macOS）
├── requirements.txt      # 项目依赖列表（可选）
└── README.md             # 项目说明文档
```

------

## 🛠️ 依赖项

CheckIPs 基于以下优秀的开源库构建：

- `selenium` - 网页自动化测试框架，用于 IP 信息查询
- `colorama` - 终端彩色输出工具，美化控制台显示
- `openpyxl` - Excel 文件处理库，用于生成检测报告

------

## ⚠️ 注意事项

- ⚡ 务必确保 Chrome 浏览器与 ChromeDriver 版本匹配，版本不匹配会导致程序无法运行
- 🌐 网络环境会影响检测速度和成功率，请确保网络连接稳定
- 🔄 程序会自动处理一定的页面变化，但网站结构重大变更可能导致检测失败
- ⏱️ 大量 IP 检测可能需要较长时间，请耐心等待
- 📜 过于频繁的请求可能会被目标网站限制，程序已内置请求间隔调整机制
- 🚨 请遵守目标 IP 查询服务的使用条款，合理使用本工具

------

## 📜 许可证

本项目采用 MIT 许可证 - 详见[LICENSE](#)文件（如果提供）。

------

## 🙏 致谢

- 感谢[ipip.la](https://ipip.la/)提供的 IP 查询服务

------



<div align="center"><p>✨ 用CheckIPs，让IP检测变得简单高效 ✨</p><p>© 2025 一只鱼（Bifish）</p></div>
