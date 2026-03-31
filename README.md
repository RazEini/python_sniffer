<div dir="rtl">

  <h1 align="center">🕵️ NetGuard – Python Network Sniffer & DPI</h1>

  <p align="center">
    מנתח תעבורת רשת בזמן אמת עם יכולות <strong>Deep Packet Inspection (DPI)</strong> וזיהוי אנומליות.<br>
    הכלי מאפשר ניטור חבילות מידע (Packets), זיהוי פרוטוקולים והתרעה על תעבורה לא מאובטחת.<br>
    מבוסס <strong>Python + Scapy</strong>.
  </p>

  <br>
  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python Badge">
    <img src="https://img.shields.io/badge/Library-Scapy-red" alt="Scapy Badge">
    <img src="https://img.shields.io/badge/Security-DPI-orange" alt="DPI Badge">
    <img src="https://img.shields.io/badge/License-MIT-green" alt="License Badge">
  </p>

  <br>

  <hr>

  <h2 align="center">🔎 Overview</h2>
  <p align="center" dir="rtl">
    <strong>NetGuard</strong> נועד לספק הצצה עמוקה למה שקורה בתוך כרטיס הרשת שלך. 
    <br>
    בניגוד לסניפרים רגילים, הכלי לא רק מציג את הכתובות (IP), אלא "פותח" את חבילות המידע בשכבת האפליקציה.    זהו כלי עזר קריטי להבנת מודל ה-OSI, איתור חולשות אבטחה ברשת המקומית וחילוץ נתונים מפורטים (Payload) בזמן אמת.
</p>

  <br>

  <hr>

  <br>

  <h2 align="center">🚀 Features</h2>

  <table align="center" dir="rtl">
    <thead>
      <tr>
        <th>תחום</th>
        <th>תכונה</th>
        <th>סטטוס</th>
        <th>הערות</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>📡 Sniffing</td>
        <td>Real-time Packet Capture</td>
        <td>✅</td>
        <td>לכידה וניתוח של תעבורת IP חיה</td>
      </tr>
      <tr>
        <td>🛡️ Security</td>
        <td>HTTP Alerting</td>
        <td>✅</td>
        <td>זיהוי והתראה על תעבורה בפורט 80</td>
      </tr>
      <tr>
        <td>🔍 DPI</td>
        <td>Deep Packet Inspection</td>
        <td>✅</td>
        <td>פענוח Payload לטקסט קריא (UTF-8)</td>
      </tr>
      <tr>
        <td>📝 Logging</td>
        <td>Automated Security Log</td>
        <td>✅</td>
        <td>רישום אירועים ב-security_log.txt</td>
      </tr>
      <tr>
        <td>🚦 Protocols</td>
        <td>Protocol Analysis</td>
        <td>✅</td>
        <td>תמיכה ב-TCP, UDP, DNS ו-HTTPS</td>
      </tr>
      <tr>
        <td>🎨 UI</td>
        <td>Color-Coded CLI</td>
        <td>✅</td>
        <td>ממשק טרמינל צבעוני וקריא</td>
      </tr>
      <tr>
        <td>⚙️ Performance</td>
        <td>Zero-Storage Mode</td>
        <td>✅</td>
        <td>שימוש יעיל במשאבים (store=0)</td>
      </tr>
    </tbody>
  </table>

  <br>

  <hr>

  <div dir="rtl">
  <h2>🛠️ טכנולוגיות</h2>
  <ul>
    <li><strong>שפת פיתוח:</strong> Python 3.x</li>
    <li><strong>ספריה מרכזית:</strong> Scapy</li>
    <li><strong>פרוטוקולים נתמכים:</strong> IP, TCP, UDP, DNS, HTTP</li>
    <li><strong>ניהול נתונים:</strong> Raw Data Payload Processing</li>
    <li><strong>סביבת עבודה:</strong> Virtual Environment (venv)</li>
  </ul>
</div>

  <hr>

  <h2>⚙️ התקנה והרצה</h2>
  <div dir="ltr" align="left">
    <pre>
1. python -m venv .venv
2. .\.venv\Scripts\activate  # Windows
3. pip install scapy
4. python main.py
    </pre>
  </div>

  <hr>

  <h2>📄 רישיון</h2>
  <p>
    הפרויקט מופץ תחת רישיון <strong>MIT</strong> – חופשי לשימוש, שינוי והפצה, כל עוד נשמר קרדיט למחבר.
  </p>

  <hr>

  <p align="center"><strong>👨‍💻 Raz Eini (2025)</strong></p>

</div>
