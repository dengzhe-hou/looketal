"""Site text in English, Japanese and Simplified Chinese.

Each entry is (en, ja, zh). Strings may hold {placeholders} filled by build_site.py with str.format.
DESIGN.md files stay in English; only the site around them is translated. Per-entry text (mood,
selection reason) lives in data/i18n/<lang>.json.
"""
LANGS = ("en", "ja", "zh")
LANG_NAMES = {"en": "English", "ja": "日本語", "zh": "简体中文"}
HTML_LANG = {"en": "en", "ja": "ja", "zh": "zh-Hans"}

S = {
    # chrome
    "tagline": ("Design research for academic pages", "学術ページのデザイン資料集", "学术网页的设计资料库"),
    "nav_home": ("Home", "ホーム", "首页"),
    "nav_project": ("Project pages", "論文プロジェクトページ", "论文项目页"),
    "nav_researcher": ("Researcher pages", "研究者ページ", "研究者主页"),
    "nav_readme": ("Code READMEs", "コード README", "代码 README"),
    "nav_all": ("All styles", "すべてのスタイル", "全部风格"),
    "nav_collections": ("Collections", "コレクション", "专题"),
    "nav_prompts": ("Design prompts", "デザインプロンプト", "设计提示词"),
    "nav_about": ("About", "概要", "关于"),
    "theme": ("Theme", "テーマ", "主题"),
    "theme_auto": ("auto", "自動", "自动"),
    "theme_light": ("light", "ライト", "浅色"),
    "theme_dark": ("dark", "ダーク", "深色"),
    "side_foot": ('Screenshots © their authors, linked to the original pages.<br>DESIGN.md text <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener">CC BY-NC 4.0</a>, code MIT.',
                  'スクリーンショットの著作権は各ページの著者にあり、元ページにリンクしています。<br>DESIGN.md の文章は <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener">CC BY-NC 4.0</a>、コードは MIT です。',
                  '截图版权归各页面作者所有，并链接到原页面。<br>DESIGN.md 文本采用 <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener">CC BY-NC 4.0</a>，代码采用 MIT。'),
    "lang_label": ("Language", "言語", "语言"),

    # home
    "hero_lede": ("{tagline}. Real paper project pages, researcher homepages and code READMEs, each with an AI-readable DESIGN.md: colors, type, spacing, components and page modules.",
                  "実在する論文プロジェクトページ、研究者ページ、コード README を集め、それぞれに AI が読める DESIGN.md を付けました。色、文字、余白、部品、ページ構成を記録しています。",
                  "收集真实的论文项目页、研究者主页和代码 README，每一条都附有 AI 能读的 DESIGN.md，记录配色、字体、间距、组件和页面模块。"),
    "search_ph": ("Search a paper, person, template or mood…", "論文、人名、テンプレート、雰囲気で検索…", "搜索论文、人名、模板或风格…"),
    "search_btn": ("Search", "検索", "搜索"),
    "facet_venues": ("Venues", "会議・ジャーナル", "会议与期刊"),
    "facet_years": ("Years", "年", "年份"),
    "facet_templates": ("Templates", "テンプレート", "模板"),
    "facet_modules": ("Page modules", "ページの構成要素", "页面模块"),
    "facet_fields": ("Fields", "分野", "领域"),
    "new_2026": ("New from 2026", "2026 年の新着", "2026 年新收录"),
    "see_all": ("See all", "すべて見る", "查看全部"),

    # browse
    "browse": ("Browse", "一覧", "浏览"),
    "search_short": ("Search…", "検索…", "搜索…"),
    "kind_all": ("All", "すべて", "全部"),
    "kind_researchers": ("Researchers", "研究者", "研究者"),
    "all_venues": ("All venues", "すべての会議・ジャーナル", "全部会议与期刊"),
    "all_years": ("All years", "すべての年", "全部年份"),
    "all_templates": ("All templates", "すべてのテンプレート", "全部模板"),
    "any_theme": ("Any theme", "すべての配色", "全部配色"),
    "light": ("Light", "ライト", "浅色"),
    "dark": ("Dark", "ダーク", "深色"),
    "both": ("Light + dark", "ライトとダーク", "浅色和深色"),
    "count": ("{n} of {total} styles", "{total} 件中 {n} 件", "共 {total} 条，显示 {n} 条"),
    "searching": (" · searching titles, metadata and DESIGN.md text", "・タイトル、メタデータ、DESIGN.md 本文を検索中", "・正在搜索标题、元数据和 DESIGN.md 正文"),
    "loading_index": (" · loading full-text index…", "・全文索引を読み込み中…", "・正在加载全文索引…"),
    "no_match": ("No pages match these filters.", "条件に合うページはありません。", "没有符合条件的页面。"),
    "copied": ("Copied", "コピーしました", "已复制"),
    "copy_failed": ("Copy failed", "コピーできませんでした", "复制失败"),
    "not_available": ("Not available for this style.", "このスタイルにはありません。", "这一条没有该内容。"),
    "researcher": ("Researcher", "研究者", "研究者"),
    "readme": ("README", "README", "README"),

    # style page
    "visit": ("Visit page ↗", "ページを開く ↗", "打开原页面 ↗"),
    "visit_repo": ("Visit repository ↗", "リポジトリを開く ↗", "打开仓库 ↗"),
    "download_md": ("Download DESIGN.md", "DESIGN.md をダウンロード", "下载 DESIGN.md"),
    "status_rendered": ("Checked against the rendered page.", "表示されたページと照合済みです。", "已对照实际渲染的页面核对。"),
    "status_static": ("Written from static HTML/CSS; the rendered page was not viewed.", "静的な HTML と CSS から書いたもので、表示されたページは確認していません。", "根据静态 HTML 和 CSS 编写，没有查看实际渲染的页面。"),
    "m_venue": ("Venue", "会議・ジャーナル", "会议或期刊"),
    "m_award": ("Award", "受賞", "奖项"),
    "m_year": ("Year", "年", "年份"),
    "m_first_author": ("First author", "筆頭著者", "第一作者"),
    "m_person": ("Person", "人物", "人物"),
    "m_field": ("Field", "分野", "领域"),
    "m_template": ("Template", "テンプレート", "模板"),
    "m_theme": ("Theme", "配色", "配色"),
    "why_here": ("Why it is here", "選んだ理由", "入选理由"),
    "overview": ("Overview", "概要", "概述"),
    "palette": ("Color Palette", "カラーパレット", "配色"),
    "typography": ("Typography", "タイポグラフィ", "字体"),
    "spacing": ("Spacing &amp; Shape", "余白と形", "间距与形状"),
    "page_modules": ("Page Modules", "ページの構成要素", "页面模块"),
    "guidelines": ("Guidelines", "ガイドライン", "使用建议"),
    "header_block": ("Header Block", "ヘッダー部分", "头部区块"),
    "badge_colors": ("Badge Colors", "バッジの色", "徽章配色"),
    "section_outline": ("Section Outline", "セクション構成", "章节结构"),
    "more_like": ("More like this", "似たスタイル", "相似风格"),
    "shot_caption": ("Screenshot of {link}, © the authors. Shown for reference.", "{link} のスクリーンショット。著作権は著者にあり、参考として掲載しています。", "{link} 的截图，版权归作者所有，仅作参考展示。"),
    "request_removal": ("Request removal", "削除を依頼", "申请删除"),
    "feedback": ("Feedback or bug report", "フィードバック・不具合の報告", "反馈或报告问题"),
    "md_in_english": ("", "以下の説明と DESIGN.md 本文は英語です。コーディングエージェントが同じ一つの版を読めるよう、翻訳していません。",
                      "下面的说明和 DESIGN.md 正文是英文。为了让编程 agent 读同一个版本，这部分没有翻译。"),
    "compact": ("Compact", "簡易版", "精简"),
    "extended": ("Extended", "完全版", "完整"),
    "copy": ("Copy", "コピー", "复制"),
    "design_system": ("{title} design system", "{title} のデザインシステム", "{title} 的设计系统"),

    # collections
    "collections_lede": ("Groups of pages that share a template, a feature or a theme.", "同じテンプレート、機能、配色を持つページをまとめました。", "按模板、功能或配色归类的页面。"),
    "look_closer": ("Look closer", "注目点", "看点"),

    # prompts
    "prompts_h1": ("Design prompts from real academic pages", "実在の学術ページから作るデザインプロンプト", "基于真实学术网页的设计提示词"),
    "prompts_lede": ("A DESIGN.md gives your coding agent visual rules. Your paper supplies the content. Fill in the brackets and attach the DESIGN.md you picked.",
                     "DESIGN.md はコーディングエージェントに見た目のルールを渡し、内容はあなたの論文から入れます。括弧の中を埋め、選んだ DESIGN.md を添付してください。",
                     "DESIGN.md 告诉编程 agent 视觉规则，内容来自你的论文。把方括号填好，再附上你选的 DESIGN.md。"),
    "p_project": ("Build a project page", "プロジェクトページを作る", "做一个项目页"),
    "p_researcher": ("Build a researcher homepage", "研究者ページを作る", "做一个研究者主页"),
    "p_restyle": ("Restyle an existing page", "既存のページの見た目を変える", "给现有页面换风格"),
    "p_readme": ("Write a code README", "コードの README を書く", "写一个代码 README"),
    "example_ref": ("Example reference", "参考例", "参考示例"),
    "prompt_project": ("""Build a project page for our paper "[title]" ([venue]). Use the attached DESIGN.md for colors, type, spacing and component styling only.
Content comes from our paper: authors and affiliations, [teaser figure or video], abstract, [method figure], [results: tables / videos / comparison slider], BibTeX.
Link buttons: [Paper] [arXiv] [Code] [Data] [Demo].
Keep it a static page that works on GitHub Pages. List which visual decisions came from the reference and which you changed.""",
                       """私たちの論文「[タイトル]」([会議名])のプロジェクトページを作ってください。添付の DESIGN.md は色、文字、余白、部品の見た目にだけ使ってください。
内容は論文から取ります。著者と所属、[ティーザー図または動画]、アブストラクト、[手法の図]、[結果として表、動画、比較スライダー]、BibTeX。
リンクボタンは [Paper] [arXiv] [Code] [Data] [Demo]。
GitHub Pages で動く静的ページにしてください。見た目の判断のうち、参考ページから取ったものと変えたものを書き出してください。""",
                       """为我们的论文《[标题]》([会议名])做一个项目页。附上的 DESIGN.md 只用于配色、字体、间距和组件样式。
内容来自论文，包括作者和单位、[预告图或视频]、摘要、[方法图]、[结果，可以是表格、视频或对比滑块]、BibTeX。
链接按钮是 [Paper] [arXiv] [Code] [Data] [Demo]。
做成能在 GitHub Pages 上运行的静态页面。列出哪些视觉决定来自参考页面，哪些是你改的。"""),
    "prompt_researcher": ("""Build my academic homepage. Use the attached DESIGN.md for visual rules only.
Content: name, [position, affiliation], photo, short bio, [news], selected publications with [thumbnails / venue badges], [awards], contact links.
Generate the publication list from [publications.bib]. Keep it static and accessible; support dark mode only if the reference does.""",
                          """私の研究者ページを作ってください。添付の DESIGN.md は見た目のルールにだけ使ってください。
内容は、名前、[職位と所属]、写真、短い紹介文、[ニュース]、[サムネイルや会議名バッジ付きの]主要論文、[受賞]、連絡先リンクです。
論文リストは [publications.bib] から生成してください。静的でアクセシブルなページにし、参考ページにダークモードがある場合だけ対応してください。""",
                          """为我做一个学术主页。附上的 DESIGN.md 只用于视觉规则。
内容包括姓名、[职位和单位]、照片、简短介绍、[新闻]、带[缩略图或会议标签]的代表论文、[获奖]、联系方式链接。
论文列表从 [publications.bib] 生成。做成静态、无障碍的页面；只有参考页面有深色模式时才支持深色模式。"""),
    "prompt_restyle": ("""Restyle our existing project page (attached HTML) using the attached DESIGN.md. Keep every piece of content and every link.
Change only colors, fonts, spacing, button and card styling, and section rhythm. Report the before/after tokens you changed.""",
                       """添付の DESIGN.md を使って、既存のプロジェクトページ(添付の HTML)の見た目を変えてください。内容とリンクはすべて残してください。
変えてよいのは色、フォント、余白、ボタンとカードの見た目、セクションの並びのリズムだけです。変更したトークンを変更前と変更後で報告してください。""",
                       """用附上的 DESIGN.md 给我们现有的项目页(附上的 HTML)换风格。所有内容和链接都保留。
只改配色、字体、间距、按钮和卡片样式，以及各节的节奏。报告你改了哪些 token，写出改前和改后的值。"""),
    "prompt_readme": ("""Write the README.md for our code repository "[repo]" (paper: "[title]", [venue]). Use the attached DESIGN.md for structure and presentation only: header block, badges, teaser, section order, tables, code blocks and the citation block.
Content comes from our project: [one-line summary], [teaser image or GIF], installation, [data preparation], [training / evaluation commands], [results table], [pretrained weights], BibTeX, license, acknowledgements.
Use only GitHub-flavored Markdown and the HTML GitHub allows. Do not invent results, links or badges that do not exist.""",
                      """私たちのコードリポジトリ「[リポジトリ名]」(論文「[タイトル]」、[会議名])の README.md を書いてください。添付の DESIGN.md は構成と見せ方にだけ使ってください。ヘッダー、バッジ、ティーザー、セクションの順番、表、コードブロック、引用ブロックが対象です。
内容は私たちのプロジェクトから取ります。[一行の要約]、[ティーザー画像または GIF]、インストール、[データの準備]、[学習と評価のコマンド]、[結果の表]、[学習済み重み]、BibTeX、ライセンス、謝辞。
GitHub Flavored Markdown と GitHub が許可する HTML だけを使ってください。存在しない結果、リンク、バッジは作らないでください。""",
                      """为我们的代码仓库「[仓库名]」(论文《[标题]》，[会议名])写 README.md。附上的 DESIGN.md 只用于结构和呈现方式，包括头部、徽章、预告图、章节顺序、表格、代码块和引用块。
内容来自我们的项目，包括[一句话简介]、[预告图或 GIF]、安装、[数据准备]、[训练和评测命令]、[结果表]、[预训练权重]、BibTeX、许可证、致谢。
只用 GitHub Flavored Markdown 和 GitHub 允许的 HTML。不要编造不存在的结果、链接或徽章。"""),
}

# display names for page-module filters (the English name stays the filter value in URLs)
MODULE_NAMES = {
    "Teaser video": ("ティーザー動画", "预告视频"), "BibTeX": ("BibTeX", "BibTeX"), "Code": ("コード", "代码"),
    "arXiv / paper": ("arXiv・論文", "arXiv 与论文"), "Demo": ("デモ", "演示"), "Interactive 3D": ("インタラクティブ 3D", "交互式 3D"),
    "Comparison slider": ("比較スライダー", "对比滑块"), "Results table": ("結果の表", "结果表"), "Dataset": ("データセット", "数据集"),
    "Publication list": ("論文リスト", "论文列表"), "News": ("ニュース", "新闻"), "Bio / photo": ("紹介文・写真", "简介与照片"),
    "Badges": ("バッジ", "徽章"), "Install": ("インストール", "安装"), "Model zoo": ("学習済みモデル", "预训练模型"),
}

# collections: id -> ((title en, ja, zh), (description en, ja, zh), (closer en, ja, zh))
COLLECTIONS = {
    "nerfies-family": (
        ("The Nerfies family", "Nerfies ファミリー", "Nerfies 家族"),
        ("Pages built on the Nerfies template or its descendant, the Academic Project Page Template.",
         "Nerfies テンプレート、またはその派生である Academic Project Page Template で作られたページです。",
         "基于 Nerfies 模板或其衍生版 Academic Project Page Template 做的页面。"),
        ("Most of these share Bulma's grid, Google Sans titles and dark pill link buttons. Compare where authors departed from the defaults: a venue color, a custom teaser band, a results table style. Those small edits are what a DESIGN.md should record.",
         "多くは Bulma のグリッド、Google Sans の見出し、黒い丸型のリンクボタンを共有しています。会議のテーマ色、独自のティーザー帯、結果の表の見せ方など、著者が既定値から離れた部分を比べてみてください。DESIGN.md が記録すべきなのは、こうした小さな変更です。",
         "这些页面大多共用 Bulma 网格、Google Sans 标题和深色圆角链接按钮。可以比较作者在哪里偏离了默认设置，比如会议配色、自定义预告条、结果表样式。DESIGN.md 要记录的正是这些小改动。")),
    "built-from-scratch": (
        ("Built from scratch", "ゼロから作られたページ", "从零搭建"),
        ("Project pages that do not use a known academic template.", "既知の学術テンプレートを使っていないプロジェクトページです。", "没有使用常见学术模板的项目页。"),
        ("Custom pages show the wider range: editorial serif layouts, dark product-style launches, single-file HTML. Read the Layout and Components sections to see which choices carry the identity.",
         "独自のページは幅が広く、雑誌風のセリフ体レイアウト、製品発表のような暗い画面、1 ファイルだけの HTML まであります。Layout と Components の節を読むと、どの選択が個性を生んでいるかがわかります。",
         "自定义页面的跨度更大，有杂志风的衬线排版，有产品发布会式的深色页面，也有单文件 HTML。读 Layout 和 Components 两节，可以看出哪些选择撑起了它的辨识度。")),
    "show-dont-tell": (
        ("Show, don't tell", "見せて伝える", "用演示说话"),
        ("Pages whose main evidence is interactive or comparative: sliders, 3D viewers, live demos.",
         "スライダー、3D ビューア、ライブデモなど、操作や比較で結果を見せるページです。",
         "主要靠交互或对比展示结果的页面，比如滑块、3D 查看器、在线演示。"),
        ("When results are visual, the page layout is built around a comparison widget. Check how each page frames the widget and what it puts next to it.",
         "結果が視覚的な場合、ページは比較ウィジェットを中心に組まれます。各ページがウィジェットをどう囲み、隣に何を置いているかを見てください。",
         "结果是视觉性的时候，页面会围绕对比组件来排。看看每个页面怎样框住这个组件，旁边又放了什么。")),
    "researcher-homepages": (
        ("Researcher homepages", "研究者のホームページ", "研究者主页"),
        ("Award-winning researchers, chosen by fixed rules (see About).", "受賞歴のある研究者を、決まった規則で選びました(概要を参照)。", "按固定规则选出的获奖研究者(见“关于”)。"),
        ("Homepages range from 1990s hand-written HTML to al-folio and Hugo themes. The Page Modules table shows how each orders bio, news and publications.",
         "1990 年代の手書き HTML から al-folio や Hugo のテーマまで幅があります。Page Modules の表を見ると、紹介文、ニュース、論文をどの順に並べているかがわかります。",
         "从上世纪 90 年代的手写 HTML 到 al-folio、Hugo 主题都有。Page Modules 表展示了每个主页怎样排列简介、新闻和论文。")),
    "dark-and-dual": (
        ("Dark and dual-theme pages", "ダークと二つの配色", "深色与双配色页面"),
        ("Pages that ship a dark theme or a light/dark switch.", "ダークテーマ、またはライトとダークの切り替えがあるページです。", "提供深色主题或浅色/深色切换的页面。"),
        ("Dark academic pages are rare. Look at how surfaces step up in lightness and how figures with white backgrounds are handled.",
         "ダークの学術ページは珍しいです。面の明るさを段階的に上げる方法と、白背景の図の扱い方を見てください。",
         "深色学术页面很少见。可以看看各层底色怎样逐级变亮，白底的图又是怎样处理的。")),
    "readme-gallery": (
        ("Code READMEs", "コード README", "代码 README"),
        ("README files of official code repositories for recent papers.", "最近の論文の公式コードリポジトリにある README です。", "近期论文官方代码仓库的 README。"),
        ("A README has fewer tools than a web page: Markdown, a little HTML, images and badges. Compare how each one orders the header, the teaser, the install steps and the citation block.",
         "README で使えるのは Markdown、少しの HTML、画像、バッジだけです。ヘッダー、ティーザー、インストール手順、引用ブロックをどの順に置いているかを比べてください。",
         "README 能用的只有 Markdown、少量 HTML、图片和徽章。比较一下每个 README 怎样安排头部、预告图、安装步骤和引用块的顺序。")),
}


def t(key, lang, **kw):
    s = S[key][LANGS.index(lang)]
    return s.format(**kw) if kw else s


from i18n_about import about  # noqa: E402,F401
