import os

def generate_header_banner(output_svg="header-banner.svg"):
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 190" width="860" height="190">
  <defs>
    <!-- Background Linear Gradient -->
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d1117" />
      <stop offset="50%" stop-color="#161b22" />
      <stop offset="100%" stop-color="#091b34" />
    </linearGradient>

    <!-- Accent Gradient for Text and Borders -->
    <linearGradient id="cyan-blue" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#58a6ff" />
      <stop offset="50%" stop-color="#79c0ff" />
      <stop offset="100%" stop-color="#39c5cf" />
    </linearGradient>

    <linearGradient id="wave-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1f6feb" stop-opacity="0.25" />
      <stop offset="50%" stop-color="#39c5cf" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#1f6feb" stop-opacity="0.1" />
    </linearGradient>

    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <style>
      @keyframes floatSlow {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-4px); }
      }
      @keyframes pulseGlow {
        0%, 100% { opacity: 0.6; }
        50% { opacity: 1; }
      }
      .title-text {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        font-size: 38px;
        font-weight: 800;
        letter-spacing: -0.5px;
        fill: #ffffff;
      }
      .subtitle-text {
        font-family: "Courier New", Courier, monospace;
        font-size: 15px;
        font-weight: 600;
        fill: #79c0ff;
        letter-spacing: 1px;
      }
      .tag-text {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 12px;
        font-weight: 500;
        fill: #c9d1d9;
      }
      .glow-wave {
        animation: pulseGlow 4s ease-in-out infinite;
      }
      .hero-content {
        animation: floatSlow 5s ease-in-out infinite;
      }
    </style>
  </defs>

  <!-- Background Base with Rounded Corners -->
  <rect width="860" height="190" rx="12" fill="url(#bg-grad)" stroke="#30363d" stroke-width="1.5"/>

  <!-- Tech Grid Background Accents -->
  <g opacity="0.12">
    <line x1="0" y1="38" x2="860" y2="38" stroke="#58a6ff" stroke-width="1" stroke-dasharray="4,6" />
    <line x1="0" y1="76" x2="860" y2="76" stroke="#58a6ff" stroke-width="1" stroke-dasharray="4,6" />
    <line x1="0" y1="114" x2="860" y2="114" stroke="#58a6ff" stroke-width="1" stroke-dasharray="4,6" />
    <line x1="0" y1="152" x2="860" y2="152" stroke="#58a6ff" stroke-width="1" stroke-dasharray="4,6" />
    <line x1="120" y1="0" x2="120" y2="190" stroke="#58a6ff" stroke-width="1" stroke-dasharray="4,6" />
    <line x1="340" y1="0" x2="340" y2="190" stroke="#58a6ff" stroke-width="1" stroke-dasharray="4,6" />
    <line x1="560" y1="0" x2="560" y2="190" stroke="#58a6ff" stroke-width="1" stroke-dasharray="4,6" />
    <line x1="740" y1="0" x2="740" y2="190" stroke="#58a6ff" stroke-width="1" stroke-dasharray="4,6" />
  </g>

  <!-- Decorative Wave / Fluid Shape at Bottom -->
  <path class="glow-wave" d="M0,140 Q 215,110 430,145 T 860,135 L 860,190 L 0,190 Z" fill="url(#wave-grad)" />

  <!-- Top Accent Bar -->
  <rect x="25" y="0" width="810" height="3" fill="url(#cyan-blue)" rx="1.5" />

  <!-- Main Hero Content -->
  <g class="hero-content">
    <!-- Status Pill -->
    <g transform="translate(30, 26)">
      <rect width="195" height="24" rx="12" fill="#161b22" stroke="#238636" stroke-width="1.2" />
      <circle cx="14" cy="12" r="4.5" fill="#2ea043" />
      <circle cx="14" cy="12" r="7" fill="#2ea043" opacity="0.35" />
      <text x="26" y="16" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" fill="#7ee787">OPEN TO OPPORTUNITIES</text>
    </g>

    <!-- University Badge -->
    <g transform="translate(235, 26)">
      <rect width="145" height="24" rx="12" fill="#161b22" stroke="#1f6feb" stroke-width="1.2" />
      <text x="12" y="16" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" fill="#58a6ff">🎓 UADER ALUMNI</text>
    </g>

    <!-- Main Title -->
    <text x="30" y="94" class="title-text">Tobias Carballo</text>

    <!-- Subtitle -->
    <text x="30" y="126" class="subtitle-text">&gt; Systems Analyst &amp; Full Stack Software Developer_</text>

    <!-- Tech Pills -->
    <g transform="translate(30, 146)">
      <text x="0" y="12" class="tag-text">⚙️ Event-Driven (Kafka) · ☕ Java Spring · 🌐 Node.js &amp; React · 🗄️ Redis &amp; PostgreSQL · 📱 React Native</text>
    </g>
  </g>

  <!-- Right Decorative Icon/Geometric Symbol -->
  <g transform="translate(740, 45)" opacity="0.85">
    <circle cx="45" cy="45" r="40" fill="none" stroke="url(#cyan-blue)" stroke-width="2" stroke-dasharray="6,4" />
    <circle cx="45" cy="45" r="28" fill="#161b22" stroke="#30363d" stroke-width="1" />
    <path d="M 35 45 L 43 53 L 57 37" fill="none" stroke="#58a6ff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />
  </g>
</svg>'''

    with open(output_svg, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Header Banner generado con éxito: {output_svg}")

if __name__ == "__main__":
    generate_header_banner()
