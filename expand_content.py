import json, os

BASE = "/Users/borbix/.openclaw/workspace-cfo/emotion-trades-app/data"

# ─── TikTok Scripts additional 270 items ───────────────────────────────────
extra_scripts = []

# SMC/ICT #11-50
smc_topics = [
    ("Inducement คืออะไร","คุณเคยรู้สึกไหมว่า setup ดูดีมาก แต่พอเข้าแล้วโดน stop ทันที?","Inducement คือ fake setup ที่ Smart Money สร้างขึ้นเพื่อดึง retail เข้า trade ผิดทิศ มันดูเหมือน OB หรือ FVG แต่จริงๆ คือกับดัก วิธีหลีกเลี่ยง: รอให้ราคา clear liquidity ก่อน แล้วค่อยหา entry จริงๆ หลัง manipulation เสร็จ","กด Follow รับเทคนิค SMC ทุกวัน"),
    ("Breaker Block คืออะไร","OB ที่โดน break แล้วกลายเป็นอะไร? คำตอบนี้เปลี่ยน entry ของคุณได้เลย","Breaker Block คือ Order Block ที่ราคา break ผ่านไปแล้ว เมื่อ Bullish OB โดน break ลง มันกลายเป็น Bearish Breaker Block — Supply Zone ที่แข็งแกร่งมาก เมื่อราคากลับมา retest จะมักหล่นต่อ ใช้ Breaker Block เป็น entry ขาลงได้ดีมาก","Save ไว้เลย Breaker Block ใช้บ่อยมากบน XAU"),
    ("Mitigation Block คืออะไร","หลังจาก Smart Money เข้า order แล้ว พวกเขาทำอะไรต่อ?","Mitigation คือการที่ Smart Money กลับมา 'ปิด' position ที่ขาดทุนก่อนหน้า เมื่อราคากลับมาถึง Mitigation Block Smart Money จะเข้าขายเพื่อ average หรือ hedge position เดิม นั่นคือเหตุผลที่ราคามักกลับทิศที่โซนเหล่านี้","อยากรู้ concept นี้เพิ่ม ติดตาม Emotion Trades ไว้เลย"),
    ("Power of 3 คืออะไร","ทำไมตลาดถึงวิ่งผิดทิศก่อนทุกครั้ง? ICT มีคำตอบ","Power of 3 ของ ICT คือ 3 Phase ของตลาด: Accumulation (ช่วงสะสม ราคาไม่ไปไหน), Manipulation (วิ่งหลอก retail), Distribution (วิ่งทิศแท้จริง) ตลาดวน loop นี้ทุกวัน ทุก session รู้จัก 3 Phase นี้แล้ว อ่าน Price Action ได้ดีขึ้นมาก","Comment 'P3' ถ้าเคยโดน Manipulation มาแล้ว 😅"),
    ("OTE คืออะไร ทำไม ICT ชอบใช้","ICT เข้า trade ที่ Fibonacci 62-79% เสมอ ทำไม?","OTE หรือ Optimal Trade Entry คือ zone ที่ ICT เชื่อว่า Institutional Order เกิดขึ้น วาด Fibonacci จาก swing low ไป high, zone 62-79% คือ Optimal Entry สำหรับ Buy และ zone 62-79% จาก high ไป low คือ Optimal Entry สำหรับ Sell ใช้ร่วมกับ OB หรือ FVG ได้ผลดีมาก","ลองวาด OTE บน XAU วันนี้แล้ว DM ผลมาได้เลย"),
    ("Killzone คืออะไร เทรดช่วงไหนดีที่สุด","คุณเทรดผิดเวลามาตลอดหรือเปล่า? ดูนี้เลย","ICT Killzone คือช่วงเวลาที่ตลาดมี volume สูงและ move ชัด: London KZ 14:00-16:00 GMT+7, NY AM 20:30-22:00 GMT+7, NY Lunch 22:00-00:00 GMT+7, NY PM 01:00-03:00 GMT+7 ช่วงนอก KZ ตลาดมักนิ่งหรือ manipulate เทรดเฉพาะใน KZ = ผลลัพธ์ดีขึ้นมาก","ตั้ง alarm ช่วง London และ NY Open ไว้เลยครับ"),
    ("Daily Bias วิธีหาอย่างถูกต้อง","ก่อนเทรดทุกวัน ต้องรู้สิ่งนี้ก่อน ไม่งั้นเสี่ยงมาก","Daily Bias คือทิศทางที่ตลาดน่าจะไปในวันนั้น วิธีหา: 1) ดู Daily chart ว่า structure เป็น uptrend หรือ downtrend 2) มี liquidity อยู่ที่ไหน ฝั่งบนหรือล่าง 3) ราคาอยู่ใน Premium หรือ Discount zone Bias ชัด = เทรดตามได้ Bias ไม่ชัด = รอ","Share ให้เพื่อนที่เทรดโดยไม่มี bias ด้วยนะครับ"),
    ("Weekly Bias กับ Daily Bias ต่างกันยังไง","Top-down analysis ที่แท้จริงต้องเริ่มจาก Timeframe ไหน?","Weekly Bias คือทิศทางใหญ่ของสัปดาห์ ดูจาก Weekly chart ว่า smart money กำลังสะสมหรือกระจาย Daily Bias คือทิศทางของวันนั้น ต้องสอดคล้องกับ Weekly Bias ถ้า Weekly Bullish แต่ Daily Bearish = วันนั้นน่าจะแค่ pullback ไม่ใช่ reverse เต็มรูปแบบ","ดู Weekly chart ก่อนเทรดทุกวัน เปลี่ยนเกมได้เลย"),
    ("Displacement คืออะไร","Candle ที่วิ่งแรงบน chart — มันบอกอะไรเราได้บ้าง?","Displacement คือการเคลื่อนที่ของราคาอย่างรวดเร็วและรุนแรง มักทิ้ง FVG และ OB ไว้เบื้องหลัง เกิดขึ้นเมื่อ Smart Money เข้า order ขนาดใหญ่ Displacement แรง = Zone ที่ทิ้งไว้มีนัยยะสำคัญมาก เมื่อราคากลับมา retest มักเป็น entry ที่ดีมาก","กด Follow เรียน SMC ครบ system"),
    ("Internal vs External Structure","Structure ที่นักเทรดส่วนใหญ่ดูผิดมาตลอด","External Structure คือ swing high/low ที่เห็นชัดบน Higher TF, Internal Structure คือ swing เล็กๆ ภายใน External swing การอ่านทั้งสองแบบประกอบกัน: External บอก bias ใหญ่, Internal บอกจุด entry แม่นๆ รู้จักทั้งคู่แล้ว entry จะ precise ขึ้นมาก","ติดตามไว้ สอน Structure ครบทุก concept"),
]

for i, (title, hook, content, cta) in enumerate(smc_topics, 11):
    extra_scripts.append({"id": i, "category": "SMC/ICT", "title": title, "hook": hook, "content": content, "cta": cta})

# Fill remaining SMC to #50
smc_fill_titles = [
    "Consequent Encroachment คืออะไร","Silver Bullet Setup","Judas Swing คือกับดักอะไร","NWOG และ NDOG",
    "True Day Open คืออะไร","Balanced Price Range","Rejection Block","Propulsion Block",
    "ICT Market Maker Model","PD Array คืออะไร","Institutional Order Flow","Order Flow Imbalance",
    "Stop Hunt Pattern","Liquidity Pool คืออะไร","Run on Stops","Equal Highs/Lows",
    "Sell Side Liquidity","Buy Side Liquidity","London Open Manipulation","NY Session Reversal",
    "IPDA (Interbank Price Delivery Algorithm)","Time and Price Theory ICT","AMD Model",
    "HTF vs LTF Confluence","How to Mark POI","Entry Model 1-2-3","Risk Definition in SMC",
    "Confirmation Entry vs Aggressive Entry","SMC on Gold Complete Walkthrough","SMC Recap Week Strategy",
]
for i, title in enumerate(smc_fill_titles, 21):
    if i <= 50:
        extra_scripts.append({
            "id": i, "category": "SMC/ICT", "title": title,
            "hook": f"รู้จัก {title.split(' ')[0]} ไหม? ถ้าไม่รู้ คุณกำลังเสียเปรียบอยู่",
            "content": f"{title} คือหนึ่งใน concept สำคัญของ SMC/ICT ที่ช่วยให้อ่านตลาดได้แม่นยำขึ้น การเรียนรู้ concept นี้จะช่วยให้คุณเข้าใจว่า Smart Money กำลังทำอะไรในตลาด และใช้ข้อมูลนั้นในการหา entry ที่มีโอกาสสูงกว่า",
            "cta": "ติดตาม Emotion Trades รับ SMC content ทุกวัน"
        })

# XAU #51-100
xau_topics = [
    (51,"Gold Seasonality ทองมีช่วงขึ้นลงประจำปีไหม","ทองขึ้นเดือนไหนบ้าง? มีรูปแบบที่คาดเดาได้ไหม?","Gold มี Seasonal Pattern ที่น่าสนใจ: Q1 (ม.ค.-มี.ค.) มักแข็งแกร่ง, Q2 อ่อนตัว, Q3 ผสม, Q4 มักแข็งแกร่งก่อนปลายปี Central Bank มักซื้อทองช่วง Q1 และ Q4 นี่คือ Seasonality ที่ควรรู้ก่อนวางแผน trade ระยะยาว","Save ไว้ดูทุกต้นไตรมาสนะครับ"),
    (52,"Central Bank กับทอง ทำไม Bank ซื้อทองเยอะมาก","ทำไม China Russia และอีกหลายประเทศกำลังซื้อทองสำรองเพิ่มขึ้น?","Central Bank ทั่วโลกซื้อทองสูงสุดในรอบ 55 ปีในปี 2022-2023 เหตุผล: ลด dependency ต่อ USD, Diversify reserve, ป้องกัน Sanction ความต้องการจาก Central Bank นี้สร้าง floor ให้ทองระยะยาว การรู้ flow ของ Bank ช่วยให้เทรด macro ได้ดีขึ้น","อยากเข้าใจ Macro เพิ่ม ติดตาม Emotion Trades"),
    (53,"NFP กับทอง เทรดยังไงให้ได้ประโยชน์","NFP ออกทุกศุกร์แรกของเดือน — นี่คือ strategy ที่ใช้ได้จริง","NFP (Non-Farm Payroll) คือข้อมูลการจ้างงานสหรัฐ ผล: NFP สูงกว่าคาด = Dollar แข็ง = Gold ลง, NFP ต่ำกว่าคาด = Dollar อ่อน = Gold ขึ้น Strategy: อย่าเปิด trade 30 นาทีก่อนข่าว รอ spike แล้วหา reversal setup ใน 15-30 นาทีหลังข่าว","กด Follow รับ recap NFP ทุกเดือน"),
    (54,"CPI กับทอง ความสัมพันธ์ที่ต้องรู้","เงินเฟ้อสูง ทองขึ้น? ไม่เสมอไป — นี่คือความจริง","CPI หรือ Consumer Price Index วัดเงินเฟ้อ ความสัมพันธ์กับทองซับซ้อนกว่าที่คิด: CPI สูง + Fed ขึ้นดอกเบี้ยตาม = Real Rate บวก = ทองลง CPI สูง + Fed ไม่ขึ้นดอกเบี้ย = Real Rate ลบ = ทองขึ้น กุญแจคือ Real Interest Rate ไม่ใช่แค่ Inflation","คำนวณ Real Rate = ดอกเบี้ย Fed - CPI inflation"),
    (55,"Fed Rate Decision ส่งผลต่อทองยังไง","เมื่อ Fed พูด ทั้งโลกฟัง และทองก็ฟังด้วย","Fed Rate Decision เกิดขึ้น 8 ครั้งต่อปี Hawkish (ขึ้นดอกเบี้ย/ส่งสัญญาณแข็งกร้าว) = ทองมักลง Dovish (ลดดอกเบี้ย/ส่งสัญญาณผ่อนปรน) = ทองมักขึ้น Dot Plot และ FOMC Statement สำคัญมาก Press Conference หลัง decision มักมี volatility สูงสุด","Mark วันประชุม Fed ไว้ในปฏิทินเทรดด้วย"),
]
extra_scripts.extend([{"id": id_, "category": "XAU", "title": t, "hook": h, "content": c, "cta": cta} 
                       for id_, t, h, c, cta in xau_topics])

# Fill XAU to #100
xau_fill = ["XAU Technical Levels ที่สำคัญ","Gold ETF Flow Analysis","Physical vs Paper Gold","Gold Mining Stocks Correlation",
            "XAU vs Bitcoin เปรียบเทียบ","Gold as Currency Hedge","Geopolitical Risk and Gold","Treasury Yields Impact",
            "XAUEUR vs XAUUSD","Gold Options Market","COT Report กับทอง","Fibonacci on XAU","Elliott Wave on Gold",
            "Wyckoff Method on Gold","Volume Profile XAU","VWAP on Gold","ATR ใช้ยังไงกับ XAU","Bollinger Band ใช้ได้ไหม",
            "RSI Divergence on Gold","MACD Gold Setup","Moving Average Gold","Ichimoku Gold","Pivot Points Gold",
            "Gold Scalping 5M Setup","Gold Swing Trade Setup","Gold Position Trade","Gold Day Trading Rules",
            "Managing Gold Trade","Partial TP Gold Strategy","Trailing Stop Gold",
            "Gold Pre-Market Analysis","Gold Post-Market Review","Weekly Gold Recap","Monthly Gold Outlook","Gold Year in Review",
            "Common Gold Mistakes","Gold Risk Management","Gold Position Sizing","Gold Psychology","Gold Success Stories",
            "XAU Broker Selection","Gold Demo Trading","Gold Live Trading Start","XAU Chart Setup TradingView","Gold Alert Strategy"]

for i, title in enumerate(xau_fill, 56):
    if i <= 100:
        extra_scripts.append({
            "id": i, "category": "XAU", "title": title,
            "hook": f"{title.split(' ')[0]} — สิ่งที่นักเทรดทองต้องรู้",
            "content": f"{title} เป็น concept สำคัญสำหรับการเทรด XAU/USD ให้มีประสิทธิภาพ การเข้าใจเรื่องนี้จะช่วยให้คุณมีข้อมูลมากขึ้นในการตัดสินใจ entry และ exit ที่ดีขึ้น",
            "cta": "ติดตาม Emotion Trades สำหรับ XAU content ทุกวัน"
        })

# MNQ #101-150
mnq_fill = ["MNQ vs NQ ต่างกันยังไง","Margin Requirements MNQ","CME Exchange คืออะไร","Futures Contract Specs",
            "Rolling Futures คืออะไร","MNQ Gap Strategy","Opening Range Breakout MNQ","MNQ Pre-Market","MNQ Session Time",
            "Correlation ES MNQ","Tech Sector Impact MNQ","FAANG Stocks and NQ","Earnings Season MNQ","VIX and MNQ",
            "MNQ Scalp Setup London","MNQ Scalp Setup NY","MNQ Swing Setup","MNQ SMC Application","MNQ Liquidity Zones",
            "MNQ Order Book","MNQ DOM Trading","MNQ Footprint Chart","MNQ Volume Analysis","MNQ VWAP Strategy",
            "MNQ Fibonacci Levels","MNQ Support Resistance","MNQ Trend Following","MNQ Counter Trend","MNQ Breakout Trade",
            "MNQ News Trading","MNQ Risk Per Trade","MNQ Daily Loss Limit","MNQ Win Rate Target","MNQ Journal Setup",
            "MNQ Backtest Method","MNQ Prop Firm","Topstep MNQ","Apex Trader MNQ","Earn2Trade MNQ","MyFundedFutures",
            "MNQ Paper Trading","MNQ First Live Trade","MNQ Common Mistakes","MNQ Psychology","MNQ Community",
            "MNQ Weekly Recap","MNQ Monthly Review","MNQ vs Forex","MNQ Tax Thailand","MNQ Getting Started"]
for i, title in enumerate(mnq_fill, 101):
    if i <= 150:
        extra_scripts.append({
            "id": i, "category": "MNQ", "title": title,
            "hook": f"สิ่งที่นักเทรด MNQ มือใหม่ต้องรู้เกี่ยวกับ {title.split(' ')[0]}",
            "content": f"{title} เป็นหัวข้อสำคัญสำหรับการเทรด MNQ Futures ให้ประสบความสำเร็จ การเข้าใจเรื่องนี้จะช่วยลดความเสี่ยงและเพิ่มโอกาสในการทำกำไรอย่างสม่ำเสมอ",
            "cta": "ติดตาม Emotion Trades สำหรับ MNQ content"
        })

# Mindset #151-200
mindset_fill = ["Acceptance ในการเทรด","Process Based Thinking","Expected Value คืออะไร","Variance ในการเทรด",
                "Sample Size กับ Edge","Confidence vs Overconfidence","Patience เป็นทักษะ","Discipline คือกุญแจ",
                "Self-Awareness Trader","Emotional Regulation","Stress Management","Work-Life Balance Trader",
                "Sleep and Trading Performance","Exercise and Focus","Nutrition and Decision Making","Meditation for Traders",
                "Morning Routine Trader","Evening Review Routine","Weekend Preparation","Month End Review",
                "Setting Realistic Goals","Tracking Progress","Celebrating Small Wins","Learning from Losses",
                "Finding Your Edge","Defining Your Style","Building Consistency","Long-term Thinking","Career as Trader",
                "Trading as Business","Net Worth Building","Income Diversification","Emergency Fund Trader",
                "Risk of Ruin คืออะไร","Kelly Criterion","Optimal f","Fixed Ratio","Fixed Fractional",
                "Anti-Martingale","When to Scale Up","When to Stop Trading","Taking Breaks","Vacation and Trading",
                "Family Support Trading","Finding Mentors","Trading Community Value","Books for Traders","Podcasts Trading",
                "Trading Videos Learn","Paper Trading Value","Simulator Trading","Forward Testing"]
for i, title in enumerate(mindset_fill, 151):
    if i <= 200:
        extra_scripts.append({
            "id": i, "category": "Mindset", "title": title,
            "hook": f"นักเทรดที่ประสบความสำเร็จทุกคนรู้เรื่อง {title.split(' ')[0]} — คุณรู้ไหม?",
            "content": f"{title} คือส่วนหนึ่งของ trading psychology ที่มักถูกมองข้าม แต่กลับมีผลต่อผลลัพธ์การเทรดอย่างมาก การพัฒนาด้านนี้จะช่วยให้คุณรักษา consistency ได้ดีขึ้นในระยะยาว",
            "cta": "กด Follow เรียน Trading Psychology กับ Emotion Trades"
        })

# Myth #201-250
myth_fill = ["Myth: เทรดวันละ 100 pip ได้ทุกวัน","Myth: System ดีไม่มีแพ้","Myth: Forex ง่าย",
             "Myth: ดู YouTube แล้วเทรดได้เลย","Myth: ลงทุนน้อยรวยเร็ว","Myth: Bot เทรดแทนได้",
             "Myth: EA ทำกำไรได้ไม่หยุด","Myth: Signal ดีทำกำไรได้","Myth: เทรดระยะสั้นเสี่ยงกว่า",
             "Myth: Leverage สูงยิ่งดี","Myth: ต้องมีทุน 100k ขึ้นไป","Myth: เทรดช่วงข่าวห้ามทำ",
             "Myth: Pattern มักแม่น 100%","Myth: ใช้ Support Resistance ง่ายๆ","Myth: ทองวิ่งตาม indicator",
             "Myth: Scalping ไม่ได้กำไรระยะยาว","Myth: ต้องเทรดทุกวัน","Myth: Win rate ต้องสูงกว่า 70%",
             "Myth: เทรด 1 pair ดีที่สุด","Myth: เพิ่ม lot เพื่อเอาคืน","Myth: ตลาดมี Pattern ชัดเจนเสมอ",
             "Myth: Demo Trading ไม่มีประโยชน์","Myth: นักเทรดโปรไม่แพ้","Myth: Market Maker คือศัตรู",
             "Myth: เทรดพร้อมงานประจำไม่ได้","Myth: ต้องเรียนหลาย Course","Myth: ใหม่ทำกำไรได้เลย",
             "Myth: Stop Loss ไม่จำเป็น","Myth: Average Down ดีเสมอ","Myth: Cut Loss แล้วแพ้",
             "Myth: ทองขึ้นเสมอในระยะยาว","Myth: Dollar กับทองวิ่งสวนทางเสมอ","Myth: VIX สูง = เทรดยาก",
             "Myth: Trend following ง่าย","Myth: Counter trend trading ยาก","Myth: ต้องเทรดทุก setup",
             "Myth: กราฟแบบไหนก็เหมือนกัน","Myth: Broker ทุกเจ้าเหมือนกัน","Myth: เทรด Crypto ดีกว่า Forex",
             "Myth: AI เทรดแทนคนได้","Myth: Follow กูรูแล้วรวย","Myth: ซื้อของแพง = ดีกว่า",
             "Myth: ต้องมีคอมพิวเตอร์แรง","Myth: เทรดมือถือไม่ได้","Myth: Broker ขายทำกำไรจากคุณ",
             "Myth: Spread ไม่สำคัญ","Myth: Commission ไม่กระทบกำไร","Myth: Backtest ไม่มีประโยชน์","Myth: Forward test เท่านั้นที่สำคัญ"]
for i, title in enumerate(myth_fill, 201):
    if i <= 250:
        clean_title = title.replace("Myth: ","")
        extra_scripts.append({
            "id": i, "category": "Myth", "title": title,
            "hook": f"คนส่วนใหญ่เชื่อว่า {clean_title} — แต่ความจริงคือ...",
            "content": f"นี่คือความเชื่อผิดๆ ที่หลายคนยังยึดถืออยู่เกี่ยวกับ {clean_title} ความเข้าใจที่ถูกต้องจะช่วยให้คุณหลีกเลี่ยงกับดักที่ทำให้นักเทรดส่วนใหญ่ขาดทุน",
            "cta": "ติดตาม Emotion Trades เพื่อทลายความเชื่อผิดๆ ทุกวัน"
        })

# Soft Sell #251-300
soft_fill = ["ทำไมต้องเลือก Emotion Trades","Community ของเราต่างกันอย่างไร","Free vs Paid ได้อะไรต่างกัน",
             "Join Discord Emotion Trades","Discord VIP มีอะไรบ้าง","คอร์สสอนอะไรบ้าง","1on1 เหมาะกับใคร",
             "IB Exness ผ่าน Emotion Trades","IB HFM ผ่าน Emotion Trades","ทำไมต้องเปิดผ่าน IB link",
             "Results จาก Community","Member พูดถึงเราว่ายังไง","3 เดือนกับ Emotion Trades","ก่อน vs หลังเรียน SMC",
             "เรื่องเล่าจากมือใหม่","จาก Demo ไป Live Trade","วิธีเริ่มต้นกับเรา","FAQ คำถามที่ถามบ่อย",
             "ข้อผิดพลาดที่ Community ช่วยได้","การเรียนแบบ Active vs Passive","เป้าหมายของ Emotion Trades",
             "เราสอนอะไรบ้าง","Curriculum ครบ","Module แต่ละอัน","Bonus Material","Community Support",
             "Weekly Live Session","Q&A รายสัปดาห์","Trade Review Session","Chart Lab Practice",
             "Accountability Partner","Group Trading Challenge","Monthly Performance Review","Leaderboard Community",
             "Special Event Trading","Holiday Schedule","Black Friday Offer","New Year Trading Plan",
             "ต้อนรับสมาชิกใหม่","Referral Program","Invite เพื่อนมาเรียน","Family Plan Trading",
             "Student Success Story 1","Student Success Story 2","Student Story 3","Mentor Story",
             "Why SMC over Indicators","Why Gold and MNQ","Why Discord Community","Why Emotion Trades Thailand",
             "Final Call Join Us","Trade with Edge Not Emotion"]
for i, title in enumerate(soft_fill, 251):
    if i <= 300:
        extra_scripts.append({
            "id": i, "category": "Soft Sell", "title": title,
            "hook": f"{title} — อยากรู้ไหมว่า Emotion Trades ทำได้ยังไง?",
            "content": f"Emotion Trades คือ community เทรดที่เน้นสอน process ที่แท้จริง ไม่ขายฝัน ไม่ flex P&L ปลอม เรื่อง {title} เป็นส่วนหนึ่งที่ทำให้เรา community ที่ผู้เรียนเติบโตได้จริง",
            "cta": "เข้า Discord Emotion Trades ฟรีได้เลย — link ใน bio"
        })

# Load and merge scripts
with open(f"{BASE}/scripts.json") as f:
    data = json.load(f)

existing_ids = {s["id"] for s in data["scripts"]}
for s in extra_scripts:
    if s["id"] not in existing_ids:
        data["scripts"].append(s)
        existing_ids.add(s["id"])

data["scripts"].sort(key=lambda x: x["id"])
print(f"Total scripts: {len(data['scripts'])}")

with open(f"{BASE}/scripts.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# ─── Facebook Posts 300 items ──────────────────────────────────────────────
with open(f"{BASE}/posts.json") as f:
    pdata = json.load(f)

existing_post_ids = {p["id"] for p in pdata["posts"]}

fb_templates = [
    # SMC/ICT 50 posts
    (31,"SMC/ICT","Liquidity Hunt คืออะไร","SL ของคุณโดนกินแล้วราคากลับทิศทันที — ไม่ใช่ดวงร้าย มันถูกออกแบบมา\n\nLiquidity Hunt คือเมื่อ Smart Money ดัน/กดราคาไปกวาด Stop Loss ของ retail ก่อนที่จะ reverse ทิศแท้จริง\n\nวิธีรับมือ: ตั้ง SL ห่างจาก obvious level รอให้ราคา sweep ก่อนแล้วค่อยเข้า\n\n💹 Emotion Trades | Trade with Edge, Not Emotion"),
    (32,"SMC/ICT","Order Block Entry","Order Block คือจุด entry ที่ Big Player เข้าสะสม — คุณเข้าตามได้\n\nหา OB: ดูแท่งเทียนสุดท้ายก่อน big move ราคากลับมา retest = โอกาส entry\n\nทำงานได้บน XAU, MNQ, ทุก pair\n\n💹 Emotion Trades | Trade with Edge, Not Emotion"),
    (33,"SMC/ICT","FVG Fill Strategy","ช่องว่างบน chart มีเหตุผลอยู่เสมอ — และราคามักกลับมาเติม\n\nFair Value Gap เกิดเมื่อราคาวิ่งเร็วเกิน เหลือช่องว่างระหว่างแท่งเทียน ราคามักกลับมา fill ก่อนวิ่งต่อ\n\n💹 Emotion Trades | Trade with Edge, Not Emotion"),
    (34,"SMC/ICT","BOS คือสัญญาณ Trend ต่อ","ราคา break high ใหม่ใน uptrend = BOS = Trend ยังไปต่อ\n\nอย่าเพิ่ง short แค่เพราะคิดว่าแพง รอ CHoCH ก่อนที่จะคิดเรื่อง Reversal\n\n💹 Emotion Trades | Trade with Edge, Not Emotion"),
    (35,"SMC/ICT","CHoCH Warning Signal","CHoCH ใน uptrend = เตือนว่า trend อาจเปลี่ยน\n\nเมื่อราคาทำ lower low เป็นครั้งแรกใน uptrend — นั่นคือ Change of Character หยุด buy และเฝ้าระวัง\n\n💹 Emotion Trades | Trade with Edge, Not Emotion"),
]

# Generate remaining FB posts
cats_fb = ["SMC/ICT","XAU","MNQ","Mindset","Myth","Soft Sell"]
cat_counts = {c: 0 for c in cats_fb}
for p in pdata["posts"]:
    cat_counts[p["category"]] = cat_counts.get(p["category"], 0) + 1

# Add template posts
for id_, cat, title, caption in fb_templates:
    if id_ not in existing_post_ids:
        pdata["posts"].append({"id": id_, "category": cat, "title": title, "caption": caption})
        existing_post_ids.add(id_)

# Fill to 300
next_id = max(existing_post_ids) + 1 if existing_post_ids else 36
topics_by_cat = {
    "SMC/ICT": ["Premium Discount Zone","Power of 3","Killzone Trading","OTE Setup","ICT Concepts","Inducement","Breaker Block",
                "Mitigation Block","Displacement","Market Structure","Swing High Low","HTF Analysis","LTF Entry","Confluence",
                "SMC Complete System","Daily Bias Setup","Weekly Bias","Internal Structure","Session Analysis","AMD Cycle"],
    "XAU": ["Gold Seasonality","Central Bank Gold","NFP Strategy","CPI Impact Gold","Fed Rate Gold","Gold vs Dollar",
            "Real Interest Rate","Gold ETF Flow","Gold Technical Setup","XAU Weekly Outlook","Gold Scalp Setup",
            "Gold Swing Setup","Gold Risk Management","Gold News Strategy","Gold Morning Routine",
            "XAU Monthly Outlook","Gold vs Bitcoin","Gold Safe Haven","Gold Level Watch","Gold Analysis Daily"],
    "MNQ": ["MNQ Introduction","MNQ vs NQ","MNQ Session Time","MNQ RTH ETH","MNQ Scalp Setup","MNQ Swing Setup",
            "MNQ Risk Per Trade","MNQ Daily Loss Limit","MNQ Prop Firm","MNQ SMC Setup",
            "MNQ Opening Range","MNQ Gap Strategy","MNQ Volume Analysis","MNQ Psychology","MNQ Journal",
            "MNQ Backtest","MNQ Community","MNQ Mistakes","MNQ Getting Started","MNQ Success"],
    "Mindset": ["FOMO Fix","Revenge Trade Stop","Discipline Building","Process Focus","Acceptance Loss",
                "Win Rate Reality","RR Calculator","Journal Benefits","Backtest Value","Consistency Key",
                "Morning Routine","Evening Review","Weekend Prep","Goal Setting","Progress Tracking",
                "Stress Management","Sleep Performance","Exercise Focus","Long Term Vision","Trader Career"],
    "Myth": ["No Indicator Myth","Signal Provider Truth","Get Rich Quick Reality","Copy Trade Reality","Leverage Truth",
             "Capital Myth","Screen Time Myth","Win Rate Myth","Pattern Myth","Demo Value",
             "Bot EA Reality","News Trading Myth","Scalp Long Term","Counter Trend Myth","Broker Myth",
             "Crypto vs Forex","AI Trading Reality","Guru Following Reality","Expensive = Better Myth","Backtest Myth"],
    "Soft Sell": ["Join Discord Free","Discord VIP Benefits","Course Overview","1on1 Mentorship","IB Program",
                  "Community Results","Member Stories","Free vs Paid","Why Emotion Trades","Getting Started",
                  "Weekly Live Session","Trade Review","Community Support","Referral Program","Success Stories",
                  "FAQ Trading","Special Events","New Member Welcome","Monthly Challenge","Final CTA"],
}

needed_per_cat = 50
for cat in cats_fb:
    current = sum(1 for p in pdata["posts"] if p["category"] == cat)
    needed = needed_per_cat - current
    if needed <= 0:
        continue
    fill_topics = topics_by_cat.get(cat, [])
    for j in range(needed):
        topic = fill_topics[j % len(fill_topics)] if fill_topics else f"{cat} Tips {j+1}"
        pdata["posts"].append({
            "id": next_id,
            "category": cat,
            "title": topic,
            "caption": f"{topic} — สิ่งที่นักเทรดต้องรู้\n\nEmotionTrades แชร์ความรู้เรื่องนี้เพื่อให้คุณเทรดได้ดีขึ้น ไม่ขายฝัน แชร์ของจริง\n\nJoin community ฟรีได้เลย\n\n💹 Emotion Trades | Trade with Edge, Not Emotion"
        })
        existing_post_ids.add(next_id)
        next_id += 1

pdata["posts"].sort(key=lambda x: x["id"])
print(f"Total posts: {len(pdata['posts'])}")

with open(f"{BASE}/posts.json", "w", encoding="utf-8") as f:
    json.dump(pdata, f, ensure_ascii=False, indent=2)

print("Done! Content expanded.")
