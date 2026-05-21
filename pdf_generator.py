from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm


def generate_pdf_report(report, filename="sprint_disruption_report.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )

    styles = getSampleStyleSheet()
    story = []

    normal = styles["Normal"]
    heading = styles["Heading2"]
    title = styles["Title"]

    story.append(Paragraph("AI DELIVERY INTELLIGENCE REPORT", title))
    story.append(Spacer(1, 12))

    story.append(Paragraph("SPRINT CAPACITY SUMMARY", heading))
    story.append(Paragraph(f"Total Sprint Story Points: {report['total_story_points']}", normal))
    story.append(Paragraph(f"Planned Story Points: {report['planned_story_points']}", normal))
    story.append(Paragraph(f"Unplanned Story Points: {report['unplanned_story_points']}", normal))
    story.append(Paragraph(f"Sprint Capacity Lost to Disruptions: {report['disruption_percentage']}%", normal))
    story.append(Spacer(1, 12))

    story.append(Paragraph("DISRUPTION CATEGORY IMPACT", heading))
    for category, points in report["category_summary"].items():
        story.append(Paragraph(f"{category}: {points} story points", normal))
    story.append(Spacer(1, 12))

    story.append(Paragraph("UNPLANNED PRIORITY TICKETS", heading))
    for ticket in report["unplanned_tickets"]:
        story.append(
            Paragraph(
                f"{ticket['key']} | {ticket['summary']} | {ticket['priority']} | {ticket['story_points']} SP",
                normal
            )
        )
    story.append(Spacer(1, 12))

    story.append(Paragraph("AI RETRO SUMMARY", heading))

    ai_summary = report["ai_summary"]
    ai_summary = ai_summary.replace("###", "")
    ai_summary = ai_summary.replace("**", "")

    for line in ai_summary.split("\n"):
        if line.strip():
            story.append(Paragraph(line.strip(), normal))
            story.append(Spacer(1, 6))

    doc.build(story)

    return filename