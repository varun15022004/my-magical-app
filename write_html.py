import os

content = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>My Magical Day ✨</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@400..700&family=Press+Start+2P&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{min-height:100vh;overflow-x:hidden;font-family:"Pixelify Sans",system-ui;color:#AC4C95;background:#FFF8F0;position:relative;image-rendering:pixelated}
button,input,select,textarea{font:inherit;color:inherit}
input,select,textarea{background:rgba(255,255,255,.7);border:3px solid #E8B4D0;border-radius:14px;padding:8px 14px;outline:none;transition:border-color .25s,box-shadow .25s}
input:focus,select:focus,textarea:focus{border-color:#AC4C95;box-shadow:0 0 0 4px rgba(172,76,149,.15)}
::selection{background:#F2D4FF;color:#6B2D5E}
.bg-layer{position:fixed;inset:0;overflow:hidden;pointer-events:none;z-index:0;transition:opacity .8s}
.bg-layer.hidden{opacity:0}
#bgCherry{background:linear-gradient(180deg,#FFE4F0 0%,#FFD9F2 30%,#F2D4FF 60%,#D5F1FF 100%)}
#bgNight{background:linear-gradient(180deg,#1A1028 0%,#2D1B4E 30%,#1E1133 60%,#0D0818 100%)}
#bgClouds{background:linear-gradient(180deg,#E8F8FF 0%,#D5F1FF 30%,#E0F7E9 60%,#F2D4FF 100%)}
.bg-petal,.bg-star,.bg-cloud{position:absolute;pointer-events:none;opacity:.5;image-rendering:pixelated}
.bg-petal{color:#FF99C8;font-size:18px;animation:drift linear infinite}
.bg-star{color:#FFE066;font-size:14px;animation:twinkleStar ease-in-out infinite}
.bg-cloud{color:rgba(255,255,255,.6);font-size:40px;animation:driftCloud linear infinite}
@keyframes drift{0%{transform:translateY(0) rotate(0deg);opacity:.5}50%{opacity:.8}100%{transform:translateY(-120vh) rotate(360deg);opacity:0}}
@keyframes driftCloud{0%{transform:translateX(-100px)}100%{transform:translateX(calc(100vw + 100px))}}
@keyframes twinkleStar{0%,100%{opacity:.2;transform:scale(.7)}50%{opacity:1;transform:scale(1.2)}}
.bg-sparkles{position:fixed;inset:0;overflow:hidden;pointer-events:none;z-index:1}
.bg-sparkle{position:absolute;background:#fff;image-rendering:pixelated;box-shadow:0 0 6px rgba(255,255,255,.8);border-radius:50%;animation:twinkle var(--dur) ease-in-out var(--delay) infinite}
@keyframes twinkle{0%,100%{opacity:.1;transform:translateY(0) scale(.5)}50%{opacity:1;transform:translateY(-12px) scale(1)}}
#stage{position:relative;z-index:2;min-height:100vh;padding-bottom:40px}
.hero{text-align:center;padding:36px 18px 16px}
.eyebrow{color:#C96DB1;letter-spacing:2px;font-size:15px;margin-bottom:4px}
.hero h1{font-size:clamp(40px,8vw,80px);line-height:.9;margin:6px 0;color:#A94A98;text-shadow:3px 3px #fff,6px 6px #FFD0EC;animation:bob 2.5s ease-in-out infinite;font-family:"Press Start 2P",monospace;letter-spacing:2px}
@keyframes bob{50%{transform:translateY(-6px)}}
.subtitle{font-size:18px;color:#8D69C6}
.dashboard{position:relative;z-index:2;display:grid;grid-template-columns:minmax(260px,360px) minmax(360px,1fr);gap:28px;align-items:start;width:min(1160px,94vw);margin:0 auto}
.pixel-card{background:rgba(255,255,255,.78);border:3px solid #D77AB8;box-shadow:0 0 0 6px rgba(255,255,255,.5),8px 8px 0 rgba(196,108,177,.2);border-radius:22px;backdrop-filter:blur(8px)}
#bgNight .pixel-card{background:rgba(26,16,40,.85);border-color:#7B4C9E;box-shadow:0 0 0 6px rgba(123,76,158,.3),8px 8px 0 rgba(123,76,158,.2);color:#E0C4F0}
#bgNight .pixel-card input,#bgNight .pixel-card select{background:rgba(45,27,78,.8);border-color:#7B4C9E;color:#E0C4F0}
.control-panel{padding:22px;display:grid;gap:14px;position:sticky;top:18px}
.profile{display:grid;grid-template-columns:72px 1fr;gap:14px;align-items:center}
.avatar{height:72px;width:72px;border-radius:18px;background:#FFF0FA;border:3px solid #E28CC3;display:grid;place-items:center;font-size:40px;animation:wobble 3s infinite;cursor:pointer;transition:transform .2s}
.avatar:hover{transform:scale(1.1)}
@keyframes wobble{50%{transform:rotate(4deg) scale(1.04)}}
label{display:block;color:#A94A98;margin-bottom:5px;font-size:16px;font-weight:600}
#bgNight label{color:#D4A0E8}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;text-align:center}
.stats div{background:rgba(255,255,255,.5);border-radius:14px;padding:10px 4px;border:2px solid #E8B4D0}
#bgNight .stats div{background:rgba(45,27,78,.6);border-color:#7B4C9E}
.stats strong{display:block;font-size:28px;color:#AC4C95}
#bgNight .stats strong{color:#E8B4F0}
.stats span{font-size:12px;color:#A94A98}
#bgNight .stats span{color:#C896D8}
.progress-wrap{margin:4px 0}
.progress{height:18px;background:rgba(255,255,255,.6);border-radius:12px;border:2px solid #E8B4D0;overflow:hidden;position:relative}
#bgNight .progress{background:rgba(45,27,78,.6);border-color:#7B4C9E}
.progress i{display:block;height:100%;background:linear-gradient(90deg,#FFB0D4,#E882C0);border-radius:10px;transition:width .5s ease;position:relative}
.progress i::after{content:'';position:absolute;inset:2px 4px;background:linear-gradient(90deg,rgba(255,255,255,.4),transparent);border-radius:8px}
.actions{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px}
.cute-btn{border:3px solid #E28CC3;border-radius:16px;padding:10px 8px;background:#FFF0FA;color:#AC4C95;font-weight:700;font-size:14px;cursor:pointer;transition:all .2s;text-align:center}
.cute-btn:hover{transform:scale(1.05);box-shadow:0 4px 12px rgba(172,76,149,.25)}
.cute-btn:active{transform:scale(.95)}
.cute-btn.purple{background:#F2E6FF;border-color:#B28AD0;color:#7B4C9E}
.cute-btn.purple:hover{box-shadow:0 4px 12px rgba(123,76,158,.25)}
.cute-btn.soft{background:#FFF5E6;border-color:#E8C8A0;color:#B08050}
#bgNight .cute-btn{background:rgba(45,27,78,.8);border-color:#7B4C9E;color:#E0C4F0}
#bgNight .cute-btn.purple{background:rgba(90,50,140,.6);border-color:#A070D0}
#bgNight .cute-btn.soft{background:rgba(80,50,30,.5);border-color:#A08060;color:#D0B090}
.theme-btns{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}
.theme-btn{padding:8px 4px;border:3px solid #E8B4D0;border-radius:14px;background:rgba(255,255,255,.6);cursor:pointer;font-size:22px;transition:all .2s;text-align:center}
.theme-btn.active{border-color:#AC4C95;background:#FFF0FA;box-shadow:0 0 0 4px rgba(172,76,149,.15);transform:scale(1.05)}
.theme-btn:hover{transform:scale(1.08)}
.theme-btn span{display:block;font-size:10px;color:#A94A98;margin-top:2px;font-family:"Press Start 2P",monospace}
#bgNight .theme-btn{background:rgba(45,27,78,.6);border-color:#7B4C9E}
#bgNight .theme-btn.active{border-color:#D4A0E8;background:rgba(90,50,140,.5);box-shadow:0 0 0 4px rgba(212,160,232,.2)}
#bgNight .theme-btn span{color:#C896D8}
#bgNight .theme-btn.active span{color:#E8B4F0}
.mood-btns{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}
.mood-btn{padding:8px 4px;border:3px solid #E8B4D0;border-radius:14px;background:rgba(255,255,255,.6);cursor:pointer;font-size:24px;transition:all .2s;text-align:center}
.mood-btn.active{border-color:#AC4C95;background:#FFF0FA;box-shadow:0 0 0 4px rgba(172,76,149,.15);transform:scale(1.05)}
.mood-btn:hover{transform:scale(1.08)}
.mood-btn span{display:block;font-size:10px;color:#A94A98;margin-top:2px;font-family:"Press Start 2P",monospace}
#bgNight .mood-btn{background:rgba(45,27,78,.6);border-color:#7B4C9E}
#bgNight .mood-btn.active{border-color:#D4A0E8;background:rgba(90,50,140,.5);box-shadow:0 0 0 4px rgba(212,160,232,.2)}
#bgNight .mood-btn span{color:#C896D8}
.sound-toggle{display:flex;align-items:center;gap:10px;font-size:14px;cursor:pointer;user-select:none;padding:6px 0}
.sound-toggle input{width:auto;accent-color:#AC4C95}
.printer-scene{display:flex;flex-direction:column;align-items:center;gap:12px}
.printer-wrap{position:relative;width:100%;max-width:460px;margin:0 auto}
.printer-body{cursor:pointer;transition:transform .15s;position:relative;z-index:5}
.printer-body:hover{transform:scale(1.03)}
.printer-svg{width:100%;height:auto;display:block;filter:drop-shadow(0 8px 20px rgba(172,76,149,.2))}
.printer-breathe{animation:breathe 3s ease-in-out infinite}
@keyframes breathe{0%,100%{transform:scale(1)}50%{transform:scale(1.015)}}
.printer-shake{animation:printerShake .5s ease-in-out}
@keyframes printerShake{0%,100%{transform:translateX(0)}10%{transform:translateX(-6px) rotate(-1deg)}20%{transform:translateX(5px) rotate(1deg)}30%{transform:translateX(-4px) rotate(-.5deg)}40%{transform:translateX(3px) rotate(.5deg)}50%{transform:translateX(-2px)}60%{transform:translateX(2px)}70%{transform:translateX(-1px)}80%{transform:translateX(1px)}}
.printer-label{text-align:center;font-size:13px;color:#C96DB1;margin-top:6px;font-family:"Press Start 2P",monospace;letter-spacing:2px;animation:pulseLabel 2s ease-in-out infinite}
@keyframes pulseLabel{0%,100%{opacity:.6}50%{opacity:1}}
.print-btn-container{position:relative;margin-top:-10px}
.print-btn{border:none;border-radius:50%;width:70px;height:70px;background:linear-gradient(135deg,#FFB0D4,#E882C0);color:#fff;font-size:28px;cursor:pointer;box-shadow:0 6px 20px rgba(172,76,149,.35),inset 0 -4px 0 rgba(0,0,0,.1);transition:all .2s;position:relative;display:grid;place-items:center;border:3px solid #fff}
.print-btn:hover{transform:scale(1.08);box-shadow:0 8px 28px rgba(172,76,149,.45),inset 0 -4px 0 rgba(0,0,0,.1)}
.print-btn:active{transform:scale(.92);box-shadow:0 2px 8px rgba(172,76,149,.2),inset 0 2px 0 rgba(0,0,0,.1)}
.print-btn.is-printing{animation:btnPulse .6s ease-in-out infinite;pointer-events:none}
@keyframes btnPulse{0%,100%{transform:scale(1);box-shadow:0 6px 20px rgba(172,76,149,.35)}50%{transform:scale(1.1);box-shadow:0 8px 30px rgba(172,76,149,.5)}}
.print-particle{position:fixed;pointer-events:none;z-index:100;font-size:20px;animation:particleFly .8s ease-out forwards}
@keyframes particleFly{0%{opacity:1;transform:translate(0,0) scale(1) rotate(0deg)}100%{opacity:0;transform:translate(var(--dx),var(--dy)) scale(0) rotate(720deg)}}
.receipt{background:#FFF9F0;border:3px solid #E8B4D0;border-radius:18px;padding:28px 24px 0;max-width:420px;width:100%;margin:0 auto;position:relative;z-index:3;transition:all .6s cubic-bezier(.34,1.56,.64,1);transform-origin:top center;font-family:"Pixelify Sans",system-ui;color:#6B2D5E;box-shadow:0 10px 40px rgba(172,76,149,.15)}
.receipt.closed{transform:scaleY(0);opacity:0;max-height:0;padding:0;margin:0;overflow:hidden;border-width:0}
.receipt.open{transform:scaleY(1);opacity:1}
.receipt::after{content:'';display:block;height:28px;background:#FFF9F0;clip-path:polygon(0 0,8% 100%,16% 0,24% 100%,32% 0,40% 100%,48% 0,56% 100%,64% 0,72% 100%,80% 0,88% 100%,96% 0,100% 100%,0 100%);margin:0 -24px;position:relative;width:calc(100% + 48px)}
#bgNight .receipt{background:#1E1133;border-color:#7B4C9E;color:#E0C4F0;box-shadow:0 10px 40px rgba(0,0,0,.4)}
#bgNight .receipt::after{background:#1E1133}
.washi-tape{position:absolute;top:12px;left:-8px;right:-8px;height:20px;background:repeating-linear-gradient(45deg,#FFB0D4 0,#FFB0D4 6px,#FFD9F2 6px,#FFD9F2 12px);opacity:.7;transform:rotate(-1deg);border-radius:2px;z-index:10;box-shadow:0 2px 6px rgba(172,76,149,.15)}
#bgNight .washi-tape{background:repeating-linear-gradient(45deg,#7B4C9E 0,#7B4C9E 6px,#B28AD0 6px,#B28AD0 12px)}
.receipt-header{text-align:center;margin-bottom:14px;padding-top:16px}
.receipt-date{font-family:"Press Start 2P",monospace;font-size:10px;color:#A94A98;display:block;margin-bottom:6px}
#bgNight .receipt-date{color:#C896D8}
.receipt-mood{font-size:36px;display:block;margin-bottom:4px}
.receipt-title{font-size:26px;color:#AC4C95;margin:4px 0 2px;font-weight:700;letter-spacing:1px}
#bgNight .receipt-title{color:#E8B4F0}
.receipt-subtitle{font-size:12px;color:#C96DB1;font-family:"Press Start 2P",monospace}
.receipt-section{margin:12px 0}
.receipt-section h3{font-size:18px;color:#A94A98;margin-bottom:8px;letter-spacing:1px;display:flex;align-items:center;gap:8px}
#bgNight .receipt-section h3{color:#D4A0E8}
.receipt-list{list-style:none;padding:0;display:grid;gap:6px}
.receipt-list li{background:rgba(255,255,255,.5);border-radius:12px;padding:8px 12px;border:2px solid #F2D4FF;display:grid;grid-template-columns:auto 1fr auto;gap:8px;align-items:center;transition:all .2s;cursor:pointer}
.receipt-list li:hover{transform:translateX(3px);border-color:#E28CC3}
#bgNight .receipt-list li{background:rgba(45,27,78,.5);border-color:#5B3A7E}
#bgNight .receipt-list li:hover{border-color:#B28AD0}
.receipt-list li.done{opacity:.7;background:rgba(200,245,232,.4)}
.receipt-list li.done .task-label{text-decoration:line-through;text-decoration-color:#AC4C95}
#bgNight .receipt-list li.done{background:rgba(45,27,78,.3)}
.receipt-list li.empty{opacity:.5;cursor:default;pointer-events:none;justify-content:center;display:flex;font-style:italic}
.category-dot{display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;border-radius:6px;font-size:12px;flex-shrink:0}
.category-dot.personal{background:#FFD9F2;color:#D46A9E}
.category-dot.work{background:#D5F1FF;color:#4A90B0}
.category-dot.study{background:#F2D4FF;color:#8A5AC0}
.category-dot.hobby{background:#C8F5E8;color:#3E9E7E}
.task-label{flex:1;font-size:15px;font-weight:500}
.task-time{font-size:12px;color:#C96DB1;font-family:"Press Start 2P",monospace}
#bgNight .task-time{color:#A878C8}
.priority-stars{display:flex;gap:2px;font-size:12px}
.receipt-progress{margin:12px 0;padding:10px 14px;background:rgba(255,255,255,.4);border-radius:12px;border:2px solid #F2D4FF}
#bgNight .receipt-progress{background:rgba(45,27,78,.4);border-color:#5B3A7E}
.receipt-progress-header{display:flex;justify-content:space-between;font-size:13px;margin-bottom:6px;color:#A94A98}
#bgNight .receipt-progress-header{color:#C896D8}
.receipt-progress-bar{height:16px;background:rgba(255,255,255,.5);border-radius:10px;border:2px solid #E8B4D0;overflow:hidden;position:relative}
#bgNight .receipt-progress-bar{background:rgba(45,27,78,.5);border-color:#7B4C9E}
.receipt-progress-fill{height:100%;background:linear-gradient(90deg,#FFB0D4,#E882C0);border-radius:8px;transition:width .8s cubic-bezier(.34,1.56,.64,1);position:relative}
.receipt-progress-fill::after{content:'';position:absolute;inset:2px 4px;background:linear-gradient(90deg,rgba(255,255,255,.4),transparent);border-radius:6px}
.affirmation-box{margin:12px 0;padding:12px 14px;border:2px dashed #E28CC3;border-radius:14px;text-align:center;background:rgba(255,255,255,.3);font-size:15px;color:#A94A98;line-height:1.5}
#bgNight .affirmation-box{border-color:#7B4C9E;background:rgba(45,27,78,.3);color:#D4A0E8}
.modal-overlay{position:fixed;inset:0;z-index:200;background:rgba(0,0,0,.4);backdrop-filter:blur(4px);display:none;place-items:center;animation:fadeIn .2s}
.modal-overlay.open{display:grid}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
.modal-card{background:#FFF8F0;border:3px solid #D77AB8;border-radius:22px;padding:28px 24px 20px;width:min(400px,90vw);position:relative;box-shadow:0 0 0 6px rgba(255,255,255,.5),12px 12px 0 rgba(196,108,177,.2);max-height:90vh;overflow-y:auto;animation:modalPop .3s cubic-bezier(.34,1.56,.64,1)}
@keyframes modalPop{from{transform:scale(.7);opacity:0}to{transform:scale(1);opacity:1}}
#bgNight .modal-card{background:#1E1133;border-color:#7B4C9E;box-shadow:0 0 0 6px rgba(123,76,158,.3),12px 12px 0 rgba(123,76,158,.2)}
.modal-close{position:absolute;top:10px;right:14px;background:none;border:none;font-size:28px;color:#C96DB1;cursor:pointer;padding:4px;line-height:1;transition:transform .2s}
.modal-close:hover{transform:rotate(90deg);color:#AC4C95}
.modal-bow{text-align:center;font-size:28px;color:#E882C0;margin-bottom:2px;transform:rotate(-5deg)}.modal-card h2{text-align:center;color:#AC4C95;margin-bottom:16px;font-size:22px}
#bgNight .modal-card h2{color:#E8B4F0}
.modal-card label{font-size:13px;margin-top:8px}
.modal-card input,.modal-card select,.modal-card textarea{margin-bottom:4px}
.modal-card textarea{resize:vertical;min-height:60px;width:100%}
.modal-card .event-fields,.modal-card .priority-field{display:grid;gap:4px}
.modal-card menu{display:flex;gap:10px;justify-content:center;margin-top:16px;padding:0;list-style:none}
.modal-card menu .cute-btn{min-width:100px}
.confirm-overlay{position:fixed;inset:0;z-index:300;background:rgba(0,0,0,.4);backdrop-filter:blur(4px);display:none;place-items:center}
.confirm-overlay.open{display:grid}
.confirm-card{background:#FFF8F0;border:3px solid #D77AB8;border-radius:22px;padding:32px 28px 24px;text-align:center;width:min(340px,88vw);box-shadow:0 0 0 6px rgba(255,255,255,.5),12px 12px 0 rgba(196,108,177,.2);animation:modalPop .3s cubic-bezier(.34,1.56,.64,1)}
#bgNight .confirm-card{background:#1E1133;border-color:#7B4C9E;box-shadow:0 0 0 6px rgba(123,76,158,.3),12px 12px 0 rgba(123,76,158,.2)}
.confirm-trash{font-size:48px;animation:trashShake .5s ease-in-out infinite;display:block;margin-bottom:8px}
@keyframes trashShake{0%,100%{transform:rotate(0deg)}25%{transform:rotate(-10deg)}75%{transform:rotate(10deg)}}
.confirm-card p{font-size:16px;color:#A94A98;margin-bottom:18px}
#bgNight .confirm-card p{color:#D4A0E8}
.confirm-actions{display:flex;gap:12px;justify-content:center}
.heart-burst{position:fixed;pointer-events:none;z-index:150}
.heart-particle{position:absolute;font-size:var(--size);animation:heartExplode var(--dur) ease-out forwards;color:var(--hcolor)}
@keyframes heartExplode{0%{opacity:1;transform:translate(0,0) scale(1) rotate(0deg)}100%{opacity:0;transform:translate(var(--fx),var(--fy)) scale(0) rotate(720deg)}}
.click-sparkle{position:fixed;pointer-events:none;z-index:100;font-size:18px;animation:sparkleFade .7s ease-out forwards}
@keyframes sparkleFade{0%{opacity:1;transform:translate(0,0) scale(1)}100%{opacity:0;transform:translate(var(--sx),var(--sy)) scale(0)}}
@media(max-width:720px){
.dashboard{grid-template-columns:1fr;gap:20px;width:96vw}
.control-panel{position:static}
.printer-scene{order:-1}
.hero h1{font-size:clamp(32px,10vw,52px)}
.receipt{padding:20px 14px 0;max-width:100%}
.receipt::after{width:calc(100% + 28px);margin:0 -14px}
.mood-btns,.theme-btns{grid-template-columns:repeat(3,1fr)}
.mood-btn,.theme-btn{font-size:20px}
.actions{grid-template-columns:1fr 1fr 1fr}
.theme-btn span,.mood-btn span{font-size:8px}
.modal-card{padding:22px 18px}
}
@media(max-width:400px){
.receipt{padding:16px 10px 0}
.mood-btn,.theme-btn{padding:6px 2px;font-size:16px}
.stats div{padding:6px 2px}
.stats strong{font-size:22px}
}
</style>
</head>
<body>

<div class="bg-layer" id="bgCherry"></div>
<div class="bg-layer hidden" id="bgNight"></div>
<div class="bg-layer hidden" id="bgClouds"></div>
<div class="bg-sparkles" id="bgSparkles"></div>

<div id="stage">
  <header class="hero">
    <p class="eyebrow">✦ kawaii pixel planner ✦</p>
    <h1>My Magical Day</h1>
    <p class="subtitle">a tiny enchanted stationery shop for your plans</p>
  </header>

  <div class="dashboard">
    <aside class="control-panel pixel-card">
      <div class="profile">
        <div class="avatar" id="avatar">🐰</div>
        <div>
          <label for="nameInput">planner name</label>
          <input id="nameInput" type="text" maxlength="18" placeholder="Your name...">
        </div>
      </div>

      <label>🌿 background scene</label>
      <div class="theme-btns" id="themeBtns">
        <button class="theme-btn active" data-theme="cherry">🌸<span>cherry</span></button>
        <button class="theme-btn" data-theme="night">🌙<span>night</span></button>
        <button class="theme-btn" data-theme="clouds">☁️<span>clouds</span></button>
      </div>

      <label>🌈 today's mood</label>
      <div class="mood-btns" id="moodBtns">
        <button class="mood-btn active" data-mood="happy">😊<span>happy</span></button>
        <button class="mood-btn" data-mood="tired">😴<span>tired</span></button>
        <button class="mood-btn" data-mood="stressed">😰<span>stressed</span></button>
        <button class="mood-btn" data-mood="excited">🤩<span>excited</span></button>
        <button class="mood-btn" data-mood="cozy">☕<span>cozy</span></button>
        <button class="mood-btn" data-mood="productive">💪<span>productive</span></button>
      </div>

      <label class="sound-toggle">
        <input type="checkbox" id="soundToggle" checked>
        🔊 sound effects (on)
      </label>

      <div class="stats">
        <div><strong id="eventCount">0</strong><span>events</span></div>
        <div><strong id="todoCount">0</strong><span>tasks</span></div>
        <div><strong id="doneCount">0</strong><span>done</span></div>
      </div>

      <div class="progress-wrap">
        <span style="font-size:14px;color:#A94A98">quest progress</span>
        <div class="progress"><i id="progressBar" style="width:0%"></i></div>
      </div>

      <div class="actions">
        <button class="cute-btn" id="addEventBtn">+ event</button>
        <button class="cute-btn purple" id="addTodoBtn">+ task</button>
        <button class="cute-btn soft" id="resetBtn">new day</button>
      </div>
    </aside>

    <section class="printer-scene">
      <div class="printer-wrap">
        <div class="printer-body printer-breathe" id="printerBody">
          <svg class="printer-svg" viewBox="0 0 400 280" fill="none">
            <rect x="60" y="80" width="280" height="160" rx="24" fill="#FFD9F2" stroke="#E28CC3" stroke-width="4"/>
            <rect x="50" y="70" width="300" height="30" rx="15" fill="#FFF0FA" stroke="#E28CC3" stroke-width="3"/>
            <rect x="70" y="78" width="260" height="14" rx="7" fill="#FFB0D4"/>
            <rect x="85" y="100" width="230" height="100" rx="12" fill="#FFF8F0" stroke="#E8B4D0" stroke-width="3"/>
            <line x1="100" y1="120" x2="300" y2="120" stroke="#F2D4FF" stroke-width="2" stroke-dasharray="4 4"/>
            <line x1="100" y1="140" x2="300" y2="140" stroke="#F2D4FF" stroke-width="2" stroke-dasharray="4 4"/>
            <line x1="100" y1="160" x2="300" y2="160" stroke="#F2D4FF" stroke-width="2" stroke-dasharray="4 4"/>
            <line x1="100" y1="180" x2="300" y2="180" stroke="#F2D4FF" stroke-width="2" stroke-dasharray="4 4"/>
            <rect x="110" y="115" width="6" height="6" rx="1" fill="#FFB0D4"/>
            <rect x="284" y="115" width="6" height="6" rx="1" fill="#FFB0D4"/>
            <rect x="60" y="200" width="280" height="40" rx="12" fill="#FFF0FA" stroke="#E28CC3" stroke-width="3"/>
            <rect x="170" y="210" width="60" height="20" rx="10" fill="#FFB0D4"/>
            <rect x="120" y="214" width="36" height="12" rx="6" fill="#E882C0"/>
            <rect x="244" y="214" width="36" height="12" rx="6" fill="#E882C0"/>
            <rect x="155" y="248" width="90" height="8" rx="4" fill="#E8B4D0"/>
            <circle cx="335" cy="165" r="18" fill="#FFB0D4" stroke="#E28CC3" stroke-width="3"/>
            <rect x="325" y="163" width="20" height="4" rx="2" fill="#fff"/>
            <rect x="333" y="155" width="4" height="20" rx="2" fill="#fff"/>
          </svg>
        </div>
        <div class="printer-label">₊✩‧₊˚ print magic ₊✩‧₊˚</div>
      </div>

      <div class="print-btn-container">
        <button class="print-btn" id="printBtn" aria-label="Print receipt">🖨️</button>
      </div>

      <article class="receipt closed" id="receipt">
        <div class="washi-tape"></div>
        <div class="receipt-header">
          <span class="receipt-date" id="receiptDate"></span>
          <span class="receipt-mood" id="receiptMood"></span>
          <div class="receipt-title" id="receiptTitle">My Magical Day</div>
          <div class="receipt-subtitle" id="receiptSubtitle">✦ today's plan ✦</div>
        </div>

        <section class="receipt-section">
          <h3>📅 Events</h3>
          <ul class="receipt-list" id="eventsList"></ul>
        </section>

        <section class="receipt-section">
          <h3>✅ To-do Quests</h3>
          <ul class="receipt-list" id="todosList"></ul>
        </section>

        <div class="receipt-progress">
          <div class="receipt-progress-header">
            <span id="progressLabel">quest progress</span>
            <span id="progressCount">0/0 done 🌟</span>
          </div>
          <div class="receipt-progress-bar">
            <div class="receipt-progress-fill" id="receiptProgressFill" style="width:0%"></div>
          </div>
        </div>

        <div class="affirmation-box" id="affirmationBox">You are doing amazing sweetie ✧</div>
      </article>
    </section>
  </div>
</div>

<div class="modal-overlay" id="modalOverlay">
  <div class="modal-card">
    <button class="modal-close" id="modalClose">✕</button>
    <div class="modal-bow">🎀</div>
    <h2 id="modalTitle">Add magic</h2>
    <input type="hidden" id="itemType">
    <input type="hidden" id="itemId">
    <label for="itemLabel">tiny note</label>
    <input id="itemLabel" type="text" maxlength="60" placeholder="water the moonflowers...">
    <div class="event-fields" id="eventFields">
      <label for="itemTime">time spell</label>
      <input id="itemTime" type="text" maxlength="24" placeholder="10:00 - 11:00">
      <label for="itemLink">magic link (optional)</label>
      <input id="itemLink" type="url" maxlength="200" placeholder="https://...">
    </div>
    <label for="itemCategory">sticker label</label>
    <select id="itemCategory">
      <option value="personal">🌸 personal</option>
      <option value="work">💼 work</option>
      <option value="study">📖 study</option>
      <option value="hobby">🎨 hobby</option>
    </select>
    <div class="priority-field" id="priorityField">
      <label>priority level</label>
      <select id="itemPriority">
        <option value="low">⭐ low</option>
        <option value="medium" selected>⭐⭐ medium</option>
        <option value="high">⭐⭐⭐ high</option>
      </select>
    </div>
    <menu>
      <button class="cute-btn soft" id="deleteBtn">delete</button>
      <button class="cute-btn" id="saveBtn">save magic</button>
    </menu>
  </div>
</div>

<div class="confirm-overlay" id="confirmOverlay">
  <div class="confirm-card">
    <span class="confirm-trash">🗑️</span>
    <p>Start a new day?<br>All your tasks will vanish~</p>
    <div class="confirm-actions">
      <button class="cute-btn soft" id="confirmNo">cancel</button>
      <button class="cute-btn" id="confirmYes">new day!</button>
    </div>
  </div>
</div>

<script>
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
  events: [
    { id: crypto.randomUUID(), label: 'Open the stationery shop', time: '09:00', category: 'personal', link: '' },
    { id: crypto.randomUUID(), label: 'Team spell meeting', time: '11:30', category: 'work', link: '' },
    { id: crypto.randomUUID(), label: 'Moon milk break', time: '15:00', category: 'personal', link: '' }
  ],
  todos: [
    { id: crypto.randomUUID(), label: 'Write 3 tiny priorities', category: 'personal', priority: 'medium', done: false },
    { id: crypto.randomUUID(), label: 'Finish brave work quest', category: 'work', priority: 'high', done: false },
    { id: crypto.randomUUID(), label: 'Tidy desk altar', category: 'personal', priority: 'low', done: true }
  ]
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

  openModal('todo', item);
});

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
</script>
</body>
</html>
'''

filepath = r'D:\hehe\my-magical-day\index.html'
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('File written successfully, size:', os.path.getsize(filepath), 'bytes')
