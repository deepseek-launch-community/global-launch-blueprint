# 实验性案例池

这里是社区探索SRCP协议的前沿阵地。我们鼓励大胆尝试，诚实记录困惑。

## 目录结构
- `by-contributor/` - **推荐提交位置**，按贡献者组织
- `by-topic/` - 按主题组织（目前为空，未来自动分类）

## 如何提交你的实验案例？
1. **在 `by-contributor/` 下创建你的专属目录**
   - 目录名：你的GitHub用户名（如 `artemqa89`）
   - 如果已存在，直接进入你的目录

2. **为每个案例创建子目录**
   - 命名：`YYYYMMDD-简短描述`（如 `20240119-math-reasoning`）
   - 包含三个核心文件（见下方）

3. **必须包含的文件**
   - `original-conversation.md` - 原始对话/推理文本
   - `srcp-attempt.json` - 你的SRCP转换尝试（JSON格式）
   - `pain-report.md` - **困惑报告**（必须！模板见下方）

4. **可选文件**
   - `notes.md` - 你的额外笔记
   - `screenshots/` - 相关截图目录

## 困惑报告模板（必须！）
在 `pain-report.md` 中，请包含以下内容：

````markdown
## 案例：{简短描述}
**原始文件**：`original-conversation.md`
**SRCP尝试**：`srcp-attempt.json`

### 转换难点（请详细说明）
1.  **最难填写的字段**：[哪个字段？为什么难？]
2.  **最模糊的概念**：[SRCP的哪个概念不清楚？]
3.  **丢失的信息**：[什么重要信息无法在SRCP中表达？]

### 具体建议
- 协议改进：[你的具体建议]
- 文档补充：[需要什么说明？]
- 其他想法：[自由发挥]

### 自助过程反馈
[对 conversion-starter.md 指南的反馈]
