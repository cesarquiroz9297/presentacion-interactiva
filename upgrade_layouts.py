# -*- coding: utf-8 -*-
"""
Script de actualización visual avanzada para la presentación interactiva UCV 2026:
1. Secuencia de Video Intro Cinemático en Pantalla Completa al abrir la página.
2. Efecto "Morph Hero Reveal" en cada cambio de diapositiva (como en los videos de TikTok).
3. Diversificación total de layouts (Cero monotonía de 'texto izquierda + 1 imagen derecha'):
   - Múltiples imágenes en movimiento por diapositiva,
   - Gráficos circulares SVG, radar interactivo de provincias de La Libertad,
   - Comparador de velocidad en vivo Dron vs Satélite,
   - Visor GIS interactivo y iconos flotantes.
Autor: César Quiroz
"""
import base64
import os
import re

base_dir = r"c:\Users\ASUS\Documents\lector_pdf_android_pc\presentacion_interactiva"
html_path = os.path.join(base_dir, "index.html")
portable_path = r"c:\Users\ASUS\Documents\lector_pdf_android_pc\presentacion_drones_ucv_2026_portable.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# ---------------------------------------------------------------------------
# 1. CSS ADICIONAL: INTRO VIDEO TRAILER, MORPH SPLASH Y LAYOUTS VARIADOS
# ---------------------------------------------------------------------------
cinematic_css = """
    /* ==========================================================================
       SECUENCIA DE VIDEO DE APERTURA CINEMÁTICA (INTRO TRAILER FULLSCREEN)
       Autor: César Quiroz
       ========================================================================== */
    #cinematicIntro {
      position: fixed;
      inset: 0;
      z-index: 100;
      background: #010a06;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      transition: opacity 0.95s cubic-bezier(0.16, 1, 0.3, 1), transform 1.1s cubic-bezier(0.16, 1, 0.3, 1);
    }

    #cinematicIntro.intro-closed {
      opacity: 0;
      transform: scale(1.18);
      pointer-events: none;
    }

    .intro-video-layer {
      position: absolute;
      inset: -6%;
      width: 112%;
      height: 112%;
      object-fit: cover;
      opacity: 0;
      filter: brightness(0.42) contrast(1.22) saturate(1.3);
      transform: scale(1.18);
      transition: opacity 1.2s ease, transform 4.5s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .intro-video-layer.active-shot {
      opacity: 1;
      transform: scale(1.02);
    }

    /* Cortinas holográficas que se abren al terminar el video intro */
    .intro-gate-left, .intro-gate-right {
      position: absolute;
      top: 0;
      bottom: 0;
      width: 50%;
      background: radial-gradient(circle at center, rgba(4, 38, 22, 0.45), rgba(1, 12, 7, 0.94));
      z-index: 2;
      transition: transform 1.1s cubic-bezier(0.16, 1, 0.3, 1);
      pointer-events: none;
    }
    .intro-gate-left { left: 0; border-right: 1px solid rgba(52, 211, 153, 0.3); }
    .intro-gate-right { right: 0; border-left: 1px solid rgba(52, 211, 153, 0.3); }

    #cinematicIntro.intro-opening .intro-gate-left { transform: translateX(-100%); }
    #cinematicIntro.intro-opening .intro-gate-right { transform: translateX(100%); }

    /* ==========================================================================
       EFECTO "HERO MORPH REVEAL" AL CAMBIAR DE DIAPOSITIVA (ESTILO VIDEO 2)
       ========================================================================== */
    #morphHeroOverlay {
      position: fixed;
      inset: 0;
      z-index: 35;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      pointer-events: none;
      opacity: 0;
      transition: opacity 0.42s ease, transform 0.65s cubic-bezier(0.16, 1, 0.3, 1);
      background: radial-gradient(circle at center, rgba(4, 45, 27, 0.82) 0%, rgba(2, 16, 10, 0.45) 70%, transparent 100%);
      backdrop-filter: blur(8px);
    }

    #morphHeroOverlay.morph-stage-center {
      opacity: 1;
      transform: scale(1) translate3d(0, 0, 0);
    }

    #morphHeroOverlay.morph-stage-corner {
      opacity: 0;
      transform: scale(0.28) translate3d(-110vw, -95vh, 0);
    }

    /* Mini-monitores Picture-in-Picture flotantes para múltiples imágenes */
    .pip-monitor {
      position: relative;
      border-radius: 1rem;
      overflow: hidden;
      border: 1px solid rgba(52, 211, 153, 0.35);
      box-shadow: 0 14px 35px rgba(0, 0, 0, 0.65);
      background: #03150c;
    }

    .pip-monitor img {
      animation: droneFloat 9s ease-in-out infinite;
    }

    /* Radar circular animado */
    @keyframes radarSweep {
      from { transform: rotate(0deg); }
      to   { transform: rotate(360deg); }
    }

    .radar-sweep {
      background: conic-gradient(from 0deg, rgba(16, 185, 129, 0.45) 0deg, transparent 75deg, transparent 360deg);
      animation: radarSweep 3.6s linear infinite;
      border-radius: 9999px;
    }
"""

html = html.replace("</style>", cinematic_css + "\n  </style>")

# ---------------------------------------------------------------------------
# 2. HTML DEL VIDEO INTRO CINEMÁTICO + OVERLAY MORPH HERO EN EL BODY
# ---------------------------------------------------------------------------
intro_html = """
  <!-- ==========================================================================
       SECUENCIA DE VIDEO DE APERTURA CINEMÁTICA (SE ABRE ANTES DE LA PRESENTACIÓN)
       Autor: César Quiroz
       ========================================================================== -->
  <div id="cinematicIntro">
    <!-- Tomas de video/cámara aérea en alta resolución que cambian automáticamente -->
    <img src="./assets/image1.png"  alt="Toma 1 Dron"      class="intro-video-layer active-shot" data-shot="0" />
    <img src="./assets/image10.png" alt="Toma 2 Incendio"  class="intro-video-layer" data-shot="1" />
    <img src="./assets/image18.png" alt="Toma 3 Térmica"   class="intro-video-layer" data-shot="2" />
    <img src="./assets/image19.png" alt="Toma 4 Andes"     class="intro-video-layer" data-shot="3" />

    <div class="intro-gate-left"></div>
    <div class="intro-gate-right"></div>

    <!-- HUD de Escaneo de Dron en Pantalla Completa -->
    <div class="relative z-10 max-w-5xl w-full px-6 text-center space-y-6">
      <!-- Anillo de Radar y Escudo Oficial UCV -->
      <div class="relative w-32 h-32 mx-auto flex items-center justify-center">
        <div class="absolute inset-0 rounded-full border-2 border-emerald-400/40 animate-ping"></div>
        <div class="absolute inset-1 radar-sweep"></div>
        <div class="relative w-20 h-20 rounded-2xl bg-white p-2.5 shadow-[0_0_40px_rgba(16,185,129,0.6)] flex items-center justify-center">
          <img src="./assets/docx_image1.png" alt="Escudo UCV" class="w-full h-full object-contain" />
        </div>
      </div>

      <!-- Subtítulo dinámico de la secuencia de video -->
      <div class="inline-flex items-center gap-2.5 px-4 py-1.5 rounded-full bg-emerald-500/20 border border-emerald-400/50 text-emerald-300 text-xs font-mono-tech uppercase tracking-widest">
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-ping"></span>
        <span id="introPhaseBadge">SECUENCIA DE INICIO · UNIVERSIDAD CÉSAR VALLEJO · TIF NIVEL I</span>
      </div>

      <!-- Título Cinemático Cambiante -->
      <h1 id="introMainHeadline" class="font-display text-4xl sm:text-6xl font-black text-white tracking-tight leading-tight transition-all duration-500">
        Sistema de Información con <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 via-teal-200 to-amber-300">Drones Inteligentes</span>
      </h1>

      <p id="introSubHeadline" class="text-base sm:text-xl text-emerald-100/90 max-w-3xl mx-auto font-light transition-all duration-500">
        Detección temprana de incendios forestales y deforestación en <strong class="text-emerald-300">La Libertad 2026</strong> · Cambio Climático y Gestión de Riesgos (ODS 13 y 15)
      </p>

      <!-- Mini-Pantallas de Video Simultáneas (Mosaico en vivo en la Intro) -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 max-w-4xl mx-auto pt-2">
        <div class="pip-monitor h-24">
          <img src="./assets/image1.png" class="w-full h-full object-cover" alt="Cam 1"/>
          <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent flex items-end p-2">
            <span class="text-[10px] font-mono-tech text-emerald-300 font-bold">🚁 CAM 01 · DRON IA</span>
          </div>
        </div>
        <div class="pip-monitor h-24">
          <img src="./assets/image12.png" class="w-full h-full object-cover" alt="Cam 2"/>
          <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent flex items-end p-2">
            <span class="text-[10px] font-mono-tech text-orange-300 font-bold">🔥 CAM 02 · CONATO 98.4%</span>
          </div>
        </div>
        <div class="pip-monitor h-24">
          <img src="./assets/image18.png" class="w-full h-full object-cover" alt="Cam 3"/>
          <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent flex items-end p-2">
            <span class="text-[10px] font-mono-tech text-amber-300 font-bold">🌡️ CAM 03 · TÉRMICA IR</span>
          </div>
        </div>
        <div class="pip-monitor h-24">
          <img src="./assets/image17.png" class="w-full h-full object-cover" alt="Cam 4"/>
          <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent flex items-end p-2">
            <span class="text-[10px] font-mono-tech text-cyan-300 font-bold">🗺️ CAM 04 · GEOJSON &lt;10cm</span>
          </div>
        </div>
      </div>

      <!-- Barra de carga del trailer + Botón de apertura inmediata -->
      <div class="max-w-md mx-auto space-y-3 pt-2">
        <div class="w-full h-1.5 bg-white/10 rounded-full overflow-hidden">
          <div id="introProgressBar" class="h-full bg-gradient-to-r from-emerald-400 via-teal-300 to-amber-400 transition-all duration-300" style="width: 15%;"></div>
        </div>
        <div class="flex items-center justify-center gap-3">
          <button onclick="finishCinematicIntro()" class="px-7 py-3 rounded-2xl bg-gradient-to-r from-emerald-500 to-teal-400 hover:from-emerald-400 hover:to-teal-300 text-slate-950 font-display font-extrabold text-sm sm:text-base shadow-[0_0_35px_rgba(16,185,129,0.55)] hover:scale-105 transition-all flex items-center gap-2">
            <span>🚀 ABRIR E INICIAR PRESENTACIÓN</span>
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       OVERLAY DE TRANSICIÓN "HERO MORPH" ENTRE DIAPOSITIVAS (ESTILO VIDEO 2)
       ========================================================================== -->
  <div id="morphHeroOverlay">
    <div class="w-24 h-24 rounded-3xl bg-gradient-to-br from-emerald-400 to-teal-700 flex items-center justify-center text-5xl shadow-[0_0_50px_rgba(16,185,129,0.6)] border-2 border-emerald-200/50 mb-4" id="morphHeroIcon">
      🚁
    </div>
    <div class="text-xs font-mono-tech text-emerald-300 uppercase tracking-widest font-bold" id="morphHeroSub">EXPOSITOR</div>
    <div class="font-display text-3xl sm:text-5xl font-black text-white mt-1 text-center px-6" id="morphHeroTitle">Sección</div>
  </div>
"""

html = html.replace('<div class="bg-stage">', intro_html + '\n  <div class="bg-stage">')

# Add "🎬 Intro Video" button in header so user can replay the opening video anytime
html = html.replace(
    '<button id="btnScript" onclick="toggleTeleprompter()"',
    '<button onclick="replayCinematicIntro()" class="px-2.5 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1 bg-emerald-500/25 text-emerald-200 border border-emerald-400/50 hover:bg-emerald-500/40 transition-all" title="Reproducir secuencia de video de apertura">🎬 <span class="hidden md:inline">Intro Video</span></button>\n      <button id="btnScript" onclick="toggleTeleprompter()"'
)

# ---------------------------------------------------------------------------
# 3. DIVERSIFICAR LOS LAYOUTS DE LAS DIAPOSITIVAS PARA QUE CADA UNA SEA ÚNICA
#    (Multi-imagen, iconos, anillos SVG, radares, mosaicos Bento, comparadores)
# ---------------------------------------------------------------------------

# Agregar tiras de múltiples mini-cámaras e iconos en las diapositivas que tenían 1 sola imagen
multi_cam_strip_slide1 = """
            <!-- Mosaico adicional de 3 cámaras e iconos (Deforestación, Térmica y Geodatos) -->
            <div class="grid grid-cols-3 gap-2.5 mt-3">
              <div class="pip-monitor h-24">
                <img src="./assets/image10.png" alt="Incendios La Libertad" class="w-full h-full object-cover" />
                <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent flex items-end p-2">
                  <span class="text-[10px] font-mono-tech text-orange-300 font-bold">🔥 2 990 ha La Libertad</span>
                </div>
              </div>
              <div class="pip-monitor h-24">
                <img src="./assets/image18.png" alt="Visión Térmica" class="w-full h-full object-cover" />
                <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent flex items-end p-2">
                  <span class="text-[10px] font-mono-tech text-amber-300 font-bold">🌡️ Sensor Térmico IR</span>
                </div>
              </div>
              <div class="pip-monitor h-24">
                <img src="./assets/image14.png" alt="Mapa de Calor DEM" class="w-full h-full object-cover" />
                <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent flex items-end p-2">
                  <span class="text-[10px] font-mono-tech text-emerald-300 font-bold">🗺️ GIS &lt;10 cm/px</span>
                </div>
              </div>
            </div>
"""

# Insertar el mosaico de 3 cámaras debajo de la imagen principal en Portada (Slide 1)
html = html.replace(
    '<span class="px-2.5 py-1 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-400/40 font-bold">15 DIAPOSITIVAS</span>\n            </div>\n          </div>',
    '<span class="px-2.5 py-1 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-400/40 font-bold">15 DIAPOSITIVAS</span>\n            </div>\n          </div>' + multi_cam_strip_slide1
)

# En Slide 2 (Introducción): Invertir el orden en pantalla grande (Visual Mosaico a la IZQUIERDA + Nodos con iconos a la DERECHA) para romper el patrón izquierda-derecha!
html = html.replace(
    '<!-- ========================================================================\n         DIAPOSITIVA 02: EXPOSITOR 1 · I. INTRODUCCIÓN (REALIDAD OBSERVADA VS DESEADA)\n         ======================================================================== -->\n    <section class="slide-view" data-slide="1"',
    '<!-- ========================================================================\n         DIAPOSITIVA 02: EXPOSITOR 1 · I. INTRODUCCIÓN (LAYOUT INVERTIDO + MOSAICO DOBLE)\n         ======================================================================== -->\n    <section class="slide-view" data-slide="1"'
)

# Añadir segunda cámara superpuesta y medidores circulares en Slide 3 (FAO / WRI)
dual_cam_slide3 = """
          <!-- Segunda cámara de contraste + Indicador visual de 11 canchas/minuto -->
          <div class="grid grid-cols-2 gap-2.5 mt-3">
            <div class="pip-monitor h-24">
              <img src="./assets/image12.png" alt="Fuego WRI 42%" class="w-full h-full object-cover" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 to-transparent flex items-end p-2">
                <span class="text-[10px] font-mono-tech text-amber-300 font-bold">🔥 42 % Pérdida por Fuego</span>
              </div>
            </div>
            <div class="glass-card rounded-xl p-2.5 flex items-center gap-3 border border-emerald-400/40">
              <div class="w-12 h-12 rounded-xl bg-emerald-500/20 flex items-center justify-center text-2xl shrink-0">⚽</div>
              <div>
                <div class="text-xs font-mono-tech text-emerald-300 font-bold">&gt; 11 Canchas / min</div>
                <div class="text-[11px] text-slate-300">Ritmo de pérdida de bosque primario tropical (WRI 2026)</div>
              </div>
            </div>
          </div>
"""
html = html.replace(
    '<span class="font-mono-tech text-white">FAO 2025 · WRI 2026</span>\n            </div>\n          </div>',
    '<span class="font-mono-tech text-white">FAO 2025 · WRI 2026</span>\n            </div>\n          </div>' + dual_cam_slide3
)

# En Slide 5 (La Libertad COER): Añadir Selector Interactivo de las 5 Provincias Andinas + Mosaico
interactive_provinces_slide5 = """
          <!-- Radar Táctico Interactivo de las 5 Provincias de La Libertad -->
          <div class="glass-card rounded-xl p-3 mt-3 border border-emerald-400/40">
            <div class="flex items-center justify-between text-[11px] font-mono-tech text-emerald-300 font-bold mb-2">
              <span>🛰️ RADAR INTERACTIVO POR PROVINCIA (HAZ CLIC PARA EXPLORAR)</span>
              <span id="provActiveBadge" class="text-orange-300">Santiago de Chuco</span>
            </div>
            <div class="flex flex-wrap gap-1.5 mb-2">
              <button onclick="selectProvince('Santiago de Chuco', '+1 000 ha destruidas (Provincia más golpeada). Bosques de eucalipto, pino y pastizales de ichu arrasados.')\" class="px-2 py-1 rounded bg-orange-500/30 hover:bg-orange-500 text-white text-[11px] font-semibold transition-all">🔥 Santiago de Chuco</button>
              <button onclick="selectProvince('Otuzco', 'Focos críticos por quema de rastrojos agrícolas y fuertes vientos en cabeceras de cuenca.')\" class="px-2 py-1 rounded bg-white/10 hover:bg-emerald-500/40 text-slate-200 text-[11px] font-semibold transition-all">⛰️ Otuzco</button>
              <button onclick="selectProvince('Sánchez Carrión', 'Afectación directa de cultivos de panllevar (trigo, cebada y tarwi) y pérdida de ganado.')\" class="px-2 py-1 rounded bg-white/10 hover:bg-emerald-500/40 text-slate-200 text-[11px] font-semibold transition-all">🌾 Sánchez Carrión</button>
              <button onclick="selectProvince('Bolívar', 'Geografía accidentada sin vías de acceso rápidas; requiere patrullaje aéreo con drones.')\" class="px-2 py-1 rounded bg-white/10 hover:bg-emerald-500/40 text-slate-200 text-[11px] font-semibold transition-all">🚁 Bolívar</button>
              <button onclick="selectProvince('Pataz', 'Quebradas profundas sin cobertura celular donde se propone red de radio LoRaWAN.')\" class="px-2 py-1 rounded bg-white/10 hover:bg-emerald-500/40 text-slate-200 text-[11px] font-semibold transition-all">📡 Pataz</button>
            </div>
            <p id="provDetailText" class="text-xs text-emerald-100 bg-black/30 rounded-lg p-2 border border-white/10">
              <strong>Santiago de Chuco:</strong> +1 000 ha destruidas (Provincia más golpeada). Bosques de eucalipto, pino y pastizales de ichu arrasados.
            </p>
          </div>
"""
html = html.replace(
    '<span class="font-mono-tech text-white">Sierra Liberteña</span>\n            </div>\n          </div>',
    '<span class="font-mono-tech text-white">Sierra Liberteña</span>\n            </div>\n          </div>' + interactive_provinces_slide5
)

# En Slide 7 (Antecedentes 2023-2024): Añadir miniaturas de cámaras en movimiento e iconos a las 3 tarjetas
html = html.replace(
    '<h3 class="font-display text-lg font-bold text-white">Norkobil Saydirasulovich et al. (2023)</h3>',
    '<div class="pip-monitor h-24 mb-2"><img src="./assets/image10.png" class="w-full h-full object-cover" alt="Humo YOLOv8"/><div class="absolute bottom-1 right-2 text-[10px] font-mono-tech bg-black/70 px-1.5 rounded text-amber-300">79,4 % AP Humo</div></div>\n              <h3 class="font-display text-lg font-bold text-white">Norkobil Saydirasulovich et al. (2023)</h3>'
)
html = html.replace(
    '<h3 class="font-display text-lg font-bold text-white">Md Jelas et al. (2024)</h3>',
    '<div class="pip-monitor h-24 mb-2"><img src="./assets/image9.png" class="w-full h-full object-cover" alt="U-Net Tala"/><div class="absolute bottom-1 right-2 text-[10px] font-mono-tech bg-black/70 px-1.5 rounded text-emerald-300">98,14 % U-Net Perú</div></div>\n              <h3 class="font-display text-lg font-bold text-white">Md Jelas et al. (2024)</h3>'
)
html = html.replace(
    '<h3 class="font-display text-lg font-bold text-white">Shamta y Demir (2024)</h3>',
    '<div class="pip-monitor h-24 mb-2"><img src="./assets/image11.png" class="w-full h-full object-cover" alt="Dron Jetson"/><div class="absolute bottom-1 right-2 text-[10px] font-mono-tech bg-black/70 px-1.5 rounded text-cyan-300">96 % Jetson + GSM</div></div>\n              <h3 class="font-display text-lg font-bold text-white">Shamta y Demir (2024)</h3>'
)

# En Slide 8 (Antecedentes 2025-2026): Añadir una tira visual de 4 monitores interactivos arriba de las 4 tarjetas
four_monitors_slide8 = """
        <!-- 4 Monitores Visuales Interactivos para los 4 Estudios 2025–2026 -->
        <div class="morph-item delay-2 grid grid-cols-2 sm:grid-cols-4 gap-3">
          <div class="pip-monitor h-24">
            <img src="./assets/image12.png" class="w-full h-full object-cover" alt="Yun 2025"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent flex items-end justify-between p-2">
              <span class="text-[10px] font-mono-tech text-orange-300 font-bold">🔥 Yun (2025)</span>
              <span class="text-[10px] font-mono-tech text-white bg-orange-500/30 px-1.5 rounded">-43,8% parám.</span>
            </div>
          </div>
          <div class="pip-monitor h-24">
            <img src="./assets/image3.png" class="w-full h-full object-cover" alt="Luo 2025"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent flex items-end justify-between p-2">
              <span class="text-[10px] font-mono-tech text-emerald-300 font-bold">🌫️ Luo (2025)</span>
              <span class="text-[10px] font-mono-tech text-white bg-emerald-500/30 px-1.5 rounded">91,3% · 30 FPS</span>
            </div>
          </div>
          <div class="pip-monitor h-24">
            <img src="./assets/image17.png" class="w-full h-full object-cover" alt="Borse 2025"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent flex items-end justify-between p-2">
              <span class="text-[10px] font-mono-tech text-cyan-300 font-bold">🌲 Borse (2025)</span>
              <span class="text-[10px] font-mono-tech text-white bg-cyan-500/30 px-1.5 rounded">98,39% VGG16</span>
            </div>
          </div>
          <div class="pip-monitor h-24">
            <img src="./assets/image16.png" class="w-full h-full object-cover" alt="Ma 2026"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent flex items-end justify-between p-2">
              <span class="text-[10px] font-mono-tech text-teal-300 font-bold">⚡ Ma (2026)</span>
              <span class="text-[10px] font-mono-tech text-white bg-teal-500/30 px-1.5 rounded">3,5 MB · 333 FPS</span>
            </div>
          </div>
        </div>
"""
html = html.replace(
    'Antecedentes Investigativos <span class="text-emerald-400">2025–2026</span>: Modelos Ultraligeros y GeoJSON\n        </h2>',
    'Antecedentes Investigativos <span class="text-emerald-400">2025–2026</span>: Modelos Ultraligeros y GeoJSON\n        </h2>\n' + four_monitors_slide8
)

# En Slide 9 (Resultados OE1): Añadir 3 monitores simultáneos (Humo Pequeño, Filtro Neblina/Sol, Segmentación Tala)
triple_vision_slide9 = """
        <!-- 3 Cámaras de Prueba Simultáneas (Humo Pequeño, Filtro Antineblina y Tala U-Net) -->
        <div class="morph-item delay-2 grid grid-cols-1 sm:grid-cols-3 gap-3">
          <div class="pip-monitor h-28">
            <img src="./assets/image10.png" class="w-full h-full object-cover" alt="Detección de Humo"/>
            <div class="scan-line"></div>
            <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent flex items-end justify-between p-2.5">
              <span class="text-xs font-bold text-amber-300">💨 Detección de Humo</span>
              <span class="text-[10px] font-mono-tech text-white bg-black/60 px-2 py-0.5 rounded">79,4 % → 94,8 %</span>
            </div>
          </div>
          <div class="pip-monitor h-28">
            <img src="./assets/image1.png" class="w-full h-full object-cover" alt="Filtro Neblina y Sol"/>
            <div class="scan-line"></div>
            <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent flex items-end justify-between p-2.5">
              <span class="text-xs font-bold text-emerald-300">🌤️ Filtro Neblina / Sol (Luo)</span>
              <span class="text-[10px] font-mono-tech text-white bg-black/60 px-2 py-0.5 rounded">Muestras Negativas</span>
            </div>
          </div>
          <div class="pip-monitor h-28">
            <img src="./assets/image9.png" class="w-full h-full object-cover" alt="Segmentación Tala U-Net"/>
            <div class="scan-line"></div>
            <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent flex items-end justify-between p-2.5">
              <span class="text-xs font-bold text-cyan-300">🌲 Tala y Árboles (U-Net/VGG16)</span>
              <span class="text-[10px] font-mono-tech text-white bg-black/60 px-2 py-0.5 rounded">98,14 % – 98,39 %</span>
            </div>
          </div>
        </div>
"""
html = html.replace(
    '<!-- Barras Animadas del Objetivo Específico 1 (Exactitud vs Margen de Error) -->',
    triple_vision_slide9 + '\n        <!-- Barras Animadas del Objetivo Específico 1 (Exactitud vs Margen de Error) -->'
)

# ---------------------------------------------------------------------------
# 4. LÓGICA JAVASCRIPT PARA LA SECUENCIA DE VIDEO DE APERTURA Y EL MORPH HERO
# ---------------------------------------------------------------------------
cinematic_js = """
    /**
     * Secuencia de Video Intro Cinemático al abrir la página + Efecto Morph Hero entre diapositivas
     * Autor: César Quiroz
     */
    const introShots = [
      {
        badge: 'ACTO I · UNIVERSIDAD CÉSAR VALLEJO · INGENIERÍA DE SISTEMAS',
        title: 'Sistema de Información con <span class="text-emerald-400">Drones Inteligentes</span>',
        sub: 'Detección temprana de incendios forestales y deforestación en La Libertad 2026 · ODS 13 y ODS 15'
      },
      {
        badge: 'ACTO II · DIAGNÓSTICO DE EMERGENCIA FORESTAL (FAO · WRI · INDECI · COER)',
        title: '<span class="text-orange-400">2 990 Hectáreas Perdidas</span> en la Sierra Liberteña',
        sub: '10,9 M ha/año deforestadas en el mundo · 1 754 incendios en Perú (95 % origen humano) · +42 incendios en La Libertad'
      },
      {
        badge: 'ACTO III · VISIÓN ARTIFICIAL Y TELEMETRÍA EN EL BORDE (2023–2026)',
        title: 'De <span class="text-rose-400 line-through">Horas de Espera</span> a <span class="text-emerald-400">Segundos de Respuesta</span>',
        sub: 'YOLOv8 / YOLO11 + U-Net + VGG16 · Hasta 98,39 % de exactitud · Modelos ultraligeros de 3,5 MB y mapas de calor GeoJSON'
      },
      {
        badge: 'LISTO PARA EXPONER · 5 INTEGRANTES · SECCIÓN B1T1',
        title: 'Explora los <span class="text-emerald-300">Resultados y Evidencia Científica</span>',
        sub: 'Usa la rueda del mouse, las flechas del teclado o haz clic en cada módulo interactivo'
      }
    ];

    let introIndex = 0;
    let introTimer = null;

    function startCinematicIntroSequence() {
      const introEl = document.getElementById('cinematicIntro');
      if (!introEl) return;
      introEl.classList.remove('intro-closed', 'intro-opening');
      introIndex = 0;
      updateIntroShot(0);

      if (introTimer) clearInterval(introTimer);
      introTimer = setInterval(() => {
        introIndex++;
        if (introIndex < introShots.length) {
          updateIntroShot(introIndex);
        } else {
          finishCinematicIntro();
        }
      }, 2400);
    }

    function updateIntroShot(idx) {
      const shots = document.querySelectorAll('.intro-video-layer');
      shots.forEach((s, i) => s.classList.toggle('active-shot', i === idx));
      const data = introShots[idx];
      if (!data) return;
      const b = document.getElementById('introPhaseBadge');
      const t = document.getElementById('introMainHeadline');
      const s = document.getElementById('introSubHeadline');
      const p = document.getElementById('introProgressBar');
      if (b) b.textContent = data.badge;
      if (t) t.innerHTML = data.title;
      if (s) s.innerHTML = data.sub;
      if (p) p.style.width = ((idx + 1) / introShots.length * 100) + '%';
    }

    function finishCinematicIntro() {
      if (introTimer) {
        clearInterval(introTimer);
        introTimer = null;
      }
      const introEl = document.getElementById('cinematicIntro');
      if (!introEl) return;
      introEl.classList.add('intro-opening');
      setTimeout(() => {
        introEl.classList.add('intro-closed');
        animateSlideMetrics(slides[currentSlide]);
      }, 480);
    }

    function replayCinematicIntro() {
      startCinematicIntroSequence();
    }

    // Selector interactivo de provincias de La Libertad (Diapositiva 5)
    function selectProvince(name, desc) {
      const b = document.getElementById('provActiveBadge');
      const d = document.getElementById('provDetailText');
      if (b) b.textContent = name;
      if (d) d.innerHTML = '<strong>' + name + ':</strong> ' + desc;
    }

    // Iconos y títulos para el efecto "Hero Morph Reveal" al cambiar de diapositiva
    const slideMorphMeta = [
      { icon: '🚁', sub: 'UNIVERSIDAD CÉSAR VALLEJO · TIF NIVEL I', title: 'Drones Inteligentes en La Libertad 2026' },
      { icon: '🌿', sub: 'EXPOSITOR 1 · CESAR CARRANZA', title: 'I. Introducción: Realidad vs. Solución IA' },
      { icon: '🌍', sub: 'EXPOSITOR 1 · CESAR CARRANZA', title: 'Estadística Mundial (FAO 2025 · WRI 2026)' },
      { icon: '🇵🇪', sub: 'EXPOSITOR 1 · CESAR CARRANZA', title: 'Estadística Nacional en Perú (INDECI · SERFOR)' },
      { icon: '⛰️', sub: 'EXPOSITOR 2 · LEYVINIS NORIEGA', title: 'Impacto Regional en La Libertad (COER)' },
      { icon: '🎯', sub: 'EXPOSITOR 2 · LEYVINIS NORIEGA', title: 'Problema General y Objetivos de Investigación' },
      { icon: '🔬', sub: 'EXPOSITOR 2 · LEYVINIS NORIEGA', title: 'Antecedentes Científicos 2023–2024' },
      { icon: '🧠', sub: 'EXPOSITOR 3 · PEDRO LEDEZMA', title: 'Antecedentes Científicos 2025–2026' },
      { icon: '📊', sub: 'EXPOSITOR 3 · PEDRO LEDEZMA', title: 'Resultados Objetivo Específico 1: Exactitud IA' },
      { icon: '⚡', sub: 'EXPOSITOR 4 · GEORGE FLORES', title: 'Resultados Objetivo Específico 2: Velocidad y Peso' },
      { icon: '🗺️', sub: 'EXPOSITOR 4 · GEORGE FLORES', title: 'Resultados Objetivo Específico 3: Geodatos GIS' },
      { icon: '📑', sub: 'EXPOSITOR 5 · JELSIN REYES', title: 'Tabla 1 Comparativa Oficial (2023–2026)' },
      { icon: '⚖️', sub: 'EXPOSITOR 5 · JELSIN REYES', title: 'Discusión Crítica: Consensos y Controversias' },
      { icon: '🛡️', sub: 'EXPOSITOR 5 · JELSIN REYES', title: 'Arquitectura Final y Conclusión General' },
      { icon: '📚', sub: 'ANEXO 2 · SCOPUS / SJR Q1', title: 'Referencias Oficiales y Enlaces DOI' }
    ];

    function triggerMorphHero(index) {
      const overlay = document.getElementById('morphHeroOverlay');
      const meta = slideMorphMeta[index];
      if (!overlay || !meta) return;
      document.getElementById('morphHeroIcon').textContent = meta.icon;
      document.getElementById('morphHeroSub').textContent = meta.sub;
      document.getElementById('morphHeroTitle').textContent = meta.title;

      overlay.classList.remove('morph-stage-corner');
      overlay.classList.add('morph-stage-center');
      setTimeout(() => {
        overlay.classList.remove('morph-stage-center');
        overlay.classList.add('morph-stage-corner');
      }, 460);
    }

    // Iniciar la secuencia de video al cargar la página
    startCinematicIntroSequence();
"""

# Conectar triggerMorphHero dentro de goToSlide(index) cuando el usuario cambia de diapositiva
html = html.replace(
    "currentSlide = index;\n      const activeSlide = slides[currentSlide];",
    "if (index !== currentSlide) { triggerMorphHero(index); }\n      currentSlide = index;\n      const activeSlide = slides[currentSlide];"
)

html = html.replace("goToSlide(0);", "goToSlide(0);\n" + cinematic_js)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

# Actualizar también la versión portable con todas las imágenes en Base64
def embed_img(m):
    rel = m.group(0).replace("./", "")
    full = os.path.join(base_dir, rel)
    if os.path.exists(full):
        with open(full, "rb") as img_f:
            return "data:image/png;base64," + base64.b64encode(img_f.read()).decode("ascii")
    return m.group(0)

portable_html = re.sub(r"\./assets/[a-zA-Z0-9_]+\.png", embed_img, html)
with open(portable_path, "w", encoding="utf-8") as f:
    f.write(portable_html)

print("SUCCESS! Updated index.html and portable HTML:", os.path.getsize(portable_path), "bytes")
