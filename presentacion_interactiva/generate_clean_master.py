# -*- coding: utf-8 -*-
"""
Generador Maestro Limpio (Sin inyecciones regex rotas):
- Soluciona el código JS que aparecía en el menú lateral (causado por replace en onclick="goToScene(0);").
- Elimina por completo cualquier superposición entre el Diorama 3D y los textos/títulos en las 15 escenas.
- Activa el vuelo físico en tiempo real del Robot Dron 3D Global (z-index: 65) por toda la pantalla.
Autor: César Quiroz
"""
import base64
import os
import re

base_dir = r"c:\Users\ASUS\Documents\lector_pdf_android_pc\presentacion_interactiva"
html_path = os.path.join(base_dir, "index.html")
portable_path = r"c:\Users\ASUS\Documents\lector_pdf_android_pc\presentacion_drones_ucv_2026_portable.html"

# 1. Partir de la base limpia de build_trazomedico_style.py y hacer el reemplazo ÚNICAMENTE en el bloque <script> final
with open(os.path.join(base_dir, "build_trazomedico_style.py"), "r", encoding="utf-8") as f:
    builder_code = f.read()

start_marker = 'html_content = """'
end_marker = '"""\n\nwith open(html_path'
html = builder_code.split(start_marker)[1].split(end_marker)[0]

# 2. Reemplazar #persistentHero3D por el Diorama Holográfico 3D Multicapa (SIN solapar textos)
diorama_html = """  <div id="persistentHero3D">
    <div class="diorama-3d-stage" id="dioramaStage3D">
      <!-- Capa Base 3D Biselada (Z: -45px) -->
      <div class="diorama-layer-back"></div>

      <!-- Marco Fotográfico 3D Principal (Z: +10px) -->
      <div class="diorama-main-frame">
        <img id="heroSphereImg" src="./assets/image1.png" alt="Escena 3D Principal" class="w-full h-full object-cover transition-all duration-700" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-emerald-950/25"></div>
        <div class="diorama-laser-line"></div>
        <div class="absolute bottom-3.5 left-4 right-4 flex items-center justify-between">
          <span id="dioramaCaption" class="px-3 py-1 rounded-lg bg-black/80 backdrop-blur-md border border-emerald-400/40 text-xs font-bold text-emerald-300 truncate">
            🚁 Sistema de Drones Inteligentes · UCV 2026
          </span>
          <span class="px-2.5 py-1 rounded-lg bg-emerald-500/25 border border-emerald-400/50 font-mono-code text-[10px] font-bold text-white shrink-0 ml-2">
            3D LIVE
          </span>
        </div>
      </div>

      <!-- Tarjeta KPI 3D Pop-Out Superior (Z: +70px) -->
      <div class="diorama-popout-top" id="dioramaKpiBox">
        <div class="flex items-center gap-3">
          <div id="dioramaKpiIcon" class="w-11 h-11 rounded-xl bg-gradient-to-br from-emerald-400 to-teal-600 flex items-center justify-center text-2xl shadow-lg">
            🚁
          </div>
          <div>
            <div id="dioramaKpiValue" class="title-condensed text-2xl sm:text-3xl text-white leading-none">&lt; 10 cm/px</div>
            <div id="dioramaKpiLabel" class="text-[11px] text-emerald-300 font-semibold mt-0.5">Resolución Dron IA</div>
          </div>
        </div>
      </div>

      <!-- Segunda Cámara 3D Pop-Out Inferior (Z: +88px) -->
      <div class="diorama-popout-bottom">
        <img id="dioramaSecondaryImg" src="./assets/image18.png" alt="Vista Secundaria 3D" class="w-full h-full object-cover" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent flex items-end p-2">
          <span id="dioramaSecondaryLabel" class="text-[10px] font-mono-code text-amber-300 font-bold">🌡️ Visión Térmica + RGB</span>
        </div>
      </div>
    </div>
  </div>
"""

html = re.sub(
    r'<div id="persistentHero3D">.*?<!-- ==========================================================================\s*CABECERA',
    diorama_html + '\n  <!-- ==========================================================================\n       CABECERA',
    html,
    flags=re.DOTALL
)

# 3. En la Escena 01 (Portada): alinear el título y autores a la IZQUIERDA (lg:col-span-7) y el Diorama 3D a la DERECHA (data-hero="right")
#    para que NUNCA se pisen ni se amontonen el texto con el cuadro 3D!
old_scene_01 = """    <section class="scene active" data-scene="0" data-hero="center" data-img="./assets/image1.png"
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
    </section>"""

new_scene_01 = """    <section class="scene active" data-scene="0" data-hero="right" data-img="./assets/image1.png"
      data-speaker="Portada Oficial · Grupo TIF Nivel I (Sección B1T1)"
      data-script="Buenos días/tardes estimado docente Mgtr. Luis Angel De Lucio Burga y compañeros. Presentamos nuestra investigación formativa de Nivel I de la Escuela de Ingeniería de Sistemas de la Universidad César Vallejo: Sistema de información con drones inteligentes para detección temprana de incendios forestales y deforestación en La Libertad 2026, alineada a los ODS 13 y 15.">
      <div class="w-full max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-12 items-center">
        <div class="lg:col-span-7 space-y-5 text-left pr-4">
          <div class="stagger d-1 inline-flex items-center gap-2.5 px-4 py-1.5 rounded-full bg-orange-600 text-white font-bold text-xs tracking-widest uppercase shadow-lg shadow-orange-600/40">
            <img src="./assets/docx_image1.png" alt="UCV" class="w-4 h-4 object-contain bg-white rounded-sm p-0.5" />
            UNIVERSIDAD CÉSAR VALLEJO · INGENIERÍA DE SISTEMAS · TIF NIVEL I
          </div>

          <h1 class="stagger d-2 title-condensed text-6xl sm:text-7xl xl:text-[5.6rem] font-bold tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-amber-200 via-emerald-300 to-teal-200 leading-none">
            DRONES INTELIGENTES
          </h1>

          <div class="stagger d-3 title-condensed text-2xl sm:text-3xl text-emerald-300 tracking-[0.14em]">
            DETECCIÓN TEMPRANA DE INCENDIOS FORESTALES Y DEFORESTACIÓN EN LA LIBERTAD 2026
          </div>

          <p class="stagger d-3 text-sm sm:text-base text-slate-300 max-w-xl leading-relaxed">
            Línea de Investigación: <strong class="text-white">Desarrollo de Software y Sistemas de Información</strong> · Aporte directo a los <strong class="text-emerald-300">ODS 13 (Acción por el Clima)</strong> y <strong class="text-emerald-300">ODS 15 (Ecosistemas Terrestres)</strong>.
          </p>

          <!-- Tarjetas de los 5 Integrantes Limpias -->
          <div class="stagger d-4 pt-2 space-y-2">
            <div class="text-xs font-mono-code text-emerald-400 uppercase font-bold">👥 EQUIPO EXPOSITOR (CLIC PARA IR A SU SECCIÓN)</div>
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs">
              <button onclick="goToScene(1)" class="p-2.5 rounded-xl bg-white/5 hover:bg-emerald-500/20 border border-white/10 text-left transition-all"><span class="text-emerald-400 font-bold">1.</span> Cesar Carranza</button>
              <button onclick="goToScene(4)" class="p-2.5 rounded-xl bg-white/5 hover:bg-emerald-500/20 border border-white/10 text-left transition-all"><span class="text-emerald-400 font-bold">2.</span> Leyvinis Noriega</button>
              <button onclick="goToScene(8)" class="p-2.5 rounded-xl bg-white/5 hover:bg-emerald-500/20 border border-white/10 text-left transition-all"><span class="text-emerald-400 font-bold">3.</span> Pedro Ledezma</button>
              <button onclick="goToScene(10)" class="p-2.5 rounded-xl bg-white/5 hover:bg-emerald-500/20 border border-white/10 text-left transition-all"><span class="text-emerald-400 font-bold">4.</span> George Flores</button>
              <button onclick="goToScene(12)" class="p-2.5 rounded-xl bg-white/5 hover:bg-emerald-500/20 border border-white/10 text-left transition-all"><span class="text-emerald-400 font-bold">5.</span> Jelsin Reyes</button>
              <div class="p-2.5 rounded-xl bg-amber-500/15 border border-amber-400/30 text-amber-200 font-semibold">🎓 Mgtr. Luis De Lucio</div>
            </div>
          </div>
        </div>
      </div>
    </section>"""

html = html.replace(old_scene_01, new_scene_01)
html = html.replace('<body data-hero-pos="center">', '<body data-hero-pos="right">')

# 4. Ajustar tamaños y posiciones del Diorama 3D para que quede en el espacio libre de las escenas (derecha o izquierda) sin chocar con textos
extra_styles = """
    #sceneStage {
      perspective: 1600px;
      transform-style: preserve-3d;
    }

    .scene {
      transform: translate3d(80px, 20px, -220px) rotateY(-12deg) rotateX(4deg) scale(0.94);
      filter: blur(6px);
      transform-style: preserve-3d;
    }
    .scene.active {
      transform: translate3d(0, 0, 0) rotateY(0deg) rotateX(0deg) scale(1);
      filter: blur(0px);
    }
    .scene.prev {
      transform: translate3d(-90px, -15px, -240px) rotateY(12deg) rotateX(-4deg) scale(0.94);
      filter: blur(6px);
    }

    /* Diorama 3D Multicapa ubicado limpiamente en el lado libre de la pantalla */
    #persistentHero3D {
      position: fixed;
      z-index: 6;
      width: 440px;
      height: 350px;
      perspective: 1400px;
      transform-style: preserve-3d;
      pointer-events: none;
    }

    body[data-hero-pos="right"] #persistentHero3D {
      left: 77%;
      top: 54%;
      transform: translate3d(-50%, -50%, 0) rotateY(-16deg) rotateX(5deg) scale(1);
      opacity: 1;
      filter: blur(0px);
    }

    body[data-hero-pos="left"] #persistentHero3D {
      left: 22%;
      top: 54%;
      transform: translate3d(-50%, -50%, 0) rotateY(16deg) rotateX(5deg) scale(1);
      opacity: 1;
      filter: blur(0px);
    }

    body[data-hero-pos="right-edge"] #persistentHero3D {
      left: 86%;
      top: 54%;
      transform: translate3d(-50%, -50%, 0) rotateY(-20deg) scale(0.92);
      opacity: 0.92;
      filter: blur(0px);
    }

    body[data-hero-pos="bg-blur"] #persistentHero3D {
      left: 50%;
      top: 52%;
      transform: translate3d(-50%, -50%, -180px) scale(1.25);
      opacity: 0.11;
      filter: blur(10px);
    }

    body[data-hero-pos="bottom-left"] #persistentHero3D {
      left: 16%;
      top: 78%;
      transform: translate3d(-50%, -50%, 0) rotateY(14deg) scale(0.82);
      opacity: 0.85;
      filter: blur(0px);
    }

    .diorama-3d-stage {
      position: relative;
      width: 100%;
      height: 100%;
      transform-style: preserve-3d;
      transition: transform 0.25s ease-out;
    }

    .diorama-layer-back {
      position: absolute;
      inset: -12px;
      border-radius: 1.8rem;
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.24), rgba(6, 24, 15, 0.8), rgba(249, 115, 22, 0.22));
      border: 1.5px solid rgba(52, 211, 153, 0.38);
      transform: translateZ(-40px) rotateZ(-2deg);
      box-shadow: 0 30px 70px rgba(0, 0, 0, 0.85), 0 0 45px rgba(16, 185, 129, 0.25);
    }

    .diorama-main-frame {
      position: relative;
      width: 100%;
      height: 100%;
      border-radius: 1.5rem;
      overflow: hidden;
      border: 2.5px solid rgba(255, 255, 255, 0.28);
      box-shadow: -12px 20px 45px rgba(0, 0, 0, 0.78), inset 0 2px 4px rgba(255, 255, 255, 0.35);
      transform: translateZ(10px);
      background: #04120b;
    }

    @keyframes scanLaser3D {
      0%   { top: 5%; opacity: 0.85; }
      50%  { top: 92%; opacity: 0.95; }
      100% { top: 5%; opacity: 0.85; }
    }

    .diorama-laser-line {
      position: absolute;
      left: 0;
      right: 0;
      height: 2.5px;
      background: linear-gradient(90deg, transparent, #34d399, #ffffff, #34d399, transparent);
      box-shadow: 0 0 18px #10b981;
      animation: scanLaser3D 3.8s ease-in-out infinite;
    }

    .diorama-popout-top {
      position: absolute;
      top: -22px;
      left: -22px;
      padding: 0.7rem 1.1rem;
      border-radius: 1.15rem;
      background: rgba(6, 22, 14, 0.94);
      backdrop-filter: blur(18px);
      border: 2px solid rgba(52, 211, 153, 0.65);
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.82), 0 0 25px rgba(16, 185, 129, 0.35);
      transform: translateZ(65px);
    }

    .diorama-popout-bottom {
      position: absolute;
      bottom: -24px;
      right: -22px;
      width: 175px;
      height: 110px;
      border-radius: 1rem;
      overflow: hidden;
      border: 2.5px solid rgba(251, 191, 36, 0.65);
      box-shadow: 0 22px 45px rgba(0, 0, 0, 0.85), 0 0 22px rgba(249, 115, 22, 0.35);
      transform: translateZ(82px);
      background: #06120c;
    }

    /* Robot Dron 3D Global (Por encima de todas las diapositivas · Z-Index 65) */
    #globalDroneStage {
      position: fixed;
      inset: 0;
      z-index: 65;
      pointer-events: none;
      perspective: 1400px;
      overflow: hidden;
    }

    #roamingDrone3D {
      position: absolute;
      left: 0;
      top: 0;
      width: 185px;
      height: 185px;
      pointer-events: auto;
      cursor: grab;
      transform-style: preserve-3d;
      will-change: transform;
      filter: drop-shadow(0 28px 32px rgba(0, 0, 0, 0.8));
    }

    #roamingDrone3D:active {
      cursor: grabbing;
    }

    #droneLaserCone {
      position: absolute;
      top: 122px;
      left: 50%;
      width: 150px;
      height: 195px;
      transform: translateX(-50%);
      background: conic-gradient(from 160deg at 50% 0%, transparent 0deg, rgba(16, 185, 129, 0.24) 20deg, rgba(52, 211, 153, 0.05) 40deg, transparent 45deg);
      filter: blur(4px);
      pointer-events: none;
      opacity: 0.75;
    }

    #roamingEmotionBubble {
      position: absolute;
      top: -24px;
      left: 50%;
      transform: translateX(-50%) translateZ(40px);
      white-space: nowrap;
      padding: 5px 13px;
      border-radius: 9999px;
      font-size: 11.5px;
      font-weight: 800;
      background: rgba(4, 15, 10, 0.95);
      border: 2px solid #34d399;
      color: #ecfdf5;
      box-shadow: 0 10px 24px rgba(0, 0, 0, 0.75), 0 0 20px rgba(16, 185, 129, 0.45);
      pointer-events: none;
    }

    @keyframes naturalBlink {
      0%, 94%, 100% { transform: scaleY(1); }
      97%           { transform: scaleY(0.08); }
    }

    .visor-eyes-blink {
      transform-origin: 110px 104px;
      animation: naturalBlink 4s infinite;
    }

    /* ==========================================================================
       ANIMACIÓN CONTINUA EN TIEMPO REAL PARA TODAS LAS IMÁGENES DEL PROYECTO
       Autor: César Quiroz
       ========================================================================== */
    @keyframes liveImageCinema {
      0%   { transform: scale(1.03) translate3d(0px, 0px, 0) rotate(0deg); filter: brightness(1) saturate(1.08); }
      33%  { transform: scale(1.11) translate3d(-6px, -4px, 0) rotate(-0.4deg); filter: brightness(1.08) saturate(1.22); }
      66%  { transform: scale(1.14) translate3d(6px, -5px, 0) rotate(0.4deg); filter: brightness(1.04) saturate(1.18); }
      100% { transform: scale(1.03) translate3d(0px, 0px, 0) rotate(0deg); filter: brightness(1) saturate(1.08); }
    }

    .diorama-main-frame img,
    .diorama-popout-bottom img,
    .frost-carousel-card img {
      animation: liveImageCinema 8.5s ease-in-out infinite;
      will-change: transform, filter;
    }

    .risk-card {
      cursor: pointer;
    }
    .risk-card::after,
    .frost-carousel-card::after,
    .glow-bar::after,
    .white-step-card::after,
    .entry-pill-card::after {
      content: '👁️ Ver';
      display: inline-block;
      margin-top: 0.55rem;
      padding: 0.18rem 0.65rem;
      border-radius: 9999px;
      background: rgba(16, 185, 129, 0.24);
      border: 1px solid rgba(52, 211, 153, 0.6);
      font-size: 10px;
      font-weight: 800;
      color: #ecfdf5;
      letter-spacing: 0.03em;
      transition: all 0.25s ease;
    }
    .white-step-card::after,
    .entry-pill-card::after {
      background: rgba(5, 150, 105, 0.14);
      border-color: rgba(5, 150, 105, 0.45);
      color: #065f46;
    }
    .risk-card:hover::after,
    .frost-carousel-card:hover::after,
    .glow-bar:hover::after,
    .white-step-card:hover::after,
    .entry-pill-card:hover::after {
      background: #10b981;
      color: #022c22;
      transform: scale(1.04);
    }

    /* ==========================================================================
       CAPA MODAL 3D DE COMPARACIÓN VISUAL (REALIDAD ACTUAL VS SOLUCIÓN DRON IA)
       Autor: César Quiroz
       ========================================================================== */
    #visualCompareModal3D {
      position: fixed;
      inset: 0;
      z-index: 80;
      background: rgba(2, 10, 6, 0.86);
      backdrop-filter: blur(18px);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.35s ease;
      perspective: 1500px;
    }

    #visualCompareModal3D.open {
      opacity: 1;
      pointer-events: auto;
    }

    .compare-3d-box {
      width: 100%;
      max-width: 980px;
      background: linear-gradient(145deg, rgba(6, 28, 18, 0.96), rgba(3, 14, 9, 0.98));
      border: 2px solid rgba(52, 211, 153, 0.55);
      border-radius: 1.8rem;
      padding: 1.6rem 2rem;
      box-shadow: 0 35px 90px rgba(0, 0, 0, 0.9), 0 0 60px rgba(16, 185, 129, 0.3);
      transform: rotateX(12deg) scale(0.88) translateY(30px);
      transition: transform 0.5s cubic-bezier(0.22, 1, 0.36, 1);
      transform-style: preserve-3d;
    }

    #visualCompareModal3D.open .compare-3d-box {
      transform: rotateX(0deg) scale(1) translateY(0px);
    }

    .compare-img-card {
      position: relative;
      height: 250px;
      border-radius: 1.25rem;
      overflow: hidden;
      border: 2px solid rgba(255, 255, 255, 0.2);
      box-shadow: 0 20px 45px rgba(0, 0, 0, 0.7);
    }

    .compare-img-card img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      animation: liveImageCinema 7s ease-in-out infinite;
    }

    /* ==========================================================================
       DISEÑO RESPONSIVO ELEGANTE PARA TABLETS Y CELULARES
       Autor: César Quiroz
       ========================================================================== */
    @media (max-width: 1024px) {
      .scene {
        padding: 4.2rem 1.8rem 4.5rem;
        align-items: flex-start;
        overflow-y: auto;
      }
      #persistentHero3D {
        width: 310px;
        height: 240px;
        opacity: 0.22 !important;
        left: 50% !important;
        top: 56% !important;
        filter: blur(4px) !important;
      }
      #roamingDrone3D {
        width: 125px;
        height: 125px;
      }
      #roamingEmotionBubble {
        font-size: 10px;
        padding: 3px 9px;
      }
    }

    @media (max-width: 640px) {
      .scene {
        padding: 3.8rem 1.1rem 4.5rem;
      }
      .title-condensed {
        font-size: 2.35rem !important;
        line-height: 1.06 !important;
      }
      #roamingDrone3D {
        width: 100px;
        height: 100px;
      }
      .entry-pill-card {
        padding-right: 3.5rem;
      }
      .entry-medallion {
        right: -8px;
        width: 50px;
        height: 50px;
      }
    }
"""

with open(os.path.join(base_dir, "upgrade_global_3d_robot.py"), "r", encoding="utf-8") as _u:
    _u_txt = _u.read()
roaming_drone_html = _u_txt.split('roaming_drone_html = """')[1].split('"""\n\nhtml = html.replace(\'<div id="ambientBg"></div>\'')[0]

html = html.replace("</style>", extra_styles + "\n  </style>")
html = html.replace('<div id="ambientBg"></div>', roaming_drone_html + '\n  <div id="ambientBg"></div>')

# 5. Inyectar el bloque JS del Diorama y del Robot Dron Global ÚNICAMENTE al final del bloque <script> (usando 'animateBokeh();\n\n    goToScene(0);' que es único!)
js_block = """    animateBokeh();

    const sceneDroneMoods = [
      { mood: 'happy',    text: '😊 ¡Bienvenidos! Soy el Dron UCV', color: '#10b981' },
      { mood: 'angry',    text: '😠 ¡Las nubes bloquean al satélite!', color: '#ef4444' },
      { mood: 'shocked',  text: '😱 ¡10,9 millones ha/año perdidas!', color: '#fbbf24' },
      { mood: 'angry',    text: '😡 ¡95 % son provocados por humanos!', color: '#ef4444' },
      { mood: 'shocked',  text: '😱 ¡2 990 ha quemadas en La Libertad!', color: '#fbbf24' },
      { mood: 'happy',    text: '🎯 ¡3 Objetivos listos para cumplir!', color: '#10b981' },
      { mood: 'scanning', text: '🧐 ¡Unamos detección de fuego y tala!', color: '#38bdf8' },
      { mood: 'scanning', text: '🔬 Analizando estudios 2023–2024...', color: '#38bdf8' },
      { mood: 'happy',    text: '🤩 ¡Modelos de 2025 y 2026 increíbles!', color: '#10b981' },
      { mood: 'happy',    text: '🎯 ¡98,39 % de exactitud sin falsas alarmas!', color: '#10b981' },
      { mood: 'turbo',    text: '⚡ ¡MODO TURBO: 3,5 MB a 333,3 FPS!', color: '#c084fc' },
      { mood: 'happy',    text: '🗺️ ¡Visión <10 cm/px y mapas GeoJSON!', color: '#10b981' },
      { mood: 'scanning', text: '📊 Comparando las 7 arquitecturas...', color: '#38bdf8' },
      { mood: 'scanning', text: '🌡️ ¡Activando cámara térmica y LoRaWAN!', color: '#38bdf8' },
      { mood: 'happy',    text: '🥳 ¡Salvando nuestros bosques andinos!', color: '#10b981' }
    ];

    const manualMoods = [
      { mood: 'happy',    text: '😄 ¡Vamos por ese 20 con el profesor!', color: '#10b981' },
      { mood: 'shocked',  text: '😲 ¡Vuelo bajo las nubes a <10 cm/px!', color: '#fbbf24' },
      { mood: 'angry',    text: '😤 ¡Cero tolerancia a los incendios!', color: '#ef4444' },
      { mood: 'turbo',    text: '🚀 ¡Alerta enviada en 2 segundos!', color: '#c084fc' },
      { mood: 'scanning', text: '🛰️ Escaneando cabeceras de cuenca...', color: '#38bdf8' }
    ];
    let manualIdx = 0;

    const sceneDioramaData = [
      { icon: '🚁', val: 'LA LIBERTAD', lbl: 'Drones IA · TIF Nivel I', secImg: './assets/u_drone_forest.jpg', secLbl: '🚁 Patrullaje Aéreo UCV', cap: '🚁 Sistema de Drones Inteligentes · UCV 2026' },
      { icon: '🌍', val: 'ODS 13 Y 15', lbl: 'Acción por el Clima y Bosques', secImg: './assets/u_climate_forest.jpg', secLbl: '🌿 Ecosistemas Terrestres', cap: '🌿 De Vigilancia Lenta a Visión Artificial IA' },
      { icon: '🌲', val: '10,9 M ha/año', lbl: 'Deforestación Mundial (FAO)', secImg: './assets/u_fao_global.jpg', secLbl: '🔥 42 % Pérdida por Fuego', cap: '🌍 Crisis Global: >11 Canchas de Fútbol / min' },
      { icon: '🇵🇪', val: '1 754', lbl: 'Incendios en Perú (INDECI)', secImg: './assets/u_indeci_fire.jpg', secLbl: '⚠️ 95 % Causa Humana', cap: '🚨 Perú Top 10 Global · Pico 840 en Septiembre' },
      { icon: '⛰️', val: '2 990 ha', lbl: 'Perdidas en La Libertad (COER)', secImg: './assets/u_santiago_chuco.jpg', secLbl: '💧 Cabeceras de Cuenca', cap: '🔥 Santiago de Chuco (+1 000 ha) y +42 Incendios' },
      { icon: '🎯', val: '3 OBJETIVOS', lbl: 'Exactitud · Latencia · GeoJSON', secImg: './assets/u_obj_gen.jpg', secLbl: '📡 Red Web / Móvil', cap: '🎯 Optimización de Tiempos de Detección 2026' },
      { icon: '🧠', val: 'YOLO + U-Net', lbl: 'Fusión Incendios + Tala', secImg: './assets/u_theory_yolo.jpg', secLbl: '🌲 Segmentación Semántica', cap: '🔍 Brecha Teórica: Unir Fuego y Desmonte en los Andes' },
      { icon: '🔬', val: '96 % – 98 %', lbl: 'Hitos Científicos 2023–2024', secImg: './assets/u_amazon_river.jpg', secLbl: '💨 YOLOv8 + BiFormer', cap: '📚 Revisión Scopus Q1: Sensors, Frontiers y PLOS ONE' },
      { icon: '🚀', val: '2025 – 2026', lbl: 'Modelos Ultraligeros Edge AI', secImg: './assets/u_gpu_circuit.jpg', secLbl: '🗺️ 10 400+ Árboles Auditados', cap: '⚡ Evolución hacia YOLO-UFS, AETDA y AHE-YOLO11' },
      { icon: '🎯', val: '98,39 %', lbl: 'Exactitud Máxima (OE1)', secImg: './assets/u_autumn_fog.jpg', secLbl: '🌤️ Cero Falsos Positivos', cap: '📊 Resultados OE1: Filtrado de Neblina y Brillo Solar' },
      { icon: '⚡', val: '3,5 MB', lbl: '333,3 FPS Lab / 30 FPS Dron', secImg: './assets/u_hardware_chip.jpg', secLbl: '📡 Alerta GSM en Segundos', cap: '⚡ Resultados OE2: -74 % Peso en Placa Jetson Nano' },
      { icon: '🗺️', val: '10 cm/px', lbl: '50x Más Nítido que el Satélite', secImg: './assets/u_gis_map.jpg', secLbl: '📐 Polígonos GeoJSON', cap: '🗺️ Resultados OE3: Mapas de Calor Multitemporales' },
      { icon: '📑', val: '7 ESTUDIOS', lbl: 'Síntesis Comparativa Scopus', secImg: './assets/u_command_center.jpg', secLbl: '💻 Hardware + Software IA', cap: '📋 Tabla 1 Oficial según los 3 Objetivos Específicos' },
      { icon: '🌡️', val: 'LoRaWAN + IR', lbl: 'Propuesta para los Andes', secImg: './assets/u_lorawan_tower.jpg', secLbl: '⛰️ Quebradas sin Señal GSM', cap: '⚖️ Cámara Térmica en Ichu + Radio de Largo Alcance' },
      { icon: '🛡️', val: 'SEGUNDOS', lbl: 'Que Salvan Bosques Andinos', secImg: './assets/u_andean_lagoon.jpg', secLbl: '🎓 Ingeniería de Sistemas UCV', cap: '🏆 Conclusión General · La Libertad 2026' }
    ];

    function updateDioramaContent(idx) {
      const d = sceneDioramaData[idx];
      if (!d) return;
      const ic = document.getElementById('dioramaKpiIcon');
      const vl = document.getElementById('dioramaKpiValue');
      const lb = document.getElementById('dioramaKpiLabel');
      const si = document.getElementById('dioramaSecondaryImg');
      const sl = document.getElementById('dioramaSecondaryLabel');
      const cp = document.getElementById('dioramaCaption');
      if (ic) ic.textContent = d.icon;
      if (vl) vl.textContent = d.val;
      if (lb) lb.textContent = d.lbl;
      if (si) si.src = d.secImg;
      if (sl) sl.textContent = d.secLbl;
      if (cp) cp.textContent = d.cap;
    }

    const droneEl = document.getElementById('roamingDrone3D');
    const eyesOffsetEl = document.getElementById('roamingEyesOffset');
    const trailCanvas = document.getElementById('droneTrailCanvas');
    const trailCtx = trailCanvas.getContext('2d');

    function resizeTrail() {
      trailCanvas.width = window.innerWidth;
      trailCanvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resizeTrail);
    resizeTrail();

    let droneState = {
      x: window.innerWidth * 0.78,
      y: window.innerHeight * 0.10,
      vx: 0,
      vy: 0,
      targetX: window.innerWidth * 0.78,
      targetY: window.innerHeight * 0.10,
      roll: 0,
      pitch: 0,
      flipAngle: 0,
      isDragging: false,
      roamPhase: 0,
      currentColor: '#10b981'
    };

    const sceneWaypoints = [
      { rx: 0.72, ry: 0.14 },
      { rx: 0.76, ry: 0.13 },
      { rx: 0.70, ry: 0.14 },
      { rx: 0.22, ry: 0.14 },
      { rx: 0.72, ry: 0.14 },
      { rx: 0.76, ry: 0.14 },
      { rx: 0.22, ry: 0.15 },
      { rx: 0.76, ry: 0.13 },
      { rx: 0.22, ry: 0.13 },
      { rx: 0.72, ry: 0.14 },
      { rx: 0.76, ry: 0.13 },
      { rx: 0.22, ry: 0.14 },
      { rx: 0.76, ry: 0.13 },
      { rx: 0.22, ry: 0.14 },
      { rx: 0.72, ry: 0.15 }
    ];

    function clampDroneX(val) {
      const margin = window.innerWidth < 768 ? 16 : 95;
      const rightPad = window.innerWidth < 768 ? 120 : 285;
      return Math.max(margin, Math.min(window.innerWidth - rightPad, val));
    }
    function clampDroneY(val) {
      const topPad = window.innerWidth < 768 ? 55 : 68;
      const botPad = window.innerWidth < 768 ? 140 : 265;
      return Math.max(topPad, Math.min(window.innerHeight - botPad, val));
    }

    // Soporte de gestos táctiles (Swipe izquierda/derecha) para celulares y tablets
    let touchStartX = 0;
    let touchStartY = 0;
    window.addEventListener('touchstart', (e) => {
      if (e.touches && e.touches.length > 0) {
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
      }
    }, { passive: true });
    window.addEventListener('touchend', (e) => {
      if (e.changedTouches && e.changedTouches.length > 0) {
        const dx = e.changedTouches[0].clientX - touchStartX;
        const dy = e.changedTouches[0].clientY - touchStartY;
        if (Math.abs(dx) > 55 && Math.abs(dx) > Math.abs(dy) * 1.4) {
          if (dx < 0) nextScene();
          else prevScene();
        }
      }
    }, { passive: true });

    setInterval(() => {
      if (droneState.isDragging) return;
      const wp = sceneWaypoints[currentScene] || { rx: 0.72, ry: 0.14 };
      const wanderX = (Math.random() - 0.5) * 220;
      const wanderY = (Math.random() - 0.5) * 110;
      droneState.targetX = clampDroneX(window.innerWidth * wp.rx + wanderX);
      droneState.targetY = clampDroneY(window.innerHeight * wp.ry + wanderY);
    }, 3200);

    droneEl.addEventListener('mousedown', (e) => {
      droneState.isDragging = true;
      e.stopPropagation();
    });
    window.addEventListener('mouseup', () => {
      droneState.isDragging = false;
    });

    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    window.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      if (droneState.isDragging) {
        droneState.targetX = e.clientX - 92;
        droneState.targetY = e.clientY - 92;
      }
      if (eyesOffsetEl) {
        const dx = Math.max(-8, Math.min(8, (mouseX - (droneState.x + 92)) * 0.018));
        const dy = Math.max(-5, Math.min(5, (mouseY - (droneState.y + 92)) * 0.018));
        eyesOffsetEl.setAttribute('transform', `translate(${dx}, ${dy})`);
      }
      const stage3D = document.getElementById('dioramaStage3D');
      if (stage3D) {
        const rx = ((e.clientY / window.innerHeight) - 0.5) * -14;
        const ry = ((e.clientX / window.innerWidth) - 0.5) * 16;
        stage3D.style.transform = `rotateX(${rx}deg) rotateY(${ry}deg)`;
      }
    });

    let trailParticles = [];

    function updateRoamingDronePhysics() {
      droneState.roamPhase += 0.04;
      const hoverX = Math.sin(droneState.roamPhase) * 32;
      const hoverY = Math.cos(droneState.roamPhase * 1.6) * 16;

      const ax = ((droneState.targetX + hoverX) - droneState.x) * 0.048;
      const ay = ((droneState.targetY + hoverY) - droneState.y) * 0.048;

      droneState.vx = (droneState.vx + ax) * 0.82;
      droneState.vy = (droneState.vy + ay) * 0.82;

      droneState.x = clampDroneX(droneState.x + droneState.vx);
      droneState.y = clampDroneY(droneState.y + droneState.vy);

      const targetRoll = Math.max(-28, Math.min(28, droneState.vx * 2.5));
      const lookYaw = Math.max(-18, Math.min(18, (mouseX - (droneState.x + 92)) * 0.025));
      const lookPitch = Math.max(-14, Math.min(14, (mouseY - (droneState.y + 92)) * -0.02));

      droneState.roll += (targetRoll - droneState.roll) * 0.15;
      droneState.pitch += (lookPitch - droneState.pitch) * 0.15;

      if (droneState.flipAngle > 0) {
        droneState.flipAngle = Math.max(0, droneState.flipAngle - 15);
      }

      droneEl.style.transform = `translate3d(${droneState.x}px, ${droneState.y}px, 80px) rotateZ(${droneState.roll + droneState.flipAngle}deg) rotateY(${lookYaw}deg) rotateX(${droneState.pitch}deg)`;

      if (Math.random() < 0.65) {
        trailParticles.push({
          x: droneState.x + 92 + (Math.random() - 0.5) * 14,
          y: droneState.y + 148,
          r: Math.random() * 4 + 2,
          vy: Math.random() * 2.2 + 1.2,
          vx: (Math.random() - 0.5) * 1.2,
          alpha: 0.75,
          color: droneState.currentColor
        });
      }

      trailCtx.clearRect(0, 0, trailCanvas.width, trailCanvas.height);
      for (let i = trailParticles.length - 1; i >= 0; i--) {
        const p = trailParticles[i];
        p.x += p.vx;
        p.y += p.vy;
        p.alpha -= 0.024;
        p.r *= 0.97;
        if (p.alpha <= 0.02) {
          trailParticles.splice(i, 1);
          continue;
        }
        trailCtx.beginPath();
        trailCtx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        trailCtx.fillStyle = p.color;
        trailCtx.globalAlpha = p.alpha;
        trailCtx.fill();
      }
      trailCtx.globalAlpha = 1;

      requestAnimationFrame(updateRoamingDronePhysics);
    }

    function setDroneEmotion(moodObj) {
      if (!moodObj) return;
      document.body.setAttribute('data-drone-mood', moodObj.mood);
      droneState.currentColor = moodObj.color;

      const bubble = document.getElementById('roamingEmotionBubble');
      if (bubble) {
        bubble.textContent = moodObj.text;
        bubble.style.borderColor = moodObj.color;
      }

      ['happy', 'shocked', 'angry', 'scanning', 'turbo'].forEach(m => {
        const el = document.getElementById('rface-' + m);
        if (el) el.style.display = (m === moodObj.mood) ? 'block' : 'none';
      });

      ['roamingAntennaL', 'roamingAntennaR', 'roamingGimbalLens'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.setAttribute('fill', moodObj.color);
      });

      updateDioramaContent(currentScene);

      const wp = sceneWaypoints[currentScene] || { rx: 0.72, ry: 0.14 };
      droneState.targetX = clampDroneX(window.innerWidth * wp.rx - 92);
      droneState.targetY = clampDroneY(window.innerHeight * wp.ry - 20);
    }

    function triggerDroneAcrobatics() {
      droneState.flipAngle = 360;
      manualIdx = (manualIdx + 1) % manualMoods.length;
      setDroneEmotion(manualMoods[manualIdx]);
      droneState.targetX = clampDroneX(Math.random() * (window.innerWidth - 360) + 110);
      droneState.targetY = clampDroneY(Math.random() * (window.innerHeight * 0.45) + 75);
    }

    updateRoamingDronePhysics();

    // =========================================================================
    // SISTEMA INTERACTIVO DE COMPARACIÓN VISUAL 3D (REALIDAD VS SOLUCIÓN IA)
    // Se activa al hacer clic en los cuadros de Realidad/Propuesta, OE1, OE2, OE3 y Conclusión
    // Autor: César Quiroz
    // =========================================================================
    const compareModalHtml = `
      <div id="visualCompareModal3D" onclick="closeVisualCompare(event)">
        <div class="compare-3d-box" onclick="event.stopPropagation()">
          <div class="flex items-center justify-between border-b border-white/15 pb-3 mb-4">
            <div>
              <span id="vcCategory" class="text-[11px] font-mono-code text-emerald-400 font-bold uppercase tracking-widest">COMPARATIVA VISUAL 3D · REALIDAD VS. SOLUCIÓN IA</span>
              <h3 id="vcTitle" class="title-condensed text-3xl sm:text-4xl text-white mt-0.5">Título</h3>
            </div>
            <button onclick="closeVisualCompare()" class="w-10 h-10 rounded-full bg-white/10 hover:bg-emerald-500 hover:text-slate-950 text-white font-bold text-lg flex items-center justify-center transition-all">✕</button>
          </div>

          <!-- Explicación sencilla en lenguaje claro para exponer al jurado -->
          <div class="p-3.5 rounded-2xl bg-emerald-500/15 border border-emerald-400/40 mb-4">
            <div class="text-xs font-mono-code text-emerald-300 font-bold uppercase mb-1">💡 ¿QUÉ SIGNIFICA ESTO EN SENCILLO PARA TU EXPOSICIÓN?</div>
            <p id="vcSimpleExplain" class="text-xs sm:text-sm text-white leading-relaxed"></p>
          </div>

          <!-- Comparación Visual Lado a Lado con Imágenes 3D en Movimiento -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
            <!-- Lado Izquierdo: Realidad Tradicional / Sin el Sistema -->
            <div class="space-y-2">
              <div class="flex items-center justify-between text-xs font-bold text-rose-400 uppercase font-mono-code">
                <span>❌ ANTES (SIN EL SISTEMA / TRADICIONAL)</span>
                <span id="vcBeforeMetric" class="px-2 py-0.5 rounded bg-rose-500/20 border border-rose-400/40">Lento / Impreciso</span>
              </div>
              <div class="compare-img-card border-rose-500/50">
                <img id="vcBeforeImg" src="./assets/image10.png" alt="Antes" />
                <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent flex items-end p-3.5">
                  <p id="vcBeforeCaption" class="text-xs text-rose-100 font-medium leading-snug"></p>
                </div>
              </div>
            </div>

            <!-- Lado Derecho: Solución y Progreso con Drones IA -->
            <div class="space-y-2">
              <div class="flex items-center justify-between text-xs font-bold text-emerald-400 uppercase font-mono-code">
                <span>✅ AHORA (RESULTADO CON DRONES IA)</span>
                <span id="vcAfterMetric" class="px-2 py-0.5 rounded bg-emerald-500/25 border border-emerald-400/50 text-emerald-200">Optimizado</span>
              </div>
              <div class="compare-img-card border-emerald-400/70">
                <img id="vcAfterImg" src="./assets/image1.png" alt="Después con IA" />
                <div class="diorama-laser-line"></div>
                <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/15 to-transparent flex items-end p-3.5">
                  <p id="vcAfterCaption" class="text-xs text-emerald-100 font-medium leading-snug"></p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `;
    document.body.insertAdjacentHTML('beforeend', compareModalHtml);

    // Base de conocimiento visual con temas específicos y fotos nuevas únicas para CADA cuadro de las 15 diapositivas
    const visualCompareDB = [
      // ESCENA 02 (4 cuadros)
      {
        match: 'Cambio Climático',
        cat: 'ESCENA 02 · INTRODUCCIÓN: REALIDAD ACTUAL VS. PROPUESTA IA',
        title: '🌡️ CAMBIO CLIMÁTICO Y SEQUÍAS PROLONGADAS',
        explain: 'El calentamiento global altera las lluvias y prolonga las sequías, dejando pastizales y bosques listos para arder ante cualquier chispa y reduciendo la capacidad de absorber CO₂. Con los drones inteligentes detectamos el foco térmico en sus primeros minutos (ODS 13 y 15).',
        beforeMetric: 'Sequía + Emisión de GEI',
        beforeImg: './assets/u_drought.jpg',
        beforeCap: 'Realidad observada: Suelos resecos y matorrales altamente inflamables que liberan toneladas de CO₂ al quemarse.',
        afterMetric: 'Protección Climática ODS 13',
        afterImg: './assets/u_climate_forest.jpg',
        afterCap: 'Situación deseada: Conservación de ecosistemas forestales y captura de carbono mediante vigilancia aérea preventiva.'
      },
      {
        match: 'Vigilancia Lenta',
        cat: 'ESCENA 02 · INTRODUCCIÓN: REALIDAD ACTUAL VS. PROPUESTA IA',
        title: '🛰️ VIGILANCIA TRADICIONAL LENTA VS. DRONES BAJO NUBES',
        explain: 'En zonas alejadas la vigilancia depende de rondas humanas a pie, avisos telefónicos tardíos de pobladores o satélites que tardan horas y se bloquean con las nubes. El dron vuela por debajo de las nubes y llega en minutos a quebradas sin caminos.',
        beforeMetric: 'Rondas a Pie / Nubes',
        beforeImg: './assets/u_foot_patrol.jpg',
        beforeCap: 'Vigilancia manual: Brigadistas caminando horas por senderos empinados sin visibilidad completa de las quebradas.',
        afterMetric: 'Vuelo Directo Bajo Nubes',
        afterImg: './assets/u_drone_forest.jpg',
        afterCap: 'Vigilancia con Drones IA: Sobrevuelo ágil por debajo de la capa de neblina con visión directa del bosque.'
      },
      {
        match: 'Visión Artificial IA',
        cat: 'ESCENA 02 · INTRODUCCIÓN: REALIDAD ACTUAL VS. PROPUESTA IA',
        title: '🚁 ALGORITMOS DE VISIÓN ARTIFICIAL CONTRA FALSAS ALARMAS',
        explain: 'Primer componente de Ingeniería de Sistemas: algoritmos de procesamiento de imágenes (YOLOv8 / YOLO11 y U-Net) que reconocen humo delgado, llamas o claros de tala sin confundir la neblina matutina ni el reflejo del sol.',
        beforeMetric: 'Confusión con Neblina',
        beforeImg: './assets/u_clouds_mountain.jpg',
        beforeCap: 'Cámaras sin IA entrenada: Confunden la neblina densa de la sierra o el reflejo solar con columnas de humo.',
        afterMetric: 'Reconocimiento IA Preciso',
        afterImg: './assets/u_ai_vision.jpg',
        afterCap: 'Visión por computadora embarcada: Distingue con exactitud conatos reales de fuego y áreas de tala ilegal.'
      },
      {
        match: 'Alerta y Mapas GIS',
        cat: 'ESCENA 02 · INTRODUCCIÓN: REALIDAD ACTUAL VS. PROPUESTA IA',
        title: '📡 REDES DE BAJA LATENCIA Y BASE DE DATOS ESPACIAL GIS',
        explain: 'Segundo y tercer componente de Ingeniería de Sistemas: redes de comunicación que transmiten la alerta con baja demora hacia una app web/móvil, y una base de datos que guarda las coordenadas GPS para armar mapas de calor.',
        beforeMetric: 'Avisos Telefónicos Tardíos',
        beforeImg: './assets/u_gis_map.jpg',
        beforeCap: 'Sin georreferenciación digital: Reportes verbales imprecisos que impiden ubicar el foco exacto en la montaña.',
        afterMetric: 'App Web/Móvil + Mapa de Calor',
        afterImg: './assets/u_mobile_alert.jpg',
        afterCap: 'Notificación automática en segundos con coordenadas GPS exactas e historial para mapas de calor (ODS 13 y 15).'
      },
      // ESCENA 03 (3 barras de Estadística Mundial)
      {
        match: '10,9 M ha/año',
        cat: 'ESCENA 03 · ESTADÍSTICA MUNDIAL (FAO, 2025)',
        title: '🌲 TASA MUNDIAL DE DEFORESTACIÓN: 10,9 MILLONES HA/AÑO (FAO, 2025)',
        explain: 'Según la Evaluación de los Recursos Forestales Mundiales de la FAO (2025), el planeta registra 4 140 millones de hectáreas de bosques, pero perdió 10,9 millones de hectáreas por año entre 2015 y 2025, además de 261 millones de ha afectadas por el fuego anualmente.',
        beforeMetric: '10,9 M ha/año Deforestadas',
        beforeImg: './assets/u_logged_trunks.jpg',
        beforeCap: 'Tala y pérdida forestal sostenida a nivel planetario durante la década 2015–2025 según el reporte oficial de la FAO.',
        afterMetric: '4 140 M ha por Proteger',
        afterImg: './assets/u_fao_global.jpg',
        afterCap: 'Monitoreo tecnológico global para frenar la pérdida de masa boscosa y conservar los pulmones del planeta.'
      },
      {
        match: '25,5 M ha',
        cat: 'ESCENA 03 · ESTADÍSTICA MUNDIAL (GOLDMAN ET AL. / WRI, 2026)',
        title: '🌍 PÉRDIDA GLOBAL 2025: 25,5 MILLONES DE HECTÁREAS (WRI & GLAD, 2026)',
        explain: 'El análisis de Goldman et al. (2026) para el World Resources Institute (WRI) y el laboratorio GLAD de la Universidad de Maryland reveló que en 2025 se perdieron 25,5 M ha de cobertura arbórea mundial, incluyendo 4,3 M ha de bosques primarios tropicales (>11 campos de fútbol por minuto).',
        beforeMetric: '> 11 Canchas de Fútbol / min',
        beforeImg: './assets/u_wri_tropics.jpg',
        beforeCap: 'Destrucción acelerada de bosques primarios tropicales equivalente a más de 11 canchas de fútbol cada minuto.',
        afterMetric: 'Vigilancia de Alta Resolución',
        afterImg: './assets/u_satellite_space.jpg',
        afterCap: 'Integración de sensores remotos y drones autónomos para auditar la cobertura arbórea en tiempo real.'
      },
      {
        match: '42 % del total',
        cat: 'ESCENA 03 · ESTADÍSTICA MUNDIAL DE INCENDIOS (WRI, 2026)',
        title: '🔥 EL 42 % DE LA PÉRDIDA MUNDIAL DE ÁRBOLES ES POR INCENDIOS',
        explain: 'Goldman et al. (2026) demostraron que los incendios fueron responsables del 42 % de toda la pérdida mundial de cobertura arbórea, quemando en los últimos tres años más del doble de árboles que hace dos décadas por olas de calor extremo.',
        beforeMetric: 'Doble de Árboles Quemados',
        beforeImg: './assets/u_wildfire_flames.jpg',
        beforeCap: 'Olas de calor extremo y sequías severas convierten los bosques del planeta en material altamente inflamable.',
        afterMetric: 'Detección en Fase de Conato',
        afterImg: './assets/u_fire_night.jpg',
        afterCap: 'Localización temprana del foco térmico antes de que las llamas se vuelvan incontrolables.'
      },
      // ESCENA 04 (2 cuadros de Estadística en el Perú)
      {
        match: 'Reporte INDECI',
        cat: 'ESCENA 04 · ESTADÍSTICA NACIONAL EN EL PERÚ (INDECI / COEN-SINPAD, 2024)',
        title: '🇵🇪 1 754 INCENDIOS FORESTALES EN EL PERÚ Y PICO DE 840 EN SEPTIEMBRE',
        explain: 'El INDECI (2024), mediante el COEN y la plataforma digital SINPAD, registró 1 754 incendios forestales en el Perú en 2024 (con un pico de 840 en septiembre), destruyendo 63 710,38 ha naturales y 14 971,57 ha de cultivos, dejando 285 heridos y 35 fallecidos.',
        beforeMetric: '63 710 ha + 35 Fallecidos',
        beforeImg: './assets/u_indeci_fire.jpg',
        beforeCap: 'Siniestros forestales fuera de control en la sierra y selva peruana durante la temporada crítica de septiembre.',
        afterMetric: 'Plataforma Alerta SINPAD + Drones',
        afterImg: './assets/u_command_center.jpg',
        afterCap: 'Conexión directa de las alertas de drones inteligentes con los centros de operaciones de emergencia (COEN / COER).'
      },
      {
        match: 'Defensoría del Pueblo',
        cat: 'ESCENA 04 · CAUSA HUMANA EN EL PERÚ (DEFENSORÍA N.° 225 Y SERFOR, 2024)',
        title: '⚠️ EL 95 % DE LOS INCENDIOS EN EL PERÚ SON CAUSADOS POR HUMANOS',
        explain: 'La Defensoría del Pueblo (2024, Informe Defensorial n.° 225) y el SERFOR advirtieron que el 95 % de los incendios forestales en el país se originan por actividades humanas, sobre todo por la quema tradicional de rastrojos y pastos secos para abrir chacras.',
        beforeMetric: '95 % Quemas Agrícolas',
        beforeImg: './assets/u_serfor_burn.jpg',
        beforeCap: 'Quema tradicional de rastrojos y pastos secos que se sale de control rápidamente por los fuertes vientos andinos.',
        afterMetric: 'Detección de Quemas y Tala',
        afterImg: './assets/u_farmland_drone.jpg',
        afterCap: 'Patrullaje preventivo con drones sobre zonas agrícolas altoandinas para alertar quemas no autorizadas.'
      },
      // ESCENA 05 (2 cuadros de La Libertad COER)
      {
        match: 'COER La Libertad',
        cat: 'ESCENA 05 · IMPACTO REGIONAL EN LA LIBERTAD (COER / AGRARIA.PE, 2024)',
        title: '⛰️ 2 990 HECTÁREAS DESTRUIDAS EN +42 INCENDIOS EN LA LIBERTAD',
        explain: 'En la región La Libertad se registraron más de 42 incendios forestales en una sola temporada crítica, destruyendo 2 990 hectáreas de pastizales de ichu, bosques de eucalipto y pino, y cultivos de panllevar (trigo, cebada y tarwi), además de afectar 41 viviendas y ganado.',
        beforeMetric: '2 990 ha + 41 Viviendas',
        beforeImg: './assets/u_burned_trees.jpg',
        beforeCap: 'Pérdida de bosques de eucalipto, pino y cultivos campesinos de trigo, cebada y tarwi en la sierra liberteña.',
        afterMetric: 'Protección Rural Liberteña',
        afterImg: './assets/u_santiago_chuco.jpg',
        afterCap: 'Cobertura aérea rápida sobre valles y laderas de difícil acceso para proteger viviendas y ganado comunal.'
      },
      {
        match: 'Santiago de Chuco',
        cat: 'ESCENA 05 · PROVINCIAS CRÍTICAS Y CABECERAS DE CUENCA EN LA LIBERTAD',
        title: '💧 SANTIAGO DE CHUCO (+1 000 HA), OTUZCO, SÁNCHEZ CARRIÓN, BOLÍVAR Y PATAZ',
        explain: 'Santiago de Chuco fue la provincia más perjudicada con más de 1 000 hectáreas consumidas por el fuego. No atender a tiempo estos incendios destruye los colchones naturales de agua en las cabeceras de cuenca que abastecen a los valles de La Libertad y erosiona el suelo.',
        beforeMetric: 'Erosión y Pérdida de Agua',
        beforeImg: './assets/u_eroded_slope.jpg',
        beforeCap: 'Destrucción de la cobertura vegetal en laderas andinas que provoca erosión del suelo y sequía en las cuencas.',
        afterMetric: 'Cabeceras de Cuenca Protegidas',
        afterImg: './assets/u_andean_lagoon.jpg',
        afterCap: 'Conservación de los colchones hídricos altoandinos que garantizan el agua para toda la región La Libertad.'
      },
      // ESCENA 06 (4 cuadros de Problema y Objetivos - Anexo 1)
      {
        match: 'Problema General',
        cat: 'ESCENA 06 · ANEXO 1: FORMULACIÓN DEL PROBLEMA GENERAL',
        title: '❓ PROBLEMA GENERAL DE LA INVESTIGACIÓN (LA LIBERTAD 2026)',
        explain: 'Formulación textual del informe: «¿De qué manera la implementación de un sistema de información con drones inteligentes influye en el tiempo de detección temprana de incendios forestales y deforestación en zonas vulnerables de La Libertad durante el año 2026?»',
        beforeMetric: 'Demora Crítica en la Sierra',
        beforeImg: './assets/u_prob_gen.jpg',
        beforeCap: 'Interrogante científica: La geografía accidentada y falta de caminos retrasan por horas la detección de anomalías.',
        afterMetric: 'Variable: Sistema con Drones IA',
        afterImg: './assets/u_quadcopter_sky.jpg',
        afterCap: 'Evaluación del impacto directo de los vehículos aéreos no tripulados en reducir el tiempo de detección a segundos.'
      },
      {
        match: 'Objetivo General',
        cat: 'ESCENA 06 · ANEXO 1: OBJETIVO GENERAL DE LA INVESTIGACIÓN',
        title: '🎯 OBJETIVO GENERAL: OPTIMIZAR TIEMPOS DE DETECCIÓN Y REPORTE',
        explain: 'Formulación textual del informe: «Determinar el impacto de un sistema de información con drones inteligentes en la optimización de los tiempos de detección temprana y reporte de incendios forestales y deforestación en la región La Libertad, 2026.»',
        beforeMetric: 'Tiempos de Respuesta Enormes',
        beforeImg: './assets/u_stopwatch_time.jpg',
        beforeCap: 'Sin optimización tecnológica: Las horas perdidas entre el inicio del fuego y el aviso impiden apagar el conato.',
        afterMetric: 'Tiempos Optimizados al Máximo',
        afterImg: './assets/u_obj_gen.jpg',
        afterCap: 'Propósito central: Demostrar con evidencia científica 2023–2026 la reducción drástica en los tiempos de detección y alerta.'
      },
      {
        match: 'Objetivos Específicos 1 y 2',
        cat: 'ESCENA 06 · ANEXO 1: OBJETIVOS ESPECÍFICOS 1 (ALGORITMO) Y 2 (REDES)',
        title: '⚡ OE1 (EXACTITUD VS. FALSOS POSITIVOS) Y OE2 (TIEMPO DE TRANSMISIÓN)',
        explain: 'OE1 mide la tasa de exactitud y el margen de error del algoritmo al diferenciar focos reales de falsos positivos (neblina/sol). OE2 compara el tiempo de transmisión y procesamiento desde que el dron detecta la anomalía hasta notificar a las autoridades frente a métodos tradicionales.',
        beforeMetric: 'Falsos Positivos y Latencia',
        beforeImg: './assets/u_sun_glare_trees.jpg',
        beforeCap: 'Reto informático: Evitar que el reflejo solar engañe a la cámara y evitar que el envío de datos demore.',
        afterMetric: 'Alta Exactitud + Baja Latencia',
        afterImg: './assets/u_oe1_oe2.jpg',
        afterCap: 'Medición cuantitativa de precisión algorítmica (hasta 98,39 %) y velocidad de transmisión en segundos.'
      },
      {
        match: 'Objetivo Específico 3',
        cat: 'ESCENA 06 · ANEXO 1: OBJETIVO ESPECÍFICO 3 (BASE DE DATOS ESPACIAL)',
        title: '🗺️ OE3: EFICIENCIA DEL HISTORIAL GEORREFERENCIADO PARA MAPAS DE CALOR',
        explain: 'Formulación textual del informe: «Evaluar la eficiencia del sistema informático en el almacenamiento y estructuración del historial georreferenciado de las zonas afectadas, para proyectar mapas de calor sobre el avance de la deforestación en la sierra liberteña.»',
        beforeMetric: 'Datos Dispersos sin Coordenadas',
        beforeImg: './assets/u_paper_maps.jpg',
        beforeCap: 'Registros manuales sin estructura espacial que impiden visualizar en qué laderas avanza más la tala.',
        afterMetric: 'Base de Datos GIS + Mapas de Calor',
        afterImg: './assets/u_oe3_db.jpg',
        afterCap: 'Estructuración eficiente mediante coordenadas GeoJSON y Shapefiles para proyectar mapas de calor multitemporales.'
      },
      // ESCENA 07 (2 cuadros de Marcos Teóricos)
      {
        match: 'Arquitecturas Especializadas',
        cat: 'ESCENA 07 · ANÁLISIS CRÍTICO DE MARCOS TEÓRICOS (2023–2026)',
        title: '🧠 REDES YOLO (INCENDIOS EN TIEMPO REAL) VS. U-NET / VGG16 (DEFORESTACIÓN)',
        explain: 'Los antecedentes de incendios (Saydirasulovich, Shamta, Yun, Luo, Ma) coinciden en usar redes de una sola etapa (YOLOv5, YOLOv8, YOLO11) porque procesan video al instante; mientras que en tala (Md Jelas, Borse) usan segmentación semántica U-Net, DeepLabV3+ y VGG16.',
        beforeMetric: 'Cómputo Pesado Tradicional',
        beforeImg: './assets/u_neural_code.jpg',
        beforeCap: 'Redes antiguas de dos etapas que requerían servidores gigantes y no podían correr dentro de un dron.',
        afterMetric: 'Familia YOLO + Segmentación U-Net',
        afterImg: './assets/u_theory_yolo.jpg',
        afterCap: 'Combinación de detección rápida en vuelo (YOLO) con segmentación precisa por píxeles (U-Net).'
      },
      {
        match: 'Brecha Teórica',
        cat: 'ESCENA 07 · VACÍO TEÓRICO DETECTADO EN LA LITERATURA',
        title: '🔍 BRECHA TEÓRICA: UNIR DETECCIÓN DE INCENDIOS Y TALA EN UN SOLO SISTEMA',
        explain: 'Hallazgo propio de nuestro informe: la literatura internacional estudió los incendios y la deforestación como si fueran dos problemas separados con programas distintos, pero en los Andes peruanos el desmonte (tala) y las quemas agrícolas ocurren al mismo tiempo.',
        beforeMetric: 'Sistemas Separados e Incompletos',
        beforeImg: './assets/u_theory_andes.jpg',
        beforeCap: 'En la sierra peruana los agricultores talan y queman el desmonte simultáneamente para abrir terrenos de cultivo.',
        afterMetric: 'Sistema Unificado Incendios + Tala',
        afterImg: './assets/image3.png',
        afterCap: 'Aporte de nuestra investigación: Integrar ambas detecciones dentro de una sola arquitectura informática.'
      },
      // ESCENA 08, 09, 10 y 11 (Los 7 Estudios Científicos)
      {
        match: 'Saydirasulovich',
        cat: 'ESTUDIO 1 Y RESULTADO OE1 · SAYDIRASULOVICH ET AL. (2023) · SENSORS Q1',
        title: '💨 YOLOv8 + BIFORMER + GSCONV: 79,4 % AP EN HUMO (SAYDIRASULOVICH, 2023)',
        explain: 'Agregaron atención BiFormer, convoluciones ligeras GSConv y función Wise-IoU v3 a YOLOv8 para detectar humo desde drones. Lograron 79,4 % de precisión media (+3,3 % sobre YOLOv8 base) y 92,6 % en humo grande, pero en humo pequeño bajó a 71,3 % (28,7 % de margen de error ante nubes bajas).',
        beforeMetric: '28,7 % Error en Humo Pequeño',
        beforeImg: './assets/u_low_clouds.jpg',
        beforeCap: 'Limitación detectada: Cuando la columna de humo recién empieza, las nubes bajas y cambios de luz generan falsas alarmas.',
        afterMetric: '79,4 % AP General (92,6 % Grande)',
        afterImg: './assets/image10.png',
        afterCap: 'Mecanismo BiFormer + GSConv localizando columnas de humo desde vehículos aéreos no tripulados.'
      },
      {
        match: 'Md Jelas',
        cat: 'ESTUDIO 2 Y RESULTADO OE1/OE3 · MD JELAS ET AL. (2024) · FRONTIERS Q1',
        title: '🌲 U-NET Y DEEPLABV3+: 92,78 % A 98,14 % EN TALA (>98 % EN PERÚ)',
        explain: 'Evaluaron 22 estudios indexados en Scopus y Web of Science sobre segmentación de deforestación. Los modelos U-Net con atención y DeepLabV3+ lograron hasta 98,14 % de exactitud separando bosque sano de tala o minería, superando el 98 % con drones en la Amazonía peruana.',
        beforeMetric: 'Semanas de Mapeo Manual',
        beforeImg: './assets/u_amazon_river.jpg',
        beforeCap: 'Inspección humana lenta de mapas satelitales afectada por sombras de árboles y relieve montañoso.',
        afterMetric: '98,14 % Exactitud en Minutos',
        afterImg: './assets/image9.png',
        afterCap: 'Segmentación automática píxel por píxel con drones en la Amazonía peruana superando el 98 % de acierto.'
      },
      {
        match: 'Shamta y Demir',
        cat: 'ESTUDIO 3 Y RESULTADO OE1/OE2 · SHAMTA Y DEMIR (2024) · PLOS ONE Q1',
        title: '🚁 DRON CUADRICÓPTERO CON JETSON NANO Y GSM: 96 % EXACTITUD EN VIVO',
        explain: 'Construyeron un cuadricóptero con cámara, GPS/GSM, Raspberry Pi (Navio2) y NVIDIA Jetson Nano. Alcanzaron 96 % de exactitud en clasificación (CNN-RCNN / YOLOv8) y 89 % detectando fuego en pleno vuelo (YOLOv8n), enviando foto + GPS en segundos (batería ~25 min).',
        beforeMetric: 'Batería Limitada (~25 min)',
        beforeImg: './assets/u_electronics_lab.jpg',
        beforeCap: 'Reto de hardware: La autonomía de 25 minutos exige procesar la imagen en el mismo dron sin gastar energía de más.',
        afterMetric: '96 % Exactitud + Alerta GSM',
        afterImg: './assets/image11.png',
        afterCap: 'Envío inmediato de la fotografía del fuego y coordenadas GPS a la estación terrena en cuestión de segundos.'
      },
      {
        match: 'Yun et al.',
        cat: 'ESTUDIO 4 Y RESULTADO OE2 · YUN ET AL. (2025) · REVISTA FIRE Q1',
        title: '🔥 YOLOv8 + SPDCONV + MLCA: +5,5 % SENSIBILIDAD Y -43,8 % PARÁMETROS',
        explain: 'Para detectar focos diminutos tapados por ramas y borrosos por el viento en montaña (>3 200 fotos aéreas), integraron SPDConv, C2f-PConv, atención MLCA y W-IoU. Subieron la sensibilidad en +5,5 %, la exactitud en +2,17 % y redujeron los parámetros en 43,8 % (quedando en 5,96 millones).',
        beforeMetric: 'Focos Ocultos tras Ramas',
        beforeImg: './assets/u_server_rack.jpg',
        beforeCap: 'Cuando el dron vuela alto sobre la montaña, las primeras llamas ocupan muy pocos píxeles y las ramas las tapan.',
        afterMetric: '5,96 M Parámetros (-43,8 %)',
        afterImg: './assets/image12.png',
        afterCap: 'Modelo ultraligero (-43,3 % de peso de archivo) que distingue llamas diminutas entre los árboles sin saturar el dron.'
      },
      {
        match: 'Luo et al.',
        cat: 'ESTUDIO 5 Y RESULTADO OE1/OE2 · LUO ET AL. (2025) · FORESTS Q1',
        title: '🌤️ YOLO-UFS (MOBILENETV4): 91,3 % mAP Y 7,4 MB A 30 FPS EN JETSON NANO',
        explain: 'Entrenaron la red con muestras negativas reales del bosque (brillo del sol, neblina matutina, hojas rojizas y sombras) y añadieron MobileNetV4 + BiFPN + estabilización. Lograron 91,3 % mAP (+3,8 %) y redujeron el peso en >74 %, corriendo a 30 FPS reales con solo 7,4 MB en una Jetson Nano.',
        beforeMetric: 'Brillo Solar y Hojas Rojizas',
        beforeImg: './assets/u_autumn_fog.jpg',
        beforeCap: 'Elementos distractores del bosque real (neblina matutina, sol y hojas amarillas/rojas) que engañan a cámaras normales.',
        afterMetric: '7,4 MB · 30 FPS Reales (91,3 %)',
        afterImg: './assets/u_hardware_chip.jpg',
        afterCap: 'Ejecución fluida a 30 cuadros por segundo en tarjeta económica Jetson Nano sin falsas alarmas.'
      },
      {
        match: 'Borse',
        cat: 'ESTUDIO 6 Y RESULTADO OE1/OE3 · BORSE ET AL. (2025) · PLOS ONE Q1',
        title: '🌲 SISTEMA AETDA (VGG16 + YOLOv8): 98,39 % EN 10 400+ ÁRBOLES Y GEOJSON',
        explain: 'Evaluaron más de 10 400 árboles con imágenes de dron de menos de 10 cm/píxel integradas con coordenadas GeoJSON y Shapefiles. VGG16 alcanzó 98,39 % de exactitud de prueba y YOLOv8 logró un AUC de 0,95 trazando cajas delimitadoras por cada copa de árbol.',
        beforeMetric: 'Satélite Borroso (1–5 m/px)',
        beforeImg: './assets/u_pine_canopy.jpg',
        beforeCap: 'Las imágenes satelitales no permiten distinguir copas individuales ni fiscalizar la división ilegal de tierras.',
        afterMetric: '98,39 % VGG16 · AUC 0,95',
        afterImg: './assets/image17.png',
        afterCap: 'Conteo y clasificación automatizada de 10 400 árboles exportando coordenadas exactas en GeoJSON y Shapefiles.'
      },
      {
        match: 'Ma et al.',
        cat: 'ESTUDIO 7 Y RESULTADO OE1/OE2 · MA ET AL. (2026) · SUSTAINABILITY Q1',
        title: '⚡ AHE-YOLO (YOLO11): 94,8 % mAP, PESO DE SOLO 3,5 MB Y 333,3 FPS',
        explain: 'El estudio más reciente (2026): incorporaron los módulos ADown, HS-FPN y EMBC en YOLO11 sobre 5 118 imágenes complejas (bosque denso, humo lejano e incendios nocturnos). Lograron 94,8 % mAP, 85,1 % sensibilidad, -39,7 % parámetros (1,56 M), solo 3,5 MB de peso y 333,3 FPS en laboratorio.',
        beforeMetric: 'Humo Lejano e Incendios Nocturnos',
        beforeImg: './assets/u_distant_smoke.jpg',
        beforeCap: 'Escenarios complejos de noche o con humo muy distante donde los algoritmos convencionales pierden sensibilidad.',
        afterMetric: '3,5 MB · 333,3 FPS (+16,5 %)',
        afterImg: './assets/u_gpu_circuit.jpg',
        afterCap: 'Máxima compresión (1,56 M parámetros) y mapas térmicos de activación para vigilancia forestal sostenible.'
      },
      // ESCENA 12 (3 cuadros de Resultados OE3: <10 cm/px, Amazonía Peruana y GeoJSON)
      {
        match: '10 cm/píxel',
        cat: 'RESULTADOS OBJETIVO ESPECÍFICO 3 · RESOLUCIÓN ESPACIAL EN SENCILLO',
        title: '🔍 ¿QUÉ ES RESOLUCIÓN MENOR A 10 CM/PÍXEL? (50 VECES MÁS NÍTIDO)',
        explain: 'Explicación fácil para el jurado: En una foto de satélite cada píxel mide de 1 a 5 metros, por lo que un árbol se ve como un punto borroso. Con el dron volando bajo las nubes, cada píxel mide MENOS DE 10 CENTÍMETROS: se ve cada copa y rama con nitidez total (98,39 % de exactitud en 10 400 árboles).',
        beforeMetric: 'Satélite: 1 a 5 m/píxel',
        beforeImg: './assets/u_satellite_space.jpg',
        beforeCap: 'Vista lejana desde el espacio: Baja nitidez y bloqueo por nubes que impiden detectar tala selectiva temprano.',
        afterMetric: 'Dron: < 10 cm/píxel (98,39 %)',
        afterImg: './assets/image17.png',
        afterCap: 'Vista cercana de dron: Claridad milimétrica para auditar cada copa de árbol y detectar claros de deforestación.'
      },
      {
        match: 'Amazonía Peruana',
        cat: 'RESULTADOS OBJETIVO ESPECÍFICO 3 · SEGMENTACIÓN AUTOMÁTICA EN PERÚ',
        title: '🇵🇪 ¿QUÉ ES SEGMENTACIÓN U-NET > 98 % EN LA AMAZONÍA PERUANA?',
        explain: 'Explicación fácil para el jurado: Revisar mapas a mano para buscar zonas taladas tomaba semanas. La red neuronal U-Net analiza la foto del dron y colorea automáticamente píxel por píxel dónde hay bosque sano y dónde hay tala o minería ilegal en minutos, logrando más de 98 % de exactitud en el Perú.',
        beforeMetric: 'Revisión Humana: Semanas',
        beforeImg: './assets/u_amazon_river.jpg',
        beforeCap: 'Inspección manual lenta y propensa a errores humanos frente a miles de hectáreas de bosque.',
        afterMetric: 'U-Net en Perú: > 98 % en Minutos',
        afterImg: './assets/image9.png',
        afterCap: 'Cuantificación automática de hectáreas deforestadas en minutos con precisión comprobada en territorio peruano.'
      },
      {
        match: 'GeoJSON',
        cat: 'RESULTADOS OBJETIVO ESPECÍFICO 3 · BASE DE DATOS Y MAPAS DE CALOR',
        title: '🗺️ ¿QUÉ ES FORMATO GEOJSON Y POR QUÉ REEMPLAZA AL VIDEO PESADO?',
        explain: 'Explicación fácil para el jurado: Guardar horas de video en la base de datos llenaría la memoria y no se podría transmitir desde la sierra. GeoJSON es un archivo ultraligero que guarda solo las coordenadas GPS del borde de la zona quemada o talada (polígonos), permitiendo dibujar mapas de calor mes a mes.',
        beforeMetric: 'Videos Pesados Imposibles de Subir',
        beforeImg: './assets/u_drone_battery.jpg',
        beforeCap: 'Almacenar videos completos satura el servidor y consume el ancho de banda en zonas rurales.',
        afterMetric: 'Polígonos GeoJSON + Mapas de Calor',
        afterImg: './assets/image14.png',
        afterCap: 'Estructuración ligera de latitud, longitud y fecha para proyectar mapas de calor del avance de la deforestación.'
      },
      // ESCENA 14 (3 barras de Discusión Crítica)
      {
        match: 'Consensos Científicos',
        cat: 'ESCENA 14 · DISCUSIÓN CRÍTICA: CONVERGENCIAS ENTRE LOS 7 AUTORES',
        title: '✅ CONSENSOS: SUPERIORIDAD DEL DRON BAJO NUBES Y COMPRESIÓN POR BATERÍA',
        explain: 'Existe acuerdo total en dos puntos: 1) El dron (<10 cm/px, volando bajo las nubes) supera ampliamente a las torres fijas y a los satélites (1–5 m/px, bloqueados por neblina); y 2) Como la batería dura ~25 minutos, es obligatorio comprimir los algoritmos de IA (a 3,5–7,4 MB) para ahorrar energía a bordo.',
        beforeMetric: 'Torres Fijas y Satélites Ciegos',
        beforeImg: './assets/u_lookout_tower.jpg',
        beforeCap: 'Observación estática tradicional incapaz de ver detrás de las montañas o debajo de la neblina andina.',
        afterMetric: 'Dron + IA Ultraligera (3,5–7,4 MB)',
        afterImg: './assets/image1.png',
        afterCap: 'Monitoreo aéreo activo con redes neuronales comprimidas que maximizan la autonomía de vuelo.'
      },
      {
        match: 'Controversias Técnicas',
        cat: 'ESCENA 14 · DISCUSIÓN CRÍTICA: DIVERGENCIAS EN LA LITERATURA',
        title: '⚡ CONTROVERSIAS: ¿HUMO VS. LLAMAS? Y ¿PROCESAR EN EL AIRE VS. ESTACIÓN BASE?',
        explain: 'Debate científico 1: Saydirasulovich (2023) prioriza buscar humo primero, pero Yun, Luo y Ma rebaten que en montaña la neblina matutina es idéntica al humo joven y exigen combinar con focos de calor e imágenes negativas. Debate 2: Shamta y Luo procesan a bordo en Jetson Nano (30 FPS) para alerta inmediata, mientras Borse procesa en PC base con VGG16 para máxima exactitud (98,39 %).',
        beforeMetric: 'Debate: Solo Humo / PC Base',
        beforeImg: './assets/u_clouds_mountain.jpg',
        beforeCap: 'Depender únicamente del humo visible en zonas altoandinas con neblina matutina provoca falsos positivos.',
        afterMetric: 'Fusión Humo + Calor + Edge AI',
        afterImg: './assets/u_ground_station.jpg',
        afterCap: 'Síntesis equilibrada: Procesamiento ligero de alerta rápida en el dron + auditoría geoespacial en estación base.'
      },
      {
        match: 'Lagunas y Propuesta',
        cat: 'ESCENA 14 · APORTE INGENIERÍA DE SISTEMAS PARA LA SIERRA DE LA LIBERTAD',
        title: '⛰️ PROPUESTA ANDINA: CÁMARA TÉRMICA EN ICHU + RED DE RADIO LORAWAN',
        explain: 'Descubrimos dos lagunas para aplicar en Santiago de Chuco, Otuzco, Sánchez Carrión, Bolívar y Pataz: 1) Superar el sesgo de cámaras RGB diurnas integrando cámaras térmicas infrarrojas económicas que detecten brasas nocturnas en ichu; y 2) Superar la falta de señal celular GSM en quebradas usando radio de largo alcance LoRaWAN y guardado local con sincronización automática.',
        beforeMetric: 'Incendios Nocturnos sin Señal GSM',
        beforeImg: './assets/u_andean_canyon.jpg',
        beforeCap: 'Quebradas profundas de los Andes liberteños donde no llega la cobertura de internet móvil 4G/GSM.',
        afterMetric: 'Sensor Térmico IR + Red LoRaWAN',
        afterImg: './assets/image18.png',
        afterCap: 'Detección térmica de brasas ocultas en pastizales de ichu y transmisión por radiofrecuencia LoRaWAN.'
      }
    ];

    function openVisualCompare(item) {
      document.getElementById('vcCategory').textContent = item.cat;
      document.getElementById('vcTitle').textContent = item.title;
      document.getElementById('vcSimpleExplain').textContent = item.explain;
      document.getElementById('vcBeforeMetric').textContent = item.beforeMetric;
      document.getElementById('vcBeforeImg').src = item.beforeImg;
      document.getElementById('vcBeforeCaption').textContent = item.beforeCap;
      document.getElementById('vcAfterMetric').textContent = item.afterMetric;
      document.getElementById('vcAfterImg').src = item.afterImg;
      document.getElementById('vcAfterCaption').textContent = item.afterCap;
      document.getElementById('visualCompareModal3D').classList.add('open');
    }

    function closeVisualCompare(ev) {
      document.getElementById('visualCompareModal3D').classList.remove('open');
    }

    // Conectar automáticamente el clic en todas las tarjetas (.risk-card, .frost-carousel-card, .glow-bar, .white-step-card, .entry-pill-card)
    document.querySelectorAll('.risk-card, .frost-carousel-card, .glow-bar, .white-step-card, .entry-pill-card').forEach(card => {
      card.style.cursor = 'pointer';
      card.addEventListener('click', () => {
        const text = card.innerText || '';
        const found = visualCompareDB.find(item => text.includes(item.match));
        if (found) {
          openVisualCompare(found);
        } else {
          // Comparativa general de progreso del proyecto para cualquier otra tarjeta
          openVisualCompare({
            cat: 'PROGRESO E IMPACTO DEMOSTRADO · UCV 2026',
            title: '🚁 IMPACTO REAL DEL SISTEMA DE DRONES INTELIGENTES',
            explain: 'Toda la evidencia científica revisada (2023–2026) confirma que integrar drones (<10 cm/píxel), visión artificial ultraligera (YOLO11 / U-Net), cámaras térmicas y radio LoRaWAN reduce la detección de incendios y tala en La Libertad de varias horas a pocos segundos.',
            beforeMetric: 'Vigilancia Tradicional Reactiva',
            beforeImg: './assets/image10.png',
            beforeCap: 'Sin el sistema: 2 990 ha perdidas en La Libertad y 1 754 incendios en el Perú por avisos tardíos y bloqueo satelital por nubes.',
            afterMetric: '98,39 % Exactitud · Alerta en Segundos',
            afterImg: './assets/image1.png',
            afterCap: 'Con el sistema propuesto: Detección temprana bajo las nubes, cero falsas alarmas por neblina y mapas de calor GeoJSON en tiempo real.'
          });
        }
      });
    });

    goToScene(0);"""

html = html.replace(
    "// 5. Animar barras de exactitud si la escena las tiene",
    "if (typeof sceneDroneMoods !== 'undefined') { setDroneEmotion(sceneDroneMoods[currentScene]); }\n      // 5. Animar barras de exactitud si la escena las tiene"
)

html = html.replace("    animateBokeh();\n\n    goToScene(0);", js_block)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

def embed_img(m):
    rel = m.group(0).replace("./", "")
    full = os.path.join(base_dir, rel)
    if os.path.exists(full):
        mime = "image/jpeg" if full.endswith(".jpg") else "image/png"
        with open(full, "rb") as img_f:
            return f"data:{mime};base64," + base64.b64encode(img_f.read()).decode("ascii")
    return m.group(0)

portable_html = re.sub(r"\./assets/[a-zA-Z0-9_]+\.(?:png|jpg)", embed_img, html)
with open(portable_path, "w", encoding="utf-8") as f:
    f.write(portable_html)

print("CLEAN MASTER GENERATED! No broken JS in menuDrawer, zero overlap on cover! Portable bytes:", os.path.getsize(portable_path))
