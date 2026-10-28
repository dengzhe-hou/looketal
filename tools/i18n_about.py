"""About page text in English, Japanese and Simplified Chinese (see i18n.py for the rest of the site text)."""

ABOUT = {
"en": """<header class="phead"><div class="eyebrow">About</div><h1>About {site}</h1>
<p class="lede">A reference library of academic web pages, for researchers and their coding agents.</p></header>
<section class="prose"><h2>What is included</h2>
<p><b>{n_proj} paper project pages</b>, ten per venue and year: NeurIPS, ICML, ICLR, CVPR and ACL in 2025 and 2026, ICCV 2025, ECCV 2026, SIGGRAPH 2025 and 2026, CoRL 2025, CHI 2026 and EMNLP 2025, plus ten journal papers from TMLR, TPAMI, JMLR and Nature-family journals (2025 and 2026). Candidates come from arXiv comments that state the acceptance and link a project page; a page had to load, and workshop papers were left out. That gave a pool of 907 pages. Most venue-years had 40 or more candidates; CHI 2026 had 19 and EMNLP 2025 had 37.</p>
<p><b>{n_res} researcher homepages</b> from a pool of 236, drawn by three fixed rules. The first covers ACM Turing Award laureates (2018–2025) and first or last authors of Best Paper, Outstanding Paper and Test of Time awards at NeurIPS, ICML, ICLR, CVPR and ACL (2023–2025). The second covers first and last authors of ACL Outstanding Papers (2023–2025). The third covers cognitive science and computational neuroscience: Rumelhart Prize laureates (2010–2025), Glushko Dissertation Prize winners (2018–2025), authors of the CogSci Computational Modeling Prizes (2020–2025) and CCN keynote speakers (2023–2025). Only personal pages count; institutional directory pages, Google Scholar and LinkedIn profiles do not.</p>
{readme}<h2>How pages were chosen</h2>
<p>By visual design only, in two rounds. Every candidate was screenshotted at 1440×900. In the first round a model reviewer looked at every first screen in a pool and kept 20; in the second it looked at a 2700px-tall capture of each and kept 10. The first researcher pool was judged as one group, keeping 60 and then 30. The criteria were typography, a look of its own beyond template defaults, layout and rhythm, how the work is presented, and polish. Research content, venue and fame were ignored, and near-ties went to the page that added a style not yet picked. Pages that showed a loader, a blank screen or a bot wall could not be judged and were dropped. The reason for each pick is on its style page.</p>
<h2>How a DESIGN.md is made</h2>
<p>From the rendered page first. A headless browser reports the computed styles of the title, headings, body, buttons and containers, the fonts that actually loaded, the first-viewport anatomy in DOM order, and the color share of the first screen. The page's stylesheet and markup then supply selectors, hover and responsive rules. When the CSS and the render disagree, the render wins. Each file follows a fixed section order (Overview, First Viewport, color, type and spacing tokens, Layout Metrics, Components, Page Modules, guidance for other content, an agent prompt guide and a Quick Start) and passes an automatic check that every color used in the prompts appears in the token table. {n_rend} of {n_all} entries were checked against the rendered page. DESIGN.md files are written in English only, so that every reader and every coding agent works from the same text.</p>
<p>The method was revised after a reconstruction test. Builders given only a DESIGN.md and different content rebuilt five pages, a blind judge tried to match each rebuild to its original, and an analyst scored similarity from 1 to 5 against the live page. With the first version, written from CSS alone, the judge matched all five, but overall similarity averaged 3.0 (2 to 4), mostly because of values the CSS declared and the page never showed. With the current version, the same test on the same five pages again matched all five and averaged 4.0 (all five scored 4). A separate audit of ten other files found 4 wrong values in about 129 checked claims; those were corrected.</p>
<h2>Screenshots</h2>
<p>Each entry shows an above-the-fold screenshot of the original page, reduced to 1200×750, credited to the authors and linked back to the live page. Screenshots are shown for reference and comparison, the same way design reference libraries do. DESIGN.md files describe visual style; they are not official guides of the authors.</p>
<h2>License and citation</h2>
<p>The DESIGN.md files, the selection and the site text are under <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener">CC BY-NC 4.0</a>. You can reuse them for non-commercial work with credit to Look et al. (Dengzhe Hou). For commercial use, ask first. The code is MIT. Screenshots belong to the pages' authors and are not covered by either license. To cite the library, use Hou, D. (2026), <i>Look et al.: A Design Library of Academic Web Pages for Humans and AI Agents</i>, Zenodo, <a href="https://doi.org/10.5281/zenodo.23718470" target="_blank" rel="noopener">doi:10.5281/zenodo.23718470</a>.</p>
<h2>Removal</h2>
<p>If you are an author and want your page or screenshot removed or corrected, {removal} and it will be taken down. Requests are handled by hand, usually within a few days.</p></section>""",

"ja": """<header class="phead"><div class="eyebrow">概要</div><h1>{site} について</h1>
<p class="lede">学術ウェブページの参考資料集です。研究者と、研究者が使うコーディングエージェントのために作りました。</p></header>
<section class="prose"><h2>収録しているもの</h2>
<p><b>論文プロジェクトページ {n_proj} 件</b>。会議と年ごとに 10 件ずつで、NeurIPS、ICML、ICLR、CVPR、ACL の 2025 年と 2026 年、ICCV 2025、ECCV 2026、SIGGRAPH 2025 と 2026、CoRL 2025、CHI 2026、EMNLP 2025 を対象にしています。これに TMLR、TPAMI、JMLR、Nature 系ジャーナルの論文(2025 年と 2026 年)10 件を加えました。候補は、採択を明記しプロジェクトページへリンクしている arXiv のコメントから集めました。ページが表示できることを条件にし、ワークショップ論文は除きました。候補は全部で 907 件です。多くの会議と年で候補は 40 件以上ありましたが、CHI 2026 は 19 件、EMNLP 2025 は 37 件でした。</p>
<p><b>研究者ページ {n_res} 件</b>。候補 236 人から、三つの決まった規則で集めました。一つ目は ACM チューリング賞の受賞者(2018–2025 年)と、NeurIPS、ICML、ICLR、CVPR、ACL の Best Paper、Outstanding Paper、Test of Time 賞の筆頭著者または最終著者(2023–2025 年)です。二つ目は ACL Outstanding Paper の筆頭著者と最終著者(2023–2025 年)です。三つ目は認知科学と計算論的神経科学の分野で、ルーメルハート賞の受賞者(2010–2025 年)、グラシュコ博士論文賞の受賞者(2018–2025 年)、CogSci 計算モデリング賞の著者(2020–2025 年)、CCN の基調講演者(2023–2025 年)です。対象は個人のページだけで、所属機関の名簿ページ、Google Scholar、LinkedIn は含めていません。</p>
{readme}<h2>選び方</h2>
<p>見た目のデザインだけで、二段階で選びました。候補はすべて 1440×900 でスクリーンショットを撮りました。一段階目では、モデルの審査役が候補群の最初の画面をすべて見て 20 件に絞り、二段階目では高さ 2700px のキャプチャを見て 10 件を選びました。最初の研究者候補はひとまとまりで審査し、60 件、さらに 30 件に絞りました。基準は、タイポグラフィ、テンプレートの既定値にとどまらない独自の見た目、レイアウトとリズム、研究の見せ方、仕上がりの丁寧さです。研究内容、会議名、知名度は考慮していません。ほぼ同点のときは、まだ選ばれていないスタイルを加えるページを優先しました。読み込み中の画面、白い画面、ボット対策の画面しか撮れなかったページは判断できないため除きました。それぞれの選定理由は各スタイルのページに載せています。</p>
<h2>DESIGN.md の作り方</h2>
<p>まず表示されたページから読み取ります。ヘッドレスブラウザで、タイトル、見出し、本文、ボタン、コンテナの計算済みスタイル、実際に読み込まれたフォント、最初の画面の構成(DOM の順)、最初の画面の色の割合を取得します。そのうえで、ページのスタイルシートとマークアップからセレクタ、ホバー、レスポンシブの規則を補います。CSS と表示結果が食い違うときは表示結果を採ります。各ファイルは決まった節の順番(Overview、First Viewport、色・文字・余白のトークン、Layout Metrics、Components、Page Modules、ほかの内容に使うときの指針、エージェント向けプロンプトの手引き、Quick Start)に従い、プロンプトで使う色がすべてトークン表にあるかを自動で確認しています。{n_all} 件中 {n_rend} 件は表示されたページと照合しました。DESIGN.md は英語だけで書いています。読む人もコーディングエージェントも、同じ一つの文章を使えるようにするためです。</p>
<p>方法は再現テストのあとで改めました。DESIGN.md と別の内容だけを渡された制作役が 5 ページを作り直し、元ページを知らない判定役が作り直したページと元ページを対応づけ、分析役が実際のページとの類似度を 1 から 5 で採点しました。CSS だけから書いた最初の版では、判定役は 5 件すべてを正しく対応づけましたが、類似度の平均は 3.0(2 から 4)でした。主な原因は、CSS には書かれていても実際のページには表示されない値でした。現在の版で同じ 5 ページを同じ方法でテストすると、やはり 5 件すべてが対応づけられ、類似度の平均は 4.0(5 件とも 4)になりました。別に行った 10 ファイルの監査では、確認した約 129 の記述のうち 4 件の値が間違っており、修正済みです。</p>
<h2>スクリーンショット</h2>
<p>各項目には元ページの最初の画面のスクリーンショットを 1200×750 に縮小して載せ、著者の著作物であることを明記し、元ページにリンクしています。ほかのデザイン参考サイトと同じく、参考と比較のために掲載しています。DESIGN.md は見た目のスタイルを記述したもので、著者による公式のガイドではありません。</p>
<h2>ライセンスと引用</h2>
<p>DESIGN.md、選定の結果、サイトの文章は <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener">CC BY-NC 4.0</a> です。Look et al.(Dengzhe Hou)の名前を示せば、非営利の目的で再利用できます。営利目的で使う場合は事前にご相談ください。コードは MIT です。スクリーンショットは各ページの著者のもので、どちらのライセンスの対象でもありません。引用するときは Hou, D. (2026), <i>Look et al.: A Design Library of Academic Web Pages for Humans and AI Agents</i>, Zenodo, <a href="https://doi.org/10.5281/zenodo.23718470" target="_blank" rel="noopener">doi:10.5281/zenodo.23718470</a> を使ってください。</p>
<h2>削除の依頼</h2>
<p>著者の方で、ページやスクリーンショットの削除や修正を希望される場合は、{removal}から依頼してください。掲載を取り下げます。依頼は手作業で対応しており、通常は数日以内に処理します。</p></section>""",

"zh": """<header class="phead"><div class="eyebrow">关于</div><h1>关于 {site}</h1>
<p class="lede">一个学术网页参考库，供研究者和他们使用的编程 agent 参考。</p></header>
<section class="prose"><h2>收录了什么</h2>
<p><b>{n_proj} 个论文项目页</b>，每个会议每年 10 个，覆盖 NeurIPS、ICML、ICLR、CVPR、ACL 的 2025 年和 2026 年，以及 ICCV 2025、ECCV 2026、SIGGRAPH 2025 和 2026、CoRL 2025、CHI 2026、EMNLP 2025，另外还有 10 篇期刊论文，来自 TMLR、TPAMI、JMLR 和 Nature 系列期刊(2025 年和 2026 年)。候选来自 arXiv 的论文备注，备注里要写明已被录用并链接项目页；页面必须能打开，workshop 论文不收。候选共 907 个。大多数会议每年有 40 个以上候选，CHI 2026 只有 19 个，EMNLP 2025 有 37 个。</p>
<p><b>{n_res} 个研究者主页</b>，从 236 位候选中选出，候选按三条固定规则收集。第一条是 ACM 图灵奖得主(2018–2025 年)，以及 NeurIPS、ICML、ICLR、CVPR、ACL 的 Best Paper、Outstanding Paper、Test of Time 奖的第一作者或最后作者(2023–2025 年)。第二条是 ACL Outstanding Paper 的第一作者和最后作者(2023–2025 年)。第三条来自认知科学和计算神经科学，包括鲁梅尔哈特奖得主(2010–2025 年)、格鲁什科博士论文奖得主(2018–2025 年)、CogSci 计算建模奖的作者(2020–2025 年)和 CCN 大会主旨报告人(2023–2025 年)。只收个人主页，机构的人员名录页、Google Scholar 和 LinkedIn 不算。</p>
{readme}<h2>怎么选的</h2>
<p>只看视觉设计，分两轮选。每个候选都按 1440×900 截图。第一轮由模型评审看完一组候选的首屏，留下 20 个；第二轮看每个页面高 2700px 的长截图，选出 10 个。第一批研究者候选作为一整组评审，先留 60 个，再选 30 个。标准是字体排印、超出模板默认值的独特面貌、布局和节奏、研究成果的展示方式，以及完成度。研究内容、会议和知名度都不考虑；两个页面不相上下时，优先选能带来新风格的那个。只截到加载动画、空白页或反爬页面的候选无法评判，直接去掉。每个页面的入选理由写在它的风格页上。</p>
<h2>DESIGN.md 怎么写</h2>
<p>先看实际渲染出来的页面。用无头浏览器读取标题、各级标题、正文、按钮和容器的计算样式，实际加载的字体，首屏结构(按 DOM 顺序)，以及首屏各颜色所占比例。然后再从页面的样式表和标记里补充选择器、悬停和响应式规则。CSS 和渲染结果不一致时，以渲染结果为准。每个文件都按固定的章节顺序写(Overview、First Viewport、配色/字体/间距 token、Layout Metrics、Components、Page Modules、套用到其他内容时的建议、给 agent 的提示词指南和 Quick Start)，并自动检查提示词里用到的每个颜色是否都在 token 表里。{n_all} 条里有 {n_rend} 条对照过实际渲染的页面。DESIGN.md 只写英文版，这样所有读者和编程 agent 用的都是同一份文本。</p>
<p>方法在一次还原测试之后做过修订。只拿到 DESIGN.md 和另一份内容的制作者重做了 5 个页面，一个不知道原页面的评判者把重做的页面和原页面配对，再由分析者对照线上页面按 1 到 5 分打相似度。用只根据 CSS 写的第一版时，评判者 5 个全部配对正确，但相似度平均只有 3.0(2 到 4)，主要原因是 CSS 里写了、页面上却没有显示的值。用现在的版本，在同样 5 个页面上做同样的测试，仍然全部配对正确，相似度平均 4.0(5 个都是 4 分)。另外抽查了 10 个文件，约 129 处说明里有 4 处数值写错，已经改正。</p>
<h2>截图</h2>
<p>每条都展示原页面首屏的截图，缩小到 1200×750，注明版权归作者所有，并链接回原页面。和其他设计参考网站一样，截图只用于参考和比较。DESIGN.md 描述的是视觉风格，不是作者发布的官方指南。</p>
<h2>许可与引用</h2>
<p>DESIGN.md 文件、入选名单和网站文字采用 <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener">CC BY-NC 4.0</a> 许可。注明 Look et al.(Dengzhe Hou)即可用于非商业用途；商业使用请先联系。代码采用 MIT 许可。截图归各页面作者所有，不在这两个许可范围内。引用时请写 Hou, D. (2026), <i>Look et al.: A Design Library of Academic Web Pages for Humans and AI Agents</i>, Zenodo, <a href="https://doi.org/10.5281/zenodo.23718470" target="_blank" rel="noopener">doi:10.5281/zenodo.23718470</a>。</p>
<h2>删除</h2>
<p>如果你是页面作者，希望删除或更正你的页面或截图，请通过{removal}提交，我们会撤下。申请由人工处理，通常几天内完成。</p></section>""",
}

# filled in once the README library exists; empty until then so the About page does not describe it early
README_ABOUT = {
"en": """<p><b>{n_readme} code READMEs</b>, ten in each of four groups: vision (CVPR, ICCV, ECCV), learning (NeurIPS, ICML, ICLR and the journals), language (ACL, EMNLP), and graphics, robotics and HCI (SIGGRAPH, CoRL, CHI). Candidates are the official code repositories that the project pages above link to: 744 of the 907 pages link one, and 647 of those repositories have a README of at least 2.5 KB. Each README was rendered with the HTML that GitHub's own API returns, in GitHub's light theme at the 920px width of a repository page, and judged the same way as the pages below, on header, visuals, structure and polish. Their DESIGN.md files record structure and presentation (header block, badges, section outline, components) rather than CSS, because GitHub fixes the fonts and colors.</p>
""",
"ja": """<p><b>コードの README {n_readme} 件</b>。四つのグループから 10 件ずつで、画像(CVPR、ICCV、ECCV)、機械学習(NeurIPS、ICML、ICLR とジャーナル)、言語(ACL、EMNLP)、グラフィックス・ロボティクス・HCI(SIGGRAPH、CoRL、CHI)です。候補は、上のプロジェクトページがリンクしている公式コードリポジトリです。907 ページのうち 744 ページにリンクがあり、そのうち 647 のリポジトリに 2.5 KB 以上の README がありました。README は GitHub の API が返す HTML をそのまま使い、GitHub のライトテーマで、リポジトリページと同じ 920px 幅に表示して、下に書いたページと同じ方法で審査しました。基準はヘッダー、画像、構成、仕上がりです。GitHub ではフォントと色が固定されているため、README の DESIGN.md は CSS ではなく、構成と見せ方(ヘッダー部分、バッジ、セクション構成、部品)を記録しています。</p>
""",
"zh": """<p><b>{n_readme} 个代码 README</b>，分四组各 10 个，分别是视觉(CVPR、ICCV、ECCV)、机器学习(NeurIPS、ICML、ICLR 和期刊)、语言(ACL、EMNLP)，以及图形学、机器人和人机交互(SIGGRAPH、CoRL、CHI)。候选是上面这些项目页链接的官方代码仓库：907 个页面里有 744 个链接了仓库，其中 647 个仓库的 README 不少于 2.5 KB。README 直接用 GitHub API 返回的 HTML 渲染，采用 GitHub 浅色主题和仓库页面的 920px 宽度，再按和下文页面相同的方法评审，标准是头部、图片、结构和完成度。GitHub 固定了字体和颜色，所以 README 的 DESIGN.md 记录的是结构和呈现方式(头部区块、徽章、章节结构、组件)，而不是 CSS。</p>
""",
}


def about(lang, **kw):
    readme = README_ABOUT[lang].format(**kw) if kw["n_readme"] else ""
    return ABOUT[lang].format(readme=readme, **kw)
