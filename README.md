<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-mcpic

_✨ 随机发送 MC 建筑图片 ✨_

<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/wlm3201/nonebot-plugin-mcpic.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-mcpic">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-mcpic.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

根据指令从爬好的数据库随机查询指定数量 MC 建筑图片链接下载并发送

支持直连，无需代理

[Demo](https://wlm3201.github.io/nonebot-plugin-mcpic/) (建议配合 [Sheas-Cealer](https://github.com/SpaceTimee/Sheas-Cealer))

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-mcpic

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-mcpic

</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-mcpic

</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-mcpic

</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-mcpic

</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_mcpic"]

</details>

## 🎉 使用

### 指令表

mc|MC|建筑+图片数量

e.g: 建筑, mc20

### 效果图

![效果图](eg.png)
