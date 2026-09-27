# md-table-fix

修复 PDF→MD 转换文档中缺失表头分隔行的 Markdown 表格。

- `SKILL.md` — Codex 技能说明
- `fix_md_tables.py` — 修复脚本（零依赖，Python 3.8+）

## 快速开始

```bash
python fix_md_tables.py 转换文档1.md 转换文档2.md
```

修复前自动备份为 `*.md.bak2`。

## 背景

Docling / PaddleX 等 PDF→MD 转换器输出的表格常缺少 Markdown 表头分隔行
（`| --- |`），导致 Obsidian、VS Code 等渲染器不识别表格。本工具自动补齐
分隔行并清理单元格对齐空格。
