import streamlit as st
from pipeline import run_research_pipeline

st.set_page_config(
    page_title="ResearchOS — AI Research Workspace",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
:root{
    --bg:#080b12; --panel:#0f141d; --panel2:#121925; --border:rgba(255,255,255,.09);
    --text:#eef2f7; --muted:#8b97a8; --accent:#7c5cff; --accent2:#4f8cff;
}
.stApp{
    background:
        radial-gradient(circle at 8% 0%,rgba(124,92,255,.13),transparent 28%),
        radial-gradient(circle at 92% 0%,rgba(79,140,255,.10),transparent 24%),
        linear-gradient(180deg,#070a10 0%,#090d14 100%);
    color:var(--text);
}
[data-testid="stHeader"]{background:rgba(7,10,16,.60);backdrop-filter:blur(16px)}
.block-container{padding-top:1.4rem;padding-bottom:3rem;max-width:1500px}
#MainMenu,footer{visibility:hidden}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#0a0e16,#080b12);border-right:1px solid var(--border)}
.brand{display:flex;align-items:center;gap:12px;padding:4px 6px 18px}
.brand-mark{
    width:38px;height:38px;border-radius:12px;display:flex;align-items:center;justify-content:center;
    color:#fff;font-weight:800;background:linear-gradient(135deg,var(--accent),var(--accent2));
    box-shadow:0 10px 28px rgba(124,92,255,.28)
}
.brand-name{font-weight:750;font-size:16px}.brand-sub{color:var(--muted);font-size:11px;margin-top:4px}
.side-section{color:#677386;font-size:10px;letter-spacing:1.2px;font-weight:700;margin:20px 6px 9px;text-transform:uppercase}
.side-item{border:1px solid transparent;border-radius:11px;padding:9px 10px;color:#aeb8c6;font-size:13px;margin-bottom:5px}
.side-item.active{background:rgba(124,92,255,.10);border-color:rgba(124,92,255,.20);color:#f1efff}
.side-foot{margin-top:25px;padding:12px 11px;border:1px solid var(--border);border-radius:14px;background:rgba(255,255,255,.025)}
.side-foot-title{font-size:11px;color:#b9c3d1;font-weight:650}.side-foot-text{font-size:10px;color:var(--muted);line-height:1.45;margin-top:4px}
.hero{
    position:relative;overflow:hidden;border:1px solid var(--border);border-radius:24px;padding:28px 30px 30px;
    background:radial-gradient(circle at 95% 10%,rgba(124,92,255,.16),transparent 26%),linear-gradient(135deg,rgba(18,24,37,.94),rgba(12,17,27,.90));
    box-shadow:0 20px 50px rgba(0,0,0,.28)
}
.eyebrow{display:inline-flex;align-items:center;gap:7px;color:#a99bff;font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:9px}
.eyebrow-dot{width:6px;height:6px;border-radius:999px;background:#8c75ff;box-shadow:0 0 12px #8c75ff}
.hero-title{font-size:clamp(30px,3.6vw,50px);line-height:1.02;font-weight:820;letter-spacing:-1.8px;margin:0;color:#f6f8fb}
.hero-gradient{background:linear-gradient(90deg,#f7f7fb 8%,#bbb3ff 55%,#84a5ff 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero-desc{max-width:760px;color:#9ca8b8;font-size:14px;line-height:1.65;margin-top:12px}
.hero-pills{display:flex;flex-wrap:wrap;gap:7px;margin-top:19px}
.pill{padding:6px 9px;border:1px solid var(--border);border-radius:999px;color:#bdc6d2;font-size:10px;background:rgba(255,255,255,.025)}
.section-title{font-size:14px;font-weight:700;color:#e6ebf2;margin:23px 0 10px}
.pipeline-card{min-height:120px;background:linear-gradient(180deg,rgba(18,25,37,.92),rgba(13,18,28,.92));border:1px solid var(--border);border-radius:16px;padding:15px;box-shadow:0 12px 30px rgba(0,0,0,.14)}
.pipeline-num{width:26px;height:26px;border-radius:9px;display:inline-flex;align-items:center;justify-content:center;background:rgba(124,92,255,.12);border:1px solid rgba(124,92,255,.18);color:#bfb6ff;font-size:10px;font-weight:800}
.pipeline-name{margin-top:10px;color:#edf1f6;font-size:13px;font-weight:700}.pipeline-copy{margin-top:5px;color:var(--muted);font-size:10.5px;line-height:1.45}
.connector{color:#434e60;text-align:center;font-size:20px;line-height:120px;font-weight:800}
.workspace{margin-top:25px;padding:20px;border-radius:19px;border:1px solid var(--border);background:rgba(13,18,28,.78);box-shadow:0 20px 50px rgba(0,0,0,.28)}
.workspace-head{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:13px}
.workspace-title{font-size:16px;font-weight:760;color:#edf1f6}.workspace-sub{color:var(--muted);font-size:11px;margin-top:3px}
.status-badge{white-space:nowrap;padding:6px 9px;border:1px solid rgba(46,204,145,.18);border-radius:999px;color:#77e2ba;background:rgba(46,204,145,.06);font-size:10px;font-weight:700}
.stTextInput>div>div>input,.stTextArea textarea{background:#0b111a!important;border:1px solid rgba(255,255,255,.14)!important;color:#eff3f8!important;border-radius:13px!important;box-shadow:none!important}
.stTextInput>div>div>input{padding:.8rem .9rem!important}
.stTextInput>div>div>input:focus,.stTextArea textarea:focus{border-color:rgba(124,92,255,.55)!important;box-shadow:0 0 0 1px rgba(124,92,255,.18)!important}
div[data-testid="stButton"]>button{border-radius:12px!important;border:1px solid rgba(124,92,255,.35)!important;background:linear-gradient(135deg,#7657ff,#5d80ff)!important;color:#fff!important;font-weight:750!important;min-height:44px!important;box-shadow:0 12px 28px rgba(102,87,255,.22)!important}
div[data-testid="stButton"]>button:hover{filter:brightness(1.08);transform:translateY(-1px)}
.result-header{display:flex;align-items:end;justify-content:space-between;margin-top:28px;margin-bottom:10px}
.result-title{font-size:18px;font-weight:780;color:#edf1f6}.result-sub{color:var(--muted);font-size:11px;margin-top:3px}
.stTabs [data-baseweb="tab-list"]{gap:5px;padding:4px;background:rgba(255,255,255,.025);border:1px solid var(--border);border-radius:13px}
.stTabs [data-baseweb="tab"]{border-radius:9px;color:#8e99a8;height:39px;padding:0 14px;font-size:11px;font-weight:650}
.stTabs [aria-selected="true"]{color:#efedff!important;background:rgba(124,92,255,.12)}
.report-card,.data-card{border:1px solid var(--border);border-radius:17px;background:linear-gradient(180deg,rgba(16,22,33,.92),rgba(12,17,26,.92));padding:20px;margin-top:11px}
.report-card h1,.report-card h2,.report-card h3{color:#f0f3f7}.report-card p,.report-card li{color:#c0cad6;line-height:1.72}
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:12px}
.metric{padding:13px;border:1px solid var(--border);border-radius:14px;background:rgba(255,255,255,.02)}
.metric-label{color:#7f8b9c;font-size:9px;text-transform:uppercase;letter-spacing:1px;font-weight:700}.metric-value{margin-top:7px;color:#eef2f7;font-size:17px;font-weight:780}
.agent-live{display:flex;align-items:center;gap:10px;border:1px solid rgba(124,92,255,.18);background:rgba(124,92,255,.06);border-radius:13px;padding:11px 12px;color:#c5bfff;font-size:11px;margin:12px 0 2px}
.live-dot{width:7px;height:7px;border-radius:999px;background:#8e78ff;box-shadow:0 0 12px #8e78ff}
.footer{margin-top:42px;padding-top:16px;border-top:1px solid var(--border);color:#5f6a7a;font-size:10px;display:flex;justify-content:space-between;gap:15px}
@media(max-width:900px){.metrics{grid-template-columns:repeat(2,1fr)}.connector{display:none}.hero{padding:22px}}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div class="brand">
        <div class="brand-mark">◈</div>
        <div>
            <div class="brand-name">ResearchOS</div>
            <div class="brand-sub">Autonomous research workspace</div>
        </div>
    </div>
    <div class="side-section">Workspace</div>
    <div class="side-item active">⌂ &nbsp; Research Studio</div>
    <div class="side-item">◌ &nbsp; Recent Reports</div>
    <div class="side-item">◫ &nbsp; Sources</div>
    <div class="side-section">System</div>
    <div class="side-item">⚙ &nbsp; Agent Pipeline</div>
    <div class="side-item">◉ &nbsp; Model Runtime</div>
    <div class="side-foot">
        <div class="side-foot-title">4-agent pipeline</div>
        <div class="side-foot-text">Search → Read → Write → Critique</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<section class="hero">
    <div class="eyebrow"><span class="eyebrow-dot"></span> Autonomous research system</div>
    <h1 class="hero-title">Turn a question into a <span class="hero-gradient">research report.</span></h1>
    <div class="hero-desc">
        ResearchOS coordinates specialized AI agents to search the web, read useful sources,
        draft a structured report, and critique the final result.
    </div>
    <div class="hero-pills">
        <span class="pill">Web Search</span><span class="pill">Deep Reading</span>
        <span class="pill">LLM Writing</span><span class="pill">Automated Critique</span>
        <span class="pill">Source Traceability</span>
    </div>
</section>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Agent pipeline</div>', unsafe_allow_html=True)

p1,c1,p2,c2,p3,c3,p4 = st.columns([1,.14,1,.14,1,.14,1])
items = [
    ("01","Search Agent","Finds recent, relevant web information."),
    ("02","Reader Agent","Scrapes a useful source for deeper context."),
    ("03","Writer Agent","Transforms gathered research into a report."),
    ("04","Critic Agent","Reviews quality, gaps, and overall strength."),
]
for col,(n,name,copy) in zip([p1,p2,p3,p4],items):
    with col:
        st.markdown(f'<div class="pipeline-card"><div class="pipeline-num">{n}</div><div class="pipeline-name">{name}</div><div class="pipeline-copy">{copy}</div></div>', unsafe_allow_html=True)
for col in [c1,c2,c3]:
    with col:
        st.markdown('<div class="connector">›</div>', unsafe_allow_html=True)

st.markdown("""
<div class="workspace">
    <div class="workspace-head">
        <div>
            <div class="workspace-title">Research Studio</div>
            <div class="workspace-sub">Describe the topic you want the agents to investigate.</div>
        </div>
        <div class="status-badge">● SYSTEM READY</div>
    </div>
""", unsafe_allow_html=True)

topic = st.text_input(
    "Research topic",
    placeholder="e.g. How does the Russia–Ukraine war influence global stock markets?",
    label_visibility="collapsed",
)
a,b = st.columns([1,3])
with a:
    start = st.button("Run research  →", type="primary", use_container_width=True)
with b:
    st.markdown('<div style="padding:12px 3px 0;color:#687486;font-size:10.5px;">Tip: ask focused questions for stronger retrieval, cleaner reports, and more useful sources.</div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

if start:
    if not topic.strip():
        st.warning("Enter a research topic first.")
    else:
        st.markdown('<div class="agent-live"><span class="live-dot"></span>Agents are running — search, reading, writing and critique are in progress.</div>', unsafe_allow_html=True)

        with st.status("Running autonomous research pipeline...", expanded=True) as status:
            try:
                st.write("🔎 Search Agent — discovering relevant sources")
                result = run_research_pipeline(topic)
                st.write("📖 Reader Agent — processing a selected source")
                st.write("✍️ Writer Agent — drafting the report")
                st.write("🧐 Critic Agent — reviewing the draft")
                status.update(label="Research completed successfully", state="complete", expanded=False)
                st.success("Research completed. Explore the report and agent outputs below.")
            except Exception as e:
                status.update(label="Research pipeline failed", state="error", expanded=True)
                st.error("Something went wrong while running the research pipeline.")
                st.exception(e)
                st.stop()

        st.markdown("""
        <div class="result-header">
            <div>
                <div class="result-title">Research results</div>
                <div class="result-sub">Everything generated by the multi-agent workflow.</div>
            </div>
        </div>
        <div class="metrics">
            <div class="metric"><div class="metric-label">Topic</div><div class="metric-value">Research</div></div>
            <div class="metric"><div class="metric-label">Agents</div><div class="metric-value">4 active</div></div>
            <div class="metric"><div class="metric-label">Research</div><div class="metric-value">Web + scrape</div></div>
            <div class="metric"><div class="metric-label">Review</div><div class="metric-value">Critic pass</div></div>
        </div>
        """, unsafe_allow_html=True)

        tab1,tab2,tab3,tab4 = st.tabs(["◉ Final Report","⌁ Search Results","▣ Scraped Content","✓ Critic Review"])

        with tab1:
            st.markdown('<div class="report-card">', unsafe_allow_html=True)
            st.markdown(result["report"])
            st.markdown("</div>", unsafe_allow_html=True)
            st.download_button("Download report", result["report"], "research_report.md", "text/markdown", use_container_width=True)

        with tab2:
            st.markdown('<div class="data-card">', unsafe_allow_html=True)
            st.code(result["search_results"], language="text")
            st.markdown("</div>", unsafe_allow_html=True)

        with tab3:
            st.markdown('<div class="data-card">', unsafe_allow_html=True)
            st.text_area("Scraped content", result["scraped_content"], height=520, label_visibility="collapsed")
            st.markdown("</div>", unsafe_allow_html=True)

        with tab4:
            st.markdown('<div class="data-card">', unsafe_allow_html=True)
            st.markdown(result["feedback"])
            st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="footer"><span>ResearchOS · Multi-Agent Research Workspace</span><span>Search · Read · Write · Critique</span></div>', unsafe_allow_html=True)
