const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const stage = $('#stage');
const receipt = $('#receipt');
const storeKey = 'my-magical-day:v1';
const today = new Date();

const defaults = {
  name: 'Bunny', mood: 'sparkly', theme: 'strawberry',
  events: [
    { id: crypto.randomUUID(), label: 'Open the stationery shop', time: '09:00', category: 'personal' },
    { id: crypto.randomUUID(), label: 'Team spell meeting', time: '11:30', category: 'work' },
    { id: crypto.randomUUID(), label: 'Moon milk break', time: '15:00', category: 'personal' }
  ],
  todos: [
    { id: crypto.randomUUID(), label: 'Write 3 tiny priorities', category: 'personal', done: false },
    { id: crypto.randomUUID(), label: 'Finish brave work quest', category: 'work', done: false },
    { id: crypto.randomUUID(), label: 'Tidy desk altar', category: 'personal', done: true }
  ]
};

let state = load();
function load() { try { return { ...defaults, ...JSON.parse(localStorage.getItem(storeKey)) }; } catch { return structuredClone(defaults); } }
function save() { localStorage.setItem(storeKey, JSON.stringify(state)); }

const moodCopy = {
  sparkly: { avatar: '🐰', text: 'You are sparkling like pixel sugar today.' },
  cozy: { avatar: '☕', text: 'Soft steps still count. Stay warm and gentle.' },
  brave: { avatar: '🌈', text: 'Tiny hero mode is activated. You can do hard quests.' },
  sleepy: { avatar: '🌙', text: 'A slow magical day is still magical.' }
};

function esc(str) { const d = document.createElement('div'); d.textContent = str; return d.innerHTML; }
function render() {
  $('#nameInput').value = state.name;
  $('#moodSelect').value = state.mood;
  $('#themeSelect').value = state.theme;
  $('#avatar').textContent = moodCopy[state.mood].avatar;
  receipt.className = `receipt theme-${state.theme}`;
  $('#receiptDate').textContent = today.toLocaleDateString(undefined, { weekday: 'short', month: 'short', day: 'numeric' });
  $('#receiptTitle').textContent = `${state.name || 'My'}'s Magical Day`;
  $('#affirmation').textContent = moodCopy[state.mood].text;

  $('#eventsList').innerHTML = state.events.length ? state.events.map(i => `<li data-type="event" data-id="${i.id}"><span class="sticker ${i.category}">${i.category}</span><span class="label">${esc(i.label)}</span><span class="time">${esc(i.time || 'anytime')}</span></li>`).join('') : '<li class="empty">No events yet. Add a tiny adventure ✨</li>';
  $('#todosList').innerHTML = state.todos.length ? state.todos.map(i => `<li class="todo ${i.done ? 'done' : ''}" data-type="todo" data-id="${i.id}"><span class="sticker ${i.category}">${i.category}</span><span class="label">${esc(i.label)}</span><span class="time">${i.done ? 'done' : 'tap'}</span></li>`).join('') : '<li class="empty">No quests yet. Add a cute task ♡</li>';

  const done = state.todos.filter(t => t.done).length;
  $('#eventCount').textContent = state.events.length;
  $('#todoCount').textContent = state.todos.length;
  $('#doneCount').textContent = done;
  $('#progressBar').style.width = `${state.todos.length ? Math.round(done / state.todos.length * 100) : 0}%`;
  $('#receiptFooter').textContent = done === state.todos.length && state.todos.length ? 'Perfect quest clear! stamp stamp ♡' : 'tap tasks to sparkle-complete them';
  save();
}

function openModal(type, item = null) {
  $('#itemType').value = type;
  $('#itemId').value = item?.id || '';
  $('#modalTitle').textContent = item ? `Edit ${type} charm` : `Add ${type} charm`;
  $('#itemLabel').value = item?.label || '';
  $('#itemTime').value = item?.time || '';
  $('#itemCategory').value = item?.category || 'personal';
  $('#eventFields').style.display = type === 'event' ? 'block' : 'none';
  $('#deleteBtn').style.visibility = item ? 'visible' : 'hidden';
  $('#itemModal').showModal();
  setTimeout(() => $('#itemLabel').focus(), 50);
}

$$('[data-open-modal]').forEach(b => b.addEventListener('click', () => openModal(b.dataset.openModal)));
$('#itemForm').addEventListener('submit', (e) => {
  e.preventDefault();
  const type = $('#itemType').value, id = $('#itemId').value;
  const list = type === 'event' ? state.events : state.todos;
  const data = { id: id || crypto.randomUUID(), label: $('#itemLabel').value.trim(), category: $('#itemCategory').value };
  if (type === 'event') data.time = $('#itemTime').value.trim(); else data.done = list.find(x => x.id === id)?.done || false;
  if (!data.label) return;
  const idx = list.findIndex(x => x.id === id);
  idx >= 0 ? list.splice(idx, 1, data) : list.push(data);
  $('#itemModal').close(); render(); sparkle(innerWidth / 2, innerHeight / 2, 14);
});
$('#deleteBtn').addEventListener('click', () => {
  const type = $('#itemType').value, id = $('#itemId').value;
  const list = type === 'event' ? state.events : state.todos;
  const idx = list.findIndex(x => x.id === id); if (idx >= 0) list.splice(idx, 1);
  $('#itemModal').close(); render();
});

receipt.addEventListener('click', (e) => {
  const li = e.target.closest('li[data-id]'); if (!li) return;
  const list = li.dataset.type === 'event' ? state.events : state.todos;
  const item = list.find(x => x.id === li.dataset.id); if (!item) return;
  if (li.dataset.type === 'todo' && !e.detail) return;
  if (li.dataset.type === 'todo' && e.target.closest('.time')) return openModal('todo', item);
  if (li.dataset.type === 'todo') { item.done = !item.done; save(); render(); if (item.done) sparkle(e.clientX, e.clientY, 16); }
  else openModal('event', item);
});
receipt.addEventListener('dblclick', (e) => { const li = e.target.closest('li[data-id]'); if (li?.dataset.type === 'todo') openModal('todo', state.todos.find(t => t.id === li.dataset.id)); });

['nameInput','moodSelect','themeSelect'].forEach(id => $(`#${id}`).addEventListener('input', e => { const key = id.replace('Input','').replace('Select',''); state[key] = e.target.value; render(); }));
$('#resetBtn').addEventListener('click', () => { state = structuredClone(defaults); render(); });
$('#printBtn').addEventListener('click', () => { stage.classList.remove('is-printing','is-done'); void stage.offsetWidth; stage.classList.add('is-printing'); $('#printerText').textContent = '₊ ⊹ printing your magic ⊹ ₊'; setTimeout(() => stage.classList.add('is-done'), 1200); sparkle(innerWidth/2, 220, 24); });

function sparkle(x, y, n = 8) { for (let i = 0; i < n; i++) { const s = document.createElement('span'); s.className = 'sparkle'; s.textContent = ['✦','✧','⋆','♡','✩'][Math.floor(Math.random()*5)]; s.style.left = x + 'px'; s.style.top = y + 'px'; s.style.color = ['#ec6e9e','#9e6eda','#ffd978','#6edac0'][Math.floor(Math.random()*4)]; const a = Math.random()*Math.PI*2, d = 25+Math.random()*55; s.style.setProperty('--dx', Math.cos(a)*d+'px'); s.style.setProperty('--dy', Math.sin(a)*d+'px'); document.body.appendChild(s); s.addEventListener('animationend', () => s.remove()); } }

for (let i=0;i<90;i++){const s=document.createElement('span');s.className='bg-sparkle';const z=2+Math.random()*4;s.style.cssText=`width:${z}px;height:${z}px;left:${Math.random()*100}%;top:${Math.random()*100}%;--dur:${2+Math.random()*4}s;--delay:${Math.random()*4}s`;$('.bg-sparkles').appendChild(s)}
['big1.png','big2.png','big3.png','big4.png','big5.png','Layer 5.png','Layer 6.png','Layer 12.png','Layer 18.png'].forEach((src,i)=>{const img=new Image();img.src=`assets/background-decors/${src}`;img.className='bg-decor';img.style.width=30+Math.random()*42+'px';$('.bg-decors').appendChild(img);let x=Math.random()*innerWidth,y=Math.random()*innerHeight,vx=(Math.random()-.5)*.35,vy=(Math.random()-.5)*.35;function tick(){x=(x+vx+innerWidth)%innerWidth;y=(y+vy+innerHeight)%innerHeight;img.style.transform=`translate(${x}px,${y}px)`;requestAnimationFrame(tick)}tick();img.onclick=e=>sparkle(e.clientX,e.clientY,10)});
render();
