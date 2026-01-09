from flask import Blueprint, render_template, send_from_directory
from .data_loader import load_markdown
import os

main = Blueprint("main", __name__)

@main.route("/")
def home():
    content = load_markdown("README.md")
    return render_template("home.html", content=content)


@main.route("/portfolio")
def portfolio():
    sections = {
        "Tableau Dashboards": "Interactive dashboards demonstrating business insights and data storytelling.",
        "SQL Analytics": "Business-focused SQL queries for reporting, KPI tracking, and performance analysis.",
        "Python Data Analysis": "Python scripts for data cleaning, transformation, and preparation.",
        "Case Studies": "Industry-based analytics case studies across Pharma, Banking, and Automotive domains."
    }
    return render_template("portfolio.html", sections=sections)


@main.route("/tableau")
def tableau():
    dashboards = [
        {
            "title": "Professional CV Dashboard",
            "description": "Visual summary of professional experience, skills, certifications, and industry exposure.",
            "category": "Executive Summary",
            "features": [
                "Interactive experience timeline",
                "Skills proficiency matrix",
                "Industry & technology breakdown",
                "Project portfolio overview"
            ],
            "tags": ["Tableau", "CV", "Professional"],
            "link": "https://public.tableau.com/app/profile/manpreet.kaur7485"
        }
    ]
    return render_template("tableau.html", dashboards=dashboards)


@main.route("/case-studies")
def case_studies():
    studies = {
        "Pharma Analytics": load_markdown("case-studies/pharma_analytics.md"),
        "Banking Insights": load_markdown("case-studies/banking_insights.md"),
        "Automotive Market Analysis": load_markdown("case-studies/automotive_market_analysis.md"),
    }

    return render_template("case_studies.html", studies=studies)


@main.route("/contact")
def contact():
    return render_template("contact.html")


@main.route("/resume-view")
def resume_view():
    """Display the Australian resume"""
    return render_template("resume.html")


@main.route("/resume")
def resume():
    """Display the Australian resume"""
    try:
        with open(os.path.join(os.path.dirname(__file__), '..', 'resume', 'Manpreet_Kaur_Resume_AUS.html'), 'r', encoding='utf-8') as f:
            resume_html = f.read()
        return render_template("base.html", page_content=resume_html)
    except:
        return "Resume not found", 404


@main.route("/resume/download/<filename>")
def download_resume(filename):
    """Serve the resume PDF or HTML"""
    resume_dir = os.path.join(os.path.dirname(__file__), '..', 'resume')
    try:
        return send_from_directory(resume_dir, filename, as_attachment=True)
    except:
        return "Resume not found", 404


