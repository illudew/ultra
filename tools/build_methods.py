#!/usr/bin/env python3
"""Generate dependency-free static method pages from content/methods.json."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def page(title, main, prefix="../", description="Ultra / 研途科研方法、模板与可复现案例"):
    return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{html.escape(description, quote=True)}"><title>{html.escape(title)} · Ultra / 研途</title><link rel="stylesheet" href="{prefix}assets/style.css"><link rel="stylesheet" href="{prefix}assets/library.css"></head><body><header class="library-header"><a class="brand" href="{prefix}index.html"><span class="logo">研</span>Ultra / 研途</a><nav aria-label="主导航"><a href="{prefix}index.html#roadmap">科研路线</a><a href="{prefix}methods/index.html">方法课程</a><a href="{prefix}templates/index.html">模板下载</a><a href="{prefix}case/pendulum.html">可复现案例</a><a href="https://illudew.github.io/">知识地图 ↗</a></nav></header><main class="library-main">{main}</main><footer><a class="brand" href="{prefix}index.html"><span class="logo">研</span>Ultra / 研途</a><p>让问题、方法与证据彼此对应。</p><a href="{prefix}about.html">站点介绍</a></footer></body></html>'''


def build():
    methods = json.loads((ROOT / "content/methods.json").read_text())
    cards = []
    for method in methods:
        name = method["id"]
        title = html.escape(method["title"])
        toc = ''.join(f'<a href="#section-{i}">{html.escape(s["title"])}</a>' for i, s in enumerate(method["sections"]))
        content = ''.join(f'<section id="section-{i}"><h2>{html.escape(s["title"])}</h2>{s["html"]}</section>' for i, s in enumerate(method["sections"]))
        main = f'''<nav class="crumbs" aria-label="面包屑"><a href="../index.html">Ultra</a><span>/</span><a href="index.html">方法课程</a><span>/</span><span>{title}</span></nav><div class="library-lead"><span class="library-tag">{html.escape(method["kicker"])}</span><h1>{title}</h1><p>{html.escape(method["summary"])}</p></div><div class="reading-layout"><aside class="reading-toc" aria-label="本文目录"><strong>本文目录</strong>{toc}</aside><article class="reading-body"><div class="method-prereq"><b>开始前：</b>{'；'.join(html.escape(p) for p in method["prerequisites"])}</div>{content}<div class="library-bridge"><a href="index.html">← 返回方法课程</a><a href="../case/pendulum.html">用单摆案例练习 →</a></div></article></div>'''
        (ROOT / f"methods/{name}.html").write_text(page(method["title"], main, description=method["summary"]))
        cards.append(f'<article class="library-card"><span class="meta">{html.escape(method["kicker"])}</span><h2>{title}</h2><p>{html.escape(method["summary"])}</p><a href="{name}.html">阅读完整方法 →</a></article>')
    main = '''<nav class="crumbs" aria-label="面包屑"><a href="../index.html">Ultra</a><span>/</span><span>方法课程</span></nav><div class="library-lead"><div class="eyebrow">METHODS / 从理解到执行</div><h1>把科研方法，落实到一份产物。</h1><p>首批四个方法单元覆盖问题、文献、记录和结果。每篇有具体例子、执行步骤与完成标准；理论、实验和计算研究可以按需要选择。</p></div><div class="library-grid">'''+''.join(cards)+'''</div><div class="status-row">首批已发布 4 个方法单元 · 后续将补充理论推导、实验设计、数值验证与写作专题。当前页面不记录课程完成进度。</div><div class="library-bridge"><a href="../templates/index.html">下载配套模板 →</a><a href="../case/pendulum.html">查看可复现案例 →</a></div>'''
    (ROOT / "methods/index.html").write_text(page("方法课程", main))
    return len(methods)


if __name__ == "__main__":
    print(f"Generated {build()} method units and their index.")
