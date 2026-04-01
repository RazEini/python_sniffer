<div dir="rtl">

  <h1 align="center">🕵️ NetGuard – Python Network Sniffer & DPI Engine</h1>

  <p align="center">
    מנוע לניתוח תעבורת רשת בזמן אמת עם יכולות <strong>Deep Packet Inspection (DPI)</strong>, 
    זיהוי אנומליות מבוסס היוריסטיקה (Heuristics) והתראות אבטחה מתקדמות.
    <br>
    מבוסס <strong>Python + Scapy</strong> בארכיטקטורת Multi-threaded.
  </p>

  <br>
  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python Badge">
    <img src="https://img.shields.io/badge/Library-Scapy-red" alt="Scapy Badge">
    <img src="https://img.shields.io/badge/Security-DPI-orange" alt="DPI Badge">
    <img src="https://img.shields.io/badge/Analysis-Multithreaded-lightgrey" alt="Arch Badge">
  </p>

  <br>

  <hr>

  <h2 align="center">🔎 Overview</h2>
  <p align="center" dir="rtl">
    <strong>NetGuard</strong> הוא כלי ניטור רשת (Sniffer) מתקדם שנועד לספק שקיפות מלאה לשכבות 3, 4 ו-7 במודל ה-OSI. 
    <br>
    בניגוד לסניפרים סטנדרטיים, הכלי משלב <strong>Heuristic Analysis</strong> לזיהוי דפוסי תקיפה (כמו DoS ו-Port Scanning) ומבצע פענוח של שכבת האפליקציה (Application Layer) בזמן אמת כדי לחשוף מידע רגיש בתעבורה לא מוצפנת.
</p>

  <br>

  <hr>

  <h2 align="center">🚀 Core Features</h2>

  <table align="center" dir="rtl">
    <thead>
      <tr>
        <th>Domain</th>
        <th>Feature</th>
        <th>Status</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>📡 <strong>Network</strong></td>
        <td>Real-time L2-L7 Sniffing</td>
        <td>✅</td>
        <td>לכידה וניתוח של תעבורת IP, TCP, UDP ו-DNS בזמן אמת.</td>
      </tr>
      <tr>
        <td>🛡️ <strong>Cyber Security</strong></td>
        <td>Anomaly Detection</td>
        <td>✅</td>
        <td>זיהוי אוטומטי של מתקפות <strong>DoS (SYN Flood)</strong> וסריקת פורטים.</td>
      </tr>
      <tr>
        <td>🔍 <strong>DPI</strong></td>
        <td>Deep Packet Inspection</td>
        <td>✅</td>
        <td>פענוח Payload לטקסט קריא (UTF-8) וזיהוי תעבורת HTTP חשופה.</td>
      </tr>
      <tr>
        <td>⚙️ <strong>Architecture</strong></td>
        <td>Producer-Consumer Model</td>
        <td>✅</td>
        <td>שימוש ב-<strong>Threading & Queue</strong> למניעת Packet Loss בעומסי תעבורה.</td>
      </tr>
      <tr>
        <td>🚦 <strong>IPS Logic</strong></td>
        <td>Automatic Host Isolation</td>
        <td>✅</td>
        <td>מנגנון לבידוד זמני של IP עוין לאחר זיהוי אנומליה.</td>
      </tr>
      <tr>
        <td>📝 <strong>Logging</strong></td>
        <td>Security Event Journal</td>
        <td>✅</td>
        <td>רישום אירועים קריטיים לקובץ לוג ייעודי לצורך Forensic Analysis.</td>
      </tr>
    </tbody>
  </table>

  <br>

  <hr>

  <div dir="rtl">
  <h2 align="center">🛠️ טכנולוגיות וארכיטקטורה</h2>
  <ul>
    <li><strong>Concurrency:</strong> שימוש ב-<code>threading</code> וב-<code>queue.Queue</code> להפרדה בין שלב הלכידה (Sniffing) לשלב הניתוח (Processing).</li>
    <li><strong>DPI Engine:</strong> ניתוח שכבת ה-Raw Packet לחילוץ מחרוזות טקסטואליות וזיהוי דפוסי תקיפה.</li>
    <li><strong>Security Heuristics:</strong> מנגנון מבוסס Thresholds לזיהוי הצפות (Flooding) וניסיונות גישה לא מורשים.</li>
    <li><strong>Environment:</strong> פיתוח בסביבה מבודדת (venv) לניהול תלויות נקי.</li>
  </ul>
</div>

  <hr>

  <h2>⚙️ התקנה והרצה (Quick Start)</h2>
  <div dir="ltr" align="left">
    <pre>
## Clone the repository
git clone https://github.com/Raz-Eini/python_sniffer.git
cd python_sniffer

## Setup Virtual Environment
python -m venv .venv
.\.venv\Scripts\activate  # On Windows

## Install Dependencies
pip install scapy

## Run as Administrator (Required for Raw Sockets)
python main.py
    </pre>
  </div>

  <hr>

  <h2>📄 רישיון</h2>
  <p>
    הפרויקט מופץ תחת רישיון <strong>MIT</strong> – חופשי לשימוש ושינוי למטרות לימודיות ומחקריות.
  </p>

  <hr>

  <p align="center"><strong>👨‍💻 Raz Eini (2026)</strong></p>

</div>
