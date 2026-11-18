# -*- coding: utf-8 -*-
"""
Generador de Presentación Interactiva Estilo @trazomedico (Morph 3D Limpio y Elegante)
Proyecto: Sistema de información con drones inteligentes para detección temprana de
          incendios forestales y deforestación en La Libertad 2026
Universidad César Vallejo · Ingeniería de Sistemas · TIF Nivel I
Autor: César Quiroz
"""
import base64
import os
import re

base_dir = r"c:\Users\ASUS\Documents\lector_pdf_android_pc\presentacion_interactiva"
html_path = os.path.join(base_dir, "index.html")
portable_path = r"c:\Users\ASUS\Documents\lector_pdf_android_pc\presentacion_drones_ucv_2026_portable.html"

html_content = """<!DOCTYPE html>
<!--
  Presentación Interactiva con Transiciones Morph 3D (Estilo Minimalista de Alto Impacto)
  Sistema de información con drones inteligentes para detección temprana de incendios
  forestales y deforestación en La Libertad 2026
  Universidad César Vallejo · Escuela Profesional de Ingeniería de Sistemas · TIF Nivel I
  Autor: César Quiroz
-->
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="author" content="Autor: César Quiroz" />
  <title>Drones Inteligentes · La Libertad 2026 | UCV Ingeniería de Sistemas</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Antonio:wght@600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">

  <style>
    /* ==========================================================================
       Sistema de Diseño Minimalista y Transiciones Morph (@trazomedico style)
       Autor: César Quiroz
       ========================================================================== */
    :root {
      --morph-ease: cubic-bezier(0.22, 1, 0.36, 1);
    }

    * {
      box-sizing: border-box;
      user-select: none;
    }

    body {
      margin: 0;
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      background-color: #060d09;
      color: #ffffff;
      font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Tipografía condensada de alto impacto para títulos (idéntica al video de referencia) */
    .title-condensed {
      font-family: 'Antonio', sans-serif;
      letter-spacing: 0.02em;
      text-transform: uppercase;
      line-height: 1.02;
    }

    .font-mono-code {
      font-family: 'JetBrains Mono', monospace;
    }

    /* ==========================================================================
       FONDO AMBIENTAL CON PARTÍCULAS SUAVES Y VIÑETA OSCURA LIMPIA
       ========================================================================== */
    #ambientBg {
      position: fixed;
      inset: 0;
      z-index: 0;
      background:
        radial-gradient(circle at 50% 50%, rgba(16, 185, 129, 0.14) 0%, rgba(6, 13, 9, 0.94) 68%, #040906 100%);
      transition: background 1.2s var(--morph-ease);
    }

    #bgPhotoLayer {
      position: fixed;
      inset: -5%;
      width: 110%;
      height: 110%;
      object-fit: cover;
      opacity: 0.14;
      filter: blur(18px) brightness(0.45) saturate(1.4);
      transform: scale(1.08);
      transition: opacity 1.2s var(--morph-ease), transform 1.8s var(--morph-ease);
      z-index: 1;
      pointer-events: none;
    }

    /* ==========================================================================
       OBJETO 3D PERSISTENTE QUE VIAJA Y SE TRANSFORMA ENTRE DIAPOSITIVAS
       (Como el corazón 3D en el video de referencia)
       ========================================================================== */
    #persistentHero3D {
      position: fixed;
      z-index: 5;
      width: 470px;
      height: 470px;
      left: 50%;
      top: 52%;
      transform: translate3d(-50%, -50%, 0) scale(1);
      transition:
        left 1.15s var(--morph-ease),
        top 1.15s var(--morph-ease),
        transform 1.15s var(--morph-ease),
        opacity 1.05s var(--morph-ease),
        filter 1.15s var(--morph-ease);
      pointer-events: none;
    }

    /* Posiciones Morph del Objeto 3D según la escena */
    body[data-hero-pos="center"] #persistentHero3D {
      left: 50%;
      top: 56%;
      transform: translate3d(-50%, -50%, 0) scale(1.05);
      opacity: 1;
      filter: blur(0px) drop-shadow(0 0 65px rgba(16, 185, 129, 0.45));
    }

    body[data-hero-pos="bg-blur"] #persistentHero3D {
      left: 58%;
      top: 52%;
      transform: translate3d(-50%, -50%, 0) scale(1.45);
      opacity: 0.22;
      filter: blur(6px) drop-shadow(0 0 80px rgba(249, 115, 22, 0.35));
    }

    body[data-hero-pos="right"] #persistentHero3D {
      left: 79%;
      top: 53%;
      transform: translate3d(-50%, -50%, 0) scale(1.08);
      opacity: 0.96;
      filter: blur(0px) drop-shadow(0 0 60px rgba(16, 185, 129, 0.45));
    }

    body[data-hero-pos="left"] #persistentHero3D {
      left: 22%;
      top: 53%;
      transform: translate3d(-50%, -50%, 0) scale(1.1);
      opacity: 0.96;
      filter: blur(0px) drop-shadow(0 0 60px rgba(249, 115, 22, 0.45));
    }

    body[data-hero-pos="right-edge"] #persistentHero3D {
      left: 88%;
      top: 54%;
      transform: translate3d(-50%, -50%, 0) scale(1.18);
      opacity: 0.92;
      filter: blur(0px) drop-shadow(0 0 60px rgba(16, 185, 129, 0.4));
    }

    body[data-hero-pos="bottom-left"] #persistentHero3D {
      left: 16%;
      top: 82%;
      transform: translate3d(-50%, -50%, 0) scale(0.95);
      opacity: 0.85;
      filter: blur(1px) drop-shadow(0 0 50px rgba(16, 185, 129, 0.45));
    }

    /* Animación interna de flotación suave del Objeto 3D */
    @keyframes float3D {
      0%, 100% { transform: translateY(0px) rotate(0deg); }
      50%      { transform: translateY(-14px) rotate(1.5deg); }
    }

    .hero-inner-float {
      width: 100%;
      height: 100%;
      animation: float3D 5.5s ease-in-out infinite;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    /* ==========================================================================
       TRANSICIÓN DE ESCENAS CON ENTRADA Y SALIDA MORPH SUAVE
       ========================================================================== */
    .scene {
      position: absolute;
      inset: 0;
      padding: 4.5rem 5.5rem;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      pointer-events: none;
      transform: translate3d(0, 36px, 0) scale(0.97);
      transition:
        opacity 0.85s var(--morph-ease),
        transform 0.95s var(--morph-ease);
      z-index: 10;
    }

    .scene.active {
      opacity: 1;
      pointer-events: auto;
      transform: translate3d(0, 0, 0) scale(1);
    }

    .scene.prev {
      opacity: 0;
      transform: translate3d(-48px, 0, 0) scale(0.96);
    }

    /* Elementos internos escalonados */
    .stagger {
      opacity: 0;
      transform: translate3d(0, 28px, 0);
      transition: opacity 0.8s var(--morph-ease), transform 0.9s var(--morph-ease);
    }

    .scene.active .stagger {
      opacity: 1;
      transform: translate3d(0, 0, 0);
    }

    .scene.active .d-1 { transition-delay: 0.08s; }
    .scene.active .d-2 { transition-delay: 0.16s; }
    .scene.active .d-3 { transition-delay: 0.24s; }
    .scene.active .d-4 { transition-delay: 0.32s; }
    .scene.active .d-5 { transition-delay: 0.40s; }

    /* ==========================================================================
       COMPONENTES VISUALES IDÉNTICOS AL VIDEO DE REFERENCIA (@trazomedico)
       ========================================================================== */
    /* 1. Tarjetas sólidas con icono circular flotando arriba (00:06 y 00:22) */
    .risk-card {
      position: relative;
      padding: 3.2rem 1.4rem 1.8rem;
      border-radius: 1.35rem;
      text-align: center;
      box-shadow: 0 22px 45px rgba(0, 0, 0, 0.45);
      transition: transform 0.4s var(--morph-ease), box-shadow 0.4s ease;
    }
    .risk-card:hover {
      transform: translateY(-8px);
    }
    .risk-card-icon {
      position: absolute;
      top: -34px;
      left: 50%;
      transform: translateX(-50%);
      width: 68px;
      height: 68px;
      border-radius: 9999px;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 4px solid #060d09;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.45);
    }

    /* 2. Barras horizontales con borde luminoso (00:08) */
    .glow-bar {
      background: rgba(255, 255, 255, 0.05);
      backdrop-filter: blur(16px);
      border: 1.5px solid rgba(52, 211, 153, 0.55);
      border-radius: 1rem;
      padding: 1.05rem 1.5rem;
      box-shadow: 0 0 28px rgba(16, 185, 129, 0.14);
      transition: transform 0.35s var(--morph-ease), border-color 0.35s ease, background 0.35s ease;
    }
    .glow-bar:hover {
      transform: translateX(8px);
      background: rgba(16, 185, 129, 0.14);
      border-color: #34d399;
    }

    /* 3. Tarjetas blancas limpias con chapita numerada en la esquina (00:11) */
    .white-step-card {
      position: relative;
      background: #f4f7f5;
      color: #0f172a;
      border-radius: 1.35rem;
      padding: 1.65rem 1.85rem;
      box-shadow: 0 25px 55px rgba(0, 0, 0, 0.55);
    }
    .step-badge {
      position: absolute;
      top: -16px;
      width: 38px;
      height: 38px;
      border-radius: 0.75rem;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 1rem;
      color: #fff;
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.35);
    }

    /* 4. Tarjetas píldora 2x2 con medallón circular lateral (00:13) */
    .entry-pill-card {
      position: relative;
      background: #f4f7f5;
      color: #0f172a;
      border-radius: 1.25rem;
      padding: 1.25rem 4.2rem 1.25rem 1.4rem;
      box-shadow: 0 18px 40px rgba(0, 0, 0, 0.45);
      transition: transform 0.35s var(--morph-ease);
    }
    .entry-pill-card:hover {
      transform: scale(1.03);
    }
    .entry-medallion {
      position: absolute;
      right: -18px;
      top: 50%;
      transform: translateY(-50%);
      width: 66px;
      height: 66px;
      border-radius: 9999px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
    }

    /* 5. Tarjetas de carrusel de cristal esmerilado con foto e icono superior (00:17 y 00:24) */
    .frost-carousel-card {
      background: rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(22px);
      -webkit-backdrop-filter: blur(22px);
      border: 1.5px solid rgba(255, 255, 255, 0.25);
      border-radius: 1.6rem;
      padding: 1.35rem;
      box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5);
      transition: transform 0.45s var(--morph-ease), border-color 0.35s ease;
    }
    .frost-carousel-card:hover {
      transform: translateY(-8px) scale(1.02);
      border-color: #34d399;
    }

    /* Barras de progreso animadas */
    .bar-fill {
      width: 0%;
      transition: width 1.35s var(--morph-ease);
    }
  </style>
</head>
<body data-hero-pos="center">

  <!-- ==========================================================================
       FONDO AMBIENTAL + CANVAS DE PARTÍCULAS BIOLÓGICAS / FORESTALES 3D
       ========================================================================== -->
  <div id="ambientBg"></div>
  <img id="bgPhotoLayer" src="./assets/image1.png" alt="Fondo ambiental" />
  <canvas id="bokehCanvas" class="fixed inset-0 z-[2] pointer-events-none"></canvas>

  <!-- ==========================================================================
       OBJETO 3D PERSISTENTE QUE VIAJA ENTRE ESCENAS (DRON + NÚCLEO FORESTAL 3D)
       ========================================================================== -->
  <div id="persistentHero3D">
    <div class="hero-inner-float">
      <!-- Halo luminoso volumétrico detrás del objeto -->
      <div id="heroGlowRing" class="absolute inset-8 rounded-full bg-gradient-to-tr from-emerald-500/35 via-teal-400/20 to-orange-500/30 blur-2xl animate-pulse"></div>

      <!-- Anillo orbital técnico SVG -->
      <svg class="absolute inset-2 w-[96%] h-[96%] opacity-55" viewBox="0 0 200 200" fill="none">
        <circle cx="100" cy="100" r="92" stroke="url(#gradOrb)" stroke-width="1.2" stroke-dasharray="8 6">
          <animateTransform attributeName="transform" type="rotate" from="0 100 100" to="360 100 100" dur="26s" repeatCount="indefinite"/>
        </circle>
        <circle cx="100" cy="100" r="76" stroke="rgba(249,115,22,0.45)" stroke-width="1" stroke-dasharray="4 8">
          <animateTransform attributeName="transform" type="rotate" from="360 100 100" to="0 100 100" dur="18s" repeatCount="indefinite"/>
        </circle>
        <defs>
          <linearGradient id="gradOrb" x1="0" y1="0" x2="200" y2="200">
            <stop offset="0%" stop-color="#34d399"/>
            <stop offset="50%" stop-color="#10b981"/>
            <stop offset="100%" stop-color="#f97316"/>
          </linearGradient>
        </defs>
      </svg>

      <!-- Esfera 3D Cristalina con Imagen Dinámica + Dron Holográfico Superpuesto -->
      <div class="relative w-72 h-72 rounded-full overflow-hidden border-2 border-emerald-300/40 shadow-[0_0_70px_rgba(16,185,129,0.5)] bg-slate-950">
        <img id="heroSphereImg" src="./assets/image1.png" alt="Núcleo Visual 3D" class="w-full h-full object-cover scale-110 transition-all duration-700" />
        <div class="absolute inset-0 bg-gradient-to-tr from-emerald-950/60 via-transparent to-orange-500/25"></div>
        <!-- Reflejo esférico 3D -->
        <div class="absolute -top-10 -left-10 w-44 h-44 rounded-full bg-white/15 blur-xl pointer-events-none"></div>
      </div>

      <!-- Dron 3D SVG con hélices giratorias flotando sobre la esfera -->
      <svg class="absolute -top-4 -right-2 w-28 h-28 drop-shadow-[0_10px_20px_rgba(0,0,0,0.8)]" viewBox="0 0 100 100" fill="none">
        <line x1="22" y1="22" x2="78" y2="78" stroke="#ecfdf5" stroke-width="4" stroke-linecap="round"/>
        <line x1="78" y1="22" x2="22" y2="78" stroke="#ecfdf5" stroke-width="4" stroke-linecap="round"/>
        <rect x="38" y="38" width="24" height="24" rx="7" fill="#059669" stroke="#6ee7b7" stroke-width="2.5"/>
        <circle cx="50" cy="50" r="4.5" fill="#f97316"/>
        <circle cx="20" cy="20" r="14" stroke="#34d399" stroke-width="2.5" stroke-dasharray="10 6">
          <animateTransform attributeName="transform" type="rotate" from="0 20 20" to="360 20 20" dur="0.2s" repeatCount="indefinite"/>
        </circle>
        <circle cx="80" cy="20" r="14" stroke="#34d399" stroke-width="2.5" stroke-dasharray="10 6">
          <animateTransform attributeName="transform" type="rotate" from="0 80 20" to="360 80 20" dur="0.2s" repeatCount="indefinite"/>
        </circle>
        <circle cx="20" cy="80" r="14" stroke="#34d399" stroke-width="2.5" stroke-dasharray="10 6">
          <animateTransform attributeName="transform" type="rotate" from="0 20 80" to="360 20 80" dur="0.2s" repeatCount="indefinite"/>
        </circle>
        <circle cx="80" cy="80" r="14" stroke="#34d399" stroke-width="2.5" stroke-dasharray="10 6">
          <animateTransform attributeName="transform" type="rotate" from="0 80 80" to="360 80 80" dur="0.2s" repeatCount="indefinite"/>
        </circle>
      </svg>
    </div>
  </div>

  <!-- ==========================================================================
       CABECERA ULTRA-LIMPIA IDÉNTICA A @trazomedico (Solo ☰ + Breadcrumb)
       ========================================================================== -->
  <header class="fixed top-0 left-0 right-0 z-40 h-16 px-8 flex items-center justify-between pointer-events-none">
    <!-- Botón Menú ☰ (Abre índice de expositores, guion y pantalla completa) -->
    <button onclick="toggleMenuDrawer()" class="pointer-events-auto w-10 h-10 rounded-xl bg-white/5 hover:bg-white/15 border border-white/10 flex items-center justify-center text-white text-xl transition-all" title="Menú de Expositores y Controles (M)">
      ☰
    </button>

    <!-- Breadcrumb minimalista centro-derecha (exacto al video) -->
    <div class="pointer-events-auto flex items-center gap-3 text-xs sm:text-sm text-white/75 font-medium tracking-wide">
      <span id="headerSectionLabel">Drones Inteligentes en La Libertad 2026</span>
      <span class="text-emerald-400 font-bold">|</span>
      <span id="headerSpeakerLabel" class="text-white font-semibold">Ingeniería de Sistemas UCV</span>
    </div>

    <!-- Indicador discreto de escena y guion -->
    <div class="pointer-events-auto flex items-center gap-2">
      <button onclick="toggleScriptModal()" class="px-3 py-1 rounded-full bg-white/5 hover:bg-emerald-500/20 border border-white/10 text-[11px] font-mono-code text-emerald-300 transition-all" title="Ver Guion del Expositor (Tecla G)">
        🎙️ Guion
      </button>
      <button onclick="toggleFullScreen()" class="w-8 h-8 rounded-full bg-white/5 hover:bg-white/15 border border-white/10 text-xs text-white flex items-center justify-center" title="Pantalla Completa (Tecla F)">
        ⛶
      </button>
    </div>
  </header>

  <!-- ==========================================================================
       MENÚ DESPLEGABLE OCULTO (SE ABRE CON ☰ PARA NO AMONTONAR LA PANTALLA)
       ========================================================================== -->
  <div id="menuDrawer" class="fixed top-16 left-8 z-50 w-80 rounded-2xl bg-slate-950/95 backdrop-blur-2xl border border-white/15 p-4 shadow-2xl hidden">
    <div class="flex items-center justify-between border-b border-white/10 pb-2 mb-3">
      <span class="text-xs font-mono-code text-emerald-400 font-bold uppercase">Navegación por Expositor</span>
      <button onclick="toggleMenuDrawer()" class="text-slate-400 hover:text-white text-xs">✕</button>
    </div>
    <div class="space-y-1.5 text-xs">
      <button onclick="goToScene(0); toggleMenuDrawer();" class="w-full text-left px-3 py-2 rounded-xl hover:bg-white/10 text-white font-semibold flex justify-between"><span>01 · Portada Oficial UCV</span><span class="text-emerald-400">Inicio</span></button>
      <button onclick="goToScene(1); toggleMenuDrawer();" class="w-full text-left px-3 py-2 rounded-xl hover:bg-white/10 text-white font-semibold flex justify-between"><span>02–04 · Exp. 1: Cesar Carranza</span><span class="text-slate-400">Intro / FAO / Perú</span></button>
      <button onclick="goToScene(4); toggleMenuDrawer();" class="w-full text-left px-3 py-2 rounded-xl hover:bg-white/10 text-white font-semibold flex justify-between"><span>05–08 · Exp. 2: Leyvinis Noriega</span><span class="text-slate-400">COER / Obj / 2023-24</span></button>
      <button onclick="goToScene(8); toggleMenuDrawer();" class="w-full text-left px-3 py-2 rounded-xl hover:bg-white/10 text-white font-semibold flex justify-between"><span>09–10 · Exp. 3: Pedro Ledezma</span><span class="text-slate-400">2025-26 / Res. OE1</span></button>
      <button onclick="goToScene(10); toggleMenuDrawer();" class="w-full text-left px-3 py-2 rounded-xl hover:bg-white/10 text-white font-semibold flex justify-between"><span>11–12 · Exp. 4: George Flores</span><span class="text-slate-400">Res. OE2 y OE3</span></button>
      <button onclick="goToScene(12); toggleMenuDrawer();" class="w-full text-left px-3 py-2 rounded-xl hover:bg-white/10 text-white font-semibold flex justify-between"><span>13–15 · Exp. 5: Jelsin Reyes</span><span class="text-slate-400">Tabla 1 / Discusión</span></button>
    </div>
    <div class="mt-3 pt-2 border-t border-white/10 text-[11px] text-slate-400 flex justify-between font-mono-code">
      <span>Autor: César Quiroz</span>
      <span>Flechas ← → o Rueda</span>
    </div>
  </div>

  <!-- ==========================================================================
       MODAL DE GUION DEL EXPOSITOR (OCULTO HASTA PRESIONAR 'G' O EL BOTÓN)
       ========================================================================== -->
  <div id="scriptModal" class="fixed bottom-14 right-8 z-50 max-w-md w-full rounded-2xl bg-slate-950/95 backdrop-blur-2xl border border-emerald-400/40 p-5 shadow-2xl hidden">
    <div class="flex items-center justify-between border-b border-white/10 pb-2 mb-2.5">
      <span id="scriptSpeakerTitle" class="text-xs font-mono-code text-emerald-400 font-bold uppercase">🎙️ Guion del Expositor</span>
      <button onclick="toggleScriptModal()" class="text-slate-400 hover:text-white text-xs">✕</button>
    </div>
    <p id="scriptBodyText" class="text-xs sm:text-sm text-slate-200 leading-relaxed"></p>
  </div>

  <!-- ==========================================================================
       CONTENEDOR DE LAS 15 ESCENAS CON COREOGRAFÍA MORPH (@trazomedico)
       ========================================================================== -->
  <main id="sceneStage" class="relative w-full h-full z-10">

    <!-- ========================================================================
         ESCENA 01 (00:01 de @trazomedico): PORTADA CON TÍTULO GIGANTE DETRÁS DEL OBJETO 3D
         ======================================================================== -->
    <section class="scene active" data-scene="0" data-hero="center" data-img="./assets/image1.png"
      data-speaker="Portada Oficial · Grupo TIF Nivel I (Sección B1T1)"
      data-script="Buenos días/tardes estimado docente Mgtr. Luis Angel De Lucio Burga y compañeros. Presentamos nuestra investigación formativa de Nivel I de la Escuela de Ingeniería de Sistemas de la Universidad César Vallejo: Sistema de información con drones inteligentes para detección temprana de incendios forestales y deforestación en La Libertad 2026, alineada a los ODS 13 y 15.">
      <div class="w-full max-w-6xl mx-auto text-center relative">
        <!-- Píldora superior derecha estilo 'TEMA 10' de @trazomedico -->
        <div class="stagger d-1 inline-flex items-center gap-2 px-5 py-1.5 rounded-full bg-orange-600 text-white font-bold text-xs tracking-widest uppercase shadow-lg shadow-orange-600/40 mb-4">
          <img src="./assets/docx_image1.png" alt="UCV" class="w-4 h-4 object-contain bg-white rounded-sm p-0.5" />
          UNIVERSIDAD CÉSAR VALLEJO · TIF NIVEL I
        </div>

        <!-- Título Monumental que cruza detrás/alrededor del Objeto 3D central -->
        <h1 class="stagger d-2 title-condensed text-6xl sm:text-8xl xl:text-[6.8rem] font-bold tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-amber-200 via-emerald-300 to-teal-200 drop-shadow-[0_10px_35px_rgba(0,0,0,0.9)]">
          DRONES INTELIGENTES
        </h1>
        <div class="stagger d-3 title-condensed text-2xl sm:text-4xl text-white/90 tracking-[0.22em] mt-2">
          INCENDIOS Y DEFORESTACIÓN · LA LIBERTAD 2026
        </div>

        <!-- Espacio central para que luzca el Dron 3D y pie limpio con los 5 autores -->
        <div class="stagger d-4 mt-56 pt-6 inline-flex flex-wrap items-center justify-center gap-3 px-6 py-3 rounded-2xl bg-black/55 backdrop-blur-xl border border-white/15 text-xs text-slate-200">
          <span class="text-emerald-400 font-bold">Expositores:</span>
          <span>1. Cesar Carranza</span> ·
          <span>2. Leyvinis Noriega</span> ·
          <span>3. Pedro Ledezma</span> ·
          <span>4. George Flores</span> ·
          <span>5. Jelsin Reyes</span>
          <span class="text-amber-300 font-semibold ml-2">| Asesor: Mgtr. Luis Angel De Lucio Burga (B1T1)</span>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         ESCENA 02 (00:06 de @trazomedico): 4 TARJETAS DE COLOR CON ICONO CIRCULAR SUPERIOR
         ======================================================================== -->
    <section class="scene" data-scene="1" data-hero="bg-blur" data-img="./assets/image3.png"
      data-speaker="Expositor 1 · Cesar Carranza (I. Introducción)"
      data-script="En la introducción contrastamos la realidad observada frente a la solución deseada desde la Ingeniería de Sistemas: el cambio climático prolonga las sequías e inflama los bosques reduciendo la absorción de CO2. Hoy la vigilancia depende de rondas a pie o satélites bloqueados por nubes. Proponemos un sistema con drones inteligentes que integra tres componentes informáticos: visión artificial contra falsos positivos, redes de baja latencia y base de datos georreferenciada, aportando a los ODS 13 y 15.">
      <div class="w-full max-w-6xl mx-auto space-y-12">
        <h2 class="stagger d-1 title-condensed text-5xl sm:text-6xl text-center text-white">
          REALIDAD ACTUAL Y PROPUESTA IA
        </h2>

        <!-- 4 Tarjetas idénticas a 'GRUPOS DE RIESGO' (00:06) -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 pt-4">
          <div class="stagger d-1 risk-card bg-gradient-to-b from-orange-600 to-red-700">
            <div class="risk-card-icon bg-orange-500 text-3xl">🌡️</div>
            <h3 class="font-bold text-lg text-white">Cambio Climático</h3>
            <p class="text-xs text-orange-100 mt-2 leading-relaxed">
              Sequías prolongadas inflaman bosques y pastizales, reduciendo la absorción de $\text{CO}_2$ y liberando más gases de efecto invernadero.
            </p>
          </div>

          <div class="stagger d-2 risk-card bg-gradient-to-b from-amber-600 to-orange-700">
            <div class="risk-card-icon bg-amber-500 text-3xl">🛰️</div>
            <h3 class="font-bold text-lg text-white">Vigilancia Lenta</h3>
            <p class="text-xs text-amber-100 mt-2 leading-relaxed">
              Rondas humanas a pie, avisos telefónicos tardíos y satélites que demoran horas y quedan bloqueados por nubes o neblina.
            </p>
          </div>

          <div class="stagger d-3 risk-card bg-gradient-to-b from-emerald-600 to-teal-800">
            <div class="risk-card-icon bg-emerald-500 text-3xl">🚁</div>
            <h3 class="font-bold text-lg text-white">Visión Artificial IA</h3>
            <p class="text-xs text-emerald-100 mt-2 leading-relaxed">
              Drones bajo las nubes con algoritmos que reconocen conatos de fuego y claros de tala sin confundir neblina ni sol.
            </p>
          </div>

          <div class="stagger d-4 risk-card bg-gradient-to-b from-teal-600 to-cyan-800">
            <div class="risk-card-icon bg-teal-500 text-3xl">📡</div>
            <h3 class="font-bold text-lg text-white">Alerta y Mapas GIS</h3>
            <p class="text-xs text-teal-100 mt-2 leading-relaxed">
              Notificación web/móvil en segundos con coordenadas GPS y base de datos para mapas de calor (<strong>ODS 13 y ODS 15</strong>).
            </p>
          </div>
        </div>

        <!-- Nota inferior con icono ⓘ idéntica a 00:06 -->
        <div class="stagger d-5 max-w-3xl mx-auto flex items-center gap-3 px-5 py-3 rounded-2xl bg-white/5 border border-white/10 text-xs sm:text-sm text-slate-200">
          <span class="w-6 h-6 rounded-full bg-white text-slate-950 font-bold flex items-center justify-center shrink-0">i</span>
          <span><strong>Justificación en Ingeniería de Sistemas:</strong> Integra procesamiento de imágenes, redes de comunicación de baja demora y base de datos espacial para actuar en los primeros minutos del incendio.</span>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         ESCENA 03 (00:08 de @trazomedico): OBJETO 3D A LA DERECHA + 3 BARRAS LUMINOSAS A LA IZQUIERDA
         ======================================================================== -->
    <section class="scene" data-scene="2" data-hero="right" data-img="./assets/image9.png"
      data-speaker="Expositor 1 · Cesar Carranza (Estadística Mundial FAO / WRI)"
      data-script="A nivel internacional, la FAO (2025) reporta que el planeta posee 4 140 millones de hectáreas de bosques, pero pierde 10,9 millones de hectáreas por año por deforestación y 261 millones de hectáreas anuales son afectadas por el fuego. Asimismo, Goldman et al. (2026) para el World Resources Institute (WRI) y el laboratorio GLAD de la Universidad de Maryland revelaron que en 2025 se perdieron 25,5 millones de hectáreas de cobertura arbórea, incluidos 4,3 millones de bosques primarios tropicales, equivalentes a más de 11 campos de fútbol por minuto, siendo los incendios responsables del 42 % de toda esa pérdida.">
      <div class="w-full max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-12 items-center">
        <div class="lg:col-span-7 space-y-5">
          <h2 class="stagger d-1 title-condensed text-5xl sm:text-6xl text-white">
            EVIDENCIA ESTADÍSTICA MUNDIAL
          </h2>

          <ul class="stagger d-2 space-y-2 text-sm sm:text-base text-slate-200">
            <li>• <strong>FAO (2025):</strong> De las <strong>4 140 millones de ha</strong> de bosques del planeta, el fuego afecta <strong>261 millones de ha</strong> cada año.</li>
            <li>• <strong>Goldman et al. (2026) · WRI &amp; GLAD:</strong> Las olas de calor quemaron el doble de árboles que hace dos décadas (<strong>&gt; 11 campos de fútbol/minuto</strong>).</li>
          </ul>

          <!-- 3 Barras Horizontales con Borde Luminoso (idénticas a 00:08) -->
          <div class="space-y-3.5 pt-2">
            <div class="stagger d-3 glow-bar flex items-center justify-between">
              <span class="font-semibold text-base text-white">Deforestación anual sostenida 2015–2025 (FAO, 2025)</span>
              <span class="font-mono-code font-bold text-xl text-emerald-400">10,9 M ha/año</span>
            </div>

            <div class="stagger d-4 glow-bar flex items-center justify-between">
              <span class="font-semibold text-base text-white">Cobertura arbórea perdida en 2025 · 4,3 M ha primarias (WRI, 2026)</span>
              <span class="font-mono-code font-bold text-xl text-amber-300">25,5 M ha</span>
            </div>

            <div class="stagger d-5 glow-bar flex items-center justify-between">
              <span class="font-semibold text-base text-white">Pérdida mundial de árboles causada directamente por incendios</span>
              <span class="font-mono-code font-bold text-xl text-orange-400">42 % del total</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         ESCENA 04 (00:10 de @trazomedico): OBJETO 3D VIAJA A LA IZQUIERDA + TEXTO A LA DERECHA
         ======================================================================== -->
    <section class="scene" data-scene="3" data-hero="left" data-img="./assets/image12.png"
      data-speaker="Expositor 1 · Cesar Carranza (Estadística Nacional en Perú)"
      data-script="En el Perú, Goldman et al. (2026) nos ubican entre los diez países del mundo con mayor pérdida de bosques primarios tropicales. Respecto a los incendios, el INDECI (2024), mediante el COEN y la plataforma SINPAD, registró 1 754 incendios forestales en 2024, con un pico crítico de 840 emergencias en septiembre, destruyendo 63 710,38 hectáreas naturales y 14 971,57 hectáreas de cultivos, además de 285 heridos y 35 fallecidos. Según la Defensoría del Pueblo (Informe n.° 225) y el SERFOR, el 95 % de estos siniestros son causados por actividades humanas.">
      <div class="w-full max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-12 items-center">
        <div class="lg:col-span-5"></div>
        <div class="lg:col-span-7 space-y-5 text-left lg:pl-8">
          <h2 class="stagger d-1 title-condensed text-5xl sm:text-6xl text-white">
            ESCENARIO CRÍTICO EN EL PERÚ
          </h2>

          <p class="stagger d-2 text-base text-emerald-300 font-semibold">
            El Perú figura entre los <strong>10 países del mundo con mayor pérdida de bosque primario tropical</strong> por ampliación agrícola, pasturas y actividades extractivas (Goldman et al., 2026):
          </p>

          <div class="stagger d-3 space-y-4 text-sm sm:text-base text-slate-200 leading-relaxed">
            <div class="p-4 rounded-2xl bg-white/5 border-l-4 border-l-orange-500">
              • <strong>Reporte INDECI / COEN-SINPAD (2024):</strong> Se registraron <strong>1 754 incendios forestales</strong> a nivel nacional (septiembre fue el mes más crítico con <strong>840 emergencias</strong>), destruyendo <strong>63 710,38 ha</strong> de cobertura natural y <strong>14 971,57 ha</strong> de cultivo, dejando <strong>285 heridos y 35 fallecidos</strong>.
            </div>

            <div class="p-4 rounded-2xl bg-white/5 border-l-4 border-l-emerald-400">
              • <strong>Defensoría del Pueblo (2024, Informe n.° 225) y SERFOR:</strong> Cerca del <strong>95 % de los incendios en el país</strong> son originados por actividades humanas, principalmente por la <strong>quema tradicional de rastrojos y pastos secos</strong> para abrir chacras, agravada por el viento y la sequía andina.
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         ESCENA 05 (00:11 de @trazomedico): OBJETO 3D A LA DERECHA + 2 TARJETAS BLANCAS NUMERADAS 1 Y 2
         ======================================================================== -->
    <section class="scene" data-scene="4" data-hero="right" data-img="./assets/image10.png"
      data-speaker="Expositor 2 · Leyvinis Noriega (Problemática en La Libertad - COER)"
      data-script="A nivel local, en la región La Libertad, el COER difundido por Agraria.pe (2024) reportó más de 42 incendios forestales en una sola temporada crítica, destruyendo 2 990 hectáreas de pastizales naturales, bosques de eucalipto y pino, y cultivos de trigo, cebada y tarwi, además de afectar 41 viviendas y ganado. La provincia más golpeada fue Santiago de Chuco con más de 1 000 hectáreas consumidas, seguida por Otuzco, Sánchez Carrión, Bolívar y Pataz, destruyendo los colchones naturales de agua en las cabeceras de cuenca.">
      <div class="w-full max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-12 items-center">
        <div class="lg:col-span-7 space-y-6">
          <h2 class="stagger d-1 title-condensed text-5xl sm:text-6xl text-white">
            IMPACTO EN LA SIERRA LIBERTEÑA
          </h2>

          <!-- Tarjeta Blanca 1 con chapita roja '1' a la izquierda (exacta a 00:11) -->
          <div class="stagger d-2 white-step-card mr-8">
            <div class="step-badge bg-orange-600 left-6">1</div>
            <p class="text-sm sm:text-base leading-relaxed pt-1">
              Según el <strong>COER La Libertad (Agraria.pe, 2024)</strong>, se registraron <strong>+42 incendios forestales</strong> en una temporada crítica, destruyendo <strong>2 990 hectáreas</strong> entre pastizales de ichu, bosques de <strong>eucalipto y pino</strong>, y cultivos de <strong>trigo, cebada y tarwi</strong>, con <strong>41 viviendas afectadas</strong> y pérdida de ganado.
            </p>
          </div>

          <!-- Tarjeta Blanca 2 desplazada con chapita azul/verde '2' a la derecha (exacta a 00:11) -->
          <div class="stagger d-3 white-step-card ml-10">
            <div class="step-badge bg-emerald-600 right-6">2</div>
            <p class="text-sm sm:text-base leading-relaxed pt-1">
              La provincia más golpeada fue <strong>Santiago de Chuco (+1 000 ha quemadas)</strong>, seguida por <strong>Otuzco, Sánchez Carrión, Bolívar y Pataz</strong>. Esto destruye los <strong>colchones naturales de agua en las cabeceras de cuenca</strong> que abastecen a los valles liberteños y erosiona el suelo agrícola.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         ESCENA 06 (00:13 de @trazomedico): 4 PÍLDORAS 2x2 CON MEDALLÓN CIRCULAR LATERAL
         ======================================================================== -->
    <section class="scene" data-scene="5" data-hero="right-edge" data-img="./assets/image11.png"
      data-speaker="Expositor 2 · Leyvinis Noriega (Problema y Objetivos - Anexo 1)"
      data-script="Por ello planteamos nuestro Problema General: ¿De qué manera la implementación de un sistema de información con drones inteligentes influye en el tiempo de detección temprana de incendios forestales y deforestación en zonas vulnerables de La Libertad durante el año 2026? Nuestro Objetivo General es determinar su impacto en optimizar los tiempos de detección y reporte. Y definimos tres objetivos específicos: medir la exactitud y margen de error frente a falsos positivos; comparar el tiempo de transmisión y procesamiento frente a la vigilancia tradicional; y evaluar la eficiencia en el almacenamiento del historial georreferenciado para mapas de calor.">
      <div class="w-full max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-12 items-center">
        <div class="lg:col-span-9 space-y-8">
          <h2 class="stagger d-1 title-condensed text-5xl sm:text-6xl text-white">
            PROBLEMA Y OBJETIVOS DE INVESTIGACIÓN
          </h2>

          <!-- Cuadrícula 2x2 de tarjetas blancas con medallón circular a la derecha (idéntica a 00:13) -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-x-10 gap-y-6 pr-6">
            <div class="stagger d-2 entry-pill-card">
              <div class="text-xs font-bold uppercase text-orange-600">Problema General</div>
              <p class="text-xs sm:text-sm font-medium mt-1">
                ¿Cómo influye el sistema con drones inteligentes en el <strong>tiempo de detección temprana</strong> en zonas vulnerables de La Libertad 2026?
              </p>
              <div class="entry-medallion bg-orange-500 text-white text-2xl">❓</div>
            </div>

            <div class="stagger d-3 entry-pill-card">
              <div class="text-xs font-bold uppercase text-amber-600">Objetivo General</div>
              <p class="text-xs sm:text-sm font-medium mt-1">
                Determinar el impacto del sistema en <strong>optimizar los tiempos de detección temprana y reporte</strong> de incendios y deforestación.
              </p>
              <div class="entry-medallion bg-amber-500 text-white text-2xl">🎯</div>
            </div>

            <div class="stagger d-4 entry-pill-card">
              <div class="text-xs font-bold uppercase text-emerald-700">Objetivos Específicos 1 y 2</div>
              <p class="text-xs sm:text-sm font-medium mt-1">
                <strong>OE1:</strong> Medir exactitud vs. falsos positivos (sol/neblina).<br/>
                <strong>OE2:</strong> Comparar tiempo de transmisión frente al satélite.
              </p>
              <div class="entry-medallion bg-emerald-500 text-white text-2xl">⚡</div>
            </div>

            <div class="stagger d-5 entry-pill-card">
              <div class="text-xs font-bold uppercase text-teal-700">Objetivo Específico 3</div>
              <p class="text-xs sm:text-sm font-medium mt-1">
                <strong>OE3:</strong> Evaluar la eficiencia en estructurar el <strong>historial georreferenciado</strong> para proyectar <strong>mapas de calor</strong>.
              </p>
              <div class="entry-medallion bg-teal-500 text-white text-2xl">🗺️</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         ESCENA 07 (00:15 de @trazomedico): 4 MEDALLONES ARRIBA + TÍTULO + 2 TARJETAS BLANCAS
         ======================================================================== -->
    <section class="scene" data-scene="6" data-hero="bg-blur" data-img="./assets/image3.png"
      data-speaker="Expositor 2 · Leyvinis Noriega (Análisis Crítico de Bases Teóricas)"
      data-script="Al analizar críticamente los marcos teóricos de los 7 artículos indexados entre 2023 y 2026, identificamos el paso de una vigilancia pasiva hacia el monitoreo aéreo activo con IA a bordo del dron. Sin embargo, descubrimos una brecha teórica fundamental: la literatura estudia los incendios forestales (con redes YOLO) y la deforestación (con redes U-Net y VGG16) como si fueran problemas separados, cuando en los Andes peruanos el desmonte y las quemas agrícolas ocurren al mismo tiempo para abrir chacras, demostrando la necesidad de unir ambas funciones en un solo sistema.">
      <div class="w-full max-w-5xl mx-auto text-center space-y-6">
        <!-- Los 4 medallones de la escena anterior ahora alineados arriba al centro (exacto a 00:15) -->
        <div class="stagger d-1 flex items-center justify-center gap-4">
          <div class="w-14 h-14 rounded-full bg-orange-500 flex items-center justify-center text-2xl shadow-lg">❓</div>
          <div class="w-14 h-14 rounded-full bg-amber-500 flex items-center justify-center text-2xl shadow-lg">🎯</div>
          <div class="w-14 h-14 rounded-full bg-emerald-500 flex items-center justify-center text-2xl shadow-lg">⚡</div>
          <div class="w-14 h-14 rounded-full bg-teal-500 flex items-center justify-center text-2xl shadow-lg">🗺️</div>
        </div>

        <h2 class="stagger d-2 title-condensed text-5xl sm:text-6xl text-white">
          ANÁLISIS DE MARCOS TEÓRICOS (2023–2026)
        </h2>

        <p class="stagger d-3 text-sm sm:text-base text-slate-200 max-w-2xl mx-auto">
          En la revisión documental e informativa de los 7 estudios indexados en <strong>Scopus / SJR (Q1/Q2)</strong> se identificó una tendencia clara y un <strong>vacío teórico en los Andes</strong>:
        </p>

        <!-- 2 Tarjetas blancas lado a lado (exactas a 00:15) -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-left pt-2">
          <div class="stagger d-4 white-step-card">
            <h3 class="font-bold text-lg text-emerald-800 mb-2">1. Arquitecturas Especializadas</h3>
            <p class="text-xs sm:text-sm text-slate-700 leading-relaxed">
              Los estudios de incendios (<em>Saydirasulovich, Shamta, Yun, Luo, Ma</em>) coinciden en usar redes de una sola etapa <strong>YOLOv5, YOLOv8 y YOLO11</strong> para video en tiempo real; mientras que en deforestación (<em>Md Jelas, Borse</em>) usan segmentación semántica <strong>U-Net, DeepLabV3+ y VGG16</strong> con coordenadas espaciales.
            </p>
          </div>

          <div class="stagger d-5 white-step-card">
            <h3 class="font-bold text-lg text-orange-700 mb-2">2. Brecha Teórica en los Andes Peruanos</h3>
            <p class="text-xs sm:text-sm text-slate-700 leading-relaxed">
              La literatura estudió los incendios y la tala como <strong>dos problemas separados con programas distintos</strong>; pero en el Perú (<em>Defensoría, 2024; Agraria.pe, 2024</em>) <strong>la tala/desmonte y las quemas agrícolas ocurren al mismo tiempo</strong>, exigiendo unificarlos en un solo sistema de información.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         ESCENA 08 (00:17 de @trazomedico): CARRUSEL DE CRISTAL (ANTECEDENTES 2023–2024)
         ======================================================================== -->
    <section class="scene" data-scene="7" data-hero="bg-blur" data-img="./assets/image11.png"
      data-speaker="Expositor 2 · Leyvinis Noriega (Antecedentes 2023–2024)"
      data-script="Revisando cronológicamente los antecedentes de 2023 y 2024: Primero, Norkobil Saydirasulovich et al. (2023) en Sensors modificaron YOLOv8 con atención BiFormer y convoluciones GSConv para detectar humo temprano desde drones, logrando 79,4 % AP (71,3 % en humo pequeño y 92,6 % en grande). Segundo, Md Jelas et al. (2024) en Frontiers evaluaron 22 estudios con U-Net y DeepLabV3+, alcanzando entre 92,78 % y 98,14 % de exactitud al segmentar tala, superando el 98 % con drones en la Amazonía peruana. Tercero, Shamta y Demir (2024) en PLOS ONE construyeron un cuadricóptero con NVIDIA Jetson Nano, Raspberry Pi y GSM, logrando 96 % en clasificación y 89 % en vuelo real.">
      <div class="w-full max-w-6xl mx-auto text-center space-y-6">
        <h2 class="stagger d-1 title-condensed text-5xl sm:text-6xl text-white">
          ANTECEDENTES CIENTÍFICOS (2023–2024)
        </h2>

        <div class="relative flex items-center justify-center gap-5 pt-4">
          <!-- Botón de flecha de carrusel (como el « de 00:17) -->
          <button onclick="goToScene(8)" class="hidden lg:flex w-11 h-11 rounded-full bg-white/10 hover:bg-emerald-500 text-white items-center justify-center text-xl font-bold transition-all shrink-0" title="Deslizar hacia estudios 2025–2026">
            «
          </button>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-6 w-full">
            <!-- Card 1 -->
            <div class="stagger d-2 space-y-3">
              <div class="text-3xl text-emerald-300">💨</div>
              <div class="frost-carousel-card text-left">
                <div class="text-xs font-mono-code text-amber-300 font-bold">Sensors (2023) · Q1/Q2</div>
                <div class="font-bold text-base text-white mt-0.5">Saydirasulovich et al.</div>
                <div class="h-36 rounded-xl overflow-hidden my-3 border border-white/20">
                  <img src="./assets/image10.png" alt="Saydirasulovich 2023" class="w-full h-full object-cover" />
                </div>
                <p class="text-xs text-slate-200 leading-relaxed">
                  <strong>YOLOv8 + BiFormer + GSConv:</strong> Logra <strong>79,4 % AP</strong> en humo (+3,3 % sobre base), con <strong>71,3 %</strong> en focos pequeños y <strong>92,6 %</strong> en columnas grandes.
                </p>
              </div>
            </div>

            <!-- Card 2 -->
            <div class="stagger d-3 space-y-3">
              <div class="text-3xl text-emerald-300">🌲</div>
              <div class="frost-carousel-card text-left">
                <div class="text-xs font-mono-code text-emerald-300 font-bold">Frontiers (2024) · Q1</div>
                <div class="font-bold text-base text-white mt-0.5">Md Jelas et al. (22 estudios)</div>
                <div class="h-36 rounded-xl overflow-hidden my-3 border border-white/20">
                  <img src="./assets/image9.png" alt="Md Jelas 2024" class="w-full h-full object-cover" />
                </div>
                <p class="text-xs text-slate-200 leading-relaxed">
                  <strong>U-Net con atención y DeepLabV3+:</strong> Logra <strong>92,78 % a 98,14 %</strong> de exactitud separando bosque sano de tala (<strong>&gt;98 % con drones en la Amazonía peruana</strong>).
                </p>
              </div>
            </div>

            <!-- Card 3 -->
            <div class="stagger d-4 space-y-3">
              <div class="text-3xl text-emerald-300">🚁</div>
              <div class="frost-carousel-card text-left">
                <div class="text-xs font-mono-code text-cyan-300 font-bold">PLOS ONE (2024) · Q1</div>
                <div class="font-bold text-base text-white mt-0.5">Shamta y Demir (Hardware)</div>
                <div class="h-36 rounded-xl overflow-hidden my-3 border border-white/20">
                  <img src="./assets/image11.png" alt="Shamta y Demir 2024" class="w-full h-full object-cover" />
                </div>
                <p class="text-xs text-slate-200 leading-relaxed">
                  Dron cuadricóptero + <strong>NVIDIA Jetson Nano + Raspberry Pi + GSM</strong>. <strong>96 % exactitud</strong> (CNN-RCNN/YOLOv8) y <strong>89 % en vuelo real</strong> (~25 min batería).
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         ESCENA 09 (00:18–00:19 de @trazomedico): CARRUSEL DESLIZADO (ANTECEDENTES 2025–2026)
         ======================================================================== -->
    <section class="scene" data-scene="8" data-hero="bg-blur" data-img="./assets/image16.png"
      data-speaker="Expositor 3 · Pedro Ledezma (Antecedentes 2025–2026)"
      data-script="Avanzando en el carrusel hacia los estudios de 2025 y 2026: Yun et al. (2025) en Fire mejoraron YOLOv8 con SPDConv y atención MLCA en más de 3 200 fotos aéreas, subiendo la sensibilidad en 5,5 % y reduciendo los parámetros en 43,8 % (5,96 M). Luo et al. (2025) en Forests crearon YOLO-UFS con MobileNetV4 y muestras negativas de sol, neblina y hojas rojas, logrando 91,3 % mAP y reduciendo el peso en más de 74 % (7,4 MB a 30 FPS en Jetson Nano). Borse et al. (2025) en PLOS ONE evaluaron 10 400 árboles a menos de 10 cm/píxel con GeoJSON, logrando 98,39 % con VGG16 y AUC 0,95 con YOLOv8. Y Ma et al. (2026) en Sustainability crearon AHE-YOLO (YOLO11) en 5 118 fotos, logrando 94,8 % mAP, 3,5 MB y 333,3 FPS.">
      <div class="w-full max-w-6xl mx-auto text-center space-y-6">
        <h2 class="stagger d-1 title-condensed text-5xl sm:text-6xl text-white">
          ANTECEDENTES CIENTÍFICOS (2025–2026)
        </h2>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5 pt-2">
          <!-- Card 4 -->
          <div class="stagger d-1 space-y-2">
            <div class="text-2xl">🔥</div>
            <div class="frost-carousel-card text-left">
              <div class="text-[11px] font-mono-code text-orange-300 font-bold">Fire (2025) · Yun et al.</div>
              <div class="h-28 rounded-xl overflow-hidden my-2.5 border border-white/20">
                <img src="./assets/image12.png" alt="Yun 2025" class="w-full h-full object-cover" />
              </div>
              <p class="text-xs text-slate-200 leading-relaxed">
                <strong>YOLOv8 + SPDConv + MLCA</strong> (&gt;3 200 fotos). Sube sensibilidad <strong>+5,5 %</strong> y reduce parámetros en <strong>43,8 % (5,96 M)</strong> para focos tras ramas.
              </p>
            </div>
          </div>

          <!-- Card 5 -->
          <div class="stagger d-2 space-y-2">
            <div class="text-2xl">🌤️</div>
            <div class="frost-carousel-card text-left">
              <div class="text-[11px] font-mono-code text-emerald-300 font-bold">Forests (2025) · Luo et al.</div>
              <div class="h-28 rounded-xl overflow-hidden my-2.5 border border-white/20">
                <img src="./assets/image3.png" alt="Luo 2025" class="w-full h-full object-cover" />
              </div>
              <p class="text-xs text-slate-200 leading-relaxed">
                <strong>YOLO-UFS (MobileNetV4 + BiFPN)</strong> entrenado con neblina y sol. <strong>91,3 % mAP</strong>, <strong>-74 % peso (7,4 MB)</strong> a <strong>30 FPS en Jetson Nano</strong>.
              </p>
            </div>
          </div>

          <!-- Card 6 -->
          <div class="stagger d-3 space-y-2">
            <div class="text-2xl">🗺️</div>
            <div class="frost-carousel-card text-left">
              <div class="text-[11px] font-mono-code text-cyan-300 font-bold">PLOS ONE (2025) · Borse et al.</div>
              <div class="h-28 rounded-xl overflow-hidden my-2.5 border border-white/20">
                <img src="./assets/image17.png" alt="Borse 2025" class="w-full h-full object-cover" />
              </div>
              <p class="text-xs text-slate-200 leading-relaxed">
                <strong>AETDA (VGG16 + YOLOv8)</strong> en <strong>10 400+ árboles (&lt;10 cm/px)</strong>. Logra <strong>98,39 % exactitud</strong>, <strong>AUC 0,95</strong> y archivos <strong>GeoJSON</strong>.
              </p>
            </div>
          </div>

          <!-- Card 7 -->
          <div class="stagger d-4 space-y-2">
            <div class="text-2xl">⚡</div>
            <div class="frost-carousel-card text-left">
              <div class="text-[11px] font-mono-code text-teal-300 font-bold">Sustainability (2026) · Ma et al.</div>
              <div class="h-28 rounded-xl overflow-hidden my-2.5 border border-white/20">
                <img src="./assets/image16.png" alt="Ma 2026" class="w-full h-full object-cover" />
              </div>
              <p class="text-xs text-slate-200 leading-relaxed">
                <strong>AHE-YOLO (YOLO11 + ADown + EMBC)</strong> en <strong>5 118 fotos</strong> día/noche. <strong>94,8 % mAP</strong>, <strong>85,1 % recall</strong>, solo <strong>3,5 MB</strong> y <strong>333,3 FPS</strong>.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         ESCENA 10 (00:08 style): OBJETO 3D A LA DERECHA + BARRAS ANIMADAS OE1 A LA IZQUIERDA
         ======================================================================== -->
    <section class="scene" data-scene="9" data-hero="right" data-img="./assets/image12.png"
      data-speaker="Expositor 3 · Pedro Ledezma (Resultados Objetivo Específico 1: Exactitud IA)"
      data-script="En los resultados del Objetivo Específico 1, medimos la tasa de exactitud y el margen de error frente a falsos positivos. Saydirasulovich (2023) alcanzó 79,4 % AP, pero en humo pequeño bajó a 71,3 % dejando 28,7 % de margen de error ante nubes bajas. Luo et al. (2025) entrenaron YOLO-UFS con muestras negativas de reflejos solares, neblina matutina y hojas rojizas subiendo a 91,3 % mAP. Ma et al. (2026) lograron 94,8 % mAP con AHE-YOLO11 en 5 118 imágenes día/noche; Shamta y Demir (2024) alcanzaron 96 % en clasificación y 89 % en vuelo; y Md Jelas (2024) junto a Borse (2025) llegaron hasta 98,14 % y 98,39 % en detección de tala y conteo arbóreo.">
      <div class="w-full max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-12 items-center">
        <div class="lg:col-span-8 space-y-4">
          <h2 class="stagger d-1 title-condensed text-5xl sm:text-6xl text-white">
            RESULTADOS OE1: EXACTITUD VS. FALSOS POSITIVOS
          </h2>
          <p class="stagger d-2 text-xs sm:text-sm text-slate-300">
            Para evitar falsas alarmas en la sierra liberteña es indispensable añadir <strong>filtros de atención visual y entrenar con muestras negativas reales de neblina matutina y brillo solar</strong>:
          </p>

          <div class="space-y-3 pt-1">
            <div class="stagger d-2 glow-bar">
              <div class="flex justify-between text-xs sm:text-sm font-semibold mb-1.5">
                <span>Saydirasulovich et al. (2023) · YOLOv8 + BiFormer (71,3 % humo pequeño → 28,7 % error)</span>
                <span class="font-mono-code text-amber-300 font-bold">79,4 % AP</span>
              </div>
              <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden"><div class="bar-fill h-full bg-amber-400 rounded-full" data-width="79.4%"></div></div>
            </div>

            <div class="stagger d-3 glow-bar">
              <div class="flex justify-between text-xs sm:text-sm font-semibold mb-1.5">
                <span>Luo et al. (2025) · YOLO-UFS (+3,8 % filtrando neblina matutina, sol y hojas rojizas)</span>
                <span class="font-mono-code text-emerald-300 font-bold">91,3 % mAP</span>
              </div>
              <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden"><div class="bar-fill h-full bg-emerald-400 rounded-full" data-width="91.3%"></div></div>
            </div>

            <div class="stagger d-4 glow-bar">
              <div class="flex justify-between text-xs sm:text-sm font-semibold mb-1.5">
                <span>Ma et al. (2026) · AHE-YOLO11 (85,1 % sensibilidad en 5 118 fotos día/noche; Yun: +5,5 %)</span>
                <span class="font-mono-code text-teal-300 font-bold">94,8 % mAP</span>
              </div>
              <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden"><div class="bar-fill h-full bg-teal-400 rounded-full" data-width="94.8%"></div></div>
            </div>

            <div class="stagger d-5 glow-bar">
              <div class="flex justify-between text-xs sm:text-sm font-semibold mb-1.5">
                <span>Shamta y Demir (2024) · CNN-RCNN / YOLOv8 (89 % detección directa en vuelo real)</span>
                <span class="font-mono-code text-orange-400 font-bold">96,0 % Exactitud</span>
              </div>
              <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden"><div class="bar-fill h-full bg-orange-400 rounded-full" data-width="96.0%"></div></div>
            </div>

            <div class="stagger d-5 glow-bar">
              <div class="flex justify-between text-xs sm:text-sm font-semibold mb-1.5">
                <span>Md Jelas (2024) y Borse (2025) · U-Net (&gt;98 % Amazonía Perú) y VGG16 (10 400 árboles)</span>
                <span class="font-mono-code text-emerald-300 font-bold">98,39 % Exactitud</span>
              </div>
              <div class="w-full h-2.5 bg-white/10 rounded-full overflow-hidden"><div class="bar-fill h-full bg-gradient-to-r from-emerald-400 to-cyan-300 rounded-full" data-width="98.39%"></div></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         ESCENA 11 (00:22 de @trazomedico): 4 TARJETAS CON ICONO SUPERIOR (RESULTADOS OE2)
         ======================================================================== -->
    <section class="scene" data-scene="10" data-hero="bg-blur" data-img="./assets/image16.png"
      data-speaker="Expositor 4 · George Flores (Resultados Objetivo Específico 2: Velocidad y Peso)"
      data-script="Respecto al Objetivo Específico 2 sobre tiempo de transmisión y procesamiento: mientras que los avisos telefónicos o el paso satelital tardan horas, Shamta y Demir (2024) demostraron que procesar el video a bordo del dron con NVIDIA Jetson Nano y Raspberry Pi envía la alerta con GPS por red GSM en segundos. Yun et al. (2025) bajaron los parámetros en 43,8 % (5,96 M); Luo et al. (2025) redujeron el peso computacional en más de 74 % llegando a 7,4 MB y 30 FPS reales en Jetson Nano; y Ma et al. (2026) comprimieron su modelo a 3,5 MB y 333,3 FPS. No obstante, advertimos críticamente que los 30 FPS de Luo se midieron en minicomputadoras reales de dron, mientras que los 333,3 FPS de Ma se midieron en GPUs potentes de laboratorio.">
      <div class="w-full max-w-6xl mx-auto space-y-10">
        <div class="text-center space-y-1">
          <div class="stagger d-1 text-sm font-bold tracking-widest text-emerald-400 uppercase">OBJETIVO ESPECÍFICO 2 · LATENCIA Y PROCESAMIENTO EN EL BORDE</div>
          <h2 class="stagger d-1 title-condensed text-5xl sm:text-6xl text-white">
            COMPRESIÓN DE IA Y TIEMPO DE RESPUESTA
          </h2>
        </div>

        <!-- 4 Tarjetas en fila idénticas a 'MANIFESTACIONES CARDIACAS' (00:22) -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 pt-4">
          <div class="stagger d-1 risk-card bg-gradient-to-b from-teal-600 to-emerald-800">
            <div class="risk-card-icon bg-teal-500 text-2xl font-mono-code font-bold">-44%</div>
            <h3 class="font-bold text-lg text-white">Yun et al. (2025)</h3>
            <p class="text-xs text-teal-100 mt-2 leading-relaxed">
              Reduce <strong>43,8 % de parámetros (5,96 M)</strong> y <strong>43,3 % de peso</strong> de archivo con atención MLCA sin sobrecargar el procesador del dron.
            </p>
          </div>

          <div class="stagger d-2 risk-card bg-gradient-to-b from-emerald-600 to-green-800">
            <div class="risk-card-icon bg-emerald-500 text-xl font-mono-code font-bold">7,4MB</div>
            <h3 class="font-bold text-lg text-white">Luo et al. (2025)</h3>
            <p class="text-xs text-emerald-100 mt-2 leading-relaxed">
              Reducción <strong>&gt; 74 % del peso computacional</strong> con bloques MobileNetV4, corriendo fluido a <strong>30 FPS reales en placa Jetson Nano</strong>.
            </p>
          </div>

          <div class="stagger d-3 risk-card bg-gradient-to-b from-amber-500 to-orange-700">
            <div class="risk-card-icon bg-amber-500 text-xl font-mono-code font-bold">3,5MB</div>
            <h3 class="font-bold text-lg text-white">Ma et al. (2026)</h3>
            <p class="text-xs text-amber-100 mt-2 leading-relaxed">
              Comprime <strong>AHE-YOLO11</strong> a solo <strong>3,5 MB (1,56 M parámetros)</strong> alcanzando <strong>333,3 FPS (+16,5 %)</strong> en laboratorio.
            </p>
          </div>

          <div class="stagger d-4 risk-card bg-gradient-to-b from-orange-600 to-red-700">
            <div class="risk-card-icon bg-orange-500 text-2xl">⚡</div>
            <h3 class="font-bold text-lg text-white">Shamta y Demir</h3>
            <p class="text-xs text-orange-100 mt-2 leading-relaxed">
              Envía <strong>solo foto de alerta + GPS por red GSM en segundos</strong> frente a las horas que tardan los satélites o rondas a pie.
            </p>
          </div>
        </div>

        <!-- Nota crítica inferior idéntica a 00:22 -->
        <div class="stagger d-5 max-w-4xl mx-auto flex items-center gap-3 px-5 py-3 rounded-2xl bg-white/5 border border-white/10 text-xs sm:text-sm text-slate-200">
          <span class="w-6 h-6 rounded-full bg-amber-400 text-slate-950 font-bold flex items-center justify-center shrink-0">i</span>
          <span><strong>Crítica Metodológica del Informe:</strong> Mientras Luo et al. (2025) y Shamta y Demir (2024) midieron <strong>30 FPS en minicomputadoras Jetson Nano reales montadas en drones</strong>, los <strong>333,3 FPS de Ma et al. (2026)</strong> se midieron en tarjetas gráficas potentes de laboratorio.</span>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         ESCENA 12 (00:24 de @trazomedico): CARRUSEL DE FOTOS CIRCULARES (RESULTADOS OE3)
         ======================================================================== -->
    <section class="scene" data-scene="11" data-hero="bg-blur" data-img="./assets/image17.png"
      data-speaker="Expositor 4 · George Flores (Resultados Objetivo Específico 3: Geodatos GIS)"
      data-script="En el Objetivo Específico 3 evaluamos la eficiencia del almacenamiento georreferenciado para mapas de calor. Md Jelas et al. (2024) demostraron que U-Net y DeepLabV3+ logran entre 92,78 % y 98,14 % de exactitud separando píxel por píxel bosque sano de terreno talado, superando el 98 % con drones en la Amazonía peruana y reduciendo semanas de trabajo manual a minutos. Borse et al. (2025) probaron en más de 10 400 árboles que cruzar fotos de dron de menos de 10 cm/píxel con archivos GeoJSON y Shapefiles alcanza 98,39 % con VGG16 y AUC 0,95 con YOLOv8. Guardar puntos y polígonos ligeros en GeoJSON es mucho más eficiente que guardar videos pesados.">
      <div class="w-full max-w-6xl mx-auto text-center space-y-6">
        <div class="space-y-1">
          <div class="stagger d-1 text-sm font-bold tracking-widest text-emerald-400 uppercase">OBJETIVO ESPECÍFICO 3 · ALMACENAMIENTO ESPACIAL Y DEFORESTACIÓN</div>
          <h2 class="stagger d-1 title-condensed text-5xl sm:text-6xl text-white">
            HISTORIAL GEORREFERENCIADO Y <span class="text-orange-400">GEOJSON</span>
          </h2>
        </div>

        <!-- 3 Tarjetas de Cristal con imagen circular adentro (idénticas a 00:24) -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-7 pt-2">
          <div class="stagger d-2 space-y-3">
            <div class="text-3xl">🔍</div>
            <div class="frost-carousel-card text-center">
              <h3 class="font-bold text-base text-white">Resolución &lt; 10 cm/píxel</h3>
              <div class="w-40 h-40 mx-auto my-4 rounded-full overflow-hidden border-2 border-emerald-400/60 shadow-lg">
                <img src="./assets/image17.png" alt="Copas de árboles" class="w-full h-full object-cover" />
              </div>
              <p class="text-xs text-slate-200 leading-relaxed">
                <strong>Borse et al. (2025):</strong> Supera los 1–5 m/píxel del satélite en <strong>&gt; 10 400 árboles</strong>, logrando <strong>98,39 % con VGG16</strong> y <strong>AUC 0,95 con YOLOv8</strong>.
              </p>
            </div>
          </div>

          <div class="stagger d-3 space-y-3">
            <div class="text-3xl">🇵🇪</div>
            <div class="frost-carousel-card text-center">
              <h3 class="font-bold text-base text-white">&gt; 98 % en Amazonía Peruana</h3>
              <div class="w-40 h-40 mx-auto my-4 rounded-full overflow-hidden border-2 border-amber-400/60 shadow-lg">
                <img src="./assets/image9.png" alt="Segmentación Tala Perú" class="w-full h-full object-cover" />
              </div>
              <p class="text-xs text-slate-200 leading-relaxed">
                <strong>Md Jelas et al. (2024):</strong> Redes <strong>U-Net y DeepLabV3+</strong> (92,78 %–98,14 %) automatizan en <strong>minutos</strong> el mapeo forestal que tomaba semanas.
              </p>
            </div>
          </div>

          <div class="stagger d-4 space-y-3">
            <div class="text-3xl">🗺️</div>
            <div class="frost-carousel-card text-center">
              <h3 class="font-bold text-base text-white">Polígonos GeoJSON y Mapas</h3>
              <div class="w-40 h-40 mx-auto my-4 rounded-full overflow-hidden border-2 border-cyan-400/60 shadow-lg">
                <img src="./assets/image14.png" alt="Mapa de Calor DEM" class="w-full h-full object-cover" />
              </div>
              <p class="text-xs text-slate-200 leading-relaxed">
                Guardar detecciones con <strong>latitud, longitud y fecha en GeoJSON / Shapefiles</strong> evita guardar videos pesados y genera <strong>mapas de calor mes a mes</strong>.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         ESCENA 13: EXPOSITOR 5 · TABLA 1 OFICIAL SINTETIZADA E INTERACTIVA
         ======================================================================== -->
    <section class="scene" data-scene="12" data-hero="bg-blur" data-img="./assets/image14.png"
      data-speaker="Expositor 5 · Jelsin Reyes (Tabla 1 Comparativa Oficial)"
      data-script="En la Tabla 1 de nuestro informe comparamos los resultados cuantitativos de los siete autores revisados frente a nuestros tres objetivos específicos: exactitud y control de falsos positivos (Objetivo 1), rendimiento, peso y tiempo de respuesta (Objetivo 2), y georreferenciación y mapas de deforestación (Objetivo 3).">
      <div class="w-full max-w-6xl mx-auto space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-3">
          <h2 class="stagger d-1 title-condensed text-4xl sm:text-5xl text-white">
            TABLA 1. COMPARACIÓN CIENTÍFICA (SCOPUS 2023–2026)
          </h2>
          <div class="stagger d-1 flex gap-1.5 bg-black/50 p-1 rounded-xl border border-white/15 text-xs">
            <button onclick="filterTableCol(0)" class="t-filter px-3 py-1 rounded-lg bg-emerald-500 text-slate-950 font-bold">Todos</button>
            <button onclick="filterTableCol(1)" class="t-filter px-3 py-1 rounded-lg text-slate-300 hover:bg-white/10">Obj. 1 (Exactitud)</button>
            <button onclick="filterTableCol(2)" class="t-filter px-3 py-1 rounded-lg text-slate-300 hover:bg-white/10">Obj. 2 (Velocidad)</button>
            <button onclick="filterTableCol(3)" class="t-filter px-3 py-1 rounded-lg text-slate-300 hover:bg-white/10">Obj. 3 (Geodatos)</button>
          </div>
        </div>

        <div class="stagger d-2 rounded-2xl overflow-hidden bg-black/60 backdrop-blur-2xl border border-white/15 shadow-2xl">
          <table class="w-full text-left border-collapse text-xs">
            <thead>
              <tr class="bg-emerald-950/80 text-emerald-300 font-mono-code uppercase text-[11px] border-b border-white/15">
                <th class="py-3 px-3.5">Autor (Año)</th>
                <th class="py-3 px-3.5">Modelo / Sistema</th>
                <th class="py-3 px-3.5 tc-1">Exactitud y Falsos Positivos (Obj. 1)</th>
                <th class="py-3 px-3.5 tc-2">Rendimiento y Peso (Obj. 2)</th>
                <th class="py-3 px-3.5 tc-3">Georreferenciación (Obj. 3)</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-white/10 text-slate-200">
              <tr>
                <td class="py-2.5 px-3.5 font-bold text-white">Saydirasulovich (2023)</td>
                <td class="py-2.5 px-3.5 font-mono-code text-amber-300">YOLOv8 + BiFormer + GSConv</td>
                <td class="py-2.5 px-3.5 tc-1"><strong>79,4 % AP</strong> humo (71,3 % pequeño / 92,6 % grande)</td>
                <td class="py-2.5 px-3.5 tc-2">GSConv reduce memoria en vuelo</td>
                <td class="py-2.5 px-3.5 tc-3 text-slate-400">Solo detección visual en vuelo</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3.5 font-bold text-white">Md Jelas et al. (2024)</td>
                <td class="py-2.5 px-3.5 font-mono-code text-emerald-300">U-Net + DeepLabV3+</td>
                <td class="py-2.5 px-3.5 tc-1"><strong>92,78 %–98,14 %</strong> tala (<strong>&gt;98 % Perú</strong>)</td>
                <td class="py-2.5 px-3.5 tc-2">Mapeo automático en <strong>minutos</strong></td>
                <td class="py-2.5 px-3.5 tc-3">Segmentación por píxeles e historial</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3.5 font-bold text-white">Shamta y Demir (2024)</td>
                <td class="py-2.5 px-3.5 font-mono-code text-cyan-300">Jetson Nano + RPi + YOLOv8</td>
                <td class="py-2.5 px-3.5 tc-1"><strong>96 % clasificación</strong> / 89 % en vuelo</td>
                <td class="py-2.5 px-3.5 tc-2"><strong>Alerta GSM inmediata</strong> (~25 min bat.)</td>
                <td class="py-2.5 px-3.5 tc-3">Envía foto + <strong>latitud/longitud GPS</strong></td>
              </tr>
              <tr>
                <td class="py-2.5 px-3.5 font-bold text-white">Yun et al. (2025)</td>
                <td class="py-2.5 px-3.5 font-mono-code text-orange-300">YOLOv8 + SPDConv + MLCA</td>
                <td class="py-2.5 px-3.5 tc-1"><strong>+5,5 % sensibilidad</strong> (&gt;3 200 fotos)</td>
                <td class="py-2.5 px-3.5 tc-2"><strong>-43,8 % parámetros</strong> (5,96 M)</td>
                <td class="py-2.5 px-3.5 tc-3">Focos pequeños tras ramas en montaña</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3.5 font-bold text-white">Luo et al. (2025)</td>
                <td class="py-2.5 px-3.5 font-mono-code text-emerald-300">YOLO-UFS (MobileNetV4)</td>
                <td class="py-2.5 px-3.5 tc-1"><strong>91,3 % mAP</strong> (filtra sol y neblina)</td>
                <td class="py-2.5 px-3.5 tc-2"><strong>-74 % peso (7,4 MB a 30 FPS)</strong></td>
                <td class="py-2.5 px-3.5 tc-3">Estabilización frente al viento</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3.5 font-bold text-white">Borse et al. (2025)</td>
                <td class="py-2.5 px-3.5 font-mono-code text-cyan-300">AETDA (VGG16 + YOLOv8)</td>
                <td class="py-2.5 px-3.5 tc-1"><strong>98,39 % exactitud</strong> (10 400 árboles)</td>
                <td class="py-2.5 px-3.5 tc-2"><strong>AUC 0,95</strong> rápido por copa</td>
                <td class="py-2.5 px-3.5 tc-3"><strong>GeoJSON y Shapefiles (&lt;10 cm/px)</strong></td>
              </tr>
              <tr class="bg-emerald-500/15">
                <td class="py-2.5 px-3.5 font-bold text-emerald-300">Ma et al. (2026)</td>
                <td class="py-2.5 px-3.5 font-mono-code text-emerald-300 font-bold">AHE-YOLO (YOLO11)</td>
                <td class="py-2.5 px-3.5 tc-1"><strong>94,8 % mAP</strong> / 85,1 % sensibilidad</td>
                <td class="py-2.5 px-3.5 tc-2"><strong>Solo 3,5 MB y 333,3 FPS</strong></td>
                <td class="py-2.5 px-3.5 tc-3">Mapas térmicos de activación</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         ESCENA 14 (00:11 / 00:13 style): OBJETO 3D A LA IZQUIERDA + DISCUSIÓN CRÍTICA A LA DERECHA
         ======================================================================== -->
    <section class="scene" data-scene="13" data-hero="left" data-img="./assets/image18.png"
      data-speaker="Expositor 5 · Jelsin Reyes (Discusión Crítica: Consensos, Controversias y Lagunas)"
      data-script="En la discusión crítica identificamos: Primero, dos consensos plenos: el dron (<10 cm/píxel bajo las nubes) supera al satélite (1 a 5 m/píxel), y el límite de batería (~25 min) obliga a comprimir los modelos. Segundo, dos controversias técnicas: Saydirasulovich prioriza detectar humo primero, pero Yun, Luo y Ma rebaten que la neblina andina imita al humo y exigen combinar con focos de calor e imágenes negativas; además, Shamta y Luo procesan a bordo en una Jetson Nano, mientras Borse procesa en estación base con VGG16. Tercero, dos oportunidades para La Libertad: integrar cámaras térmicas infrarrojas para brasas nocturnas en ichu, y redes de radio LoRaWAN con guardado local para quebradas sin cobertura celular GSM.">
      <div class="w-full max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-12 items-center">
        <div class="lg:col-span-5"></div>
        <div class="lg:col-span-7 space-y-4 lg:pl-6">
          <h2 class="stagger d-1 title-condensed text-5xl sm:text-6xl text-white">
            DISCUSIÓN CRÍTICA Y PROPUESTA ANDINA
          </h2>

          <div class="stagger d-2 glow-bar">
            <div class="text-xs font-mono-code text-emerald-400 font-bold uppercase">✅ 1. Consensos Científicos</div>
            <p class="text-xs sm:text-sm text-slate-200 mt-1">
              El dron (<strong>&lt;10 cm/píxel</strong>, volando bajo nubes) supera ampliamente al satélite (1–5 m/píxel), y la batería (<strong>~25 min</strong>) exige comprimir los algoritmos a bordo.
            </p>
          </div>

          <div class="stagger d-3 glow-bar" style="border-color: rgba(245, 158, 11, 0.55);">
            <div class="text-xs font-mono-code text-amber-300 font-bold uppercase">⚡ 2. Controversias Técnicas en la Literatura</div>
            <p class="text-xs sm:text-sm text-slate-200 mt-1">
              • <strong>¿Humo vs. Llamas/Calor?</strong> <em>Saydirasulovich (2023)</em> prioriza el humo, pero <em>Yun, Luo y Ma</em> rebaten que en montaña la <strong>neblina matutina imita al humo joven</strong>, exigiendo combinar con calor e imágenes negativas.<br/>
              • <strong>¿Edge AI vs. Estación Base?</strong> <em>Shamta y Luo</em> procesan en vuelo con <strong>Jetson Nano</strong>; <em>Borse</em> procesa en estación base con <strong>VGG16 (98,39 %)</strong>.
            </p>
          </div>

          <div class="stagger d-4 glow-bar" style="border-color: rgba(249, 115, 22, 0.65);">
            <div class="text-xs font-mono-code text-orange-400 font-bold uppercase">⛰️ 3. Lagunas y Propuesta para La Libertad</div>
            <p class="text-xs sm:text-sm text-slate-200 mt-1">
              • <strong>Cámara Térmica Infrarroja:</strong> Superar el sesgo de cámaras RGB diurnas detectando brasas nocturnas en pastizales de <strong>ichu, eucalipto y panllevar</strong>.<br/>
              • <strong>Red de Radio LoRaWAN + Caché Local:</strong> Para quebradas de Santiago de Chuco, Otuzco, Sánchez Carrión, Bolívar y Pataz sin señal celular GSM.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         ESCENA 15 (00:20 de @trazomedico): CONCLUSIÓN GENERAL + PÍLDORA CENTRAL + REFERENCIAS DOI
         ======================================================================== -->
    <section class="scene" data-scene="14" data-hero="bottom-left" data-img="./assets/image19.png"
      data-speaker="Conclusión General y Referencias · Ingeniería de Sistemas UCV 2026"
      data-script="En conclusión, la síntesis crítica de los resultados y discusiones de quienes ya implementaron estas tecnologías confirma que un sistema de información con drones inteligentes y algoritmos ligeros logra reducir el tiempo de detección de anomalías forestales de varias horas a pocos segundos, respondiendo de forma sólida al problema de investigación planteado en la región La Libertad. ¡Muchas gracias por su atención!">
      <div class="w-full max-w-5xl mx-auto text-center space-y-6">
        <h2 class="stagger d-1 title-condensed text-5xl sm:text-7xl text-white">
          CONCLUSIÓN GENERAL · UCV 2026
        </h2>

        <!-- Píldora central iluminada idéntica a 'MORFOLOGÍA DE LAS VEGETACIONES' (00:20) -->
        <div class="stagger d-2 inline-block px-8 py-4 rounded-2xl bg-gradient-to-r from-orange-600 via-amber-500 to-emerald-600 text-white font-bold text-base sm:text-xl shadow-[0_0_45px_rgba(249,115,22,0.5)] border border-white/30">
          De varias horas de espera satelital a pocos segundos que salvan nuestros bosques andinos
        </div>

        <p class="stagger d-3 text-sm sm:text-lg text-slate-200 max-w-3xl mx-auto leading-relaxed">
          Unir <strong>drones inteligentes (&lt;10 cm/píxel)</strong>, algoritmos ultraligeros (<strong>YOLO11 de 3,5 MB / U-Net &gt;98 %</strong>), <strong>cámaras térmicas</strong>, radio <strong>LoRaWAN</strong> y bases de datos <strong>GeoJSON</strong> responde de manera integral a la emergencia forestal en <strong>La Libertad</strong>.
        </p>

        <!-- Botones limpios de acceso a Referencias Scopus / DOI (Anexo 2) -->
        <div class="stagger d-4 pt-2 flex flex-wrap justify-center gap-2.5 max-w-4xl mx-auto text-xs font-mono-code">
          <a href="https://doi.org/10.3390/s23208374" target="_blank" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-emerald-500 hover:text-slate-950 border border-white/15 transition-all">🔗 Saydirasulovich (2023) DOI</a>
          <a href="https://doi.org/10.3389/ffgc.2024.1300060" target="_blank" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-emerald-500 hover:text-slate-950 border border-white/15 transition-all">🔗 Md Jelas (2024) DOI</a>
          <a href="https://doi.org/10.1371/journal.pone.0299058" target="_blank" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-emerald-500 hover:text-slate-950 border border-white/15 transition-all">🔗 Shamta y Demir (2024) DOI</a>
          <a href="https://doi.org/10.3390/fire8040138" target="_blank" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-emerald-500 hover:text-slate-950 border border-white/15 transition-all">🔗 Yun et al. (2025) DOI</a>
          <a href="https://doi.org/10.3390/f16050743" target="_blank" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-emerald-500 hover:text-slate-950 border border-white/15 transition-all">🔗 Luo et al. (2025) DOI</a>
          <a href="https://doi.org/10.1371/journal.pone.0335009" target="_blank" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-emerald-500 hover:text-slate-950 border border-white/15 transition-all">🔗 Borse et al. (2025) DOI</a>
          <a href="https://doi.org/10.3390/su18052436" target="_blank" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-emerald-500 hover:text-slate-950 border border-white/15 transition-all">🔗 Ma et al. (2026) DOI</a>
        </div>
      </div>
    </section>

  </main>

  <!-- ==========================================================================
       CONTROLES MINIMALISTAS INFERIORES (SIN AMONTONAR LA PANTALLA)
       Autor: César Quiroz
       ========================================================================== -->
  <div class="fixed bottom-4 right-8 z-40 flex items-center gap-2">
    <button onclick="prevScene()" class="w-9 h-9 rounded-full bg-white/10 hover:bg-white/20 border border-white/15 text-white flex items-center justify-center transition-all" title="Anterior (←)">
      ‹
    </button>
    <span class="px-3 py-1 rounded-full bg-black/50 border border-white/10 font-mono-code text-xs text-emerald-400">
      <span id="sceneNumLabel">01</span> / 15
    </span>
    <button onclick="nextScene()" class="w-9 h-9 rounded-full bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold flex items-center justify-center transition-all shadow-lg shadow-emerald-500/30" title="Siguiente (→)">
      ›
    </button>
  </div>

  <!-- ==========================================================================
       MOTOR JAVASCRIPT DE COREOGRAFÍA MORPH Y PARTÍCULAS 3D
       Autor: César Quiroz
       ========================================================================== -->
  <script>
    /**
     * Controlador de coreografía Morph del Objeto 3D y transición de escenas
     * Autor: César Quiroz
     */
    const scenes = Array.from(document.querySelectorAll('.scene'));
    const totalScenes = scenes.length;
    let currentScene = 0;
    let isMoving = false;

    function goToScene(index) {
      if (index < 0 || index >= totalScenes) return;
      if (isMoving && index !== currentScene) return;
      isMoving = true;
      setTimeout(() => { isMoving = false; }, 650);

      scenes.forEach((sc, i) => {
        sc.classList.remove('active', 'prev');
        if (i < index) sc.classList.add('prev');
      });

      currentScene = index;
      const active = scenes[currentScene];
      active.classList.add('active');

      // 1. Mover el Objeto 3D persistente a su nueva posición en pantalla (center, bg-blur, right, left, right-edge, bottom-left)
      const heroPos = active.dataset.hero || 'center';
      document.body.setAttribute('data-hero-pos', heroPos);

      // 2. Crossfade suave sin parpadeo dentro de la esfera 3D y el fondo difuminado
      const imgPath = active.dataset.img || './assets/image1.png';
      const sphereImg = document.getElementById('heroSphereImg');
      const bgImg = document.getElementById('bgPhotoLayer');
      if (sphereImg.getAttribute('src') !== imgPath) {
        sphereImg.style.opacity = '0.25';
        sphereImg.style.transform = 'scale(1.22) rotate(4deg)';
        setTimeout(() => {
          sphereImg.src = imgPath;
          bgImg.src = imgPath;
          sphereImg.style.opacity = '1';
          sphereImg.style.transform = 'scale(1.1) rotate(0deg)';
        }, 220);
      }

      // 3. Actualizar cabecera minimalista y contador
      document.getElementById('sceneNumLabel').textContent = String(currentScene + 1).padStart(2, '0');
      document.getElementById('headerSpeakerLabel').textContent = active.dataset.speaker || '';

      // 4. Actualizar Guion del Expositor
      document.getElementById('scriptSpeakerTitle').textContent = active.dataset.speaker || '';
      document.getElementById('scriptBodyText').textContent = active.dataset.script || '';

      // 5. Animar barras de exactitud si la escena las tiene
      active.querySelectorAll('.bar-fill').forEach(bar => {
        bar.style.width = '0%';
        setTimeout(() => { bar.style.width = bar.dataset.width; }, 160);
      });
    }

    function nextScene() {
      if (currentScene < totalScenes - 1) goToScene(currentScene + 1);
    }

    function prevScene() {
      if (currentScene > 0) goToScene(currentScene - 1);
    }

    function toggleMenuDrawer() {
      document.getElementById('menuDrawer').classList.toggle('hidden');
    }

    function toggleScriptModal() {
      document.getElementById('scriptModal').classList.toggle('hidden');
    }

    function toggleFullScreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(() => {});
      } else {
        document.exitFullscreen().catch(() => {});
      }
    }

    function filterTableCol(colIdx) {
      document.querySelectorAll('.t-filter').forEach((btn, i) => {
        btn.className = i === colIdx
          ? 't-filter px-3 py-1 rounded-lg bg-emerald-500 text-slate-950 font-bold'
          : 't-filter px-3 py-1 rounded-lg text-slate-300 hover:bg-white/10';
      });
      [1, 2, 3].forEach(c => {
        document.querySelectorAll('.tc-' + c).forEach(cell => {
          cell.style.opacity = (colIdx === 0 || colIdx === c) ? '1' : '0.28';
          cell.style.background = (colIdx === c) ? 'rgba(16, 185, 129, 0.16)' : 'transparent';
        });
      });
    }

    // Teclado
    window.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') {
        e.preventDefault();
        nextScene();
      } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
        e.preventDefault();
        prevScene();
      } else if (e.key === 'f' || e.key === 'F') {
        toggleFullScreen();
      } else if (e.key === 'g' || e.key === 'G') {
        toggleScriptModal();
      } else if (e.key === 'm' || e.key === 'M') {
        toggleMenuDrawer();
      }
    });

    // Rueda del mouse suave
    let wheelLock = false;
    window.addEventListener('wheel', (e) => {
      if (wheelLock || Math.abs(e.deltaY) < 25) return;
      wheelLock = true;
      if (e.deltaY > 0) nextScene();
      else prevScene();
      setTimeout(() => { wheelLock = false; }, 680);
    }, { passive: true });

    // Partículas Bokeh 3D flotantes (como las células/esferas del inicio de @trazomedico)
    const canvas = document.getElementById('bokehCanvas');
    const ctx = canvas.getContext('2d');
    let orbs = [];

    function resize() {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resize);
    resize();

    for (let i = 0; i < 24; i++) {
      orbs.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        r: Math.random() * 26 + 8,
        vx: (Math.random() - 0.5) * 0.35,
        vy: (Math.random() - 0.5) * 0.35,
        alpha: Math.random() * 0.22 + 0.05,
        warm: i % 3 === 0
      });
    }

    function animateBokeh() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      orbs.forEach(o => {
        o.x += o.vx;
        o.y += o.vy;
        if (o.x < -40) o.x = canvas.width + 40;
        if (o.x > canvas.width + 40) o.x = -40;
        if (o.y < -40) o.y = canvas.height + 40;
        if (o.y > canvas.height + 40) o.y = -40;

        const grad = ctx.createRadialGradient(o.x - o.r * 0.3, o.y - o.r * 0.3, o.r * 0.1, o.x, o.y, o.r);
        if (o.warm) {
          grad.addColorStop(0, `rgba(251, 146, 60, ${o.alpha * 1.6})`);
          grad.addColorStop(1, 'rgba(251, 146, 60, 0)');
        } else {
          grad.addColorStop(0, `rgba(52, 211, 153, ${o.alpha * 1.6})`);
          grad.addColorStop(1, 'rgba(16, 185, 129, 0)');
        }
        ctx.beginPath();
        ctx.arc(o.x, o.y, o.r, 0, Math.PI * 2);
        ctx.fillStyle = grad;
        ctx.fill();
      });
      requestAnimationFrame(animateBokeh);
    }
    animateBokeh();

    goToScene(0);
  </script>
</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

def embed_img(m):
    rel = m.group(0).replace("./", "")
    full = os.path.join(base_dir, rel)
    if os.path.exists(full):
        with open(full, "rb") as img_f:
            return "data:image/png;base64," + base64.b64encode(img_f.read()).decode("ascii")
    return m.group(0)

portable_html = re.sub(r"\./assets/[a-zA-Z0-9_]+\.png", embed_img, html_content)
with open(portable_path, "w", encoding="utf-8") as f:
    f.write(portable_html)

print("Generated @trazomedico style presentation! Portable size:", os.path.getsize(portable_path))
