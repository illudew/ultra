# 研途 · 科研行动指南

中文、响应式静态网站，包含选题、文献检索、研究设计、伦理、数据采集、分析、图表、写作、投稿和同行评审十个阶段，以及期刊分类、官方查询入口和科研工具。

## 本地运行

无需安装依赖。在仓库目录运行：

```sh
python3 -m http.server 8000
```

浏览器访问 `http://localhost:8000`，也可以直接打开 `index.html`。网页不依赖外部字体或脚本服务。

## 功能

- 科研流程全文搜索、阶段展开与快捷定位。
- 30 项行动清单，使用浏览器 localStorage 保存进度，可手动重置；不会上传至服务器。
- 按研究范围、内容类型、出版模式、语言与地区筛选期刊分类。
- 移动端适配、键盘导航与减少动画偏好支持。

## 部署

可直接部署到任意静态托管服务。GitHub Pages 可在仓库 **Settings → Pages** 中选择 **Deploy from a branch**，分支选择 `main`，目录选择 `/ (root)`。推送代码本身不会自动开启 Pages。

## 内容说明

内容是跨学科的通用学习指引，不代替导师指导、伦理审查或学科规范。期刊举例不构成质量排名、投稿推荐或收录保证。收录、分区、费用和投稿政策可能变更，应通过期刊及数据库官方来源核验；本网站未声称提供实时指标。清单仅辅助管理，不表示完成后自动满足所有研究要求。

主要参考入口：

- [EQUATOR 报告规范](https://www.equator-network.org/)
- [COPE 出版伦理](https://publicationethics.org/)
- [Think. Check. Submit. 选刊指南](https://thinkchecksubmit.org/)
- [Clarivate Master Journal List](https://mjl.clarivate.com/)
- [DOAJ 开放获取目录](https://doaj.org/)
- [OSF 开放研究平台](https://osf.io/)
