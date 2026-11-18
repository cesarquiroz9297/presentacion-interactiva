# -*- coding: utf-8 -*-
"""
Actualización 3D Ultra-Quality + Dron Mascota 3D Expresivo (Se alegra, se sorprende, se enoja, escanea y entra en modo turbo)
+ Transiciones 3D con perspectiva real + Tarjetas de fotos 3D adicionales e iconos expresivos.
Autor: César Quiroz
"""
import base64
import os
import re

base_dir = r"c:\Users\ASUS\Documents\lector_pdf_android_pc\presentacion_interactiva"
html_path = os.path.join(base_dir, "index.html")
portable_path = r"c:\Users\ASUS\Documents\lector_pdf_android_pc\presentacion_drones_ucv_2026_portable.html"

with open(os.path.join(base_dir, "build_trazomedico_style.py"), "r", encoding="utf-8") as f:
    builder_code = f.read()

# Extraer el html_content base del generador anterior
start_marker = 'html_content = """'
end_marker = '"""\n\nwith open(html_path'
html = builder_code.split(start_marker)[1].split(end_marker)[0]

# ---------------------------------------------------------------------------
# 1. MEJORAR EL CSS CON PERSPECTIVA 3D REAL EN CAMBIOS DE ESCENA + DRON EXPRESIVO 3D
# ---------------------------------------------------------------------------
old_scene_css = """    .scene {
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
    }"""

new_scene_css = """    #sceneStage {
      perspective: 1600px;
      transform-style: preserve-3d;
    }

    .scene {
      position: absolute;
      inset: 0;
      padding: 4.2rem 5rem;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      pointer-events: none;
      transform: translate3d(90px, 25px, -260px) rotateY(-14deg) rotateX(6deg) scale(0.92);
      transition:
        opacity 0.9s var(--morph-ease),
        transform 1.05s var(--morph-ease),
        filter 0.85s var(--morph-ease);
      filter: blur(8px);
      z-index: 10;
      transform-style: preserve-3d;
    }

    .scene.active {
      opacity: 1;
      pointer-events: auto;
      transform: translate3d(0, 0, 0) rotateY(0deg) rotateX(0deg) scale(1);
      filter: blur(0px);
    }

    .scene.prev {
      opacity: 0;
      transform: translate3d(-110px, -20px, -280px) rotateY(14deg) rotateX(-5deg) scale(0.92);
      filter: blur(8px);
    }

    /* Efecto 3D en tarjetas e imágenes flotantes */
    .card-3d-photo {
      border-radius: 1.2rem;
      overflow: hidden;
      border: 2px solid rgba(255, 255, 255, 0.22);
      box-shadow: 0 22px 45px rgba(0, 0, 0, 0.65), 0 0 25px rgba(16, 185, 129, 0.22);
      transition: transform 0.45s var(--morph-ease), box-shadow 0.45s ease;
      background: #04120b;
    }
    .card-3d-photo:hover {
      transform: translateY(-6px) scale(1.04) rotateY(-4deg);
      box-shadow: 0 28px 60px rgba(0, 0, 0, 0.8), 0 0 35px rgba(52, 211, 153, 0.4);
    }

    /* ==========================================================================
       DRON MASCOTA 3D EXPRESIVO SIEMPRE PRESENTE (CON EMOCIONES EN TIEMPO REAL)
       ========================================================================== */
    #droneMascotContainer {
      position: absolute;
      top: -38px;
      right: -24px;
      width: 175px;
      height: 175px;
      z-index: 30;
      pointer-events: auto;
      cursor: pointer;
      transition: transform 0.65s cubic-bezier(0.34, 1.56, 0.64, 1), filter 0.5s ease;
      filter: drop-shadow(0 18px 28px rgba(0, 0, 0, 0.75));
    }

    #droneMascotContainer:hover {
      transform: scale(1.14) rotate(-4deg);
    }

    #droneMascotContainer.barrel-roll {
      animation: droneFlip360 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
    }

    @keyframes droneFlip360 {
      0%   { transform: rotate(0deg) scale(1); }
      50%  { transform: rotate(180deg) scale(1.25); }
      100% { transform: rotate(360deg) scale(1); }
    }

    /* Burbuja de reacción emocional del Dron */
    #droneEmotionBubble {
      position: absolute;
      top: -34px;
      left: 50%;
      transform: translateX(-50%);
      white-space: nowrap;
      padding: 4px 12px;
      border-radius: 9999px;
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.03em;
      background: rgba(6, 20, 14, 0.92);
      border: 1.5px solid #34d399;
      color: #a7f3d0;
      box-shadow: 0 8px 22px rgba(0, 0, 0, 0.55);
      transition: all 0.4s var(--morph-ease);
    }

    /* Temas de color del Dron según su emoción */
    body[data-drone-mood="happy"] #droneEmotionBubble {
      border-color: #34d399;
      color: #6ee7b7;
      box-shadow: 0 0 20px rgba(16, 185, 129, 0.45);
    }
    body[data-drone-mood="shocked"] #droneEmotionBubble {
      border-color: #fbbf24;
      color: #fde68a;
      box-shadow: 0 0 24px rgba(245, 158, 11, 0.55);
    }
    body[data-drone-mood="angry"] #droneEmotionBubble {
      border-color: #ef4444;
      color: #fca5a5;
      box-shadow: 0 0 25px rgba(239, 68, 68, 0.6);
    }
    body[data-drone-mood="scanning"] #droneEmotionBubble {
      border-color: #38bdf8;
      color: #bae6fd;
      box-shadow: 0 0 22px rgba(56, 189, 248, 0.5);
    }
    body[data-drone-mood="turbo"] #droneEmotionBubble {
      border-color: #a855f7;
      color: #e9d5ff;
      box-shadow: 0 0 25px rgba(168, 85, 247, 0.55);
    }

    @keyframes eyeShake {
      0%, 100% { transform: translate(0, 0); }
      25% { transform: translate(-1.5px, 1px); }
      75% { transform: translate(1.5px, -1px); }
    }
    body[data-drone-mood="shocked"] #droneFaceGroup,
    body[data-drone-mood="angry"] #droneFaceGroup {
      animation: eyeShake 0.35s infinite;
    }"""

html = html.replace(old_scene_css, new_scene_css)

# ---------------------------------------------------------------------------
# 2. REEMPLAZAR EL DRON SVG SIMPLE POR EL DRON MASCOTA 3D EXPRESIVO CON CARA LED
# ---------------------------------------------------------------------------
old_drone_svg = """      <!-- Dron 3D SVG con hélices giratorias flotando sobre la esfera -->
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
      </svg>"""

new_drone_mascot_svg = """      <!-- DRON MASCOTA 3D EXPRESIVO (Cambia de emoción: Alegre, Sorprendido, Enojado, Escaneando, Turbo) -->
      <div id="droneMascotContainer" onclick="cycleDroneMoodManual()" title="¡Haz clic en mí! Soy el Dron IA de la UCV">
        <div id="droneEmotionBubble">😊 ¡Listos para exponer!</div>
        <svg class="w-full h-full" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <radialGradient id="body3D" cx="35%" cy="30%" r="70%">
              <stop offset="0%" stop-color="#f8fafc"/>
              <stop offset="55%" stop-color="#cbd5e1"/>
              <stop offset="100%" stop-color="#475569"/>
            </radialGradient>
            <linearGradient id="visorGlass" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="#0f172a"/>
              <stop offset="100%" stop-color="#020617"/>
            </linearGradient>
            <filter id="neonGlow" x="-30%" y="-30%" width="160%" height="160%">
              <feGaussianBlur stdDeviation="2.8" result="blur"/>
              <feMerge>
                <feMergeNode in="blur"/>
                <feMergeNode in="SourceGraphic"/>
              </feMerge>
            </filter>
          </defs>

          <!-- Sombra inferior 3D -->
          <ellipse cx="80" cy="146" rx="38" ry="7" fill="rgba(0,0,0,0.45)"/>

          <!-- Brazos 3D del cuadricóptero -->
          <path d="M48 64 L22 42 M112 64 L138 42 M48 96 L26 118 M112 96 L134 118" stroke="url(#body3D)" stroke-width="7" stroke-linecap="round"/>

          <!-- Motores y Hélices 3D Giratorias -->
          <g>
            <ellipse cx="22" cy="40" rx="20" ry="6" fill="rgba(52,211,153,0.35)" stroke="#34d399" stroke-width="1.8">
              <animateTransform attributeName="transform" type="rotate" from="0 22 40" to="360 22 40" dur="0.16s" repeatCount="indefinite"/>
            </ellipse>
            <circle cx="22" cy="42" r="5" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
          </g>
          <g>
            <ellipse cx="138" cy="40" rx="20" ry="6" fill="rgba(52,211,153,0.35)" stroke="#34d399" stroke-width="1.8">
              <animateTransform attributeName="transform" type="rotate" from="360 138 40" to="0 138 40" dur="0.16s" repeatCount="indefinite"/>
            </ellipse>
            <circle cx="138" cy="42" r="5" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
          </g>
          <g>
            <ellipse cx="26" cy="118" rx="18" ry="5.5" fill="rgba(52,211,153,0.3)" stroke="#34d399" stroke-width="1.6">
              <animateTransform attributeName="transform" type="rotate" from="0 26 118" to="360 26 118" dur="0.18s" repeatCount="indefinite"/>
            </ellipse>
            <circle cx="26" cy="118" r="4.5" fill="#334155"/>
          </g>
          <g>
            <ellipse cx="134" cy="118" rx="18" ry="5.5" fill="rgba(52,211,153,0.3)" stroke="#34d399" stroke-width="1.6">
              <animateTransform attributeName="transform" type="rotate" from="360 134 118" to="0 134 118" dur="0.18s" repeatCount="indefinite"/>
            </ellipse>
            <circle cx="134" cy="118" r="4.5" fill="#334155"/>
          </g>

          <!-- Antena superior con luz de estado emocional -->
          <line x1="80" y1="42" x2="80" y2="26" stroke="#cbd5e1" stroke-width="3.5" stroke-linecap="round"/>
          <circle id="droneAntennaLight" cx="80" cy="23" r="5.5" fill="#10b981" filter="url(#neonGlow)"/>

          <!-- Cápsula / Cabeza 3D del Dron (Estilo Astro Bot / EVE) -->
          <rect x="40" y="42" width="80" height="68" rx="32" fill="url(#body3D)" stroke="#e2e8f0" stroke-width="2"/>
          <!-- Brillo especular superior en el casco 3D -->
          <path d="M56 48 Q80 43 104 48" stroke="rgba(255,255,255,0.85)" stroke-width="3" stroke-linecap="round" fill="none"/>

          <!-- Pantalla Visor LED Negra donde se dibujan las expresiones faciales -->
          <rect x="48" y="54" width="64" height="42" rx="18" fill="url(#visorGlass)" stroke="#334155" stroke-width="2"/>

          <!-- Cámara térmica inferior gimball -->
          <circle cx="80" cy="116" r="8" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
          <circle id="droneGimbalLens" cx="80" cy="116" r="3.5" fill="#10b981"/>

          <!-- GRUPO DE EXPRESIONES FACIALES LED -->
          <g id="droneFaceGroup" filter="url(#neonGlow)">
            <!-- 1. CARA ALEGRE / ORGULLOSO (happy) -->
            <g id="face-happy">
              <path d="M58 74 Q65 63 72 74" stroke="#34d399" stroke-width="4.2" stroke-linecap="round" fill="none"/>
              <path d="M88 74 Q95 63 102 74" stroke="#34d399" stroke-width="4.2" stroke-linecap="round" fill="none"/>
              <path d="M72 84 Q80 91 88 84" stroke="#34d399" stroke-width="3.2" stroke-linecap="round" fill="none"/>
              <circle cx="55" cy="81" r="3" fill="rgba(52,211,153,0.45)"/>
              <circle cx="105" cy="81" r="3" fill="rgba(52,211,153,0.45)"/>
            </g>

            <!-- 2. CARA SORPRENDIDO / IMPACTADO POR LAS CIFRAS (shocked) -->
            <g id="face-shocked" style="display:none;">
              <circle cx="65" cy="72" r="8.5" stroke="#fbbf24" stroke-width="3.5" fill="rgba(251,191,36,0.15)"/>
              <circle cx="65" cy="72" r="3" fill="#fff"/>
              <circle cx="95" cy="72" r="8.5" stroke="#fbbf24" stroke-width="3.5" fill="rgba(251,191,36,0.15)"/>
              <circle cx="95" cy="72" r="3" fill="#fff"/>
              <ellipse cx="80" cy="86" rx="5.5" ry="6.5" stroke="#fbbf24" stroke-width="3" fill="none"/>
            </g>

            <!-- 3. CARA ENOJADO / ALERTA POR INCENDIOS Y TALA HUMANA (angry) -->
            <g id="face-angry" style="display:none;">
              <line x1="56" y1="64" x2="73" y2="71" stroke="#ef4444" stroke-width="4.2" stroke-linecap="round"/>
              <line x1="104" y1="64" x2="87" y2="71" stroke="#ef4444" stroke-width="4.2" stroke-linecap="round"/>
              <path d="M58 73 A7 7 0 0 0 72 73 Z" fill="#ef4444"/>
              <path d="M88 73 A7 7 0 0 0 102 73 Z" fill="#ef4444"/>
              <path d="M72 87 Q80 81 88 87" stroke="#ef4444" stroke-width="3.2" stroke-linecap="round" fill="none"/>
            </g>

            <!-- 4. CARA ESCANEANDO / ANALÍTICO CIENTÍFICO (scanning) -->
            <g id="face-scanning" style="display:none;">
              <rect x="56" y="68" width="16" height="9" rx="3" fill="#38bdf8"/>
              <circle cx="95" cy="72" r="9" stroke="#38bdf8" stroke-width="2.8" stroke-dasharray="6 3" fill="none"/>
              <circle cx="95" cy="72" r="3.5" fill="#38bdf8"/>
              <line x1="68" y1="86" x2="92" y2="86" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
            </g>

            <!-- 5. CARA MODO TURBO 333 FPS (turbo) -->
            <g id="face-turbo" style="display:none;">
              <path d="M57 66 L71 73 L57 80" stroke="#c084fc" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
              <path d="M103 66 L89 73 L103 80" stroke="#c084fc" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
              <path d="M70 86 L80 82 L90 86" stroke="#34d399" stroke-width="3.2" stroke-linecap="round" fill="none"/>
            </g>
          </g>
        </svg>
      </div>"""

html = html.replace(old_drone_svg, new_drone_mascot_svg)

# ---------------------------------------------------------------------------
# 3. AGREGAR MÁS IMÁGENES 3D Y EMOTICONES EN LAS ESCENAS QUE TENÍAN POCAS FOTOS
# ---------------------------------------------------------------------------

# En Escena 03 (Estadística Mundial FAO / WRI): añadir 2 tarjetas fotográficas 3D debajo de las barras
extra_imgs_scene3 = """
          <!-- Mini-Galería 3D de Respaldo Visual (Deforestación y Fuego Global) -->
          <div class="stagger d-5 grid grid-cols-2 gap-4 pt-2">
            <div class="card-3d-photo h-28 relative">
              <img src="./assets/image9.png" alt="Deforestación FAO" class="w-full h-full object-cover" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent flex items-end p-2.5">
                <span class="text-xs font-bold text-emerald-300">🌲 4 140 M ha de Bosques (FAO)</span>
              </div>
            </div>
            <div class="card-3d-photo h-28 relative">
              <img src="./assets/image12.png" alt="Fuego WRI" class="w-full h-full object-cover" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent flex items-end p-2.5">
                <span class="text-xs font-bold text-orange-300">🔥 &gt;11 Canchas de Fútbol / min (WRI)</span>
              </div>
            </div>
          </div>"""

html = html.replace(
    '<span class="font-mono-code font-bold text-xl text-orange-400">42 % del total</span>\n            </div>\n          </div>',
    '<span class="font-mono-code font-bold text-xl text-orange-400">42 % del total</span>\n            </div>\n          </div>' + extra_imgs_scene3
)

# En Escena 04 (Perú INDECI / SERFOR): añadir 2 tarjetas fotográficas 3D con emoticones
extra_imgs_scene4 = """
          <!-- Fotos 3D de Emergencia Nacional y Causa Humana -->
          <div class="stagger d-4 grid grid-cols-2 gap-4 pt-1">
            <div class="card-3d-photo h-28 relative">
              <img src="./assets/image10.png" alt="INDECI Perú" class="w-full h-full object-cover" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent flex items-end p-2.5">
                <span class="text-xs font-bold text-rose-300">🚨 Pico Septiembre: 840 Incendios</span>
              </div>
            </div>
            <div class="card-3d-photo h-28 relative">
              <img src="./assets/image3.png" alt="SERFOR Perú" class="w-full h-full object-cover" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent flex items-end p-2.5">
                <span class="text-xs font-bold text-amber-300">⚠️ 95 % Origen Antrópico (SERFOR)</span>
              </div>
            </div>
          </div>"""

html = html.replace(
    'quema tradicional de rastrojos y pastos secos</strong> para abrir chacras, agravada por el viento y la sequía andina.\n            </div>\n          </div>',
    'quema tradicional de rastrojos y pastos secos</strong> para abrir chacras, agravada por el viento y la sequía andina.\n            </div>\n          </div>' + extra_imgs_scene4
)

# En Escena 05 (La Libertad COER): añadir 3 mini-tarjetas 3D con fotos de la sierra liberteña
extra_imgs_scene5 = """
          <!-- 3 Vistas 3D de Impacto en La Libertad -->
          <div class="stagger d-4 grid grid-cols-3 gap-3 pt-1">
            <div class="card-3d-photo h-24 relative">
              <img src="./assets/image10.png" alt="Santiago de Chuco" class="w-full h-full object-cover" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 to-transparent flex items-end p-2">
                <span class="text-[11px] font-bold text-orange-300">🔥 Santiago de Chuco (+1 000 ha)</span>
              </div>
            </div>
            <div class="card-3d-photo h-24 relative">
              <img src="./assets/image19.png" alt="Cabeceras de Cuenca" class="w-full h-full object-cover" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 to-transparent flex items-end p-2">
                <span class="text-[11px] font-bold text-emerald-300">💧 Cabeceras de Cuenca</span>
              </div>
            </div>
            <div class="card-3d-photo h-24 relative">
              <img src="./assets/image11.png" alt="Brigadas y Drones" class="w-full h-full object-cover" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 to-transparent flex items-end p-2">
                <span class="text-[11px] font-bold text-amber-300">🏘️ 41 Viviendas Afectadas</span>
              </div>
            </div>
          </div>"""

html = html.replace(
    'abastecen a los valles liberteños y erosiona el suelo agrícola.\n            </p>\n          </div>',
    'abastecen a los valles liberteños y erosiona el suelo agrícola.\n            </p>\n          </div>' + extra_imgs_scene5
)

# En Escena 14 (Discusión Crítica): añadir 2 vistas 3D (Cámara Térmica e Imagen de Dron en los Andes)
extra_imgs_scene14 = """
          <div class="stagger d-5 grid grid-cols-2 gap-4 pt-1">
            <div class="card-3d-photo h-24 relative">
              <img src="./assets/image18.png" alt="Cámara Térmica" class="w-full h-full object-cover" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 to-transparent flex items-end p-2">
                <span class="text-xs font-bold text-orange-300">🌡️ Visión Térmica Nocturna en Ichu</span>
              </div>
            </div>
            <div class="card-3d-photo h-24 relative">
              <img src="./assets/image13.png" alt="Estación Terrena LoRaWAN" class="w-full h-full object-cover" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 to-transparent flex items-end p-2">
                <span class="text-xs font-bold text-cyan-300">📡 Radio LoRaWAN en Quebradas</span>
              </div>
            </div>
          </div>"""

html = html.replace(
    'Bolívar y Pataz sin señal celular GSM.\n            </p>\n          </div>',
    'Bolívar y Pataz sin señal celular GSM.\n            </p>\n          </div>' + extra_imgs_scene14
)

# ---------------------------------------------------------------------------
# 4. LÓGICA JAVASCRIPT DE EMOCIONES DEL DRON POR ESCENA + INCLINACIÓN 3D CON EL MOUSE
# ---------------------------------------------------------------------------
drone_mood_js = """
    /**
     * Mapa de emociones del Dron Mascota 3D para cada una de las 15 escenas
     * Autor: César Quiroz
     */
    const sceneDroneMoods = [
      { mood: 'happy',    text: '😊 ¡Bienvenidos! Soy el Dron UCV', color: '#10b981' },
      { mood: 'angry',    text: '😠 ¡El humo y las nubes bloquean todo!', color: '#ef4444' },
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

    function setDroneEmotion(moodObj) {
      if (!moodObj) return;
      document.body.setAttribute('data-drone-mood', moodObj.mood);
      const bubble = document.getElementById('droneEmotionBubble');
      if (bubble) bubble.textContent = moodObj.text;

      ['happy', 'shocked', 'angry', 'scanning', 'turbo'].forEach(m => {
        const el = document.getElementById('face-' + m);
        if (el) el.style.display = (m === moodObj.mood) ? 'block' : 'none';
      });

      const ant = document.getElementById('droneAntennaLight');
      const gim = document.getElementById('droneGimbalLens');
      if (ant) ant.setAttribute('fill', moodObj.color);
      if (gim) gim.setAttribute('fill', moodObj.color);
    }

    // Permitir hacer clic en el dron para que haga una pirueta 360° y cambie de expresión
    const manualMoods = [
      { mood: 'happy',    text: '😄 ¡Vamos por ese 20 con el profesor!', color: '#10b981' },
      { mood: 'shocked',  text: '😲 ¡Vuelo bajo las nubes a <10 cm/px!', color: '#fbbf24' },
      { mood: 'angry',    text: '😤 ¡Cero tolerancia a los incendios!', color: '#ef4444' },
      { mood: 'turbo',    text: '🚀 ¡Alerta enviada en 2 segundos!', color: '#c084fc' },
      { mood: 'scanning', text: '🛰️ Escaneando cabeceras de cuenca...', color: '#38bdf8' }
    ];
    let manualIdx = 0;

    function cycleDroneMoodManual() {
      const box = document.getElementById('droneMascotContainer');
      if (box) {
        box.classList.remove('barrel-roll');
        void box.offsetWidth;
        box.classList.add('barrel-roll');
      }
      manualIdx = (manualIdx + 1) % manualMoods.length;
      setDroneEmotion(manualMoods[manualIdx]);
    }

    // Inclinación 3D interactiva del Objeto 3D y del Dron cuando mueves el mouse
    window.addEventListener('mousemove', (e) => {
      const rx = ((e.clientY / window.innerHeight) - 0.5) * -14;
      const ry = ((e.clientX / window.innerWidth) - 0.5) * 14;
      const inner = document.querySelector('.hero-inner-float');
      if (inner) {
        inner.style.transform = `rotateX(${rx}deg) rotateY(${ry}deg)`;
      }
    });
"""

html = html.replace(
    "// 5. Animar barras de exactitud si la escena las tiene",
    "// 4.5 Actualizar la emoción del Dron Mascota 3D según la escena\n      if ( typeof sceneDroneMoods !== 'undefined' ) { setDroneEmotion(sceneDroneMoods[currentScene]); }\n\n      // 5. Animar barras de exactitud si la escena las tiene"
)

html = html.replace("goToScene(0);", drone_mood_js + "\n    goToScene(0);")

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

print("SUCCESS! 3D Perspective + Expressive Drone Mascot + Extra 3D Photos ready! Portable bytes:", os.path.getsize(portable_path))
