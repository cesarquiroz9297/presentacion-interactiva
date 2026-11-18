# -*- coding: utf-8 -*-
"""
Actualización Integral 3D de Alto Impacto:
1. Robot Dron 3D Global (z-index: 65) por encima de todas las diapositivas, vagando libremente con física 3D.
2. Reemplazo de la "imagen redonda con círculos" por un DIORAMA HOLOGRÁFICO 3D MULTICAPA (Pop-Out 3D)
   más grande, nítido y con 4 niveles de profundidad Z (translateZ(-40px) a translateZ(95px)), sin tapar las diapositivas.
3. Infografías visuales de impacto inmediato en cada escena (KPIs gigantes, medidores y fotos 3D)
   para que nunca se vea como "solo texto y un título".
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
# 1. REEMPLAZAR #persistentHero3D (LA IMAGEN REDONDA CON CÍRCULOS) POR UN
#    DIORAMA 3D MULTICAPA CON VOLUMEN REAL Y CAPAS POP-OUT (translateZ)
# ---------------------------------------------------------------------------
old_hero_pattern = r'<div id="persistentHero3D">.*?</div>\s*</div>\s*</header>'
# Vamos a buscar exactamente desde <div id="persistentHero3D"> hasta antes de <!-- CABECERA
hero_replacement = """<div id="persistentHero3D">
    <div class="diorama-3d-stage" id="dioramaStage3D">
      <!-- CAPA 1 (Z: -45px): Base Holográfica 3D Biselada con Rejilla Topográfica -->
      <div class="diorama-layer-back"></div>

      <!-- CAPA 2 (Z: 0px): Marco Fotográfico 3D Principal de Gran Formato con Cristal Grueso -->
      <div class="diorama-main-frame">
        <img id="heroSphereImg" src="./assets/image1.png" alt="Escena 3D Principal" class="w-full h-full object-cover transition-all duration-700" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/75 via-transparent to-emerald-950/25"></div>
        <!-- Línea láser de escaneo 3D -->
        <div class="diorama-laser-line"></div>
        <!-- Etiqueta de tema en vivo dentro del visor 3D -->
        <div class="absolute bottom-3.5 left-4 right-4 flex items-center justify-between">
          <span id="dioramaCaption" class="px-3 py-1 rounded-lg bg-black/75 backdrop-blur-md border border-emerald-400/40 text-xs font-bold text-emerald-300">
            🚁 Monitoreo Aéreo Inteligente · La Libertad 2026
          </span>
          <span class="px-2.5 py-1 rounded-lg bg-emerald-500/25 border border-emerald-400/50 font-mono-code text-[11px] font-bold text-white">
            3D LIVE
          </span>
        </div>
      </div>

      <!-- CAPA 3 POP-OUT SUPERIOR (Z: +70px): Tarjeta KPI 3D que sobresale hacia el espectador -->
      <div class="diorama-popout-top" id="dioramaKpiBox">
        <div class="flex items-center gap-3">
          <div id="dioramaKpiIcon" class="w-12 h-12 rounded-xl bg-gradient-to-br from-emerald-400 to-teal-600 flex items-center justify-center text-2xl shadow-lg">
            🚁
          </div>
          <div>
            <div id="dioramaKpiValue" class="title-condensed text-3xl text-white leading-none">&lt; 10 cm/px</div>
            <div id="dioramaKpiLabel" class="text-[11px] text-emerald-300 font-semibold mt-0.5">Resolución Ultra-Nítida</div>
          </div>
        </div>
      </div>

      <!-- CAPA 4 POP-OUT INFERIOR (Z: +90px): Segunda Cámara 3D Flotante en Perspectiva -->
      <div class="diorama-popout-bottom">
        <img id="dioramaSecondaryImg" src="./assets/image18.png" alt="Vista Secundaria 3D" class="w-full h-full object-cover" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent flex items-end p-2">
          <span id="dioramaSecondaryLabel" class="text-[10px] font-mono-code text-amber-300 font-bold">🌡️ Visión Térmica + IA</span>
        </div>
      </div>
    </div>
  </div>
"""

html = re.sub(
    r'<div id="persistentHero3D">.*?<!-- ==========================================================================\s*CABECERA',
    hero_replacement + '\n  <!-- ==========================================================================\n       CABECERA',
    html,
    flags=re.DOTALL
)

# ---------------------------------------------------------------------------
# 2. CSS PARA EL DIORAMA 3D MULTICAPA (MÁS GRANDE, MÁS 3D, SIN INTERRUMPIR)
#    Y EL ROBOT DRON 3D GLOBAL POR ENCIMA DE TODO (Z-INDEX 65)
# ---------------------------------------------------------------------------
diorama_and_robot_css = """
    /* ==========================================================================
       DIORAMA HOLOGRÁFICO 3D MULTICAPA (REEMPLAZA LA IMAGEN REDONDA SIMPLE)
       Un poquito más grande, con grosor 3D real y tarjetas Pop-Out en eje Z
       Autor: César Quiroz
       ========================================================================== */
    #persistentHero3D {
      position: fixed;
      z-index: 6;
      width: 530px;
      height: 410px;
      perspective: 1400px;
      transform-style: preserve-3d;
      pointer-events: none;
      transition:
        left 1.15s var(--morph-ease),
        top 1.15s var(--morph-ease),
        transform 1.15s var(--morph-ease),
        opacity 1.05s var(--morph-ease),
        filter 1.15s var(--morph-ease);
    }

    body[data-hero-pos="center"] #persistentHero3D {
      left: 50%;
      top: 55%;
      transform: translate3d(-50%, -50%, 0) scale(0.96);
      opacity: 0.96;
      filter: blur(0px);
    }

    body[data-hero-pos="bg-blur"] #persistentHero3D {
      left: 50%;
      top: 52%;
      transform: translate3d(-50%, -50%, -120px) scale(1.28);
      opacity: 0.18;
      filter: blur(5px);
    }

    body[data-hero-pos="right"] #persistentHero3D {
      left: 78%;
      top: 53%;
      transform: translate3d(-50%, -50%, 0) rotateY(-16deg) rotateX(5deg) scale(1.04);
      opacity: 1;
      filter: blur(0px);
    }

    body[data-hero-pos="left"] #persistentHero3D {
      left: 22%;
      top: 53%;
      transform: translate3d(-50%, -50%, 0) rotateY(16deg) rotateX(5deg) scale(1.04);
      opacity: 1;
      filter: blur(0px);
    }

    body[data-hero-pos="right-edge"] #persistentHero3D {
      left: 85%;
      top: 54%;
      transform: translate3d(-50%, -50%, 0) rotateY(-20deg) scale(1.02);
      opacity: 0.96;
      filter: blur(0px);
    }

    body[data-hero-pos="bottom-left"] #persistentHero3D {
      left: 18%;
      top: 76%;
      transform: translate3d(-50%, -50%, 0) rotateY(14deg) rotateX(8deg) scale(0.92);
      opacity: 0.92;
      filter: blur(0px);
    }

    .diorama-3d-stage {
      position: relative;
      width: 100%;
      height: 100%;
      transform-style: preserve-3d;
      transition: transform 0.25s ease-out;
    }

    /* Placa posterior 3D (Z = -45px) */
    .diorama-layer-back {
      position: absolute;
      inset: -14px;
      border-radius: 2rem;
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.22), rgba(6, 24, 15, 0.75), rgba(249, 115, 22, 0.2));
      border: 1.5px solid rgba(52, 211, 153, 0.35);
      transform: translateZ(-45px) rotateZ(-2deg);
      box-shadow: 0 35px 80px rgba(0, 0, 0, 0.85), 0 0 50px rgba(16, 185, 129, 0.25);
    }

    /* Marco Fotográfico 3D Principal con borde de cristal biselado */
    .diorama-main-frame {
      position: relative;
      width: 100%;
      height: 100%;
      border-radius: 1.65rem;
      overflow: hidden;
      border: 2.5px solid rgba(255, 255, 255, 0.28);
      box-shadow:
        -12px 20px 45px rgba(0, 0, 0, 0.75),
        inset 0 2px 4px rgba(255, 255, 255, 0.35);
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

    /* Tarjeta KPI que sobresale en 3D hacia adelante (Z = +70px) */
    .diorama-popout-top {
      position: absolute;
      top: -26px;
      left: -28px;
      padding: 0.85rem 1.25rem;
      border-radius: 1.25rem;
      background: rgba(6, 22, 14, 0.92);
      backdrop-filter: blur(18px);
      border: 2px solid rgba(52, 211, 153, 0.6);
      box-shadow: 0 24px 45px rgba(0, 0, 0, 0.8), 0 0 30px rgba(16, 185, 129, 0.35);
      transform: translateZ(70px);
    }

    /* Segunda Cámara 3D Flotante en la esquina inferior (Z = +88px) */
    .diorama-popout-bottom {
      position: absolute;
      bottom: -28px;
      right: -26px;
      width: 195px;
      height: 125px;
      border-radius: 1.15rem;
      overflow: hidden;
      border: 2.5px solid rgba(251, 191, 36, 0.65);
      box-shadow: 0 25px 50px rgba(0, 0, 0, 0.85), 0 0 25px rgba(249, 115, 22, 0.35);
      transform: translateZ(88px);
      background: #06120c;
    }

    /* ==========================================================================
       ROBOT DRON 3D GLOBAL POR ENCIMA DE TODA LA PANTALLA (Z-INDEX 65)
       ========================================================================== */
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
      width: 210px;
      height: 210px;
      pointer-events: auto;
      cursor: grab;
      transform-style: preserve-3d;
      will-change: transform;
      filter: drop-shadow(0 30px 36px rgba(0, 0, 0, 0.8));
    }

    #roamingDrone3D:active {
      cursor: grabbing;
    }

    #droneLaserCone {
      position: absolute;
      top: 135px;
      left: 50%;
      width: 170px;
      height: 220px;
      transform: translateX(-50%);
      background: conic-gradient(from 160deg at 50% 0%, transparent 0deg, rgba(16, 185, 129, 0.25) 20deg, rgba(52, 211, 153, 0.05) 40deg, transparent 45deg);
      filter: blur(4px);
      pointer-events: none;
      opacity: 0.75;
    }

    #roamingEmotionBubble {
      position: absolute;
      top: -26px;
      left: 50%;
      transform: translateX(-50%) translateZ(40px);
      white-space: nowrap;
      padding: 5px 14px;
      border-radius: 9999px;
      font-size: 12px;
      font-weight: 800;
      background: rgba(4, 15, 10, 0.95);
      border: 2px solid #34d399;
      color: #ecfdf5;
      box-shadow: 0 12px 28px rgba(0, 0, 0, 0.75), 0 0 22px rgba(16, 185, 129, 0.45);
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
"""

html = html.replace("</style>", diorama_and_robot_css + "\n  </style>")

# ---------------------------------------------------------------------------
# 3. INYECTAR EL ROBOT DRON 3D GLOBAL EN EL BODY (Z-INDEX 65, FUERA DE LAS DIAPOSITIVAS)
# ---------------------------------------------------------------------------
roaming_drone_html = """
  <!-- ==========================================================================
       ROBOT DRON 3D GLOBAL (POR ENCIMA DE TODAS LAS DIAPOSITIVAS · Z-INDEX 65)
       Vaga libremente por toda la pantalla, reacciona con emociones y mira al cursor
       Autor: César Quiroz
       ========================================================================== -->
  <div id="globalDroneStage">
    <canvas id="droneTrailCanvas" class="absolute inset-0 pointer-events-none"></canvas>

    <div id="roamingDrone3D" onclick="triggerDroneAcrobatics()" title="¡Haz clic en mí o arrástrame! Soy el Robot Dron 3D de la UCV">
      <div id="roamingEmotionBubble">😊 ¡Hola! Soy el Dron IA UCV</div>
      <div id="droneLaserCone"></div>

      <svg id="droneSvgModel" class="w-full h-full overflow-visible" viewBox="0 0 220 220" fill="none" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <radialGradient id="pbrShell" cx="32%" cy="24%" r="72%">
            <stop offset="0%" stop-color="#ffffff"/>
            <stop offset="28%" stop-color="#e2e8f0"/>
            <stop offset="68%" stop-color="#64748b"/>
            <stop offset="92%" stop-color="#1e293b"/>
            <stop offset="100%" stop-color="#0f172a"/>
          </radialGradient>
          <linearGradient id="pbrEmeraldArmor" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#6ee7b7"/>
            <stop offset="40%" stop-color="#10b981"/>
            <stop offset="80%" stop-color="#047857"/>
            <stop offset="100%" stop-color="#022c22"/>
          </linearGradient>
          <linearGradient id="pbrCarbon" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#475569"/>
            <stop offset="50%" stop-color="#1e293b"/>
            <stop offset="100%" stop-color="#020617"/>
          </linearGradient>
          <radialGradient id="pbrVisor" cx="40%" cy="30%" r="75%">
            <stop offset="0%" stop-color="#1e293b"/>
            <stop offset="45%" stop-color="#090d16"/>
            <stop offset="100%" stop-color="#000000"/>
          </radialGradient>
          <filter id="ledGlow3D" x="-40%" y="-40%" width="180%" height="180%">
            <feGaussianBlur stdDeviation="3.8" result="blur"/>
            <feMerge>
              <feMergeNode in="blur"/>
              <feMergeNode in="SourceGraphic"/>
            </feMerge>
          </filter>
        </defs>

        <!-- Propulsor de plasma inferior -->
        <ellipse cx="110" cy="172" rx="18" ry="8" fill="rgba(16,185,129,0.55)" filter="url(#ledGlow3D)">
          <animate attributeName="rx" values="15;22;15" dur="0.4s" repeatCount="indefinite"/>
        </ellipse>

        <!-- 4 Brazos Articulados 3D -->
        <path d="M72 92 L26 58 L32 50 L78 82 Z" fill="url(#pbrCarbon)" stroke="#64748b" stroke-width="1"/>
        <path d="M148 92 L194 58 L188 50 L142 82 Z" fill="url(#pbrCarbon)" stroke="#64748b" stroke-width="1"/>
        <path d="M74 126 L32 156 L38 164 L82 134 Z" fill="url(#pbrCarbon)" stroke="#64748b" stroke-width="1"/>
        <path d="M146 126 L188 156 L182 164 L138 134 Z" fill="url(#pbrCarbon)" stroke="#64748b" stroke-width="1"/>

        <!-- 4 Rotores 3D con Vórtices -->
        <g>
          <ellipse cx="28" cy="48" rx="28" ry="8" fill="rgba(52,211,153,0.24)" stroke="#34d399" stroke-width="2" stroke-dasharray="18 8">
            <animateTransform attributeName="transform" type="rotate" from="0 28 48" to="360 28 48" dur="0.12s" repeatCount="indefinite"/>
          </ellipse>
          <rect x="21" y="46" width="14" height="14" rx="4" fill="url(#pbrShell)" stroke="#334155"/>
          <circle cx="28" cy="46" r="4" fill="#10b981"/>
        </g>
        <g>
          <ellipse cx="192" cy="48" rx="28" ry="8" fill="rgba(52,211,153,0.24)" stroke="#34d399" stroke-width="2" stroke-dasharray="18 8">
            <animateTransform attributeName="transform" type="rotate" from="360 192 48" to="0 192 48" dur="0.12s" repeatCount="indefinite"/>
          </ellipse>
          <rect x="185" y="46" width="14" height="14" rx="4" fill="url(#pbrShell)" stroke="#334155"/>
          <circle cx="192" cy="46" r="4" fill="#10b981"/>
        </g>
        <g>
          <ellipse cx="34" cy="158" rx="25" ry="7" fill="rgba(52,211,153,0.2)" stroke="#34d399" stroke-width="1.8" stroke-dasharray="14 6">
            <animateTransform attributeName="transform" type="rotate" from="0 34 158" to="360 34 158" dur="0.14s" repeatCount="indefinite"/>
          </ellipse>
          <rect x="28" y="155" width="12" height="12" rx="4" fill="url(#pbrShell)" stroke="#334155"/>
        </g>
        <g>
          <ellipse cx="186" cy="158" rx="25" ry="7" fill="rgba(52,211,153,0.2)" stroke="#34d399" stroke-width="1.8" stroke-dasharray="14 6">
            <animateTransform attributeName="transform" type="rotate" from="360 186 158" to="0 186 158" dur="0.14s" repeatCount="indefinite"/>
          </ellipse>
          <rect x="180" y="155" width="12" height="12" rx="4" fill="url(#pbrShell)" stroke="#334155"/>
        </g>

        <!-- Antenas Duales -->
        <path d="M98 54 L92 30 M122 54 L128 30" stroke="#cbd5e1" stroke-width="3.5" stroke-linecap="round"/>
        <circle id="roamingAntennaL" cx="92" cy="28" r="6" fill="#10b981" filter="url(#ledGlow3D)"/>
        <circle id="roamingAntennaR" cx="128" cy="28" r="6" fill="#10b981" filter="url(#ledGlow3D)"/>

        <!-- Cápsula Esférica 3D Principal -->
        <rect x="54" y="50" width="112" height="96" rx="46" fill="url(#pbrShell)" stroke="#f8fafc" stroke-width="1.5"/>
        <path d="M62 74 C62 46, 158 46, 158 74 C140 64, 80 64, 62 74 Z" fill="url(#pbrEmeraldArmor)"/>
        <rect x="46" y="84" width="10" height="30" rx="5" fill="url(#pbrEmeraldArmor)" stroke="#a7f3d0" stroke-width="1"/>
        <rect x="164" y="84" width="10" height="30" rx="5" fill="url(#pbrEmeraldArmor)" stroke="#a7f3d0" stroke-width="1"/>
        <ellipse cx="92" cy="64" rx="26" ry="7" transform="rotate(-12 92 64)" fill="rgba(255,255,255,0.65)"/>

        <!-- Visor Curvo 3D OLED -->
        <rect x="64" y="72" width="92" height="54" rx="25" fill="url(#pbrVisor)" stroke="#475569" stroke-width="2.5"/>
        <path d="M72 78 Q110 73 146 80" stroke="rgba(255,255,255,0.22)" stroke-width="2.5" stroke-linecap="round" fill="none"/>

        <!-- Cámara Gimbal 3D Inferior -->
        <circle cx="110" cy="154" r="13" fill="url(#pbrCarbon)" stroke="#94a3b8" stroke-width="2"/>
        <circle cx="110" cy="154" r="7" fill="#090d16"/>
        <circle id="roamingGimbalLens" cx="110" cy="154" r="4" fill="#10b981" filter="url(#ledGlow3D)"/>
        <circle cx="108" cy="152" r="1.5" fill="#ffffff"/>

        <!-- Expresiones Faciales LED -->
        <g id="roamingEyesOffset">
          <g class="visor-eyes-blink" filter="url(#ledGlow3D)">
            <g id="rface-happy">
              <path d="M76 100 Q88 85 100 100" stroke="#34d399" stroke-width="5.5" stroke-linecap="round" fill="none"/>
              <path d="M120 100 Q132 85 144 100" stroke="#34d399" stroke-width="5.5" stroke-linecap="round" fill="none"/>
              <path d="M98 112 Q110 121 122 112" stroke="#34d399" stroke-width="4" stroke-linecap="round" fill="none"/>
              <ellipse cx="73" cy="108" rx="4.5" ry="2.5" fill="rgba(52,211,153,0.5)"/>
              <ellipse cx="147" cy="108" rx="4.5" ry="2.5" fill="rgba(52,211,153,0.5)"/>
            </g>
            <g id="rface-shocked" style="display:none;">
              <circle cx="88" cy="98" r="12" stroke="#fbbf24" stroke-width="4.5" fill="rgba(251,191,36,0.2)"/>
              <circle cx="88" cy="98" r="4.5" fill="#ffffff"/>
              <circle cx="132" cy="98" r="12" stroke="#fbbf24" stroke-width="4.5" fill="rgba(251,191,36,0.2)"/>
              <circle cx="132" cy="98" r="4.5" fill="#ffffff"/>
              <ellipse cx="110" cy="115" rx="7" ry="8" stroke="#fbbf24" stroke-width="3.8" fill="rgba(251,191,36,0.15)"/>
            </g>
            <g id="rface-angry" style="display:none;">
              <line x1="74" y1="86" x2="100" y2="96" stroke="#ef4444" stroke-width="5.5" stroke-linecap="round"/>
              <line x1="146" y1="86" x2="120" y2="96" stroke="#ef4444" stroke-width="5.5" stroke-linecap="round"/>
              <path d="M76 98 A11 11 0 0 0 100 98 Z" fill="#ef4444"/>
              <path d="M120 98 A11 11 0 0 0 144 98 Z" fill="#ef4444"/>
              <path d="M97 116 Q110 108 123 116" stroke="#ef4444" stroke-width="4" stroke-linecap="round" fill="none"/>
            </g>
            <g id="rface-scanning" style="display:none;">
              <rect x="74" y="92" width="24" height="12" rx="4" fill="#38bdf8"/>
              <circle cx="132" cy="98" r="13" stroke="#38bdf8" stroke-width="3.2" stroke-dasharray="8 4" fill="none">
                <animateTransform attributeName="transform" type="rotate" from="0 132 98" to="360 132 98" dur="3s" repeatCount="indefinite"/>
              </circle>
              <circle cx="132" cy="98" r="5" fill="#38bdf8"/>
              <line x1="94" y1="115" x2="126" y2="115" stroke="#38bdf8" stroke-width="3.8" stroke-linecap="round"/>
            </g>
            <g id="rface-turbo" style="display:none;">
              <path d="M75 88 L97 98 L75 108" stroke="#c084fc" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
              <path d="M145 88 L123 98 L145 108" stroke="#c084fc" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
              <path d="M94 114 L110 120 L126 114" stroke="#34d399" stroke-width="4" stroke-linecap="round" fill="none"/>
            </g>
          </g>
        </g>
      </svg>
    </div>
  </div>
"""

html = html.replace('<div id="ambientBg"></div>', roaming_drone_html + '\n  <div id="ambientBg"></div>')

# ---------------------------------------------------------------------------
# 4. MOTOR JAVASCRIPT: SINCRONIZAR DATOS 3D POP-OUT EN CADA ESCENA + VUELO LIBRE
# ---------------------------------------------------------------------------
diorama_and_roaming_js = """
    /**
     * Datos visuales 3D Pop-Out del Diorama para cada una de las 15 escenas
     * (Para que el espectador se impresione y entienda el tema de un solo vistazo)
     * Autor: César Quiroz
     */
    const sceneDioramaData = [
      { icon: '🚁', val: 'LA LIBERTAD', lbl: 'Drones IA · TIF Nivel I', secImg: './assets/image18.png', secLbl: '🌡️ Visión Térmica + RGB', cap: '🚁 Sistema de Drones Inteligentes · UCV 2026' },
      { icon: '🌍', val: 'ODS 13 Y 15', lbl: 'Acción por el Clima y Bosques', secImg: './assets/image12.png', secLbl: '🔥 Detección en Segundos', cap: '🌿 De Vigilancia Lenta a Visión Artificial IA' },
      { icon: '🌲', val: '10,9 M ha/año', lbl: 'Deforestación Mundial (FAO)', secImg: './assets/image12.png', secLbl: '🔥 42 % Pérdida por Fuego', cap: '🌍 Crisis Global: >11 Canchas de Fútbol / min' },
      { icon: '🇵🇪', val: '1 754', lbl: 'Incendios en Perú (INDECI)', secImg: './assets/image9.png', secLbl: '⚠️ 95 % Causa Humana', cap: '🚨 Perú Top 10 Global · Pico 840 en Septiembre' },
      { icon: '⛰️', val: '2 990 ha', lbl: 'Perdidas en La Libertad (COER)', secImg: './assets/image19.png', secLbl: '💧 Cabeceras de Cuenca', cap: '🔥 Santiago de Chuco (+1 000 ha) y +42 Incendios' },
      { icon: '🎯', val: '3 OBJETIVOS', lbl: 'Exactitud · Latencia · GeoJSON', secImg: './assets/image13.png', secLbl: '📡 Red Web / Móvil', cap: '🎯 Optimización de Tiempos de Detección 2026' },
      { icon: '🧠', val: 'YOLO + U-Net', lbl: 'Fusión Incendios + Tala', secImg: './assets/image9.png', secLbl: '🌲 Segmentación Semántica', cap: '🔍 Brecha Teórica: Unir Fuego y Desmonte en los Andes' },
      { icon: '🔬', val: '96 % – 98 %', lbl: 'Hitos Científicos 2023–2024', secImg: './assets/image10.png', secLbl: '💨 YOLOv8 + BiFormer', cap: '📚 Revisión Scopus Q1: Sensors, Frontiers y PLOS ONE' },
      { icon: '🚀', val: '2025 – 2026', lbl: 'Modelos Ultraligeros Edge AI', secImg: './assets/image17.png', secLbl: '🗺️ 10 400+ Árboles Auditados', cap: '⚡ Evolución hacia YOLO-UFS, AETDA y AHE-YOLO11' },
      { icon: '🎯', val: '98,39 %', lbl: 'Exactitud Máxima (OE1)', secImg: './assets/image3.png', secLbl: '🌤️ Cero Falsos Positivos', cap: '📊 Resultados OE1: Filtrado de Neblina y Brillo Solar' },
      { icon: '⚡', val: '3,5 MB', lbl: '333,3 FPS Lab / 30 FPS Dron', secImg: './assets/image13.png', secLbl: '📡 Alerta GSM en Segundos', cap: '⚡ Resultados OE2: -74 % Peso en Placa Jetson Nano' },
      { icon: '🗺️', val: '< 10 cm/px', lbl: '50x Más Nítido que el Satélite', secImg: './assets/image14.png', secLbl: '📐 Polígonos GeoJSON', cap: '🗺️ Resultados OE3: Mapas de Calor Multitemporales' },
      { icon: '📑', val: '7 ESTUDIOS', lbl: 'Síntesis Comparativa Scopus', secImg: './assets/image16.png', secLbl: '💻 Hardware + Software IA', cap: '📋 Tabla 1 Oficial según los 3 Objetivos Específicos' },
      { icon: '🌡️', val: 'LoRaWAN + IR', lbl: 'Propuesta para los Andes', secImg: './assets/image19.png', secLbl: '⛰️ Quebradas sin Señal GSM', cap: '⚖️ Cámara Térmica en Ichu + Radio de Largo Alcance' },
      { icon: '🛡️', val: 'SEGUNDOS', lbl: 'Que Salvan Bosques Andinos', secImg: './assets/image1.png', secLbl: '🎓 Ingeniería de Sistemas UCV', cap: '🏆 Conclusión General · La Libertad 2026' }
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

    // Motor de Vuelo Autónomo 3D del Robot Dron Global (Por encima de todas las diapositivas)
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
      y: window.innerHeight * 0.14,
      vx: 0,
      vy: 0,
      targetX: window.innerWidth * 0.78,
      targetY: window.innerHeight * 0.14,
      roll: 0,
      pitch: 0,
      flipAngle: 0,
      isDragging: false,
      roamPhase: 0,
      currentColor: '#10b981'
    };

    const sceneWaypoints = [
      { rx: 0.80, ry: 0.18 },
      { rx: 0.84, ry: 0.14 },
      { rx: 0.75, ry: 0.16 },
      { rx: 0.15, ry: 0.16 },
      { rx: 0.78, ry: 0.16 },
      { rx: 0.84, ry: 0.15 },
      { rx: 0.14, ry: 0.18 },
      { rx: 0.84, ry: 0.14 },
      { rx: 0.14, ry: 0.14 },
      { rx: 0.78, ry: 0.16 },
      { rx: 0.84, ry: 0.14 },
      { rx: 0.14, ry: 0.16 },
      { rx: 0.85, ry: 0.14 },
      { rx: 0.18, ry: 0.16 },
      { rx: 0.80, ry: 0.18 }
    ];

    // Patrullaje autónomo continuo ("vaga de allá para acá")
    setInterval(() => {
      if (droneState.isDragging) return;
      const wp = sceneWaypoints[currentScene] || { rx: 0.78, ry: 0.16 };
      const wanderX = (Math.random() - 0.5) * 320;
      const wanderY = (Math.random() - 0.5) * 140;
      droneState.targetX = Math.max(30, Math.min(window.innerWidth - 240, window.innerWidth * wp.rx + wanderX));
      droneState.targetY = Math.max(40, Math.min(window.innerHeight - 240, window.innerHeight * wp.ry + wanderY));
    }, 3400);

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
        droneState.targetX = e.clientX - 105;
        droneState.targetY = e.clientY - 105;
      }
      if (eyesOffsetEl) {
        const dx = Math.max(-8, Math.min(8, (mouseX - (droneState.x + 105)) * 0.018));
        const dy = Math.max(-5, Math.min(5, (mouseY - (droneState.y + 105)) * 0.018));
        eyesOffsetEl.setAttribute('transform', `translate(${dx}, ${dy})`);
      }
      // Inclinación 3D interactiva del Diorama Holográfico al mover el mouse
      const stage3D = document.getElementById('dioramaStage3D');
      if (stage3D) {
        const rx = ((e.clientY / window.innerHeight) - 0.5) * -14;
        const ry = ((e.clientX / window.innerWidth) - 0.5) * 16;
        stage3D.style.transform = `rotateX(${rx}deg) rotateY(${ry}deg)`;
      }
    });

    let trailParticles = [];

    function updateRoamingDronePhysics() {
      droneState.roamPhase += 0.038;
      const hoverX = Math.sin(droneState.roamPhase) * 28;
      const hoverY = Math.cos(droneState.roamPhase * 1.6) * 15;

      const ax = ((droneState.targetX + hoverX) - droneState.x) * 0.045;
      const ay = ((droneState.targetY + hoverY) - droneState.y) * 0.045;

      droneState.vx = (droneState.vx + ax) * 0.82;
      droneState.vy = (droneState.vy + ay) * 0.82;

      droneState.x += droneState.vx;
      droneState.y += droneState.vy;

      const targetRoll = Math.max(-28, Math.min(28, droneState.vx * 2.4));
      const lookYaw = Math.max(-18, Math.min(18, (mouseX - (droneState.x + 105)) * 0.025));
      const lookPitch = Math.max(-14, Math.min(14, (mouseY - (droneState.y + 105)) * -0.02));

      droneState.roll += (targetRoll - droneState.roll) * 0.15;
      droneState.pitch += (lookPitch - droneState.pitch) * 0.15;

      if (droneState.flipAngle > 0) {
        droneState.flipAngle = Math.max(0, droneState.flipAngle - 15);
      }

      droneEl.style.transform = `translate3d(${droneState.x}px, ${droneState.y}px, 80px) rotateZ(${droneState.roll + droneState.flipAngle}deg) rotateY(${lookYaw}deg) rotateX(${droneState.pitch}deg)`;

      if (Math.random() < 0.65) {
        trailParticles.push({
          x: droneState.x + 105 + (Math.random() - 0.5) * 16,
          y: droneState.y + 165,
          r: Math.random() * 4.5 + 2,
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

      const wp = sceneWaypoints[currentScene] || { rx: 0.78, ry: 0.16 };
      droneState.targetX = window.innerWidth * wp.rx - 105;
      droneState.targetY = window.innerHeight * wp.ry - 30;
    }

    function triggerDroneAcrobatics() {
      droneState.flipAngle = 360;
      manualIdx = (manualIdx + 1) % manualMoods.length;
      setDroneEmotion(manualMoods[manualIdx]);
      droneState.targetX = Math.random() * (window.innerWidth - 300) + 40;
      droneState.targetY = Math.random() * (window.innerHeight * 0.45) + 40;
    }

    updateRoamingDronePhysics();
"""

html = html.replace("goToScene(0);", diorama_and_roaming_js + "\n    goToScene(0);")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

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

print("SUCCESS! 3D Pop-Out Diorama + Roaming Global 3D Robot Drone active! Portable bytes:", os.path.getsize(portable_path))
