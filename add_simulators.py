# -*- coding: utf-8 -*-
"""
Script para agregar simuladores interactivos en vivo y alternar composiciones visuales
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

# 1. Alternar la columna visual a la IZQUIERDA (lg:order-first) en diapositivas pares (02, 04, 10)
for slide_num in ["1", "3", "9"]:
    pattern = rf'(<section class="slide-view" data-slide="{slide_num}".*?<div class="lg:col-span-5 morph-item delay-5)'
    html = re.sub(pattern, r"\1 lg:order-first", html, flags=re.DOTALL)

# 2. En Diapositiva 4 (Perú INDECI): agregar mini-gráfico de barras del pico de Septiembre (840 incendios) + segunda cámara
peru_extra = """
          <!-- Gráfico de Picos Mensuales INDECI + Segunda Cámara de Monitoreo -->
          <div class="grid grid-cols-2 gap-2.5 mt-3">
            <div class="glass-card rounded-xl p-2.5 border border-rose-400/40">
              <div class="text-[10px] font-mono-tech text-rose-300 font-bold mb-1">📈 PICO CRÍTICO SEPTIEMBRE (840)</div>
              <div class="flex items-end gap-1.5 h-12 pt-1">
                <div class="flex-1 bg-emerald-500/40 rounded-t h-3" title="Mayo"></div>
                <div class="flex-1 bg-emerald-500/60 rounded-t h-5" title="Junio"></div>
                <div class="flex-1 bg-amber-500/70 rounded-t h-7" title="Julio"></div>
                <div class="flex-1 bg-orange-500/80 rounded-t h-9" title="Agosto"></div>
                <div class="flex-1 bg-rose-500 rounded-t h-12 animate-pulse" title="Septiembre: 840 incendios"></div>
                <div class="flex-1 bg-orange-400/70 rounded-t h-6" title="Octubre"></div>
              </div>
              <div class="flex justify-between text-[9px] font-mono-tech text-slate-400 mt-1"><span>May</span><span>Jul</span><span class="text-rose-300 font-bold">Sep (840)</span><span>Oct</span></div>
            </div>
            <div class="pip-monitor h-24">
              <img src="./assets/image9.png" alt="Tala Amazonía" class="w-full h-full object-cover" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 to-transparent flex items-end p-2">
                <span class="text-[10px] font-mono-tech text-emerald-300 font-bold">🌲 Top 10 Global Tala</span>
              </div>
            </div>
          </div>
"""
html = html.replace(
    '<span class="font-mono-tech text-white">COEN · SINPAD</span>\n            </div>\n          </div>',
    '<span class="font-mono-tech text-white">COEN · SINPAD</span>\n            </div>\n          </div>' + peru_extra
)

# 3. En Diapositiva 10 (Resultados OE2): agregar comparador visual de velocidad Dron GSM (Segundos) vs Satélite (Horas)
oe2_race = """
          <!-- Simulador Visual en Vivo: Velocidad Dron Edge AI vs Satélite -->
          <div class="glass-card rounded-xl p-3 mt-3 border border-cyan-400/40 space-y-2">
            <div class="text-[10px] font-mono-tech text-cyan-300 font-bold uppercase flex justify-between">
              <span>⚡ SIMULADOR DE LATENCIA EN TIEMPO REAL</span>
              <span class="text-emerald-300">Jetson Nano 30 FPS vs Satélite</span>
            </div>
            <div class="space-y-1.5 text-[11px]">
              <div>
                <div class="flex justify-between text-emerald-300 font-mono-tech"><span>🚁 Dron + Jetson Nano + GSM/LoRa</span><span>~2–5 SEGUNDOS</span></div>
                <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden"><div class="h-full bg-gradient-to-r from-emerald-400 to-cyan-300 rounded-full animate-pulse" style="width: 96%;"></div></div>
              </div>
              <div>
                <div class="flex justify-between text-rose-300 font-mono-tech"><span>🛰️ Satélite / Rondas a pie</span><span>3 A 12 HORAS (Tardío)</span></div>
                <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden"><div class="h-full bg-rose-500/70 rounded-full" style="width: 14%;"></div></div>
              </div>
            </div>
          </div>
"""
html = html.replace(
    '<span class="font-mono-tech text-white">Segundos vs. Horas</span>\n            </div>\n          </div>',
    '<span class="font-mono-tech text-white">Segundos vs. Horas</span>\n            </div>\n          </div>' + oe2_race
)

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

print("Alternating layouts + interactive widgets synced! Portable size:", os.path.getsize(portable_path))
