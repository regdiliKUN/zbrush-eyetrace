# EyeTrace 眼睛描图 — ZBrush 描图层插件

在 ZBrush 里像 Photoshop 那样“把旧草稿垫在下面、降低透明度、在新图层上描”。专为手办眼睛水贴（waterslide decal）绘制设计：

- 旧稿直接显示在模型表面，**随模型任意旋转**，任何角度都能描；
- 旧稿深浅可随时调整，描好的线不受影响；
- 描完一键清除旧稿，只留下新线条；
- 支持单独的眼睛面片，也支持和脸连在一起的眼睛（用遮罩限定区域）。

已在 **ZBrush 2022.0.5** 和 **ZBrush 2025.0.1**（Windows）实机测试。

> English: An overlay-tracing helper for ZBrush. It fades an old polypaint draft on the mesh, creates an ink layer to trace on from any angle, lets you re-adjust the draft opacity at any time, and clears the draft when you are done. Tested on ZBrush 2022.0.5 and 2025.0.1 (Windows) with the Chinese UI. An **English UI build** is in [`dist/en/EyeTrace.txt`](dist/en/EyeTrace.txt) (menu: ZPlugin > EyeTrace); install it the same way, to `ZStartup\Macros\EyeTrace\EyeTrace.txt`. The English build has the same code as the Chinese one, but it has not been tested inside ZBrush yet, so please report anything odd (e.g. truncated button labels) in Issues.

> 觉得好用的话，点个 ⭐ Star 支持一下 · If you find it useful, please give it a ⭐ Star!

## 安装

1. 到 [Releases](../../releases/latest) 下载 `EyeTrace_v1.0.0.zip` 并解压（或直接下载 [`dist/EyeTrace.txt`](dist/EyeTrace.txt)；英文界面版是 [`dist/en/EyeTrace.txt`](dist/en/EyeTrace.txt)，两个只装一个）。
2. 放到 ZBrush 安装目录下：
   ```
   <ZBrush 安装目录>\ZStartup\Macros\EyeTrace\EyeTrace.txt
   ```
3. 重启 ZBrush。菜单 **Z插件（ZPlugin）→ 眼睛描图** 会出现（ZBrush 启动时自动编译，无需其他步骤）。

卸载：删除 `ZStartup\Macros\EyeTrace` 文件夹。

## 使用

| 按钮 | 作用 |
|---|---|
| 旧稿可见度（滑杆） | 旧稿保留的百分比，0 = 看不到，100 = 原样 |
| 描线强度（滑杆） | 你希望描线时使用的 Rgb 强度，默认 100 |
| 画笔复位 | 一键恢复描线状态：上色模式、Rgb 强度＝描线强度、黑色、`ETInk` 继续录制 |
| 开始描图 | 以当前主颜色为干净底色，淡化旧稿，新建描线图层 `ETInk` |
| 应用可见度 | 按滑杆重新设置旧稿深浅（描线不受影响） |
| 恢复旧稿 | 把旧稿按原样还原到模型上（描线图层保留） |
| 完成描图 | 旧稿区域填回干净底色，只留下描线；可选删除备份 |
| 使用说明 | 显示简要说明 |

### 完整流程

1. **准备**：选中画有旧稿的子工具，按 **T** 进入编辑模式。
   眼睛和脸连在一起时，先用遮罩把眼睛以外的区域遮住（插件只处理**未遮罩**区域）；单独的眼睛面片不用遮罩。
2. **设干净底色**：顶部菜单 **色彩** → 把 **R、G、B** 都设为 **255**（纯白）。如果眼睛底色是肤色，就设成肤色。
3. **开始描图**：打开 **Z插件 → 眼睛描图**，“旧稿可见度”保持 30（或按需调整），点 **开始描图**。
   - 确认框会显示读到的底色，**确认是 255, 255, 255 再点“继续”**（如果是 0, 0, 0 就点“取消”，回到第 2 步）。
   - 如果画笔的 Rgb 强度和“描线强度”不一致，会弹框让你选“改为 100”或“保持”。
   - 完成后旧稿变淡，画笔自动切成黑色上色模式。
4. **描线**：直接在模型上描，可以随意旋转、任意角度。线画在 `ETInk` 图层上，不要去点其他图层。画笔发虚或画不上去时，点 **画笔复位**。
5. **调深浅（可选）**：拖动“旧稿可见度”，点 **应用可见度**。描好的线不受影响，可以借此检查有没有漏描。
6. **完成**：点 **完成描图**，旧稿被清成底色，只剩描线。弹框里选 **删除备份**（不再需要旧稿）或 **保留备份**（之后还能点 **恢复旧稿** 找回）。
7. **下次再用前**：完成后主颜色仍是黑色，记得先按第 2 步把底色设回白色。

## Rgb 强度提醒

- 点“开始描图”或“应用可见度”时，如果画笔的 Rgb 强度和“描线强度”滑杆不一致，会弹框提醒，并给出 **[改为 100] / [保持 50]** 两个按钮，由你决定，插件不会强制修改。
- Rgb 强度低于 100 时，线条会发虚，颜色也会混进下面的旧稿。
- 想故意用低强度描线：点“保持”，并把“描线强度”滑杆调成同样的数值，以后就不会再问。
- Zadd 开着会改变模型形状，插件始终会自动关闭它。
- 画笔发虚、颜色不对或画不上去时，点 **画笔复位**。

## 注意事项

- 描线时 `ETInk` 图层需处于选中且录制（REC）状态；插件每次操作后会自动恢复。若手动点了其他图层，请重新点选 `ETInk`。
- 开始描图后不要改动网格拓扑（Dynamesh / ZRemesher / 增删面），否则图层和备份失效。
- “开始描图”会把子工具复制一份隐藏备份（名称以 `ETDraft` 结尾），用于调整深浅和恢复旧稿；高面数模型复制和投射需要等待数秒到数十秒。
- 颜色存在顶点上，眼睛区域面数越密，线条越清晰。
- 完成后 `ETInk` 图层仍保留，可用 工具 › 图层 › 全部烘焙（Bake All）合并。
- 修改插件文件后需**重启 ZBrush**（“重新加载所有宏”不会刷新 Z插件 面板）。

## 工作原理

- 旧稿留在底色上；“开始/应用可见度”时用干净颜色以 `(100 - 可见度)%` 的强度执行“填充对象”，把旧稿淡化。
- 描线画在独立图层上。ZBrush 图层中的绘制颜色是绝对值，所以底下的旧稿怎么变化，描线颜色都不受影响（实测：旧稿关闭后交叉点仍为 (5,5,5) 黑色）。
- 调整可见度时，先从隐藏备份用 ProjectAll 把旧稿投射回来（其他子工具临时隐藏，PA Blur 临时设为 0），再重新淡化。
- “填充对象 / ProjectAll”在图层录制时不会写入底色，所以插件在处理底色前会临时关闭 `ETInk` 的录制并隐藏它，处理完再恢复。两者都尊重遮罩。

## 从源码构建

源码 [`EyeTrace.src.txt`](EyeTrace.src.txt) 使用 UTF-8，中文写在 `CN("...")` 中。ZBrush 的 ZScript 编译器会丢弃非 ASCII 字符，因此用 [`build.py`](build.py) 把中文转换为运行时 `StrFromAsc` 字节拼接，生成纯 ASCII 的 `dist/EyeTrace.txt`：

```
python build.py                              # 正式版（中文界面）
python build.py --lang en                    # 英文界面版 -> dist/en/EyeTrace.txt，文案在 strings_en.py
python build.py <日志路径> <宏按钮绑定的例程>   # 调试版：写日志，宏菜单按钮直接调用指定例程
```

开发中踩过的 ZScript 坑（ZBrush 2025.0.1）：

- 参数里嵌套“函数结果再运算”（如 `[StrExtract,s,a,[StrLength,s]-1]`）会静默中断，需先存入变量。
- 数值变量名避免下划线。
- 图层项 `IModGet`：1 = 录制中，2 = 显示但不录制，0 = 隐藏；`IClick` 在 `(W-24, H/2)` 切换 REC，`(W-5, H/2)` 切换显示。

## 许可证

[MIT](LICENSE)
