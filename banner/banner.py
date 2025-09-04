#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_banner():
    # ANSI控制码
    BOLD = '\033[1m'
    RESET = '\033[0m'
    CLEAR_LINE = '\033[K'  # 清除当前行剩余内容

    # 配色方案
    COLOR = {
        "border": '\033[38;5;220m',  # 浅黄色边框
        "banner_main": '\033[38;5;45m',  # 亮青色主图案
        "author": '\033[38;5;46m',  # 绿色作者名
        "name_label": '\033[38;5;214m',  # 金黄色名称标签
        "github": '\033[38;5;129m',  # 紫红色Github链接
        "iphunter_base": '\033[38;5;220m',  # 亮黄主色
    }

    # 使用指定的图案
    banner_pattern = [
        r"____  _                  _     ___  ____        _  _  _ ",
        r" / ___|| |__    ___   ___ | | __|_ _||  _ \  ___ | || || |",
        r"| |    | '_ \  / _ \ / __|| |/ / | | | |_) |/ __|| || || |",
        r"| |___ | | | ||  __/| (__ |   <  | | |  __/ \__ \|_||_||_|",
        r" \____||_| |_| \___| \___||_|\_\|___||_|    |___/(_)(_)(_)"
    ]

    # 计算装饰线长度
    max_banner_width = max(len(line) for line in banner_pattern)
    border_length = max_banner_width + 6  # 左右边距

    # 顶部装饰线
    print(f"{BOLD}{COLOR['border']}{'=' * border_length}{RESET}")
    print()

    # 打印Banner（取消立体效果）
    for line in banner_pattern:
        print(f"{BOLD}{COLOR['banner_main']}{line}{CLEAR_LINE}{RESET}")

    print()

    # 中间分隔线
    print(f"{BOLD}{COLOR['name_label']}{'-' * border_length}{RESET}")
    print()

    # 信息区
    info_indent = "  "
    # 作者信息
    print(f"{info_indent}{COLOR['author']}Author: {BOLD}bifish{RESET}")

    # 名称信息（取消立体效果）
    print(
        f"{info_indent}{COLOR['name_label']}Name: {BOLD}{COLOR['iphunter_base']}IPHunter{COLOR['name_label']} v1.0{RESET}")

    # Github信息
    print(f"{info_indent}{COLOR['github']}Github: {BOLD}https://github.com/Bifishone{RESET}")

    print()

    # 底部装饰线
    print(f"{BOLD}{COLOR['border']}{'=' * border_length}{RESET}")


if __name__ == "__main__":
    print_banner()