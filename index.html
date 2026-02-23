<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BlissFullReloaded — Minecraft сервер</title>
<link href="https://db.onlinewebfonts.com/c/bf3f245b7cd53caea0cb07d265a64adc?family=Minecraftia+Regular" rel="stylesheet">
<style>
  @font-face {
    font-family: 'Minecraft';
    src: url('https://db.onlinewebfonts.com/t/bf3f245b7cd53caea0cb07d265a64adc.woff2') format('woff2'),
         url('https://db.onlinewebfonts.com/t/bf3f245b7cd53caea0cb07d265a64adc.woff') format('woff'),
         url('https://db.onlinewebfonts.com/t/bf3f245b7cd53caea0cb07d265a64adc.ttf') format('truetype');
    font-weight: normal;
  }
  :root {
    --bg: #080c10; --bg2: #0d1117; --bg3: #111820; --card: #0f1620;
    --border: #1e2d3d; --border2: #243447; --accent: #00d4ff; --accent2: #7b2fff;
    --accent3: #ff6b35; --gold: #f0c040; --text: #c8d8e8; --text2: #7a9ab8;
    --text3: #4a6a8a; --green: #00ff88; --red: #ff4455;
    --glow: 0 0 20px rgba(0,212,255,0.3);
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body { background: var(--bg); color: var(--text); font-family: 'Minecraft', 'Minecraftia Regular', monospace; font-weight: 400; overflow-x: hidden; cursor: default; font-size: 13px; line-height: 1.6; }
  body::before { content: ''; position: fixed; inset: 0; background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E"); pointer-events: none; z-index: 0; opacity: 0.6; }
  body::after { content: ''; position: fixed; inset: 0; background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.03) 2px, rgba(0,0,0,0.03) 4px); pointer-events: none; z-index: 1; }
  nav { position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: rgba(8,12,16,0.92); backdrop-filter: blur(20px); border-bottom: 1px solid var(--border); padding: 0 40px; height: 60px; display: flex; align-items: center; justify-content: space-between; }
  .nav-logo { font-family: 'Minecraft', monospace; font-weight: normal; font-size: 16px; color: var(--accent); text-shadow: var(--glow); letter-spacing: 2px; cursor: pointer; }
  .nav-logo span { color: var(--accent2); }
  .nav-links { display: flex; gap: 8px; align-items: center; }
  .nav-links a { color: var(--text2); text-decoration: none; font-size: 13px; font-weight: 600; letter-spacing: 1.5px; text-transform: uppercase; padding: 6px 14px; border-radius: 4px; transition: all 0.2s; cursor: pointer; }
  .nav-links a:hover, .nav-links a.active { color: var(--accent); background: rgba(0,212,255,0.08); }
  .nav-ip { font-family: 'Minecraft', monospace; font-size: 12px; color: var(--green); background: rgba(0,255,136,0.06); border: 1px solid rgba(0,255,136,0.2); padding: 5px 12px; border-radius: 4px; cursor: pointer; transition: all 0.2s; }
  .nav-ip:hover { background: rgba(0,255,136,0.12); border-color: var(--green); }
  .copy-toast { position: fixed; top: 70px; right: 40px; background: var(--green); color: #000; font-family: 'Minecraft', monospace; font-size: 12px; font-weight: 700; padding: 8px 16px; border-radius: 4px; z-index: 9999; opacity: 0; transform: translateY(-10px); transition: all 0.3s; pointer-events: none; }
  .copy-toast.show { opacity: 1; transform: translateY(0); }
  .page { display: none; padding-top: 60px; min-height: 100vh; position: relative; z-index: 2; }
  .page.active { display: block; }
  #home { display: none; min-height: 100vh; position: relative; overflow: hidden; }
  #home.active { display: block; }
  .hero-bg { position: absolute; top: 0; left: 0; right: 0; height: 100vh; pointer-events: none; background: radial-gradient(ellipse 80% 60% at 50% 0%, rgba(0,212,255,0.07) 0%, transparent 60%), radial-gradient(ellipse 60% 40% at 80% 80%, rgba(123,47,255,0.06) 0%, transparent 50%), radial-gradient(ellipse 40% 30% at 20% 60%, rgba(255,107,53,0.04) 0%, transparent 40%); }
  .hero-grid { position: absolute; top: 0; left: 0; right: 0; height: 100vh; pointer-events: none; background-image: linear-gradient(rgba(0,212,255,0.04) 1px, transparent 1px), linear-gradient(90deg, rgba(0,212,255,0.04) 1px, transparent 1px); background-size: 60px 60px; mask-image: radial-gradient(ellipse 80% 70% at 50% 30%, black 0%, transparent 80%); }
  .hero-content { position: relative; z-index: 2; padding: 100px 40px 80px; max-width: 1200px; margin: 0 auto; }
  .hero-badge { display: inline-flex; align-items: center; gap: 8px; background: rgba(0,255,136,0.08); border: 1px solid rgba(0,255,136,0.25); padding: 5px 14px; border-radius: 20px; font-size: 12px; font-weight: 600; color: var(--green); letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 32px; animation: fadeUp 0.6s ease both; }
  .hero-badge::before { content: ''; width: 6px; height: 6px; background: var(--green); border-radius: 50%; animation: pulse 2s infinite; }
  @keyframes pulse { 0%, 100% { opacity: 1; box-shadow: 0 0 0 0 rgba(0,255,136,0.4); } 50% { opacity: 0.7; box-shadow: 0 0 0 6px rgba(0,255,136,0); } }
  .hero-title { font-family: 'Minecraft', monospace; font-weight: normal; font-size: clamp(52px, 8vw, 96px); line-height: 1; letter-spacing: -1px; animation: fadeUp 0.6s 0.1s ease both; }
  .hero-title .line1 { color: #fff; }
  .hero-title .line2 { background: linear-gradient(135deg, var(--accent) 0%, var(--accent2) 60%, var(--accent3) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; display: block; }
  .hero-sub { font-size: 18px; font-weight: 400; color: var(--text2); max-width: 560px; line-height: 1.7; margin: 24px 0 40px; animation: fadeUp 0.6s 0.2s ease both; }
  .hero-actions { display: flex; gap: 16px; flex-wrap: wrap; animation: fadeUp 0.6s 0.3s ease both; }
  .btn-primary { background: linear-gradient(135deg, var(--accent), var(--accent2)); color: #fff; border: none; padding: 14px 32px; font-family: 'Minecraft', monospace; font-size: 15px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; border-radius: 6px; cursor: pointer; transition: all 0.3s; box-shadow: 0 4px 24px rgba(0,212,255,0.25); text-decoration: none; display: inline-block; }
  .btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 32px rgba(0,212,255,0.4); }
  .btn-outline { background: transparent; color: var(--text); border: 1px solid var(--border2); padding: 14px 32px; font-family: 'Minecraft', monospace; font-size: 15px; font-weight: 600; letter-spacing: 1.5px; text-transform: uppercase; border-radius: 6px; cursor: pointer; transition: all 0.3s; text-decoration: none; display: inline-block; }
  .btn-outline:hover { border-color: var(--accent); color: var(--accent); background: rgba(0,212,255,0.05); }
  .stats-bar { display: flex; margin-top: 80px; border: 1px solid var(--border); border-radius: 8px; overflow: hidden; animation: fadeUp 0.6s 0.4s ease both; }
  .stat-item { flex: 1; padding: 24px 28px; border-right: 1px solid var(--border); background: rgba(13,17,23,0.8); transition: background 0.2s; }
  .stat-item:last-child { border-right: none; }
  .stat-item:hover { background: rgba(0,212,255,0.04); }
  .stat-label { font-size: 11px; font-weight: 600; color: var(--text3); text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 6px; }
  .stat-value { font-family: 'Minecraft', monospace; font-size: 20px; color: #fff; }
  .stat-value.green { color: var(--green); }
  .stat-value.blue { color: var(--accent); }
  .features { padding: 80px 40px; max-width: 1200px; margin: 0 auto; position: relative; z-index: 3; }
  .section-header { text-align: center; margin-bottom: 56px; }
  .section-tag { font-size: 11px; font-weight: 700; color: var(--accent); letter-spacing: 3px; text-transform: uppercase; margin-bottom: 12px; }
  .section-title { font-family: 'Minecraft', monospace; font-size: 36px; font-weight: normal; color: #fff; margin-bottom: 12px; }
  .section-sub { color: var(--text2); font-size: 15px; max-width: 500px; margin: 0 auto; line-height: 1.6; }
  .features-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
  .feature-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 0;
    transition: all 0.35s cubic-bezier(.25,.8,.25,1);
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }
  .feature-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--card-accent, var(--accent)), transparent);
    opacity: 0;
    transition: opacity 0.3s;
    z-index: 2;
  }
  .feature-card:hover { border-color: var(--card-accent, var(--accent)); transform: translateY(-6px); box-shadow: 0 16px 48px rgba(0,0,0,0.4); }
  .feature-card:hover::before { opacity: 1; }
  .feature-img-wrap {
    width: 100%;
    height: 160px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
  }
  .feature-img-wrap::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 60px;
    background: linear-gradient(transparent, var(--card));
    z-index: 1;
  }
  .feature-img-wrap svg {
    width: 100%;
    height: 100%;
    display: block;
  }
  .feature-body { padding: 20px 24px 24px; flex: 1; }
  .feature-title { font-family: 'Minecraft', monospace; font-size: 14px; font-weight: normal; color: #fff; margin-bottom: 10px; letter-spacing: 0.5px; }
  .feature-desc { font-size: 13px; color: var(--text2); line-height: 1.65; }
  .socials-section { padding: 60px 40px 100px; max-width: 1200px; margin: 0 auto; position: relative; z-index: 3; }
  .socials-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-top: 40px; }
  .social-card { display: flex; align-items: center; gap: 16px; padding: 24px 28px; background: var(--card); border: 1px solid var(--border); border-radius: 8px; text-decoration: none; transition: all 0.3s; cursor: pointer; position: relative; z-index: 4; }
  .social-card:hover { transform: translateY(-3px); }
  .social-card.discord:hover { border-color: #5865F2; box-shadow: 0 8px 32px rgba(88,101,242,0.2); }
  .social-card.telegram:hover { border-color: #26A5E4; box-shadow: 0 8px 32px rgba(38,165,228,0.2); }
  .social-card.tiktok:hover { border-color: #ff0050; box-shadow: 0 8px 32px rgba(255,0,80,0.2); }
  .social-icon { width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 22px; flex-shrink: 0; }
  .social-icon.discord { background: rgba(88,101,242,0.15); }
  .social-icon.telegram { background: rgba(38,165,228,0.15); }
  .social-icon.tiktok { background: rgba(255,0,80,0.1); }
  .social-info { flex: 1; }
  .social-name { font-family: 'Minecraft', monospace; font-size: 15px; font-weight: normal; color: #fff; margin-bottom: 4px; }
  .social-desc { font-size: 13px; color: var(--text2); }
  .social-arrow { color: var(--text3); font-size: 18px; }
  #docs { display: none; min-height: 100vh; padding-top: 60px; }
  #docs.active { display: flex; }
  .docs-layout { display: flex; width: 100%; min-height: calc(100vh - 60px); }
  .docs-sidebar { width: 260px; flex-shrink: 0; background: var(--bg2); border-right: 1px solid var(--border); padding: 32px 0; position: sticky; top: 60px; height: calc(100vh - 60px); overflow-y: auto; z-index: 10; }
  .docs-sidebar::-webkit-scrollbar { width: 4px; }
  .docs-sidebar::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 2px; }
  .sidebar-section { margin-bottom: 8px; }
  .sidebar-section-title { font-size: 10px; font-weight: 700; color: var(--text3); text-transform: uppercase; letter-spacing: 2px; padding: 8px 24px 6px; }
  .sidebar-link { display: block; padding: 7px 24px; font-size: 13px; font-weight: 500; color: var(--text2); text-decoration: none; cursor: pointer; transition: all 0.15s; border-left: 2px solid transparent; }
  .sidebar-link:hover { color: var(--text); background: rgba(255,255,255,0.03); }
  .sidebar-link.active { color: var(--accent); border-left-color: var(--accent); background: rgba(0,212,255,0.06); }
  .docs-content { flex: 1; padding: 48px 60px; max-width: 900px; overflow-y: auto; }
  .doc-section { display: none; }
  .doc-section.active { display: block; }
  .doc-section h1 { font-family: 'Minecraft', monospace; font-size: 32px; font-weight: normal; color: #fff; margin-bottom: 8px; line-height: 1.2; }
  .doc-section .doc-lead { font-size: 16px; color: var(--text2); line-height: 1.7; margin-bottom: 40px; padding-bottom: 32px; border-bottom: 1px solid var(--border); }
  .doc-section h2 { font-family: 'Minecraft', monospace; font-size: 20px; font-weight: normal; color: #fff; margin: 40px 0 16px; padding-bottom: 8px; border-bottom: 1px solid var(--border); }
  .doc-section p { font-size: 15px; color: var(--text); line-height: 1.75; margin-bottom: 16px; }
  .doc-section ul { list-style: none; margin: 0 0 20px; }
  .doc-section ul li { font-size: 15px; color: var(--text); line-height: 1.6; padding: 5px 0 5px 20px; position: relative; }
  .doc-section ul li::before { content: '›'; position: absolute; left: 0; color: var(--accent); font-weight: 700; }
  .doc-table { width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 14px; }
  .doc-table th { background: rgba(0,212,255,0.08); color: var(--accent); font-weight: 700; font-size: 11px; text-transform: uppercase; letter-spacing: 1.5px; padding: 10px 16px; text-align: left; border-bottom: 1px solid var(--border2); }
  .doc-table td { padding: 10px 16px; border-bottom: 1px solid var(--border); color: var(--text); vertical-align: top; }
  .doc-table tr:last-child td { border-bottom: none; }
  .doc-table tr:hover td { background: rgba(255,255,255,0.02); }
  .doc-table td:first-child { font-family: 'Minecraft', monospace; font-size: 13px; color: var(--accent2); white-space: nowrap; }
  .info-box { background: rgba(0,212,255,0.06); border: 1px solid rgba(0,212,255,0.2); border-radius: 6px; padding: 16px 20px; margin: 20px 0; font-size: 14px; color: var(--text); line-height: 1.6; }
  .info-box.warning { background: rgba(240,192,64,0.06); border-color: rgba(240,192,64,0.25); }
  .info-box.future { background: rgba(123,47,255,0.06); border-color: rgba(123,47,255,0.25); }
  .info-box strong { color: var(--accent); }
  .info-box.warning strong { color: var(--gold); }
  .info-box.future strong { color: var(--accent2); }
  .zone-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 20px 0; }
  .zone-card { border-radius: 6px; padding: 20px; border: 1px solid; }
  .zone-card.safe { background: rgba(0,255,136,0.04); border-color: rgba(0,255,136,0.2); }
  .zone-card.danger { background: rgba(255,68,85,0.04); border-color: rgba(255,68,85,0.2); }
  .zone-card h4 { font-family: 'Minecraft', monospace; font-size: 14px; font-weight: normal; margin-bottom: 12px; }
  .zone-card.safe h4 { color: var(--green); }
  .zone-card.danger h4 { color: var(--red); }
  .zone-card ul { margin: 0; }
  .zone-card ul li { font-size: 13px; }
  .event-grid { display: grid; gap: 8px; margin: 16px 0; }
  .event-row { display: grid; grid-template-columns: 200px 1fr 110px; border: 1px solid var(--border); border-radius: 6px; overflow: hidden; }
  .event-row .ev-name { padding: 12px 16px; background: rgba(13,17,23,0.8); font-weight: 700; font-size: 13px; color: #fff; border-right: 1px solid var(--border); }
  .event-row .ev-desc { padding: 12px 16px; font-size: 13px; color: var(--text2); border-right: 1px solid var(--border); }
  .event-row .ev-time { padding: 12px 16px; font-family: 'Minecraft', monospace; font-size: 12px; color: var(--gold); text-align: center; }
  code { font-family: 'Minecraft', monospace; font-size: 13px; background: rgba(0,212,255,0.08); color: var(--accent); padding: 2px 7px; border-radius: 3px; }
  #news { display: none; min-height: 100vh; padding-top: 60px; }
  #news.active { display: block; }
  .news-header { padding: 60px 40px 40px; max-width: 1100px; margin: 0 auto; border-bottom: 1px solid var(--border); }
  .news-header h1 { font-family: 'Minecraft', monospace; font-size: 40px; font-weight: normal; color: #fff; margin-bottom: 8px; }
  .news-header p { color: var(--text2); font-size: 15px; }
  .news-container { max-width: 1100px; margin: 0 auto; padding: 40px; display: grid; grid-template-columns: 1fr 340px; gap: 40px; align-items: start; }
  .news-list { display: flex; flex-direction: column; gap: 16px; }
  .news-card { background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 28px; transition: all 0.25s; position: relative; overflow: hidden; }
  .news-card::after { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 3px; }
  .news-card.type-update::after { background: var(--accent); }
  .news-card.type-event::after { background: var(--gold); }
  .news-card.type-announce::after { background: var(--accent2); }
  .news-card.type-fix::after { background: var(--green); }
  .news-card.type-info::after { background: var(--text2); }
  .news-card:hover { border-color: var(--border2); transform: translateX(4px); }
  .news-meta { display: flex; align-items: center; gap: 12px; margin-bottom: 12px; }
  .news-type { font-size: 10px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; padding: 3px 8px; border-radius: 3px; }
  .type-update .news-type { background: rgba(0,212,255,0.1); color: var(--accent); }
  .type-event .news-type { background: rgba(240,192,64,0.1); color: var(--gold); }
  .type-announce .news-type { background: rgba(123,47,255,0.1); color: var(--accent2); }
  .type-fix .news-type { background: rgba(0,255,136,0.1); color: var(--green); }
  .type-info .news-type { background: rgba(200,216,232,0.1); color: var(--text2); }
  .news-date { font-family: 'Minecraft', monospace; font-size: 12px; color: var(--text3); }
  .news-card h2 { font-family: 'Minecraft', monospace; font-size: 18px; font-weight: normal; color: #fff; margin-bottom: 10px; line-height: 1.3; }
  /* text body: line-height and spacing, <br> tags handle newlines */
  .news-card p { font-size: 14px; color: var(--text2); line-height: 1.75; margin-bottom: 16px; }
  .news-tags { display: flex; gap: 8px; flex-wrap: wrap; }
  .news-tag { font-size: 11px; color: var(--text3); background: rgba(255,255,255,0.04); border: 1px solid var(--border); padding: 3px 10px; border-radius: 20px; }
  .news-sidebar { display: flex; flex-direction: column; gap: 20px; }
  .sidebar-widget { background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 24px; }
  .widget-title { font-family: 'Minecraft', monospace; font-size: 14px; font-weight: normal; color: #fff; margin-bottom: 16px; padding-bottom: 12px; border-bottom: 1px solid var(--border); }
  .server-status { display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; }
  .status-indicator { display: flex; align-items: center; gap: 8px; font-size: 13px; font-weight: 600; }
  .status-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--green); animation: pulse 2s infinite; }
  .status-dot.offline { background: var(--red); animation: none; }
  .status-dot.loading { background: var(--gold); animation: pulse 1s infinite; }
  .players-online { font-family: 'Minecraft', monospace; font-size: 24px; color: var(--green); font-weight: bold; margin: 8px 0 4px; }
  .players-label { font-size: 11px; color: var(--text3); text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 10px; }
  .players-max { font-size: 11px; color: var(--text3); }
  .admin-fab { position: fixed; bottom: 28px; right: 28px; width: 44px; height: 44px; background: rgba(123,47,255,0.15); border: 1px solid rgba(123,47,255,0.3); border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 500; transition: all 0.2s; font-size: 18px; color: var(--accent2); }
  .admin-fab:hover { background: rgba(123,47,255,0.25); border-color: var(--accent2); }
  .modal-overlay { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.7); backdrop-filter: blur(6px); z-index: 2000; align-items: center; justify-content: center; }
  .modal-overlay.open { display: flex; }
  .modal-box { background: var(--bg2); border: 1px solid var(--border2); border-radius: 10px; padding: 32px; width: 100%; max-width: 560px; position: relative; max-height: 90vh; overflow-y: auto; }
  .modal-title { font-family: 'Minecraft', monospace; font-size: 20px; color: #fff; margin-bottom: 24px; display: flex; align-items: center; gap: 10px; }
  .modal-close { position: absolute; top: 16px; right: 16px; background: none; border: none; color: var(--text3); font-size: 20px; cursor: pointer; padding: 4px 8px; border-radius: 4px; transition: all 0.15s; }
  .modal-close:hover { color: #fff; background: rgba(255,255,255,0.06); }
  .form-group { margin-bottom: 16px; }
  .form-label { display: block; font-size: 11px; font-weight: 700; color: var(--text3); text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 6px; }
  .form-input, .form-textarea, .form-select { width: 100%; background: var(--bg3); border: 1px solid var(--border); border-radius: 6px; color: var(--text); font-family: 'Minecraft', monospace; font-size: 14px; padding: 10px 14px; transition: border-color 0.2s; outline: none; }
  .form-input:focus, .form-textarea:focus, .form-select:focus { border-color: var(--accent); }
  /* textarea: preserve whitespace and allow newlines */
  .form-textarea { resize: vertical; min-height: 120px; white-space: pre-wrap; font-family: monospace; tab-size: 2; }
  .form-select { cursor: pointer; }
  .form-tags-input { width: 100%; background: var(--bg3); border: 1px solid var(--border); border-radius: 6px; color: var(--text); font-family: 'Minecraft', monospace; font-size: 14px; padding: 10px 14px; outline: none; transition: border-color 0.2s; }
  .form-tags-input:focus { border-color: var(--accent); }
  .btn-submit { background: linear-gradient(135deg, var(--accent2), var(--accent)); color: #fff; border: none; padding: 12px 28px; font-family: 'Minecraft', monospace; font-size: 14px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; border-radius: 6px; cursor: pointer; transition: all 0.2s; width: 100%; margin-top: 8px; }
  .btn-submit:hover { opacity: 0.9; transform: translateY(-1px); }
  .btn-danger { background: rgba(255,68,85,0.12); color: var(--red); border: 1px solid rgba(255,68,85,0.3); padding: 6px 14px; font-family: 'Minecraft', monospace; font-size: 12px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; border-radius: 4px; cursor: pointer; transition: all 0.2s; }
  .btn-danger:hover { background: rgba(255,68,85,0.22); }
  .btn-edit { background: rgba(0,212,255,0.08); color: var(--accent); border: 1px solid rgba(0,212,255,0.2); padding: 6px 14px; font-family: 'Minecraft', monospace; font-size: 12px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; border-radius: 4px; cursor: pointer; transition: all 0.2s; }
  .btn-edit:hover { background: rgba(0,212,255,0.15); }
  .news-actions { display: flex; gap: 8px; margin-top: 14px; padding-top: 14px; border-top: 1px solid var(--border); }
  .admin-bar { background: rgba(123,47,255,0.06); border-bottom: 1px solid rgba(123,47,255,0.2); padding: 10px 40px; display: flex; align-items: center; justify-content: space-between; gap: 12px; }
  .admin-bar-text { font-size: 12px; color: var(--accent2); font-weight: 600; letter-spacing: 1px; }
  .btn-add-news { background: rgba(123,47,255,0.15); color: var(--accent2); border: 1px solid rgba(123,47,255,0.35); padding: 7px 18px; font-family: 'Minecraft', monospace; font-size: 13px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; border-radius: 5px; cursor: pointer; transition: all 0.2s; }
  .btn-add-news:hover { background: rgba(123,47,255,0.25); }
  .btn-logout { background: none; color: var(--text3); border: 1px solid var(--border); padding: 7px 14px; font-family: 'Minecraft', monospace; font-size: 12px; font-weight: 600; letter-spacing: 1px; border-radius: 5px; cursor: pointer; transition: all 0.2s; }
  .btn-logout:hover { color: var(--red); border-color: rgba(255,68,85,0.3); }
  .server-ip { font-family: 'Minecraft', monospace; font-size: 13px; color: var(--accent); background: rgba(0,212,255,0.06); border: 1px solid rgba(0,212,255,0.15); padding: 8px 12px; border-radius: 4px; text-align: center; cursor: pointer; transition: all 0.2s; margin-top: 8px; }
  .server-ip:hover { background: rgba(0,212,255,0.12); }
  .version-tag { font-family: 'Minecraft', monospace; font-size: 12px; color: var(--text3); background: rgba(255,255,255,0.04); padding: 3px 8px; border-radius: 3px; }
  .changelog-list { display: flex; flex-direction: column; gap: 10px; }
  .changelog-item { display: flex; align-items: flex-start; gap: 10px; font-size: 13px; }
  .changelog-version { font-family: 'Minecraft', monospace; font-size: 11px; color: var(--accent2); background: rgba(123,47,255,0.1); padding: 2px 6px; border-radius: 3px; white-space: nowrap; margin-top: 2px; }
  .changelog-text { color: var(--text2); line-height: 1.5; }
  .docs-admin-bar { background: rgba(123,47,255,0.06); border-bottom: 1px solid rgba(123,47,255,0.2); padding: 10px 40px; display: flex; align-items: center; justify-content: space-between; gap: 12px; position: sticky; top: 60px; z-index: 50; }
  .doc-section-actions { display: flex; gap: 8px; margin-top: 40px; padding-top: 16px; border-top: 1px solid var(--border); }
  .doc-order-btn { background: rgba(255,255,255,0.04); color: var(--text3); border: 1px solid var(--border); padding: 6px 10px; font-family: 'Minecraft', monospace; font-size: 12px; border-radius: 4px; cursor: pointer; transition: all 0.2s; }
  .doc-order-btn:hover { color: var(--text); border-color: var(--border2); }
  @keyframes fadeUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
  ::-webkit-scrollbar { width: 6px; }
  ::-webkit-scrollbar-track { background: var(--bg); }
  ::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 3px; }
  ::-webkit-scrollbar-thumb:hover { background: var(--text3); }
</style>
</head>
<body>

<nav>
  <div class="nav-logo" onclick="showPage('home')">Bliss<span>Full</span>Reloaded</div>
  <div class="nav-links">
    <a onclick="showPage('home')" id="nav-home" class="active">Главная</a>
    <a onclick="showPage('docs')" id="nav-docs">Документация</a>
    <a onclick="showPage('news')" id="nav-news">Новости</a>
  </div>
  <div class="nav-ip" onclick="copyIP()">blissfull.mc-server.net:25816</div>
</nav>
<div class="copy-toast" id="copyToast">✓ IP скопирован!</div>

<div id="home" class="page active">
  <div class="hero-bg"></div>
  <div class="hero-grid"></div>
  <div class="hero-content">
    <div class="hero-badge">Сервер онлайн</div>
    <div class="hero-title">
      <span class="line1">Vanilla+</span>
      <span class="line2">BlissFullReloaded</span>
    </div>
    <p class="hero-sub">Кооперативное выживание с живой экономикой, системой власти и расширяющимся миром. Каждая смерть имеет цену.</p>
    <div class="hero-actions">
      <a class="btn-primary" onclick="showPage('docs')">Документация</a>
      <a class="btn-outline" onclick="showPage('news')">Новости</a>
    </div>
    <div class="stats-bar">
      <div class="stat-item"><div class="stat-label">Версия</div><div class="stat-value blue" id="hero-version">1.21.x</div></div>
      <div class="stat-item"><div class="stat-label">Режим</div><div class="stat-value">Vanilla+</div></div>
      <div class="stat-item"><div class="stat-label">Игроков онлайн</div><div class="stat-value green" id="hero-players">—</div></div>
      <div class="stat-item"><div class="stat-label">Статус</div><div class="stat-value green" id="hero-status">Проверка...</div></div>
    </div>
  </div>
  <div class="features">
    <div class="section-header">
      <div class="section-tag">Механики</div>
      <div class="section-title">Чем живёт сервер</div>
      <div class="section-sub">Уникальные механики, которые заставляют игроков работать вместе</div>
    </div>
    <div class="features-grid">
      <div class="feature-card" style="--card-accent:#00d4ff">
        <div class="feature-img-wrap"><svg viewBox="0 0 400 160" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
  <defs>
    <radialGradient id="bg1" cx="50%" cy="50%" r="70%"><stop offset="0%" stop-color="#0a1628"/><stop offset="100%" stop-color="#080c10"/></radialGradient>
    <radialGradient id="glow1" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#00d4ff" stop-opacity="0.2"/><stop offset="100%" stop-color="#00d4ff" stop-opacity="0"/></radialGradient>
  </defs>
  <rect width="400" height="160" fill="url(#bg1)"/>
  <rect width="400" height="160" fill="url(#glow1)"/>
  <!-- Grid -->
  <g stroke="#00d4ff" stroke-opacity="0.08" stroke-width="1">
    <line x1="0" y1="20" x2="400" y2="20"/><line x1="0" y1="40" x2="400" y2="40"/>
    <line x1="0" y1="60" x2="400" y2="60"/><line x1="0" y1="80" x2="400" y2="80"/>
    <line x1="0" y1="100" x2="400" y2="100"/><line x1="0" y1="120" x2="400" y2="120"/>
    <line x1="0" y1="140" x2="400" y2="140"/>
    <line x1="40" y1="0" x2="40" y2="160"/><line x1="80" y1="0" x2="80" y2="160"/>
    <line x1="120" y1="0" x2="120" y2="160"/><line x1="160" y1="0" x2="160" y2="160"/>
    <line x1="200" y1="0" x2="200" y2="160"/><line x1="240" y1="0" x2="240" y2="160"/>
    <line x1="280" y1="0" x2="280" y2="160"/><line x1="320" y1="0" x2="320" y2="160"/>
    <line x1="360" y1="0" x2="360" y2="160"/>
  </g>
  <!-- Barrier circle -->
  <circle cx="200" cy="80" r="55" fill="none" stroke="#00d4ff" stroke-width="1.5" stroke-opacity="0.6" stroke-dasharray="4 3"/>
  <circle cx="200" cy="80" r="55" fill="none" stroke="#00d4ff" stroke-width="8" stroke-opacity="0.05"/>
  <circle cx="200" cy="80" r="40" fill="none" stroke="#00d4ff" stroke-width="0.8" stroke-opacity="0.3" stroke-dasharray="2 4"/>
  <!-- World icon pixels -->
  <g fill="#00d4ff" fill-opacity="0.9">
    <rect x="192" y="64" width="4" height="4"/><rect x="196" y="64" width="4" height="4"/>
    <rect x="200" y="64" width="4" height="4"/><rect x="204" y="64" width="4" height="4"/>
    <rect x="188" y="68" width="4" height="4"/><rect x="192" y="68" width="4" height="4"/>
    <rect x="200" y="68" width="4" height="4"/><rect x="208" y="68" width="4" height="4"/>
    <rect x="188" y="72" width="4" height="4"/><rect x="196" y="72" width="4" height="4"/>
    <rect x="204" y="72" width="4" height="4"/><rect x="208" y="72" width="4" height="4"/>
    <rect x="188" y="76" width="4" height="4"/><rect x="208" y="76" width="4" height="4"/>
    <rect x="188" y="80" width="4" height="4"/><rect x="192" y="80" width="4" height="4"/>
    <rect x="204" y="80" width="4" height="4"/><rect x="208" y="80" width="4" height="4"/>
    <rect x="188" y="84" width="4" height="4"/><rect x="196" y="84" width="4" height="4"/>
    <rect x="200" y="84" width="4" height="4"/><rect x="208" y="84" width="4" height="4"/>
    <rect x="192" y="88" width="4" height="4"/><rect x="200" y="88" width="4" height="4"/>
    <rect x="204" y="88" width="4" height="4"/>
    <rect x="196" y="92" width="4" height="4"/><rect x="200" y="92" width="4" height="4"/>
  </g>
  <!-- Glow dots on barrier -->
  <circle cx="200" cy="25" r="3" fill="#00d4ff" fill-opacity="0.8"/>
  <circle cx="255" cy="80" r="2.5" fill="#00d4ff" fill-opacity="0.6"/>
  <circle cx="145" cy="80" r="2.5" fill="#00d4ff" fill-opacity="0.6"/>
  <circle cx="200" cy="135" r="3" fill="#00d4ff" fill-opacity="0.8"/>
  <circle cx="248" cy="47" r="2" fill="#00d4ff" fill-opacity="0.5"/>
  <circle cx="152" cy="113" r="2" fill="#00d4ff" fill-opacity="0.5"/>
</svg></div>
        <div class="feature-body"><div class="feature-title">Всемирный барьер</div><div class="feature-desc">Размер мира зависит от общего опыта всех игроков. Каждая смерть сужает барьер для всех.</div></div>
      </div>
      <div class="feature-card" style="--card-accent:#7b2fff">
        <div class="feature-img-wrap"><svg viewBox="0 0 400 160" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
  <defs>
    <radialGradient id="bg2" cx="50%" cy="100%" r="80%"><stop offset="0%" stop-color="#120a1e"/><stop offset="100%" stop-color="#080c10"/></radialGradient>
    <radialGradient id="glow2" cx="50%" cy="80%" r="40%"><stop offset="0%" stop-color="#7b2fff" stop-opacity="0.25"/><stop offset="100%" stop-color="#7b2fff" stop-opacity="0"/></radialGradient>
  </defs>
  <rect width="400" height="160" fill="url(#bg2)"/>
  <rect width="400" height="160" fill="url(#glow2)"/>
  <!-- Ground -->
  <rect x="0" y="128" width="400" height="32" fill="#1a1228" fill-opacity="0.7"/>
  <!-- Big building center -->
  <rect x="172" y="56" width="56" height="72" fill="#1e1530" stroke="#7b2fff" stroke-width="1" stroke-opacity="0.5"/>
  <rect x="176" y="44" width="48" height="16" fill="#261a3a" stroke="#7b2fff" stroke-width="1" stroke-opacity="0.4"/>
  <rect x="186" y="32" width="28" height="14" fill="#2c1e40" stroke="#7b2fff" stroke-width="0.8" stroke-opacity="0.4"/>
  <rect x="194" y="20" width="12" height="14" fill="#7b2fff" fill-opacity="0.7"/>
  <!-- Windows center building -->
  <rect x="180" y="64" width="8" height="8" fill="#7b2fff" fill-opacity="0.6"/><rect x="192" y="64" width="8" height="8" fill="#7b2fff" fill-opacity="0.4"/>
  <rect x="204" y="64" width="8" height="8" fill="#7b2fff" fill-opacity="0.6"/><rect x="216" y="64" width="8" height="8" fill="#7b2fff" fill-opacity="0.4"/>
  <rect x="180" y="78" width="8" height="8" fill="#7b2fff" fill-opacity="0.3"/><rect x="192" y="78" width="8" height="8" fill="#7b2fff" fill-opacity="0.6"/>
  <rect x="204" y="78" width="8" height="8" fill="#7b2fff" fill-opacity="0.4"/><rect x="216" y="78" width="8" height="8" fill="#7b2fff" fill-opacity="0.5"/>
  <rect x="180" y="92" width="8" height="8" fill="#7b2fff" fill-opacity="0.5"/><rect x="204" y="92" width="8" height="8" fill="#7b2fff" fill-opacity="0.4"/>
  <!-- Door -->
  <rect x="192" y="108" width="16" height="20" fill="#7b2fff" fill-opacity="0.4"/>
  <!-- Left building -->
  <rect x="108" y="80" width="48" height="48" fill="#160f24" stroke="#7b2fff" stroke-width="0.8" stroke-opacity="0.35"/>
  <rect x="114" y="68" width="36" height="14" fill="#1e1530" stroke="#7b2fff" stroke-width="0.6" stroke-opacity="0.3"/>
  <rect x="122" y="58" width="20" height="12" fill="#7b2fff" fill-opacity="0.4"/>
  <rect x="116" y="88" width="6" height="6" fill="#7b2fff" fill-opacity="0.4"/><rect x="126" y="88" width="6" height="6" fill="#7b2fff" fill-opacity="0.5"/>
  <rect x="136" y="88" width="6" height="6" fill="#7b2fff" fill-opacity="0.35"/><rect x="146" y="88" width="6" height="6" fill="#7b2fff" fill-opacity="0.4"/>
  <rect x="116" y="100" width="6" height="6" fill="#7b2fff" fill-opacity="0.3"/><rect x="136" y="100" width="6" height="6" fill="#7b2fff" fill-opacity="0.45"/>
  <!-- Right building -->
  <rect x="244" y="76" width="48" height="52" fill="#160f24" stroke="#7b2fff" stroke-width="0.8" stroke-opacity="0.35"/>
  <rect x="250" y="64" width="36" height="14" fill="#1e1530" stroke="#7b2fff" stroke-width="0.6" stroke-opacity="0.3"/>
  <rect x="258" y="52" width="20" height="14" fill="#7b2fff" fill-opacity="0.5"/>
  <rect x="252" y="84" width="6" height="6" fill="#7b2fff" fill-opacity="0.5"/><rect x="262" y="84" width="6" height="6" fill="#7b2fff" fill-opacity="0.35"/>
  <rect x="274" y="84" width="6" height="6" fill="#7b2fff" fill-opacity="0.5"/><rect x="284" y="84" width="6" height="6" fill="#7b2fff" fill-opacity="0.4"/>
  <rect x="252" y="96" width="6" height="6" fill="#7b2fff" fill-opacity="0.4"/><rect x="274" y="96" width="6" height="6" fill="#7b2fff" fill-opacity="0.3"/>
  <!-- Stars -->
  <circle cx="60" cy="20" r="1.2" fill="#fff" fill-opacity="0.4"/>
  <circle cx="100" cy="40" r="1" fill="#fff" fill-opacity="0.3"/>
  <circle cx="320" cy="15" r="1.2" fill="#fff" fill-opacity="0.4"/>
  <circle cx="350" cy="35" r="1" fill="#fff" fill-opacity="0.35"/>
  <circle cx="340" cy="55" r="0.8" fill="#7b2fff" fill-opacity="0.8"/>
  <circle cx="60" cy="50" r="0.8" fill="#7b2fff" fill-opacity="0.6"/>
</svg></div>
        <div class="feature-body"><div class="feature-title">Столица и власть</div><div class="feature-desc">Мэр, Судья, Следователь, Охрана. Живая политическая система внутри игры.</div></div>
      </div>
      <div class="feature-card" style="--card-accent:#ff6b35">
        <div class="feature-img-wrap"><svg viewBox="0 0 400 160" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
  <defs>
    <radialGradient id="bg3" cx="50%" cy="50%" r="70%"><stop offset="0%" stop-color="#1a0808"/><stop offset="100%" stop-color="#080c10"/></radialGradient>
    <radialGradient id="glow3" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#ff4455" stop-opacity="0.15"/><stop offset="100%" stop-color="transparent"/></radialGradient>
  </defs>
  <rect width="400" height="160" fill="url(#bg3)"/>
  <rect width="400" height="160" fill="url(#glow3)"/>
  <!-- Ground blocks -->
  <g fill="#1c1208" stroke="#ff6b35" stroke-width="0.5" stroke-opacity="0.25">
    <rect x="0" y="128" width="32" height="32"/><rect x="32" y="128" width="32" height="32"/>
    <rect x="64" y="128" width="32" height="32"/><rect x="96" y="128" width="32" height="32"/>
    <rect x="128" y="128" width="32" height="32"/><rect x="160" y="128" width="32" height="32"/>
    <rect x="192" y="128" width="32" height="32"/><rect x="224" y="128" width="32" height="32"/>
    <rect x="256" y="128" width="32" height="32"/><rect x="288" y="128" width="32" height="32"/>
    <rect x="320" y="128" width="32" height="32"/><rect x="352" y="128" width="32" height="32"/>
  </g>
  <!-- Sword left (pixel art) -->
  <g fill="#c8d8e8" fill-opacity="0.9" transform="translate(130, 30) rotate(-45, 40, 70)">
    <rect x="38" y="20" width="4" height="4"/>
    <rect x="38" y="24" width="4" height="4"/>
    <rect x="38" y="28" width="4" height="4"/>
    <rect x="38" y="32" width="4" height="4"/>
    <rect x="38" y="36" width="4" height="4"/>
    <rect x="38" y="40" width="4" height="4"/>
    <rect x="38" y="44" width="4" height="4"/>
    <rect x="38" y="48" width="4" height="4"/>
    <!-- Guard -->
    <rect x="30" y="52" width="20" height="4" fill="#f0c040"/>
    <!-- Handle -->
    <rect x="38" y="56" width="4" height="8" fill="#8b5e2a"/>
    <rect x="38" y="64" width="4" height="4" fill="#f0c040"/>
  </g>
  <!-- Sword right (pixel art) -->
  <g fill="#c8d8e8" fill-opacity="0.9" transform="translate(230, 30) rotate(45, 40, 70) scaleX(-1) translate(-80,0)">
    <rect x="38" y="20" width="4" height="4"/>
    <rect x="38" y="24" width="4" height="4"/>
    <rect x="38" y="28" width="4" height="4"/>
    <rect x="38" y="32" width="4" height="4"/>
    <rect x="38" y="36" width="4" height="4"/>
    <rect x="38" y="40" width="4" height="4"/>
    <rect x="38" y="44" width="4" height="4"/>
    <rect x="38" y="48" width="4" height="4"/>
    <rect x="30" y="52" width="20" height="4" fill="#ff4455"/>
    <rect x="38" y="56" width="4" height="8" fill="#8b2a2a"/>
    <rect x="38" y="64" width="4" height="4" fill="#ff4455"/>
  </g>
  <!-- Clash sparks center -->
  <g fill="#ff4455">
    <rect x="195" y="58" width="4" height="4" fill-opacity="0.9"/>
    <rect x="203" y="54" width="4" height="4" fill-opacity="0.7"/>
    <rect x="191" y="50" width="4" height="4" fill-opacity="0.5"/>
    <rect x="207" y="62" width="4" height="4" fill-opacity="0.6"/>
    <rect x="199" y="46" width="4" height="4" fill-opacity="0.4"/>
  </g>
  <g fill="#ff6b35">
    <rect x="197" y="62" width="4" height="4" fill-opacity="0.8"/>
    <rect x="205" y="50" width="4" height="4" fill-opacity="0.6"/>
    <rect x="189" y="58" width="4" height="4" fill-opacity="0.5"/>
  </g>
</svg></div>
        <div class="feature-body"><div class="feature-title">Полное ПВП</div><div class="feature-desc">За пределами Столицы — дикие земли. Рейды, убийства, захват территорий.</div></div>
      </div>
      <div class="feature-card" style="--card-accent:#f0c040">
        <div class="feature-img-wrap"><svg viewBox="0 0 400 160" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
  <defs>
    <radialGradient id="bg4" cx="50%" cy="50%" r="70%"><stop offset="0%" stop-color="#141008"/><stop offset="100%" stop-color="#080c10"/></radialGradient>
    <radialGradient id="glow4" cx="50%" cy="60%" r="40%"><stop offset="0%" stop-color="#f0c040" stop-opacity="0.15"/><stop offset="100%" stop-color="transparent"/></radialGradient>
  </defs>
  <rect width="400" height="160" fill="url(#bg4)"/>
  <rect width="400" height="160" fill="url(#glow4)"/>
  <!-- Chest pixels (large center) -->
  <g transform="translate(164, 30)">
    <!-- Chest body -->
    <rect x="0" y="20" width="72" height="48" fill="#5c3a1e" stroke="#f0c040" stroke-width="1" stroke-opacity="0.6"/>
    <!-- Chest lid -->
    <rect x="0" y="8" width="72" height="14" fill="#6b4422" stroke="#f0c040" stroke-width="1" stroke-opacity="0.6"/>
    <!-- Chest top curve pixels -->
    <rect x="4" y="4" width="64" height="6" fill="#6b4422" stroke="#f0c040" stroke-width="0.5" stroke-opacity="0.4"/>
    <!-- Lock -->
    <rect x="30" y="26" width="12" height="10" fill="#f0c040" fill-opacity="0.8"/>
    <rect x="32" y="36" width="8" height="6" fill="#f0c040" fill-opacity="0.6"/>
    <!-- Stripes -->
    <rect x="0" y="19" width="72" height="2" fill="#f0c040" fill-opacity="0.4"/>
    <rect x="0" y="67" width="72" height="2" fill="#f0c040" fill-opacity="0.3"/>
  </g>
  <!-- Gold coins scattered -->
  <g fill="#f0c040">
    <rect x="100" y="72" width="12" height="12" fill-opacity="0.9" rx="2"/>
    <rect x="102" y="74" width="8" height="8" fill="#ffd700" fill-opacity="0.5"/>
    <text x="104" y="82" font-size="7" fill="#8b6000" font-family="monospace" font-weight="bold">G</text>
    
    <rect x="288" y="68" width="12" height="12" fill-opacity="0.9" rx="2"/>
    <rect x="290" y="70" width="8" height="8" fill="#ffd700" fill-opacity="0.5"/>
    <text x="292" y="78" font-size="7" fill="#8b6000" font-family="monospace" font-weight="bold">G</text>
    
    <rect x="112" y="92" width="10" height="10" fill-opacity="0.6" rx="1"/>
    <rect x="280" y="88" width="10" height="10" fill-opacity="0.7" rx="1"/>
    <rect x="130" y="108" width="8" height="8" fill-opacity="0.4" rx="1"/>
    <rect x="262" y="104" width="8" height="8" fill-opacity="0.5" rx="1"/>
    <rect x="84" y="108" width="8" height="8" fill-opacity="0.3" rx="1"/>
    <rect x="310" y="100" width="8" height="8" fill-opacity="0.35" rx="1"/>
  </g>
  <!-- XP bottles -->
  <g transform="translate(80, 50)">
    <rect x="0" y="12" width="10" height="16" fill="#00ff88" fill-opacity="0.6" rx="1"/>
    <rect x="2" y="8" width="6" height="6" fill="#00ff88" fill-opacity="0.5"/>
    <rect x="3" y="5" width="4" height="4" fill="#00d4ff" fill-opacity="0.6"/>
  </g>
  <g transform="translate(316, 46)">
    <rect x="0" y="12" width="10" height="16" fill="#00ff88" fill-opacity="0.5" rx="1"/>
    <rect x="2" y="8" width="6" height="6" fill="#00ff88" fill-opacity="0.4"/>
    <rect x="3" y="5" width="4" height="4" fill="#00d4ff" fill-opacity="0.5"/>
  </g>
  <!-- Ground -->
  <rect x="0" y="128" width="400" height="32" fill="#1a1408" fill-opacity="0.6"/>
</svg></div>
        <div class="feature-body"><div class="feature-title">Живая экономика</div><div class="feature-desc">Умные бочки-магазины, доска найма, торги между игроками, тендеры от Мэра.</div></div>
      </div>
      <div class="feature-card" style="--card-accent:#00ff88">
        <div class="feature-img-wrap"><svg viewBox="0 0 400 160" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
  <defs>
    <radialGradient id="bg5" cx="50%" cy="50%" r="70%"><stop offset="0%" stop-color="#0a1410"/><stop offset="100%" stop-color="#080c10"/></radialGradient>
    <radialGradient id="glow5" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#00ff88" stop-opacity="0.12"/><stop offset="100%" stop-color="transparent"/></radialGradient>
    <radialGradient id="sun" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#f0c040" stop-opacity="0.9"/><stop offset="100%" stop-color="#ff6b35" stop-opacity="0.6"/></radialGradient>
  </defs>
  <rect width="400" height="160" fill="url(#bg5)"/>
  <rect width="400" height="160" fill="url(#glow5)"/>
  <!-- Stars BG -->
  <circle cx="40" cy="20" r="1" fill="#fff" fill-opacity="0.3"/>
  <circle cx="80" cy="35" r="1.2" fill="#fff" fill-opacity="0.25"/>
  <circle cx="320" cy="18" r="1" fill="#fff" fill-opacity="0.3"/>
  <circle cx="360" cy="30" r="1.2" fill="#fff" fill-opacity="0.2"/>
  <circle cx="130" cy="15" r="0.8" fill="#fff" fill-opacity="0.2"/>
  <circle cx="270" cy="22" r="0.8" fill="#fff" fill-opacity="0.25"/>
  <!-- Sun/event beacon center -->
  <circle cx="200" cy="70" r="24" fill="url(#sun)" fill-opacity="0.85"/>
  <circle cx="200" cy="70" r="18" fill="#f0c040" fill-opacity="0.3"/>
  <!-- Rays -->
  <g stroke="#f0c040" stroke-width="2" stroke-opacity="0.5">
    <line x1="200" y1="36" x2="200" y2="28"/>
    <line x1="200" y1="104" x2="200" y2="112"/>
    <line x1="166" y1="70" x2="158" y2="70"/>
    <line x1="234" y1="70" x2="242" y2="70"/>
    <line x1="176" y1="46" x2="170" y2="40"/>
    <line x1="224" y1="94" x2="230" y2="100"/>
    <line x1="224" y1="46" x2="230" y2="40"/>
    <line x1="176" y1="94" x2="170" y2="100"/>
  </g>
  <!-- Lightning bolt pixel left -->
  <g fill="#00ff88" fill-opacity="0.8">
    <rect x="100" y="44" width="8" height="4"/>
    <rect x="104" y="48" width="8" height="4"/>
    <rect x="100" y="52" width="12" height="4"/>
    <rect x="104" y="56" width="8" height="4"/>
    <rect x="100" y="60" width="8" height="4"/>
  </g>
  <!-- Lightning bolt pixel right -->
  <g fill="#00ff88" fill-opacity="0.6">
    <rect x="296" y="44" width="8" height="4"/>
    <rect x="292" y="48" width="8" height="4"/>
    <rect x="288" y="52" width="12" height="4"/>
    <rect x="292" y="56" width="8" height="4"/>
    <rect x="296" y="60" width="8" height="4"/>
  </g>
  <!-- XP bar bottom -->
  <rect x="60" y="118" width="280" height="8" fill="#1a2a1a" rx="2"/>
  <rect x="60" y="118" width="196" height="8" fill="#00ff88" fill-opacity="0.6" rx="2"/>
  <rect x="60" y="118" width="196" height="3" fill="#00ff88" fill-opacity="0.4" rx="2"/>
  <!-- XP label -->
  <text x="265" y="126" font-size="9" fill="#00ff88" fill-opacity="0.7" font-family="monospace">XP</text>
  <!-- Ground -->
  <rect x="0" y="132" width="400" height="28" fill="#0d1a0d" fill-opacity="0.5"/>
</svg></div>
        <div class="feature-body"><div class="feature-title">Система ивентов</div><div class="feature-desc">Золотая Лихорадка, Коллапс, Жертвоприношение — мир живёт и меняется в реальном времени.</div></div>
      </div>
      <div class="feature-card" style="--card-accent:#ff4455">
        <div class="feature-img-wrap"><svg viewBox="0 0 400 160" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
  <defs>
    <radialGradient id="bg6" cx="50%" cy="50%" r="70%"><stop offset="0%" stop-color="#0e0810"/><stop offset="100%" stop-color="#080c10"/></radialGradient>
    <radialGradient id="glowL" cx="25%" cy="50%" r="40%"><stop offset="0%" stop-color="#00d4ff" stop-opacity="0.12"/><stop offset="100%" stop-color="transparent"/></radialGradient>
    <radialGradient id="glowR" cx="75%" cy="50%" r="40%"><stop offset="0%" stop-color="#ff4455" stop-opacity="0.12"/><stop offset="100%" stop-color="transparent"/></radialGradient>
  </defs>
  <rect width="400" height="160" fill="url(#bg6)"/>
  <rect width="400" height="160" fill="url(#glowL)"/>
  <rect width="400" height="160" fill="url(#glowR)"/>
  <!-- Dividing line -->
  <line x1="200" y1="0" x2="200" y2="160" stroke="#4a3060" stroke-width="1" stroke-opacity="0.5" stroke-dasharray="3 4"/>
  <!-- Left flag (blue) -->
  <rect x="68" y="24" width="4" height="80" fill="#4a6a8a"/>
  <polygon points="72,24 100,36 72,48" fill="#00d4ff" fill-opacity="0.8"/>
  <!-- Left fortress pixels -->
  <g fill="#0f1e2a" stroke="#00d4ff" stroke-width="0.8" stroke-opacity="0.5">
    <rect x="48" y="72" width="64" height="56"/>
    <rect x="44" y="60" width="16" height="16"/>
    <rect x="96" y="60" width="16" height="16"/>
    <rect x="66" y="60" width="12" height="12"/>
  </g>
  <!-- Left windows -->
  <rect x="60" y="84" width="8" height="8" fill="#00d4ff" fill-opacity="0.5"/>
  <rect x="76" y="84" width="8" height="8" fill="#00d4ff" fill-opacity="0.35"/>
  <rect x="92" y="84" width="8" height="8" fill="#00d4ff" fill-opacity="0.45"/>
  <rect x="68" y="100" width="24" height="28" fill="#00d4ff" fill-opacity="0.15"/>
  <!-- Right flag (red) -->
  <rect x="328" y="24" width="4" height="80" fill="#8a4a4a"/>
  <polygon points="328,24 300,36 328,48" fill="#ff4455" fill-opacity="0.8"/>
  <!-- Right fortress pixels -->
  <g fill="#1e0f0f" stroke="#ff4455" stroke-width="0.8" stroke-opacity="0.5">
    <rect x="288" y="72" width="64" height="56"/>
    <rect x="284" y="60" width="16" height="16"/>
    <rect x="336" y="60" width="16" height="16"/>
    <rect x="302" y="60" width="12" height="12"/>
  </g>
  <!-- Right windows -->
  <rect x="300" y="84" width="8" height="8" fill="#ff4455" fill-opacity="0.5"/>
  <rect x="316" y="84" width="8" height="8" fill="#ff4455" fill-opacity="0.35"/>
  <rect x="332" y="84" width="8" height="8" fill="#ff4455" fill-opacity="0.45"/>
  <rect x="308" y="100" width="24" height="28" fill="#ff4455" fill-opacity="0.1"/>
  <!-- Center VS -->
  <rect x="188" y="62" width="24" height="24" fill="#1a0f20" stroke="#7b2fff" stroke-width="1" stroke-opacity="0.6" rx="2"/>
  <text x="192" y="79" font-size="13" fill="#7b2fff" fill-opacity="0.9" font-family="monospace" font-weight="bold">VS</text>
  <!-- Cannonball trails -->
  <circle cx="150" cy="80" r="3" fill="#00d4ff" fill-opacity="0.4"/>
  <circle cx="165" cy="76" r="2.5" fill="#00d4ff" fill-opacity="0.3"/>
  <circle cx="178" cy="73" r="2" fill="#00d4ff" fill-opacity="0.2"/>
  <circle cx="250" cy="80" r="3" fill="#ff4455" fill-opacity="0.4"/>
  <circle cx="235" cy="76" r="2.5" fill="#ff4455" fill-opacity="0.3"/>
  <circle cx="222" cy="73" r="2" fill="#ff4455" fill-opacity="0.2"/>
</svg></div>
        <div class="feature-body"><div class="feature-title">Войны фракций</div><div class="feature-desc">Стройте города, создавайте союзы, объявляйте войны. Политика внутри Minecraft.</div></div>
      </div>
    </div>
  </div>
  <div class="socials-section">
    <div class="section-header">
      <div class="section-tag">Сообщество</div>
      <div class="section-title">Присоединяйся</div>
    </div>
    <div class="socials-grid">
      <a href="https://discord.gg/MY32B5hn3q" target="_blank" class="social-card discord">
        <div class="social-icon discord"><svg width="24" height="24" viewBox="0 0 24 24" fill="#5865F2"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057.1 18.08.112 18.1.132 18.11c2.053 1.508 4.041 2.423 5.993 3.03a.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994a.076.076 0 0 0-.041-.106 13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.892.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028c1.961-.607 3.95-1.522 6.002-3.03a.077.077 0 0 0 .032-.027c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.03z"/></svg></div>
        <div class="social-info"><div class="social-name">Discord</div><div class="social-desc">Основное сообщество</div></div>
        <div class="social-arrow">›</div>
      </a>
      <a href="https://t.me/BlissFullReloaded" target="_blank" class="social-card telegram">
        <div class="social-icon telegram"><svg width="24" height="24" viewBox="0 0 24 24" fill="#26A5E4"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg></div>
        <div class="social-info"><div class="social-name">Telegram</div><div class="social-desc">Новости и обновления</div></div>
        <div class="social-arrow">›</div>
      </a>
      <a href="https://www.tiktok.com/@jayrest29" target="_blank" class="social-card tiktok">
        <div class="social-icon tiktok"><svg width="24" height="18" viewBox="0 0 24 24" fill="#fff"><path d="M19.59 6.69a4.83 4.83 0 01-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 01-2.88 2.5 2.89 2.89 0 01-2.89-2.89 2.89 2.89 0 012.89-2.89c.28 0 .54.04.79.1V9.01a6.27 6.27 0 00-.79-.05 6.34 6.34 0 00-6.34 6.34 6.34 6.34 0 006.34 6.34 6.34 6.34 0 006.33-6.34V8.69a8.18 8.18 0 004.78 1.52V6.75a4.85 4.85 0 01-1.01-.06z"/></svg></div>
        <div class="social-info"><div class="social-name">TikTok</div><div class="social-desc">Видео с сервера</div></div>
        <div class="social-arrow">›</div>
      </a>
    </div>
  </div>
</div>

<div id="docs" class="page">
  <div class="docs-admin-bar" id="docsAdminBar" style="display:none">
    <div class="admin-bar-text">⚙️ Редактирование документации</div>
    <div style="display:flex;gap:8px">
      <button class="btn-add-news" onclick="openAddDoc()">+ Добавить раздел</button>
    </div>
  </div>
  <div class="docs-layout">
    <aside class="docs-sidebar" id="docsSidebar"></aside>
    <div class="docs-content" id="docsContent"></div>
  </div>
</div>

<div id="news" class="page">
  <div class="news-header">
    <h1>Новости и обновления</h1>
    <p>Следи за развитием сервера — новые механики, события и анонсы</p>
  </div>
  <div class="admin-bar" id="adminBar" style="display:none">
    <div class="admin-bar-text">⚙️ Режим администратора</div>
    <div style="display:flex;gap:8px">
      <button class="btn-add-news" onclick="openAddNews()">+ Добавить новость</button>
      <button class="btn-logout" onclick="adminLogout()">Выйти</button>
    </div>
  </div>
  <div class="news-container">
    <div class="news-list" id="newsList"></div>
    <div class="news-sidebar">
      <div class="sidebar-widget">
        <div class="widget-title">Статус сервера</div>
        <div class="server-status">
          <div class="status-indicator"><div class="status-dot loading" id="sidebar-dot"></div><span id="sidebar-status-text">Проверка...</span></div>
          <div class="version-tag" id="sidebar-version">1.21.x</div>
        </div>
        <div style="margin:8px 0 4px">
          <div class="players-online" id="sidebar-players">—</div>
          <div class="players-label">игроков в сети <span class="players-max" id="sidebar-max"></span></div>
        </div>
        <div class="server-ip" onclick="copyIP()">blissfull.mc-server.net:25816</div>
      </div>
      <div class="sidebar-widget">
        <div class="widget-title">Последние изменения</div>
        <div class="changelog-list">
          <div class="changelog-item"><div class="changelog-version">v1.7</div><div class="changelog-text">SmartBarrel — уникальный режим магазина</div></div>
          <div class="changelog-item"><div class="changelog-version">v2.0</div><div class="changelog-text">EternalBorder — стабильный релиз</div></div>
          <div class="changelog-item"><div class="changelog-version">v1.2</div><div class="changelog-text">TradeExperience — интеграция с EternalBorder</div></div>
          <div class="changelog-item"><div class="changelog-version">v1.5</div><div class="changelog-text">SmartBarrel — защита от взрывов</div></div>
        </div>
      </div>
      <div class="sidebar-widget">
        <div class="widget-title">Сообщество</div>
        <div style="display:flex;flex-direction:column;gap:10px">
          <a href="https://discord.gg/MY32B5hn3q" target="_blank" style="display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--text2);font-size:13px;padding:10px;background:rgba(88,101,242,0.08);border:1px solid rgba(88,101,242,0.2);border-radius:6px;transition:all 0.2s" onmouseover="this.style.background='rgba(88,101,242,0.15)'" onmouseout="this.style.background='rgba(88,101,242,0.08)'"><span style="font-size:18px">💬</span> Discord сервер</a>
          <a href="https://t.me/BlissFullReloaded" target="_blank" style="display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--text2);font-size:13px;padding:10px;background:rgba(38,165,228,0.08);border:1px solid rgba(38,165,228,0.2);border-radius:6px;transition:all 0.2s" onmouseover="this.style.background='rgba(38,165,228,0.15)'" onmouseout="this.style.background='rgba(38,165,228,0.08)'"><span style="font-size:18px">✈️</span> Telegram канал</a>
          <a href="https://www.tiktok.com/@jayrest29" target="_blank" style="display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--text2);font-size:13px;padding:10px;background:rgba(255,0,80,0.06);border:1px solid rgba(255,0,80,0.15);border-radius:6px;transition:all 0.2s" onmouseover="this.style.background='rgba(255,0,80,0.12)'" onmouseout="this.style.background='rgba(255,0,80,0.06)'"><span style="font-size:18px">🎵</span> TikTok</a>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
  const AUTH_URL = '/auth';
  const NEWS_URL = '/api/news';
  const DOCS_URL = '/api/docs';
  const TYPE_LABELS = { update:'Обновление', event:'Событие', announce:'Анонс', fix:'Фикс', info:'Инфо' };

  let isAdmin = false, editingId = null, cachedNews = [];
  let cachedDocs = [], editingDocId = null, currentDocId = null;

  // ── NEWS ──────────────────────────────────────────────────────────────
  async function fetchNews() {
    try { const r = await fetch(NEWS_URL); cachedNews = await r.json(); }
    catch(e) { cachedNews = []; }
    renderNews();
  }

  function renderNews() {
    const c = document.getElementById('newsList');
    if (!c) return;
    c.innerHTML = cachedNews.map(n => `
      <div class="news-card type-${n.type}" id="nc-${n.id}">
        <div class="news-meta">
          <span class="news-type">${escHtml(n.typeLabel || TYPE_LABELS[n.type] || n.type)}</span>
          <span class="news-date">${escHtml(n.date)}</span>
        </div>
        <h2>${escHtml(n.title)}</h2>
        <p>${escHtml(n.text).replace(/\n/g, '<br>')}</p>
        <div class="news-tags">${(n.tags||[]).map(t=>`<span class="news-tag">${escHtml(t)}</span>`).join('')}</div>
        ${isAdmin ? `<div class="news-actions">
          <button class="btn-edit" onclick="openEditNews(${n.id})">✏️ Редактировать</button>
          <button class="btn-danger" onclick="deleteNews(${n.id})">🗑 Удалить</button>
        </div>` : ''}
      </div>`).join('');
  }

  function escHtml(s) {
    return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }

  // ── DOCS ──────────────────────────────────────────────────────────────
  async function fetchDocs() {
    try { const r = await fetch(DOCS_URL); cachedDocs = await r.json(); }
    catch(e) { cachedDocs = []; }
    renderDocs();
  }

  function renderDocs() {
    renderDocsSidebar();
    // Show first or currently active
    if (cachedDocs.length > 0) {
      const target = currentDocId && cachedDocs.find(d => d.id === currentDocId)
        ? currentDocId : cachedDocs[0].id;
      showDocById(target, false);
    } else {
      document.getElementById('docsContent').innerHTML =
        '<div style="padding:48px 60px;color:var(--text3);font-size:15px;">Разделы ещё не добавлены.</div>';
    }
  }

  function renderDocsSidebar() {
    const sidebar = document.getElementById('docsSidebar');
    if (!sidebar) return;

    // Group by category
    const categories = {};
    cachedDocs.forEach(d => {
      const cat = d.category || 'Общее';
      if (!categories[cat]) categories[cat] = [];
      categories[cat].push(d);
    });

    sidebar.innerHTML = Object.entries(categories).map(([cat, docs]) => `
      <div class="sidebar-section">
        <div class="sidebar-section-title">${escHtml(cat)}</div>
        ${docs.map(d => `
          <a class="sidebar-link${currentDocId === d.id ? ' active' : ''}"
             onclick="showDocById(${d.id})">${escHtml(d.title)}</a>
        `).join('')}
      </div>
    `).join('');
  }

  function showDocById(id, updateSidebar = true) {
    currentDocId = id;
    const doc = cachedDocs.find(d => d.id === id);
    if (!doc) return;

    const content = document.getElementById('docsContent');
    content.innerHTML = `
      <div class="doc-section active">
        <h1>${escHtml(doc.title)}</h1>
        ${doc.lead ? `<p class="doc-lead">${escHtml(doc.lead)}</p>` : ''}
        <div class="doc-body">${renderDocBody(doc.body || '')}</div>
        ${isAdmin ? `
          <div class="doc-section-actions">
            <button class="btn-edit" onclick="openEditDoc(${doc.id})">✏️ Редактировать</button>
            <button class="btn-danger" onclick="deleteDoc(${doc.id})">🗑 Удалить</button>
            <button class="doc-order-btn" onclick="moveDoc(${doc.id}, -1)">↑ Выше</button>
            <button class="doc-order-btn" onclick="moveDoc(${doc.id}, 1)">↓ Ниже</button>
          </div>` : ''}
      </div>`;

    if (updateSidebar) renderDocsSidebar();
  }

  function renderDocBody(text) {
    // Simple markdown-like renderer for doc body
    // Supports: ## headings, bullet lists (- item), blank lines as paragraphs
    if (!text) return '';
    const lines = text.split('\n');
    let html = '';
    let inList = false;

    lines.forEach(line => {
      const safe = escHtml(line);
      if (line.startsWith('## ')) {
        if (inList) { html += '</ul>'; inList = false; }
        html += `<h2>${escHtml(line.slice(3))}</h2>`;
      } else if (line.startsWith('- ')) {
        if (!inList) { html += '<ul>'; inList = true; }
        html += `<li>${escHtml(line.slice(2))}</li>`;
      } else if (line.trim() === '') {
        if (inList) { html += '</ul>'; inList = false; }
      } else {
        if (inList) { html += '</ul>'; inList = false; }
        html += `<p>${safe}</p>`;
      }
    });
    if (inList) html += '</ul>';
    return html;
  }

  function openAddDoc() {
    editingDocId = null;
    document.getElementById('docFormModalTitle').textContent = '➕ Добавить раздел';
    document.getElementById('docFormCategory').value = '';
    document.getElementById('docFormTitle').value = '';
    document.getElementById('docFormLead').value = '';
    document.getElementById('docFormBody').value = '';
    document.getElementById('docModal').classList.add('open');
    document.getElementById('docFormTitle').focus();
  }

  function openEditDoc(id) {
    const doc = cachedDocs.find(d => d.id === id);
    if (!doc) return;
    editingDocId = id;
    document.getElementById('docFormModalTitle').textContent = '✏️ Редактировать раздел';
    document.getElementById('docFormCategory').value = doc.category || '';
    document.getElementById('docFormTitle').value = doc.title || '';
    document.getElementById('docFormLead').value = doc.lead || '';
    document.getElementById('docFormBody').value = doc.body || '';
    document.getElementById('docModal').classList.add('open');
  }

  function closeDocModal() { document.getElementById('docModal').classList.remove('open'); }

  async function saveDocForm() {
    const category = document.getElementById('docFormCategory').value.trim();
    const title    = document.getElementById('docFormTitle').value.trim();
    const lead     = document.getElementById('docFormLead').value.trim();
    const body     = document.getElementById('docFormBody').value; // preserve newlines
    if (!title) { alert('Введите заголовок раздела.'); return; }
    const payload = { category: category || 'Общее', title, lead, body };
    try {
      const r = editingDocId !== null
        ? await fetch(`${DOCS_URL}/${editingDocId}`, {method:'PUT', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload)})
        : await fetch(DOCS_URL, {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload)});
      if (r.ok) {
        const saved = await r.json();
        if (editingDocId === null && saved.item) currentDocId = saved.item.id;
        closeDocModal();
        await fetchDocs();
      } else alert('Ошибка сохранения');
    } catch(e) { alert('Ошибка соединения'); }
  }

  async function deleteDoc(id) {
    if (!confirm('Удалить этот раздел?')) return;
    try {
      const r = await fetch(`${DOCS_URL}/${id}`, {method:'DELETE'});
      if (r.ok) {
        if (currentDocId === id) currentDocId = null;
        await fetchDocs();
      }
    } catch(e) { alert('Ошибка удаления'); }
  }

  async function moveDoc(id, dir) {
    try {
      const r = await fetch(`${DOCS_URL}/${id}/move`, {
        method:'POST', headers:{'Content-Type':'application/json'},
        body: JSON.stringify({direction: dir})
      });
      if (r.ok) await fetchDocs();
    } catch(e) {}
  }

  // ── AUTH ──────────────────────────────────────────────────────────────
  function openAdminLogin() {
    document.getElementById('adminLoginModal').classList.add('open');
    document.getElementById('adminPassInput').value = '';
    document.getElementById('adminPassInput').focus();
    document.getElementById('adminLoginError').style.display = 'none';
  }
  function closeAdminLogin() { document.getElementById('adminLoginModal').classList.remove('open'); }

  async function doAdminLogin() {
    const val = document.getElementById('adminPassInput').value;
    if (!val) return;
    const btn = document.querySelector('#adminLoginModal .btn-submit');
    const err = document.getElementById('adminLoginError');
    btn.textContent = 'Проверка...'; btn.disabled = true; err.style.display = 'none';
    try {
      const r = await fetch(AUTH_URL, { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({password:val}) });
      const d = await r.json();
      if (d.ok) {
        isAdmin = true; closeAdminLogin();
        document.getElementById('adminBar').style.display = '';
        document.getElementById('docsAdminBar').style.display = '';
        renderNews();
        renderDocs();
      } else {
        err.textContent = r.status === 429 ? 'Слишком много попыток, подожди минуту' : 'Неверный пароль';
        err.style.display = 'block';
        document.getElementById('adminPassInput').value = '';
        document.getElementById('adminPassInput').focus();
      }
    } catch(e) { err.textContent = 'Ошибка соединения'; err.style.display = 'block'; }
    finally { btn.textContent = 'Войти'; btn.disabled = false; }
  }

  function adminLogout() {
    isAdmin = false;
    document.getElementById('adminBar').style.display = 'none';
    document.getElementById('docsAdminBar').style.display = 'none';
    renderNews();
    renderDocs();
  }

  // ── NEWS MODALS ───────────────────────────────────────────────────────
  function openAddNews() {
    editingId = null;
    document.getElementById('newsFormTitle').textContent = '➕ Добавить новость';
    document.getElementById('newsFormType').value = 'update';
    document.getElementById('newsFormDate').value = new Date().toLocaleDateString('ru-RU');
    document.getElementById('newsFormTitle2').value = '';
    document.getElementById('newsFormText').value = '';
    document.getElementById('newsFormTags').value = '';
    document.getElementById('newsModal').classList.add('open');
  }

  function openEditNews(id) {
    const item = cachedNews.find(n => n.id === id);
    if (!item) return;
    editingId = id;
    document.getElementById('newsFormTitle').textContent = '✏️ Редактировать новость';
    document.getElementById('newsFormType').value = item.type;
    document.getElementById('newsFormDate').value = item.date;
    document.getElementById('newsFormTitle2').value = item.title;
    document.getElementById('newsFormText').value = item.text;
    document.getElementById('newsFormTags').value = (item.tags||[]).join(', ');
    document.getElementById('newsModal').classList.add('open');
  }

  function closeNewsModal() { document.getElementById('newsModal').classList.remove('open'); }

  async function saveNewsForm() {
    const type  = document.getElementById('newsFormType').value;
    const date  = document.getElementById('newsFormDate').value.trim();
    const title = document.getElementById('newsFormTitle2').value.trim();
    const text  = document.getElementById('newsFormText').value;
    const tags  = document.getElementById('newsFormTags').value.trim().split(',').map(t=>t.trim()).filter(Boolean);
    if (!title || !text.trim()) { alert('Заполните заголовок и текст.'); return; }
    const payload = { type, typeLabel: TYPE_LABELS[type]||type, date, title, text, tags };
    try {
      const r = editingId !== null
        ? await fetch(`${NEWS_URL}/${editingId}`, {method:'PUT', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload)})
        : await fetch(NEWS_URL, {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload)});
      if (r.ok) { closeNewsModal(); await fetchNews(); }
      else alert('Ошибка сохранения');
    } catch(e) { alert('Ошибка соединения'); }
  }

  async function deleteNews(id) {
    if (!confirm('Удалить эту новость?')) return;
    try { const r = await fetch(`${NEWS_URL}/${id}`, {method:'DELETE'}); if (r.ok) await fetchNews(); }
    catch(e) { alert('Ошибка удаления'); }
  }

  // ── PAGE / DOC NAVIGATION ─────────────────────────────────────────────
  function showPage(id) {
    document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.nav-links a').forEach(a => a.classList.remove('active'));
    document.getElementById(id).classList.add('active');
    document.getElementById('nav-' + id).classList.add('active');
    window.scrollTo(0, 0);
    if (id === 'news') fetchNews();
    if (id === 'docs') fetchDocs();
  }

  function copyIP() {
    navigator.clipboard.writeText('blissfull.mc-server.net:25816').catch(()=>{});
    const t = document.getElementById('copyToast');
    t.classList.add('show');
    setTimeout(() => t.classList.remove('show'), 2000);
  }

  // ── SERVER STATUS ─────────────────────────────────────────────────────
  async function fetchServerStatus() {
    try {
      const r = await fetch('/api/status');
      updateServerUI(r.ok ? await r.json() : null);
    } catch(e) { updateServerUI(null); }
  }

  function updateServerUI(data) {
    const online = data && data.online;
    const players = online ? (data.players_online ?? 0) : 0;
    const max     = online ? (data.players_max    ?? 0) : 0;
    const version = (online && data.version) ? data.version : '1.21.x';
    const badge = document.querySelector('.hero-badge');
    if (badge) {
      badge.innerHTML = online
        ? '<span style="width:6px;height:6px;background:var(--green);border-radius:50%;animation:pulse 2s infinite;display:inline-block"></span> Сервер онлайн'
        : '<span style="width:6px;height:6px;background:var(--red);border-radius:50%;display:inline-block"></span> Сервер офлайн';
      badge.style.borderColor = online ? 'rgba(0,255,136,0.25)' : 'rgba(255,68,85,0.25)';
      badge.style.background  = online ? 'rgba(0,255,136,0.08)' : 'rgba(255,68,85,0.08)';
    }
    const hp = document.getElementById('hero-players'), hs = document.getElementById('hero-status'), hv = document.getElementById('hero-version');
    if (hp) { hp.textContent = online ? players : '—'; hp.style.color = online ? 'var(--green)' : 'var(--red)'; }
    if (hs) { hs.textContent = online ? 'Онлайн' : 'Офлайн'; hs.style.color = online ? 'var(--green)' : 'var(--red)'; }
    if (hv) hv.textContent = version;
    const dot = document.getElementById('sidebar-dot');
    const st = document.getElementById('sidebar-status-text');
    const sp = document.getElementById('sidebar-players');
    const sm = document.getElementById('sidebar-max');
    const sv = document.getElementById('sidebar-version');
    if (dot) dot.className = 'status-dot' + (online ? '' : ' offline');
    if (st)  st.textContent = online ? 'Онлайн' : 'Офлайн';
    if (sp)  { sp.textContent = online ? players : '—'; sp.style.color = online ? 'var(--green)' : 'var(--red)'; }
    if (sm)  sm.textContent = online && max ? `/ ${max}` : '';
    if (sv)  sv.textContent = version;
  }

  // ── INIT ──────────────────────────────────────────────────────────────
  fetchNews();
  fetchDocs();
  fetchServerStatus();
  setInterval(fetchServerStatus, 10000);
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      document.getElementById('newsModal').classList.remove('open');
      document.getElementById('adminLoginModal').classList.remove('open');
      document.getElementById('docModal').classList.remove('open');
    }
  });
</script>

<button class="admin-fab" onclick="openAdminLogin()" title="Войти как администратор">⚙️</button>

<div class="modal-overlay" id="adminLoginModal">
  <div class="modal-box" style="max-width:380px">
    <div class="modal-title">🔒 Вход для администратора</div>
    <button class="modal-close" onclick="closeAdminLogin()">✕</button>
    <div class="form-group">
      <label class="form-label">Пароль</label>
      <input type="password" class="form-input" id="adminPassInput" placeholder="Введите пароль" onkeydown="if(event.key==='Enter')doAdminLogin()">
    </div>
    <div id="adminLoginError" style="display:none;color:var(--red);font-size:13px;margin-bottom:12px;">Неверный пароль</div>
    <button class="btn-submit" onclick="doAdminLogin()">Войти</button>
  </div>
</div>

<div class="modal-overlay" id="newsModal">
  <div class="modal-box">
    <div class="modal-title" id="newsFormTitle">➕ Добавить новость</div>
    <button class="modal-close" onclick="closeNewsModal()">✕</button>
    <div class="form-group">
      <label class="form-label">Тип</label>
      <select class="form-select" id="newsFormType">
        <option value="update">Обновление</option>
        <option value="announce">Анонс</option>
        <option value="event">Событие</option>
        <option value="fix">Фикс</option>
        <option value="info">Инфо</option>
      </select>
    </div>
    <div class="form-group">
      <label class="form-label">Дата</label>
      <input type="text" class="form-input" id="newsFormDate" placeholder="ДД.ММ.ГГГГ">
    </div>
    <div class="form-group">
      <label class="form-label">Заголовок</label>
      <input type="text" class="form-input" id="newsFormTitle2" placeholder="Название новости">
    </div>
    <div class="form-group">
      <label class="form-label">Текст (Enter = новая строка, пробелы сохраняются)</label>
      <textarea class="form-textarea" id="newsFormText" placeholder="Описание обновления..."></textarea>
    </div>
    <div class="form-group">
      <label class="form-label">Теги (через запятую)</label>
      <input type="text" class="form-tags-input" id="newsFormTags" placeholder="Тег1, Тег2, Тег3">
    </div>
    <button class="btn-submit" onclick="saveNewsForm()">💾 Сохранить</button>
  </div>
</div>


<div class="modal-overlay" id="docModal">
  <div class="modal-box" style="max-width:680px">
    <div class="modal-title" id="docFormModalTitle">➕ Добавить раздел</div>
    <button class="modal-close" onclick="closeDocModal()">✕</button>
    <div class="form-group">
      <label class="form-label">Категория в сайдбаре</label>
      <input type="text" class="form-input" id="docFormCategory" placeholder="Например: Мир, Общество, Справочник">
    </div>
    <div class="form-group">
      <label class="form-label">Заголовок раздела</label>
      <input type="text" class="form-input" id="docFormTitle" placeholder="Название раздела">
    </div>
    <div class="form-group">
      <label class="form-label">Подзаголовок (lead)</label>
      <input type="text" class="form-input" id="docFormLead" placeholder="Краткое описание раздела под заголовком">
    </div>
    <div class="form-group">
      <label class="form-label" style="margin-bottom:4px">Содержимое раздела</label>
      <div style="font-size:11px;color:var(--text3);margin-bottom:6px;line-height:1.6;">
        Поддерживается простая разметка:<br>
        <code>## Заголовок</code> — подзаголовок h2<br>
        <code>- Пункт</code> — элемент списка<br>
        Обычный текст — параграф. Enter = новая строка.
      </div>
      <textarea class="form-textarea" id="docFormBody" placeholder="## Основные правила&#10;- Пункт первый&#10;- Пункт второй&#10;&#10;Обычный текст параграфа." style="min-height:200px;font-family:monospace;font-size:13px;tab-size:2;white-space:pre"></textarea>
    </div>
    <button class="btn-submit" onclick="saveDocForm()">💾 Сохранить раздел</button>
  </div>
</div>

</body>
</html>
