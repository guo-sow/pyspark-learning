# pyspark-learning

## 概要 / 概述

### 日本語

このリポジトリは、PySpark を共同で学習するためのリポジトリです。

PySpark の基礎から実践的なデータ処理まで、ノート、サンプルコード、演習問題、プロジェクトを共有しながら学習していきます。

### 中文

这是一个用于共同学习 PySpark 的仓库。

从 PySpark 基础知识到实际数据处理，将学习过程中的笔记、示例代码、练习和项目整理并共享。

---

## 学習目標 / 学习目标

### 日本語

- PySpark の基本概念を理解する
- DataFrame / SQL / RDD の使い方を学ぶ
- データ処理の実践力を身につける
- パフォーマンス最適化について学ぶ
- データエンジニアリングの基礎を習得する

### 中文

- 理解 PySpark 的基本概念
- 学习 DataFrame / SQL / RDD 的使用方法
- 提升数据处理的实践能力
- 学习性能优化相关知识
- 打下数据工程基础

---

## 環境構築 / 环境搭建

### 推奨環境 / 推荐环境

| Tool    | Version |
| ------- | ------- |
| Python  | 3.12    |
| Java    | 17+     |
| PySpark | 4.x     |
| Git     | Latest  |
| VS Code | Latest  |

### Step 1：Python の確認 / 确认 Python

Python がインストールされているか確認します。

确认 Python 是否已经安装。

```bash
python --version
```

期待される出力 / 预期输出：

```text
Python 3.12.x
```

---

### Step 2：Java の確認 / 确认 Java

PySpark は内部で Java (JVM) を利用します。

PySpark 底层依赖 Java（JVM）运行。

Java 17 以上の LTS バージョン（Java 17 または Java 21 推奨）がインストールされているか確認します。

建议使用 Java 17 以上的 LTS 版本（推荐 Java 17 或 Java 21）。

```bash
java -version
```

期待される出力 / 预期输出：

```text
openjdk version "17.x.x"

または / 或者

openjdk version "21.x.x"
```

---

### Step 3：プロジェクトを Clone / 克隆项目

```bash
git clone https://github.com/guo-sow/pyspark-learning.git

cd pyspark-learning
```

---

### Step 4：Python 仮想環境を作成 / 创建 Python 虚拟环境

```bash
python -m venv .venv
```

成功すると `.venv` ディレクトリが作成されます。

成功后会生成 `.venv` 目录。

---

### Step 5：仮想環境を有効化 / 激活虚拟环境

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

成功すると、ターミナルの先頭に表示されます。

激活后，终端前面会出现：

```text
(.venv)
```

---

### Step 6：PySpark をインストール / 安装 PySpark

```bash
pip install pyspark
```

インストール後、バージョンを確認します。

安装完成后确认版本：

```bash
python -c "import pyspark; print(pyspark.__version__)"
```

---

### Step 7：動作確認 / 验证环境

新しいファイル `test.py` を作成します。

创建 `test.py` 文件：

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PySpark Learning") \
    .getOrCreate()

print(f"Spark Version: {spark.version}")

spark.stop()
```

実行：

```bash
python test.py
```

以下のような出力が表示されれば成功です。

如果看到类似输出，则表示环境配置成功。

```text
Spark Version: 4.x.x
```

---

## ディレクトリ構成 / 目录结构

```text
.
├── notebooks/    # Jupyter Notebook
├── examples/     # 示例代码
├── exercises/    # 练习题
├── datasets/     # 测试数据
└── README.md
```

---

## 学習ロードマップ / 学习路线

- PySpark 基礎（Basic）
- DataFrame
- Spark SQL
- RDD
- ETL
- Performance Tuning
- 実践プロジェクト（Projects）

---

## Contribution Rules / 协作规范

### 日本語

- `main` ブランチへ直接 push しない
- `feature` ブランチで作業する
- Pull Request を作成してからマージする
- 他のメンバーの PR を積極的にレビューする

### 中文

- 不要直接向 `main` 分支提交代码
- 请在 `feature` 分支进行开发
- 通过 Pull Request 合并代码
- 鼓励互相 Review 学习内容

---

## 備考 / 备注

このリポジトリは継続的に更新していく予定です。

本仓库将持续更新，记录学习过程与实践经验。
