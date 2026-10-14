"""Agrega la tarjeta de Nomad Pizza Automation al portafolio.

Uso (desde la carpeta de tu portafolio):
    python agregar_proyecto.py
o indicando la ruta:
    python agregar_proyecto.py ruta/a/index.html
Se puede ejecutar una sola vez; si la tarjeta ya existe, no hace nada.
Para deshacer: git checkout index.html
"""
import re
import sys
from pathlib import Path

path = Path(sys.argv[1] if len(sys.argv) > 1 else "index.html")
html = path.read_text(encoding="utf-8")

if 'data-gallery="nomadauto"' in html:
    print("La tarjeta ya existe. No se hizo ningún cambio.")
    sys.exit(0)

NEW_CARD = '''<article class="card card-split">
      <div class="card-text">
        <div class="card-top">
          <h3>Automation – Nomad Pizza Public Order Flow | 10/2026</h3>
          <span class="status">PASS</span>
        </div>
        <p class="desc">
          UI automation of the public ordering journey (menu, cart and order information) of the Nomad Pizza web app.
        </p>
        <p>
             <img src="https://img.shields.io/badge/Python-3776AB?logo=python&amp;logoColor=white" height="35" loading="lazy">
             <img src="https://img.shields.io/badge/Selenium-43B02A?logo=selenium&amp;logoColor=white" height="35" loading="lazy">
             <img src="https://img.shields.io/badge/Pytest-0A9EDC?logo=pytest&amp;logoColor=white" height="35" loading="lazy">
             <img src="https://img.shields.io/badge/Firebase-FFCA28?logo=firebase&amp;logoColor=black" height="35" loading="lazy">
        </p>
        <ul class="metrics">
          <li>Page Object Model with parametrized test data, covering the NO-001–NO-023 test case catalog.</li>
          <li>Validated menu, customizable pizza ingredient combinations and prices, cart totals, and order ticket details.</li>
          <li>Tests run against the Firebase Hosting Emulator, with a safeguard that blocks order creation on any other URL.</li>
          <li>Documented 3 findings in Jira (NP-1 to NP-3) with public defect reports.</li>
        </ul>
        <div class="card-links">
          <a href="https://github.com/JanRDLP/nomad-pizza-order-flow-automation" target="_blank">GitHub →</a>
        </div>
      </div>
      <div class="card-img">
        <div class="gallery">
          <div class="gallery-track">
            <img
              src="assets/img/npa_resultados.png"
              alt="Pytest results"
              data-gallery="nomadauto"
              data-description="Pytest run of the public order flow tests."
              >
            <img
              src="assets/img/npa_test_cart.png"
              alt="test_cart.py"
              data-gallery="nomadauto"
              data-description="Parametrized cart tests checking quantities, subtotals and totals."
              >
            <img
              src="assets/img/npa_page_object.png"
              alt="cart_page.py"
              data-gallery="nomadauto"
              data-description="Cart Page Object with reusable locators and actions."
              >
          </div>
          <button class="gallery-btn prev" onclick="slideGallery(this, -1)">❮</button>
          <button class="gallery-btn next" onclick="slideGallery(this, 1)">❯</button>
          <div class="gallery-dots">
            <span class="active"></span>
            <span></span>
            <span></span>
          </div>
        </div>
      </div>
    </article>

    '''

# 1) Alterna el lado de la imagen en las tarjetas existentes
def flip(m):
    return '<article class="card card-split">' if m.group(1) else '<article class="card card-split reverse">'

html, flipped = re.subn(r'<article class="card card-split( reverse)?">', flip, html)

# 2) Inserta la nueva tarjeta como primera de Projects
html, inserted = re.subn(r'(<h2>Projects</h2>\s*\n\s*)', lambda m: m.group(1) + NEW_CARD, html, count=1)
if inserted != 1:
    sys.exit("No encontré <h2>Projects</h2>. No se guardó ningún cambio.")

# 3) Arreglos pequeños
html, fix_white = re.subn(r'logoColor=whit"', 'logoColor=white"', html)
html, fix_close = re.subn(r'(loading="lazy")(\s*\n\s*</p>)', r'\1>\2', html)

path.write_text(html, encoding="utf-8")
print(f"Tarjeta agregada. Tarjetas alternadas: {flipped}. "
      f"Badges Jira corregidos: {fix_white}. Etiquetas img cerradas: {fix_close}.")
