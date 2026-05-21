import streamlit as st
from jira_engine import generate_report
from pdf_generator import generate_pdf_report

st.set_page_config(
    page_title="AI Delivery Intelligence Agent",
    layout="wide"
)

st.title("AI Delivery Intelligence Agent")
st.subheader("Sprint Disruption & Capacity Impact Analyzer")

st.write("""
This tool analyzes Jira sprint data and detects:
- Unplanned priority work
- Sprint disruptions
- Capacity loss
- Disruption categories
- AI-generated retro summaries
- PDF report generation
""")

if st.button("Generate Sprint Report"):

    report = generate_report()

    st.success("Live Jira data fetched successfully.")
    st.info(f"Fetched {report['ticket_count']} Jira tickets from live Jira project.")

    total_story_points = report["total_story_points"]
    planned_story_points = report["planned_story_points"]
    unplanned_story_points = report["unplanned_story_points"]
    disruption_percentage = report["disruption_percentage"]

    category_summary = report["category_summary"]
    unplanned_tickets = report["unplanned_tickets"]
    ai_summary = report["ai_summary"]

    st.header("Sprint Capacity Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Story Points", total_story_points)
    col2.metric("Planned SP", planned_story_points)
    col3.metric("Unplanned SP", unplanned_story_points)
    col4.metric("Capacity Loss %", f"{disruption_percentage}%")

    st.header("Disruption Category Impact")

    for category, points in category_summary.items():
        st.write(f"• {category}: {points} SP")

    st.header("Unplanned Priority Tickets")

    for ticket in unplanned_tickets:
        st.write(
            f"{ticket['key']} | "
            f"{ticket['summary']} | "
            f"{ticket['priority']} | "
            f"{ticket['story_points']} SP"
        )

    st.header("AI Retro Summary")
    st.info(ai_summary)

    st.header("Download Report")

    pdf_file = generate_pdf_report(report)

    with open(pdf_file, "rb") as file:
        st.download_button(
            label="Download PDF Report",
            data=file,
            file_name="sprint_disruption_report.pdf",
            mime="application/pdf"
        )