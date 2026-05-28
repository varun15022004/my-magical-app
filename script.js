(function(){
'use strict';

const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];

const today = new Date();
const daySeed = today.toDateString();

const affirmations = [
  "You are doing amazing sweetie ✧",
  "One task at a time 🌸",
  "Today is a gift 💝",
  "You're made of stars and sugar ✩",
  "Small steps still count 🐾",
  "Be kind to yourself today 🌷",
  "Your best is enough ✨",
  "Stay cozy and dream big ☁️",
  "You glow differently when you smile 🌟",
  "Every flower blooms in its own time 🌻",
  "You have magic inside you ✦",
  "Rest is productive too 🧸",
  "Today is full of possibilities 🌈",
  "You are loved and cherished ♡",
  "Go at your own pace 🐢"
];

const moodData = {
  happy: { emoji: "😊", label: "Happy", receiptEmoji: "🌸✨" },
  tired: { emoji: "😴", label: "Tired", receiptEmoji: "🌙💤" },
  stressed: { emoji: "😰", label: "Stressed", receiptEmoji: "🌊🧘" },
  excited: { emoji: "🤩", label: "Excited", receiptEmoji: "🎉🌟" },
  cozy: { emoji: "☕", label: "Cozy", receiptEmoji: "☕🧸" },
  productive: { emoji: "💪", label: "Productive", receiptEmoji: "⚡🌟" }
};

const defaultState = {
  name: 'Bunny',
  mood: 'happy',
  theme: 'cherry',
  sound: true,
  events: [],
  todos: []
};

let state = JSON.parse(JSON.stringify(defaultState));

let audioCtx = null;
function getAudioCtx() {
  if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  return audioCtx;
}

function playTypewriter() {
  if (!state.sound) return;
  try {
    const ctx = getAudioCtx();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.connect(gain); gain.connect(ctx.destination);
    osc.type = 'square'; osc.frequency.value = 800 + Math.random() * 400;
    gain.gain.setValueAtTime(0.06, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.04);
    osc.start(ctx.currentTime); osc.stop(ctx.currentTime + 0.04);
  } catch(e) {}
}

function playKaChunk() {
  if (!state.sound) return;
  try {
    const ctx = getAudioCtx();
    const bufSize = ctx.sampleRate * 0.15;
    const buf = ctx.createBuffer(1, bufSize, ctx.sampleRate);
    const data = buf.getChannelData(0);
    for (let i = 0; i < bufSize; i++) {
      data[i] = (Math.random() * 2 - 1) * Math.exp(-i / (ctx.sampleRate * 0.03));
    }
    const noise = ctx.createBufferSource();
    noise.buffer = buf;
    const ng = ctx.createGain();
    ng.gain.setValueAtTime(0.15, ctx.currentTime);
    ng.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.15);
    noise.connect(ng); ng.connect(ctx.destination);
    noise.start(ctx.currentTime);

    const osc = ctx.createOscillator();
    const og = ctx.createGain();
    osc.connect(og); og.connect(ctx.destination);
    osc.type = 'sine'; osc.frequency.setValueAtTime(150, ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(40, ctx.currentTime + 0.12);
    og.gain.setValueAtTime(0.2, ctx.currentTime);
    og.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.12);
    osc.start(ctx.currentTime); osc.stop(ctx.currentTime + 0.12);

    const osc2 = ctx.createOscillator();
    const og2 = ctx.createGain();
    osc2.connect(og2); og2.connect(ctx.destination);
    osc2.type = 'square'; osc2.frequency.value = 2000;
    og2.gain.setValueAtTime(0.05, ctx.currentTime);
    og2.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.02);
    osc2.start(ctx.currentTime); osc2.stop(ctx.currentTime + 0.02);
  } catch(e) {}
}

function playChime() {
  if (!state.sound) return;
  try {
    const ctx = getAudioCtx();
    const now = ctx.currentTime;
    [523.25, 659.25, 783.99].forEach((freq, i) => {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.connect(gain); gain.connect(ctx.destination);
      osc.type = 'sine';
      osc.frequency.value = freq;
      gain.gain.setValueAtTime(0, now + i * 0.08);
      gain.gain.linearRampToValueAtTime(0.12, now + i * 0.08 + 0.02);
      gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.08 + 0.2);
      osc.start(now + i * 0.08); osc.stop(now + i * 0.08 + 0.2);
    });
  } catch(e) {}
}

function getDailyAffirmation() {
  let hash = 0;
  for (let i = 0; i < daySeed.length; i++) {
    hash = ((hash << 5) - hash) + daySeed.charCodeAt(i); hash |= 0;
  }
  return affirmations[Math.abs(hash) % affirmations.length];
}

function render() {
  $('#nameInput').value = state.name;
  $('#soundToggle').checked = state.sound;

  $$('.mood-btn').forEach(b => b.classList.toggle('active', b.dataset.mood === state.mood));
  $$('.theme-btn').forEach(b => b.classList.toggle('active', b.dataset.theme === state.theme));

  ['bgCherry','bgNight','bgClouds'].forEach(id => {
    const el = $(`#${id}`);
    if ((id === 'bgCherry' && state.theme === 'cherry') ||
        (id === 'bgNight' && state.theme === 'night') ||
        (id === 'bgClouds' && state.theme === 'clouds')) {
      el.classList.remove('hidden');
    } else {
      el.classList.add('hidden');
    }
  });

  $('#avatar').textContent = moodData[state.mood]?.emoji || '🐰';

  $('#receiptDate').textContent = today.toLocaleDateString(undefined, {
    weekday: 'short', month: 'short', day: 'numeric'
  });
  $('#receiptMood').textContent = moodData[state.mood]?.receiptEmoji || '🌸✨';
  $('#receiptTitle').textContent = `${state.name || 'My'}'s Magical Day`;
  $('#receiptSubtitle').textContent = `✦ ${moodData[state.mood]?.label || 'Happy'} vibes today ✦`;

  const eventsList = $('#eventsList');
  if (state.events.length) {
    eventsList.innerHTML = state.events.map(e => `<li data-type="event" data-id="${e.id}">
      <span class="category-dot ${e.category}">${e.category === 'personal' ? '🌸' : e.category === 'work' ? '💼' : e.category === 'study' ? '📖' : '🎨'}</span>
      <span class="task-label">${esc(e.label)}${e.time ? ' <span class="task-time">'+esc(e.time)+'</span>' : ''}</span>
      <span class="task-time">${e.link ? '🔗' : ''}</span>
    </li>`).join('');
  } else {
    eventsList.innerHTML = '<li class="empty">No events yet. Add a tiny adventure ✨</li>';
  }

  const todosList = $('#todosList');
  if (state.todos.length) {
    todosList.innerHTML = state.todos.map(t => {
      const stars = t.priority === 'high' ? '⭐⭐⭐' : t.priority === 'medium' ? '⭐⭐' : '⭐';
      const cls = t.done ? 'done' : '';
      return `<li class="${cls}" data-type="todo" data-id="${t.id}">
        <span class="category-dot ${t.category}">${t.category === 'personal' ? '🌸' : t.category === 'work' ? '💼' : t.category === 'study' ? '📖' : '🎨'}</span>
        <span class="task-label">${esc(t.label)}</span>
        <span class="priority-stars">${stars}</span>
      </li>`;
    }).join('');
  } else {
    todosList.innerHTML = '<li class="empty">No quests yet. Add a cute task ♡</li>';
  }

  const done = state.todos.filter(t => t.done).length;
  $('#eventCount').textContent = state.events.length;
  $('#todoCount').textContent = state.todos.length;
  $('#doneCount').textContent = done;

  const pct = state.todos.length ? Math.round(done / state.todos.length * 100) : 0;
  $('#progressBar').style.width = pct + '%';
  $('#receiptProgressFill').style.width = pct + '%';
  $('#progressCount').textContent = `${done}/${state.todos.length} done 🌟`;
  $('#progressLabel').textContent = done === state.todos.length && state.todos.length ? '✨ All quests cleared! ✨' : 'quest progress';

  $('#affirmationBox').textContent = getDailyAffirmation();
}

function esc(str) {
  const d = document.createElement('div');
  d.textContent = str;
  return d.innerHTML;
}

function burstSparkle(x, y, n = 8) {
  const chars = ['✦','✧','⋆','♡','✩','☆'];
  const colors = ['#FFB0D4','#E882C0','#FFD700','#B28AD0','#6EDAB4','#FF99C8'];
  for (let i = 0; i < n; i++) {
    const el = document.createElement('span');
    el.className = 'click-sparkle';
    el.textContent = chars[Math.floor(Math.random() * chars.length)];
    el.style.left = x + 'px';
    el.style.top = y + 'px';
    el.style.color = colors[Math.floor(Math.random() * colors.length)];
    const angle = Math.random() * Math.PI * 2;
    const dist = 25 + Math.random() * 55;
    el.style.setProperty('--sx', Math.cos(angle) * dist + 'px');
    el.style.setProperty('--sy', Math.sin(angle) * dist + 'px');
    document.body.appendChild(el);
    el.addEventListener('animationend', () => el.remove());
  }
}

function heartBurst(x, y) {
  const container = document.createElement('div');
  container.className = 'heart-burst';
  container.style.position = 'fixed';
  container.style.inset = '0';
  container.style.pointerEvents = 'none';
  container.style.zIndex = '150';
  document.body.appendChild(container);

  const hearts = ['♡','♥','✧','✦','⋆','✩','🌸','✨','💖','🌟'];
  const colors = ['#FFB0D4','#E882C0','#FFD700','#FF99C8','#B28AD0','#FF6B9D','#FFE066'];

  for (let i = 0; i < 30; i++) {
    const el = document.createElement('span');
    el.className = 'heart-particle';
    el.textContent = hearts[Math.floor(Math.random() * hearts.length)];
    el.style.position = 'absolute';
    el.style.left = x + 'px';
    el.style.top = y + 'px';
    el.style.setProperty('--size', (14 + Math.random() * 18) + 'px');
    el.style.setProperty('--hcolor', colors[Math.floor(Math.random() * colors.length)]);
    const angle = Math.random() * Math.PI * 2;
    const dist = 60 + Math.random() * 140;
    el.style.setProperty('--fx', Math.cos(angle) * dist + 'px');
    el.style.setProperty('--fy', Math.sin(angle) * dist - 60 + 'px');
    el.style.setProperty('--dur', (0.6 + Math.random() * 0.6) + 's');
    container.appendChild(el);
  }

  setTimeout(() => container.remove(), 1500);
}

function printReceipt() {
  const receipt = $('#receipt');
  const printerBody = $('#printerBody');
  const printBtn = $('#printBtn');

  if (printBtn.classList.contains('is-printing')) return;
  printBtn.classList.add('is-printing');

  receipt.classList.remove('open');
  receipt.classList.add('closed');

  printerBody.classList.remove('printer-breathe', 'printer-shake');

  setTimeout(() => {
    printerBody.classList.add('printer-shake');
    playKaChunk();

    const rect = printerBody.getBoundingClientRect();
    const px = rect.left + rect.width / 2;
    const py = rect.top + rect.height * 0.35;

    for (let i = 0; i < 8; i++) {
      setTimeout(() => {
        const p = document.createElement('span');
        p.className = 'print-particle';
        p.textContent = ['♡','✧','✦','⋆','☆','♥'][Math.floor(Math.random() * 6)];
        p.style.left = px + 'px';
        p.style.top = py + 'px';
        p.style.color = ['#FFB0D4','#E882C0','#FFD700','#FF99C8','#B28AD0'][Math.floor(Math.random() * 5)];
        const angle = -Math.PI / 2 + (Math.random() - 0.5) * Math.PI * 0.8;
        const dist = 40 + Math.random() * 80;
        p.style.setProperty('--dx', Math.cos(angle) * dist + 'px');
        p.style.setProperty('--dy', Math.sin(angle) * dist + 'px');
        document.body.appendChild(p);
        p.addEventListener('animationend', () => p.remove());
      }, i * 60);
    }
  }, 200);

  setTimeout(() => {
    printerBody.classList.remove('printer-shake');
    printerBody.classList.add('printer-breathe');
    render();
    receipt.classList.remove('closed');
    void receipt.offsetWidth;
    receipt.classList.add('open');

    const rect = printerBody.getBoundingClientRect();
    heartBurst(rect.left + rect.width / 2, rect.top + rect.height * 0.4);
    playChime();

    printBtn.classList.remove('is-printing');
  }, 1200);
}

let editTarget = null;

function openModal(type, item = null) {
  editTarget = item;
  $('#itemType').value = type;
  $('#itemId').value = item?.id || '';
  $('#modalTitle').textContent = item ? `Edit ${type} charm` : `Add ${type} charm`;
  $('#itemLabel').value = item?.label || '';
  $('#itemTime').value = item?.time || '';
  $('#itemLink').value = item?.link || '';
  $('#itemCategory').value = item?.category || 'personal';
  $('#itemPriority').value = item?.priority || 'medium';

  $('#eventFields').style.display = type === 'event' ? 'block' : 'none';
  $('#priorityField').style.display = type === 'todo' ? 'block' : 'none';

  $('#deleteBtn').style.display = item ? 'inline-block' : 'none';
  $('#modalOverlay').classList.add('open');
  setTimeout(() => $('#itemLabel').focus(), 80);
}

function closeModal() {
  $('#modalOverlay').classList.remove('open');
  editTarget = null;
}

$('#addEventBtn').addEventListener('click', () => openModal('event'));
$('#addTodoBtn').addEventListener('click', () => openModal('todo'));
$('#modalClose').addEventListener('click', closeModal);
$('#modalOverlay').addEventListener('click', (e) => {
  if (e.target === $('#modalOverlay')) closeModal();
});

$('#saveBtn').addEventListener('click', (e) => {
  e.preventDefault();
  const type = $('#itemType').value;
  const id = $('#itemId').value;
  const list = type === 'event' ? state.events : state.todos;
  const label = $('#itemLabel').value.trim();
  if (!label) return;

  const data = {
    id: id || crypto.randomUUID(),
    label,
    category: $('#itemCategory').value
  };
  if (type === 'event') {
    data.time = $('#itemTime').value.trim();
    data.link = $('#itemLink').value.trim();
  } else {
    data.priority = $('#itemPriority').value;
    data.done = editTarget?.done || false;
  }

  const idx = list.findIndex(x => x.id === id);
  if (idx >= 0) {
    list.splice(idx, 1, data);
  } else {
    list.push(data);
  }

  closeModal();
  render();
  burstSparkle(window.innerWidth / 2, window.innerHeight / 2, 10);
  playChime();
});

$('#deleteBtn').addEventListener('click', () => {
  const type = $('#itemType').value;
  const id = $('#itemId').value;
  const list = type === 'event' ? state.events : state.todos;
  const idx = list.findIndex(x => x.id === id);
  if (idx >= 0) list.splice(idx, 1);
  closeModal();
  render();
});

$('#receipt').addEventListener('click', (e) => {
  const li = e.target.closest('li[data-id]');
  if (!li) return;
  const type = li.dataset.type;
  const id = li.dataset.id;
  const list = type === 'event' ? state.events : state.todos;
  const item = list.find(x => x.id === id);
  if (!item) return;

  if (type === 'event') {
    openModal('event', item);
    return;
  }

  if (e.target.closest('.task-label') || e.target.closest('.priority-stars') || e.target.closest('.category-dot')) {
    item.done = !item.done;
    render();
    if (item.done) {
      burstSparkle(e.clientX, e.clientY, 12);
      playChime();
    }
    return;
  }

  openTarget(item);
});

function openTarget(item) {
  openModal('todo', item);
}

$('#receipt').addEventListener('dblclick', (e) => {
  const li = e.target.closest('li[data-id]');
  if (!li || li.dataset.type !== 'todo') return;
  const item = state.todos.find(t => t.id === li.dataset.id);
  if (item) openModal('todo', item);
});

$('#nameInput').addEventListener('input', () => {
  state.name = $('#nameInput').value;
  render();
});

$('#soundToggle').addEventListener('change', () => {
  state.sound = $('#soundToggle').checked;
});

$$('.mood-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    state.mood = btn.dataset.mood;
    render();
  });
});

$$('.theme-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    state.theme = btn.dataset.theme;
    render();
  });
});

$('#printBtn').addEventListener('click', printReceipt);

function showConfirm() {
  $('#confirmOverlay').classList.add('open');
}
function hideConfirm() {
  $('#confirmOverlay').classList.remove('open');
}

$('#resetBtn').addEventListener('click', showConfirm);
$('#confirmNo').addEventListener('click', hideConfirm);
$('#confirmOverlay').addEventListener('click', (e) => {
  if (e.target === $('#confirmOverlay')) hideConfirm();
});
$('#confirmYes').addEventListener('click', () => {
  state = JSON.parse(JSON.stringify(defaultState));
  state.events.forEach(e => e.id = crypto.randomUUID());
  state.todos.forEach(t => t.id = crypto.randomUUID());
  hideConfirm();
  render();
  const receipt = $('#receipt');
  receipt.classList.remove('open');
  receipt.classList.add('closed');
  burstSparkle(window.innerWidth / 2, window.innerHeight / 2, 15);
  playChime();
});

['#itemLabel','#itemTime','#nameInput','#itemLink'].forEach(sel => {
  const el = $(sel);
  if (el) el.addEventListener('keydown', playTypewriter);
});

function createBgElements() {
  const sparkles = $('#bgSparkles');
  for (let i = 0; i < 90; i++) {
    const s = document.createElement('span');
    s.className = 'bg-sparkle';
    const z = 2 + Math.random() * 4;
    s.style.cssText = `width:${z}px;height:${z}px;left:${Math.random()*100}%;top:${Math.random()*100}%;--dur:${2+Math.random()*4}s;--delay:${Math.random()*4}s`;
    sparkles.appendChild(s);
  }

  for (let i = 0; i < 15; i++) {
    const p = document.createElement('span');
    p.className = 'bg-petal';
    p.textContent = '🌸';
    p.style.left = Math.random() * 100 + '%';
    p.style.top = Math.random() * 120 + 10 + '%';
    p.style.animationDuration = (8 + Math.random() * 12) + 's';
    p.style.animationDelay = (Math.random() * 10) + 's';
    p.style.fontSize = (14 + Math.random() * 10) + 'px';
    $('#bgCherry').appendChild(p);
  }

  for (let i = 0; i < 25; i++) {
    const s = document.createElement('span');
    s.className = 'bg-star';
    s.textContent = '✦';
    s.style.left = Math.random() * 100 + '%';
    s.style.top = Math.random() * 60 + '%';
    s.style.animationDuration = (2 + Math.random() * 3) + 's';
    s.style.animationDelay = (Math.random() * 3) + 's';
    s.style.fontSize = (10 + Math.random() * 8) + 'px';
    $('#bgNight').appendChild(s);
  }

  for (let i = 0; i < 5; i++) {
    const s = document.createElement('span');
    s.className = 'bg-star';
    s.textContent = '🌟';
    s.style.left = Math.random() * 100 + '%';
    s.style.top = Math.random() * 40 + '%';
    s.style.animationDuration = (3 + Math.random() * 2) + 's';
    s.style.fontSize = (20 + Math.random() * 12) + 'px';
    s.style.opacity = '0.7';
    $('#bgNight').appendChild(s);
  }

  for (let i = 0; i < 5; i++) {
    const c = document.createElement('span');
    c.className = 'bg-cloud';
    c.textContent = '☁️';
    c.style.top = (10 + Math.random() * 40) + '%';
    c.style.animationDuration = (20 + Math.random() * 15) + 's';
    c.style.animationDelay = -(Math.random() * 20) + 's';
    c.style.fontSize = (30 + Math.random() * 20) + 'px';
    c.style.opacity = '0.4';
    $('#bgClouds').appendChild(c);
  }
}

createBgElements();

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    if ($('#modalOverlay').classList.contains('open')) closeModal();
    if ($('#confirmOverlay').classList.contains('open')) hideConfirm();
  }
  if (e.key === 'Enter' && $('#modalOverlay').classList.contains('open')) {
    if (e.target.closest('.modal-card')) {
      e.preventDefault();
      $('#saveBtn').click();
    }
  }
});

render();

})();
