// Emotion Trades — App JS
const API = { scripts: 'data/scripts.json', posts: 'data/posts.json', prompts: 'data/prompts.json' };
let cache = {};

async function load(key) {
  if (cache[key]) return cache[key];
  const r = await fetch(API[key]);
  cache[key] = await r.json();
  return cache[key];
}

function copyText(text, btn) {
  navigator.clipboard.writeText(text).then(() => {
    const orig = btn.textContent;
    btn.textContent = '✅ Copied!';
    btn.classList.add('copied');
    setTimeout(() => { btn.textContent = orig; btn.classList.remove('copied'); }, 1800);
  }).catch(() => {
    const ta = document.createElement('textarea');
    ta.value = text; document.body.appendChild(ta); ta.select();
    document.execCommand('copy'); document.body.removeChild(ta);
    btn.textContent = '✅ Copied!'; btn.classList.add('copied');
    setTimeout(() => { btn.textContent = '📋 Copy'; btn.classList.remove('copied'); }, 1800);
  });
}

function catClass(cat) {
  const m = { 'SMC/ICT':'SMC','XAU':'XAU','MNQ':'MNQ','Mindset':'Mindset','Myth':'Myth','Soft Sell':'Soft' };
  return 'cat-' + (m[cat] || 'SMC');
}

// ── SCRIPTS PAGE ─────────────────────────────────────────────
async function initScripts() {
  const data = await load('scripts');
  const grid = document.getElementById('scripts-grid');
  const count = document.getElementById('result-count');
  let current = data.scripts;

  function render(items) {
    count.textContent = `แสดง ${items.length} scripts`;
    if (!items.length) { grid.innerHTML = '<div class="empty"><div class="icon">🔍</div><p>ไม่พบ script ที่ค้นหา</p></div>'; return; }
    grid.innerHTML = items.map(s => `
      <div class="script-card" data-cat="${s.category}">
        <div class="card-header">
          <span class="card-num">#${s.id}</span>
          <span class="cat-badge ${catClass(s.category)}">${s.category}</span>
        </div>
        <div class="card-title">${s.title}</div>
        <div class="card-section">
          <div class="card-label">🎣 Hook</div>
          <div class="card-text">${s.hook}</div>
        </div>
        <div class="card-section">
          <div class="card-label">📹 Content</div>
          <div class="card-text">${s.content}</div>
        </div>
        <div class="card-section">
          <div class="card-label">📢 CTA</div>
          <div class="card-text">${s.cta}</div>
        </div>
        <div class="card-actions">
          <button class="btn-copy" onclick="copyText(\`🎣 Hook:\\n${s.hook.replace(/`/g,"'")}\\n\\n📹 Content:\\n${s.content.replace(/`/g,"'")}\\n\\n📢 CTA:\\n${s.cta.replace(/`/g,"'")}\`,this)">📋 Copy Script</button>
          <button class="btn-copy" style="flex:0;background:#2a3150;color:var(--text)" onclick="copyText(\`${s.hook.replace(/`/g,"'")}\`,this)">Hook</button>
        </div>
      </div>`).join('');
  }

  function filter() {
    const cat = document.querySelector('.filter-btn.active')?.dataset.cat || 'all';
    const q = document.getElementById('search')?.value.toLowerCase() || '';
    let items = data.scripts;
    if (cat !== 'all') items = items.filter(s => s.category === cat);
    if (q) items = items.filter(s => (s.title+s.hook+s.content+s.cta).toLowerCase().includes(q));
    render(items);
  }

  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active'); filter();
    });
  });
  document.getElementById('search')?.addEventListener('input', filter);
  render(current);
}

// ── FACEBOOK PAGE ─────────────────────────────────────────────
async function initFacebook() {
  const data = await load('posts');
  const grid = document.getElementById('posts-grid');
  const count = document.getElementById('result-count');

  function render(items) {
    count.textContent = `แสดง ${items.length} posts`;
    if (!items.length) { grid.innerHTML = '<div class="empty"><div class="icon">🔍</div><p>ไม่พบ post ที่ค้นหา</p></div>'; return; }
    grid.innerHTML = items.map(p => `
      <div class="post-card" data-cat="${p.category}">
        <div class="card-header">
          <span class="card-num">#${p.id}</span>
          <span class="cat-badge ${catClass(p.category)}">${p.category}</span>
        </div>
        <div class="card-title">${p.title}</div>
        <div class="post-caption" id="cap-${p.id}">${p.caption.replace(/\n/g,'<br>')}</div>
        <div class="card-actions">
          <button class="btn-copy" onclick="copyText(\`${p.caption.replace(/`/g,"'")}\`,this)">📋 Copy Caption</button>
          <button class="btn-copy" style="flex:0;background:#2a3150;color:var(--text)" onclick="toggleCaption('cap-${p.id}',this)">▼</button>
        </div>
      </div>`).join('');
  }

  function filter() {
    const cat = document.querySelector('.filter-btn.active')?.dataset.cat || 'all';
    const q = document.getElementById('search')?.value.toLowerCase() || '';
    let items = data.posts;
    if (cat !== 'all') items = items.filter(p => p.category === cat);
    if (q) items = items.filter(p => (p.title+p.caption).toLowerCase().includes(q));
    render(items);
  }

  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active'); filter();
    });
  });
  document.getElementById('search')?.addEventListener('input', filter);
  render(data.posts);
}

window.toggleCaption = function(id, btn) {
  const el = document.getElementById(id);
  el.classList.toggle('expanded');
  btn.textContent = el.classList.contains('expanded') ? '▲' : '▼';
};

// ── PROMPTS PAGE ──────────────────────────────────────────────
async function initPrompts() {
  const data = await load('prompts');
  const grid = document.getElementById('prompts-grid');

  function render(items) {
    if (!items.length) { grid.innerHTML = '<div class="empty"><div class="icon">🎨</div><p>ไม่พบ prompt</p></div>'; return; }
    grid.innerHTML = items.map(p => `
      <div class="prompt-card">
        <div class="card-header">
          <span class="card-num">#${p.id}</span>
          <span class="cat-badge cat-SMC">${p.category || 'General'}</span>
        </div>
        <div class="prompt-title">${p.title}</div>
        <div class="prompt-text">${p.prompt}</div>
        <button class="btn-copy" onclick="copyText(\`${p.prompt.replace(/`/g,"'")}\`,this)">📋 Copy Prompt</button>
      </div>`).join('');
  }

  document.getElementById('search')?.addEventListener('input', e => {
    const q = e.target.value.toLowerCase();
    render(q ? data.prompts.filter(p => (p.title+p.prompt).toLowerCase().includes(q)) : data.prompts);
  });
  render(data.prompts);
}

// ── CALENDAR PAGE ─────────────────────────────────────────────
function initCalendar() {
  const KEY = 'et_calendar';
  let cal = JSON.parse(localStorage.getItem(KEY) || '{}');
  const today = new Date();
  let viewDate = new Date(today.getFullYear(), today.getMonth(), 1);

  function save() { localStorage.setItem(KEY, JSON.stringify(cal)); }

  function render() {
    const y = viewDate.getFullYear(), m = viewDate.getMonth();
    document.getElementById('cal-title').textContent = viewDate.toLocaleDateString('th-TH', { month:'long', year:'numeric' });
    const firstDay = new Date(y, m, 1).getDay();
    const daysInMonth = new Date(y, m+1, 0).getDate();
    const grid = document.getElementById('cal-grid');
    const days = ['อา','จ','อ','พ','พฤ','ศ','ส'];
    let html = days.map(d => `<div class="cal-day-label">${d}</div>`).join('');
    for (let i=0; i<firstDay; i++) html += '<div></div>';
    for (let d=1; d<=daysInMonth; d++) {
      const key = `${y}-${m+1}-${d}`;
      const isToday = (d===today.getDate() && m===today.getMonth() && y===today.getFullYear());
      const c = cal[key] || { tiktok:0, fb:0 };
      html += `<div class="cal-day${isToday?' today':''}${(c.tiktok||c.fb)?' has-content':''}" onclick="editDay('${key}','${d}')">
        <div class="day-num">${d}</div>
        ${c.tiktok ? `<div class="day-chip chip-tiktok">🎵 ${c.tiktok}</div>` : ''}
        ${c.fb ? `<div class="day-chip chip-fb">📘 ${c.fb}</div>` : ''}
      </div>`;
    }
    grid.innerHTML = html;
    // Summary
    let totalTT=0, totalFB=0;
    Object.values(cal).forEach(v => { totalTT+=v.tiktok||0; totalFB+=v.fb||0; });
    document.getElementById('cal-summary').textContent = `รวมทั้งเดือน: 🎵 TikTok ${totalTT} คลิป | 📘 Facebook ${totalFB} โพส`;
  }

  window.editDay = function(key, d) {
    const c = cal[key] || { tiktok:0, fb:0 };
    const tt = prompt(`วันที่ ${d} — TikTok กี่คลิป?`, c.tiktok);
    if (tt === null) return;
    const fb = prompt(`วันที่ ${d} — Facebook กี่โพส?`, c.fb);
    if (fb === null) return;
    cal[key] = { tiktok: parseInt(tt)||0, fb: parseInt(fb)||0 };
    save(); render();
  };

  document.getElementById('prev-month')?.addEventListener('click', () => { viewDate.setMonth(viewDate.getMonth()-1); render(); });
  document.getElementById('next-month')?.addEventListener('click', () => { viewDate.setMonth(viewDate.getMonth()+1); render(); });
  render();
}

// ── NEWS BUILDER ──────────────────────────────────────────────
function initNews() {
  document.getElementById('generate-btn')?.addEventListener('click', () => {
    const headline = document.getElementById('news-headline').value.trim();
    const detail = document.getElementById('news-detail').value.trim();
    const impact = document.getElementById('news-impact').value;
    const asset = document.getElementById('news-asset').value;
    if (!headline) { alert('กรุณากรอกหัวข้อข่าว'); return; }

    const impactEmoji = { High:'🔴', Medium:'🟡', Low:'🟢' }[impact] || '⚪';
    const assetInfo = {
      XAU: 'Gold (XAU/USD) มักตอบสนองต่อข่าวนี้ด้วยความผันผวนสูง ควรเฝ้าระวัง level สำคัญ',
      MNQ: 'Nasdaq Futures (MNQ) มักได้รับผลกระทบจากข่าวนี้ ระวัง gap opening',
      DXY: 'Dollar Index (DXY) เคลื่อนตัว ส่งผลต่อ XAU และ pairs อื่นๆ',
      ALL: 'ตลาดทุกสินทรัพย์อาจได้รับผลกระทบ ควรลด size และเพิ่ม SL'
    }[asset] || '';

    const tiktokHook = `${impactEmoji} ข่าว${impact} impact เพิ่งออก — ${headline}`;
    const tiktokContent = `${detail}\n\n${assetInfo}\n\nStrategy: รอ initial spike สงบก่อน แล้วค่อยหา reversal setup ห้ามเข้าระหว่างข่าวเด็ดขาด`;
    const tiktokCTA = `ติดตาม Emotion Trades รับ news update ทุกวัน 📡`;

    const fbPost = `${impactEmoji} Breaking: ${headline}\n\n${detail}\n\nผลต่อการเทรด:\n${assetInfo}\n\n🎯 วิธีรับมือ:\n→ อย่าเปิด trade ระหว่างข่าว\n→ รอ spike สงบ 10-15 นาที\n→ หา SMC setup หลังข่าว\n\n💹 Emotion Trades | Trade with Edge, Not Emotion`;

    document.getElementById('output-tiktok-hook').textContent = tiktokHook;
    document.getElementById('output-tiktok').textContent = `Hook:\n${tiktokHook}\n\nContent:\n${tiktokContent}\n\nCTA:\n${tiktokCTA}`;
    document.getElementById('output-fb').textContent = fbPost;
    document.getElementById('output-section').style.display = 'block';
  });
}

// ── AUTO INIT ─────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  const page = document.body.dataset.page;
  if (page === 'scripts') initScripts();
  else if (page === 'facebook') initFacebook();
  else if (page === 'prompts') initPrompts();
  else if (page === 'calendar') initCalendar();
  else if (page === 'news') initNews();
});
