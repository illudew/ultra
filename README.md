# Ultra / 研途 · 科研方法与实践

中文、响应式静态网站，包含选题、文献检索、研究设计、伦理、数据采集、分析、图表、写作、投稿和同行评审十个阶段，以及期刊分类、官方查询入口和科研工具。

首批方法库提供4个完整方法单元、5份可填写模板与1个可复现物理教学案例。所有页面为静态HTML，无需打包或CDN依赖。站点介绍位于 `about.html`，不会再以全屏遮罩拦截章节链接。

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
- `methods/index.html`：研究问题与选题书、文献检索与证据矩阵、可复现记录与数据管理、不确定性与结果报告。
- `templates/index.html`：选题书、文献矩阵、研究日志、数据字典、报告核查表，可下载Markdown或CSV自行填写。
- `case/pendulum.html`：从明确标记的合成数据出发，用Python标准库完成单摆周期拟合、残差与条件标准不确定度分析。

原有清单的 `yantu-progress-v1` 存储键、30项顺序和下标未改变。新增方法页不计入这30项；它们当前不记录阅读完成度。

## 方法正文维护

方法内容源文件为 `content/methods.json`。修改后可在仓库根目录运行：

```sh
python3 tools/build_methods.py
```

提交生成的 `methods/*.html` 即可静态部署，访客无需运行Python。

## 验证教学案例

Python 3，无第三方依赖：

```sh
python3 case/pendulum/generate.py
python3 case/pendulum/fit.py --verify
```

第一条命令只核对CSV是否与公式和固定扰动序列逐字节一致；第二条执行拟合并核对已发布的教学结果范围。预期21条记录、7组长度，`g ≈ 9.809277602 m/s²`，条件OLS标准不确定度约 `0.011414829 m/s²`。数据不是实验测量，模型限制、异方差与未纳入的系统项见案例页和 `case/pendulum/README.md`。

网页检查应覆盖：首页到方法/模板/案例的往返、下载文件可读取、手机公式/表格局部滚动、原有30项清单刷新保存与期刊筛选。网站不要求访问外部链接才能阅读正文；外部参考入口不代表实时数据库状态。

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
