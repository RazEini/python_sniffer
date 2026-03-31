# 🕵️ NetGuard – Python Network Sniffer & DPI

מנתח תעבורת רשת בזמן אמת עם יכולות **Deep Packet Inspection (DPI)** וזיהוי אנומליות.
הכלי מאפשר ניטור חבילות מידע (Packets), זיהוי פרוטוקולים והתרעה על תעבורה לא מאובטחת.
מבוסס **Python + Scapy**.

&nbsp;&nbsp;&nbsp;

## 🎬 Demo / המחשה

<p align="center">
  <img src="https://via.placeholder.com/400x200?text=Network+Traffic+Monitoring+View" alt="Monitoring View">
</p>
<p align="center">
  <em>ממשק הניטור והתראות האבטחה בזמן אמת</em>
</p>

## 🔎 Overview

**NetGuard** נועד לספק הצצה עמוקה למה שקורה בתוך כרטיס הרשת שלך. 
בניגוד לסניפרים רגילים, הכלי לא רק מציג את הכתובות (IP), אלא "פותח" את חבילות המידע בשכבת האפליקציה כדי לחשוף נתונים שעוברים בפורטים לא מוצפנים (כמו פורט 80). זהו כלי עזר קריטי להבנת מודל ה-OSI ואיתור חולשות אבטחה ברשת המקומית.

## 🚀 Features

| תחום | תכונה | סטטוס | הערות |
| :--- | :--- | :---: | :--- |
| 📡 **Sniffing** | Real-time Packet Capture | ✅ | ניטור רציף של כל תעבורת ה-IP |
| 🛡️ **Security** | HTTP Alerting (Port 80) | ✅ | התראה אדומה על תעבורה לא מוצפנת |
| 🔍 **DPI** | Deep Packet Inspection | ✅ | חילוץ Payload ופענוח טקסט גולמי |
| 📝 **Logging** | Automated Security Log | ✅ | שמירת אירועים ב-`security_log.txt` |
| 🚦 **Protocols** | Protocol Identification | ✅ | זיהוי אוטומטי של TCP, UDP, DNS ו-HTTPS |
| 🎨 **Visuals** | Color-Coded Terminal | ✅ | שימוש בקודי ANSI להבחנה בין סוגי תנועה |
| ⚙️ **Performance** | Zero-Storage Mode | ✅ | עבודה ללא צריכת זיכרון מיותרת (`store=0`) |

## 🛠️ טכנולוגיות

* **שפת פיתוח:** Python 3.x
* **ספריה מרכזית:** [Scapy](https://scapy.net/) (Network Manipulation Tool)
* **מודולים נוספים:** `datetime`, `socket`
* **ניהול סביבה:** `venv` + `requirements.txt`
* **מערכת הפעלה:** Windows / Linux (דורש הרשאות מנהל)

## ⚙️ התקנה והרצה

הגדרת הסביבה והפעלת הפרויקט בכמה צעדים פשוטים:

| שלב | פעולה | פקודה |
| :--- | :--- | :--- |
| 1️⃣ | יצירת סביבה וירטואלית | `python -m venv .venv` |
| 2️⃣ | הפעלת הסביבה (Windows) | `.\.venv\Scripts\activate` |
| 3️⃣ | התקנת תלויות | `pip install scapy` |
| 4️⃣ | הרצה (כמנהל מערכת) | `python main.py` |

## ⚠️ הערות חשובות

* יש להריץ את הטרמינל כ-**Administrator** (ב-Windows) או עם **sudo** (ב-Linux) כדי לאפשר גישה ל-Raw Sockets.
* הכלי מיועד למטרות לימודיות ומחקר אבטחה בלבד.

## 📄 רישיון

הפרויקט מופץ תחת רישיון **MIT** – חופשי לשימוש, שינוי והפצה, כל עוד נשמר קרדיט למחבר.

👨‍💻 **Raz Eini (2025)**
