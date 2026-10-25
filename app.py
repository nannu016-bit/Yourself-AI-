# Page Configuration
st.set_page_config(
    page_title="Yourself — AI Workspace",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- SIDEBAR NAVIGATION ---
st.sidebar.markdown("# ✨ Yourself")
st.sidebar.markdown("*An All-in-One AI Workspace designed to think, work, and code like you.*")
st.sidebar.divider()

app_mode = st.sidebar.radio(
    "Navigation",
    [
        "💬 Chat Assistant", 
        "📊 Workflow Dashboard (Swing Trading)", 
        "💻 Developer Studio", 
        "💎 Subscription & Billing"
    ]
)

st.sidebar.divider()
st.sidebar.markdown("### Account Status")
st.sidebar.info("Plan: **Free Tier**\n\nDaily Actions: 12 / 20 used")
if st.sidebar.button("Upgrade to Pro ($20/mo)"):
    st.sidebar.success("Redirecting to secure Stripe checkout...")

# --- VIEW 1: CHAT ASSISTANT ---
if app_mode == "💬 Chat Assistant":
    st.markdown("# Chat Assistant")
    st.markdown("Your everyday thinking partner for simple Q&A, writing, and brainstorming.")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I am **Yourself**. How can I help you think through things today?"}
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Type your message here..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        response = f"I've processed your request: *'{prompt}'*. As your AI platform, I'm ready to assist you further!"
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

# --- VIEW 2: WORKFLOW DASHBOARD (SWING TRADING MODULE) ---
elif app_mode == "📊 Workflow Dashboard (Swing Trading)":
    st.markdown("# Workflow Dashboard: Indian Equity Swing Trading Engine")
    st.markdown("A research-backed, rule-based swing trading system for NSE/BSE markets (2-10 day holding periods)[span_1](start_span)[span_1](end_span).")
    
    # Mandatory Legal Disclaimer Banner
    st.warning("⚠️ **Disclaimer:** Educational content only. Not investment advice. Author is not a SEBI-registered Investment Adviser or Research Analyst[span_2](start_span)[span_2](end_span).")

    sub_tab1, sub_tab2, sub_tab3 = st.tabs([
        "⚖️ Position Sizing (Layer 4)", 
        "🛡️ Market Regime Filter (Layer 1)", 
        "📈 Strategy Playbook"
    ])

    with sub_tab1:
        st.markdown("### Layer 4: Position Sizing & Risk Control")
        st.markdown("Never risk more than **1% of total capital** on any single trade[span_3](start_span)[span_3](end_span).")

        col1, col2 = st.columns(2)
        with col1:
            total_capital = st.number_input("Total Trading Capital (₹)", value=500000, step=50000)
            risk_pct = st.slider("Risk per Trade (%)", min_value=0.5, max_value=3.0, value=1.0, step=0.5)
            entry_price = st.number_input("Planned Entry Price (₹)", value=2900.0, step=10.0)
            
        with col2:
            stop_loss_price = st.number_input("Planned Stop-Loss Price (₹)", value=2840.0, step=10.0)
            strategy_type = st.selectbox("Selected Strategy", [
                "Strategy 1: NIFTY 200 Momentum 30[span_4](start_span)[span_4](end_span)", 
                "Strategy 2: 52-Week High Breakout + Volume[span_5](start_span)[span_5](end_span)",
                "Strategy 3: 20-DMA Pullback in Uptrend[span_6](start_span)[span_6](end_span)"
            ])

        if st.button("Calculate Position Size", type="primary"):
            risk_per_share = entry_price - stop_loss_price
            if risk_per_share <= 0:
                st.error("Stop-loss price must be lower than entry price for long positions!")
            else:
                rupee_risk = total_capital * (risk_pct / 100.0)
                quantity = int(rupee_risk / risk_per_share)
                position_value = quantity * entry_price
                portfolio_allocation = (position_value / total_capital) * 100

                st.success("Calculation Successful!")
                r1, r2, r3 = st.columns(3)
                r1.metric("Recommended Quantity", f"{quantity} shares")
                r2.metric("Total Position Value", f"₹{position_value:,.2f} ({portfolio_allocation:.1f}% cap)")
                r3.metric("Total Rupee Risk", f"₹{rupee_risk:,.2f}")

                if portfolio_allocation > 50:
                    st.warning("⚠️ Warning: Position size consumes a large percentage of your capital. Check liquidity filters.")

    with sub_tab2:
        st.markdown("### Layer 1: Market Regime Filter")
        st.markdown("Run this 3-point check before opening any position to cut drawdown risk[span_7](start_span)[span_7](end_span).")

        nifty_50_dma = st.radio(
            "Nifty 50 vs 50-DMA", 
            ["Above 50-DMA (Trade Long)[span_8](start_span)[span_8](end_span)", "Below 50-DMA (Reduce size 50% or pause)[span_9](start_span)[span_9](end_span)"]
        )
        nifty_200_dma = st.radio(
            "Nifty 50 vs 200-DMA (Weekly)", 
            ["Above 200-DMA[span_10](start_span)[span_10](end_span)", "Below 200-DMA (ALL LONGS OFF. Move to Cash)[span_11](start_span)[span_11](end_span)"]
        )
        india_vix = st.select_slider(
            "India VIX Level", 
            options=[
                "< 15 (Normal Sizing)[span_12](start_span)[span_12](end_span)", 
                "15 - 20 (Reduce size 25%, widen stops)[span_13](start_span)[span_13](end_span)", 
                "> 20 (Reduce size 50%. No breakouts)[span_14](start_span)[span_14](end_span)"
            ]
        )

        if st.button("Evaluate Market Regime"):
            if "Below 200-DMA" in nifty_200_dma:
                st.error("🚨 CRITICAL ALERT: Market is below 200-DMA weekly close. **ALL LONGS OFF. MOVE TO CASH.**[span_15](start_span)[span_15](end_span)")
            elif "Below 50-DMA" in nifty_50_dma or "> 20" in india_vix:
                st.warning("⚠️ CAUTION: Defensive regime active. Reduce position sizes by 50% and pause new breakout entries[span_16](start_span)[span_16](end_span).")
            else:
                st.success("✅ GREEN LIGHT: Market regime favorable for standard swing trading operations.")

    with sub_tab3:
        st.markdown("### Strategy Playbook Summary")
        st.info("**Strategy 1: NIFTY 200 Momentum 30** — Rule-based monthly rebalancing delivering ~19.3% backtested CAGR versus 14.3% for Nifty 200 TRI[span_17](start_span)[span_17](end_span).")
        st.info("**Strategy 2: 52-Week High Breakout** — Darvas/O'Neil style breakout with volume $\ge 1.5\\times$ average[span_18](start_span)[span_18](end_span).")
        st.info("**Strategy 3: 20-DMA Pullback** — Mean-reversion dip buying when RSI(2) < 10 inside a confirmed uptrend[span_19](start_span)[span_19](end_span).")

# --- VIEW 3: DEVELOPER STUDIO ---
elif app_mode == "💻 Developer Studio":
    st.markdown("# Developer Studio")
    st.markdown("Write, test, and debug scripts with your technical co-founder.")

    col_c, col_d = st.columns([1, 1])
    with col_c:
        st.markdown("### Coding Assistant Chat")
        code_prompt = st.text_input("Ask for a script or debugging help:", placeholder="e.g., Write a Python function for position risk")
        if st.button("Generate Code"):
            st.session_state["generated_code"] = f"# Generated script based on: {code_prompt}\n\ndef calculate_risk(capital, risk_pct, entry, sl):\n    risk_amt = capital * (risk_pct / 100)\n    return int(risk_amt / (entry - sl))\n\nprint('Execution successful!')"
            st.success("Code generated!")

    with col_d:
        st.markdown("### Live Code Sandbox Preview")
        default_code = st.session_state.get(
            "generated_code", 
            "# Your generated code will appear here\n\ndef welcome():\n    print('Welcome to Yourself Studio!')\n\nwelcome()"
        )
        st.code(default_code, language="python")
        if st.button("▶ Run Script"):
            st.toast("Script executed successfully in sandbox environment!", icon="✅")

# --- VIEW 4: SUBSCRIPTION & BILLING ---
elif app_mode == "💎 Subscription & Billing":
    st.markdown("# Subscription Plans")
    st.markdown("Choose the right plan to unlock advanced AI capabilities and automated workflows.")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 🆓 Free Tier")
        st.markdown("**$0 / month**")
        st.markdown("- 20 daily actions")
        st.markdown("- Basic Chat Assistant")
        st.button("Current Plan", disabled=True)

    with c2:
        st.markdown("### 🚀 Pro Tier")
        st.markdown("**$20 / month**")
        st.markdown("- **Unlimited** daily actions & chats")
        st.markdown("- Advanced Workflow Automation (including Swing Trading Framework)")
        st.markdown("- Full Developer Studio Sandbox")
        if st.button("Upgrade with Stripe", type="primary"):
            st.success("Stripe Checkout simulation initiated!")
              
