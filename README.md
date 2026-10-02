# amoko

个人介绍单页。黑白蓝三色，可切换明暗主题。

**线上**：https://derecat.github.io/amoko/

## 内容

| 文件 | 说明 |
| --- | --- |
| `index.html` | 主站（deluxe 版）。ASCII 3D 海洋背景 + 明暗主题切换 + 鸣谢页 |
| `basics.html` | 早期简洁版，保留作对照 |
| `fonts-local.css` + `fonts/` | 自托管字体（Cormorant Garamond / Inter），离线可用，无需外链 |
| `logos/` | 鸣谢页所用品牌图标源文件（已内联进 HTML，此处仅作留存） |
| `build_credits.py` | 从 `logos/` 生成内联 SVG 片段 |
| `fetch_fonts.py` | 拉取并本地化 Google Fonts |

## 技术要点

- **海洋**：canvas 逐字符渲染的高度场，四个正弦波叠加；射线与海面迭代求交得到每格深度、法线和光照；按深度雾化、底部渐隐向底色柔化。明暗两套「黑白蓝」调色板。
- **主题切换**：由近及远推进的「深度色浪」，双调色板按波前 `smoothstep` 混合，浪峰带高光与字符加密。
- **动画**：全部 CSS 关键帧（跑在主线程外），JS 只负责加 class；入场采用分段缓动（`0.16, 1, 0.3, 1` 出场 / `0.45, 0, 0.55, 1` 过渡）与 `clip-path` 遮罩揭示。
- **降级**：`prefers-reduced-motion` 下海洋静止为单帧、幕布与装饰隐藏、其余降为短淡入。
