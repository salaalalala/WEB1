from flask import Flask, render_template, send_from_directory, abort
import os
import json

app = Flask(__name__)

# ─── ADD YOUR TOPICS HERE ───────────────────────────────────────────────────
# Each topic: { title, slug, description, category, pdf (filename in static/pdfs/) }
TOPICS = [
    {
        "title": "Polymarket Arbitrage Strategies 2025",
        "slug": "polymarket-arbitrage-2025",
        "description": "Complete playbook for finding and executing arbitrage opportunities on Polymarket prediction markets. Includes risk management, sizing, and real trade examples.",
        "category": "Trading",
        "pdf": "polymarket-arbitrage.pdf",
        "badge": "HOT"
    },
    {
        "title": "Claude Code: Power User Prompts",
        "slug": "claude-code-prompts",
        "description": "Curated prompts that unlock Claude Code's full potential — from complex refactors to full-stack app generation. Used by top engineers.",
        "category": "AI Prompts",
        "pdf": "claude-code-prompts.pdf",
        "badge": "NEW"
    },
    {
        "title": "Business Automation Prompt Pack",
        "slug": "business-automation-prompts",
        "description": "50+ battle-tested prompts for automating business workflows, writing SOPs, cold emails, and scaling operations using AI tools.",
        "category": "Business",
        "pdf": "business-automation.pdf",
        "badge": ""
    },
    {
        "title": "Viral Twitter/X Thread Templates",
        "slug": "viral-twitter-templates",
        "description": "Proven thread structures that drive engagement, follows, and clicks. Based on analysis of 1,000+ viral posts in tech and finance.",
        "category": "Growth",
        "pdf": "twitter-templates.pdf",
        "badge": "POPULAR"
    },
    {
        "title": "DeFi Yield Farming Guide 2025",
        "slug": "defi-yield-farming-2025",
        "description": "Step-by-step framework for evaluating, entering, and exiting yield positions across major protocols. Includes risk scoring rubric.",
        "category": "Trading",
        "pdf": "defi-yield.pdf",
        "badge": ""
    },
    {
        "title": "ChatGPT vs Claude: Best Prompts Comparison",
        "slug": "chatgpt-vs-claude-prompts",
        "description": "Side-by-side comparison of what prompts work best on each model. Save hours of testing with this definitive reference guide.",
        "category": "AI Prompts",
        "pdf": "chatgpt-vs-claude.pdf",
        "badge": "NEW"
    },
]

CATEGORIES = sorted(set(t["category"] for t in TOPICS))

@app.route("/")
def index():
    return render_template("index.html", topics=TOPICS, categories=CATEGORIES)

@app.route("/topic/<slug>")
def topic(slug):
    t = next((x for x in TOPICS if x["slug"] == slug), None)
    if not t:
        abort(404)
    return render_template("topic.html", topic=t, topics=TOPICS)

@app.route("/pdf/<filename>")
def serve_pdf(filename):
    pdf_dir = os.path.join(app.root_path, "static", "pdfs")
    return send_from_directory(pdf_dir, filename)

@app.route("/category/<cat>")
def category(cat):
    filtered = [t for t in TOPICS if t["category"] == cat]
    return render_template("index.html", topics=filtered, categories=CATEGORIES, active_cat=cat)

if __name__ == "__main__":
    app.run(debug=True)
