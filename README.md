# PromptVault 🗄️

Professional Flask website for prompts, strategies & downloadable PDFs.

## Run Locally

```bash
pip install -r requirements.txt
python app.py
# → http://localhost:5000
```

## ✅ How to Add a New Topic + PDF

### Step 1 — Add your PDF
Put your PDF file inside:
```
static/pdfs/your-filename.pdf
```

### Step 2 — Add the topic in app.py
Open `app.py` and find the `TOPICS` list (line ~10).
Add a new entry like this:

```python
{
    "title": "Your Topic Title Here",
    "slug": "your-topic-slug",          # URL: /topic/your-topic-slug
    "description": "Short description shown on cards and topic page.",
    "category": "AI Prompts",           # Trading / Business / Growth / AI Prompts
    "pdf": "your-filename.pdf",         # must match the file in static/pdfs/
    "badge": "NEW"                      # HOT / NEW / POPULAR / "" (empty = no badge)
},
```

That's it. Save → push to GitHub → Railway auto-deploys.

---

## 📢 Adsterra Ad Placements

Open `templates/base.html` — there are 4 clearly labelled spots:

| Label | Location | Best Ad Type |
|---|---|---|
| `ADSTERRA_HEAD_SCRIPT_START` | `<head>` | Script tag (Social Bar, Push) |
| `ADSTERRA_BANNER_TOP_START` | Below nav | Banner / Leaderboard (728×90) |
| `ADSTERRA_BANNER_BOTTOM_START` | Above footer | Banner / Leaderboard |
| `ADSTERRA_INFEED_START` | Homepage feed | Native / In-feed |

Open `templates/topic.html` — 2 more spots:

| Label | Location | Best Ad Type |
|---|---|---|
| `ADSTERRA_TOPIC_AD_START` | Topic page top | Direct Link / Popunder |
| `ADSTERRA_INARTICLE_START` | Mid-page | In-article Native |

Just paste your Adsterra `<script>` tag between the START and END comment lines.

---

## Deploy to Railway

1. Push this folder to a GitHub repo
2. Go to railway.app → New Project → Deploy from GitHub
3. Select your repo → Railway auto-detects Python
4. Done. Your site is live at your Railway URL.

## Folder Structure

```
promptvault/
├── app.py              ← Add topics here
├── requirements.txt
├── Procfile            ← Railway deployment
├── static/
│   ├── css/style.css
│   ├── js/main.js
│   └── pdfs/           ← Put your PDFs here
└── templates/
    ├── base.html       ← Adsterra ad slots here
    ├── index.html
    └── topic.html
```
