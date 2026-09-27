---
name: md-table-fix
description: 修复 Markdown 转换文档（PDF→MD，Docling/PaddleX 等）中缺失表头分隔行的表格，补 "| --- |" 分隔行并清理单元格对齐空格，使表格在 Obsidian/VS Code/Typora 中正常渲染。当用户提到转换后的 md 表格乱码/错乱、表格缺分隔行、或要求批量修复 markdown 表格格式时使用。
---

# md-table-fix

修复 PDF→MD 转换产物中的表格格式。

## 何时使用
- 转换出的 md 里表格显示为一堆竖线文本（缺 `| --- |` 表头分隔行）
- 单元格内充满对齐空格
- 需要批量修复某个目录下所有 md

## 用法

```bash
# 修复单个或多个文件（自动在修改前写 .bak2 备份）
python fix_md_tables.py <file1.md> [file2.md ...]
```

## 逻辑
1. 逐行扫描连续的 `| ... |` 行块（跳过已是分隔行的块）；
2. 清理每行首尾 `|` 与单元格内对齐空格；
3. 在表格块第一行（表头）之后插入 `| --- | ... |` 分隔行；
4. 仅在确实修改时写回，原文件备份为 `<name>.md.bak2`。

## 集成建议（转换管线）
在 PDF→MD 转换器最终写库前调用等价逻辑；参考实现见
shencha-platform `server/lib/converter.js` 中的 `fixMarkdownTables()`（JS 版）。

## 注意
- 表头默认取表格块第一行；若原表无表头（纯数据表），分隔行会被插在第一行数据后，渲染上仍可接受但语义上是把首行当表头。
- 修复前务必确认已备份；脚本自带 .bak2 机制。
