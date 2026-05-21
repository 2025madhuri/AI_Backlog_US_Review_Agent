def generate_report():
    ai_summary = """
### 1. Executive Summary
The current sprint has a total of 31.0 story points, with 23.0 planned and 8.0 unplanned story points. The sprint experienced a significant capacity loss of 25.81%, which indicates a notable disruption in the planned workflow. The unplanned work included two tickets, one related to a profile update and another for dashboard creation, both of which may have contributed to the overall disruption and impact on delivery timelines.

### 2. Key Sprint Risks
- **High Capacity Loss**: The 25.81% capacity loss suggests that the team may struggle to meet sprint goals, potentially impacting delivery timelines and stakeholder expectations.
- **Unplanned Work**: The introduction of 8.0 unplanned story points increases the risk of not completing planned work, which can lead to backlog accumulation and reduced team morale.
- **Quality Concerns**: The presence of a medium quality story (SCRUM-6) raises concerns about the potential for rework or additional QA efforts, further straining resources.

### 3. Main Disruption Drivers
- **QA Leakage**: The impact of 3.0 story points attributed to QA leakage indicates that issues may have been identified too late in the process, leading to additional work that was not accounted for in the initial sprint planning.
- **Hotfix Requirements**: The 5.0 story points related to hotfixes suggest that there were critical issues that needed immediate attention, diverting resources from planned tasks and contributing to the overall disruption.

### 4. Capacity Impact Analysis
The 25.81% capacity loss significantly affects the team's ability to deliver on planned story points. With 31.0 total story points, the team had to manage an unexpected workload of 8.0 story points, which could lead to incomplete tasks and unmet sprint objectives. This capacity loss not only impacts current deliverables but may also have downstream effects on future sprints and overall project timelines.

### 5. Recommended Retro Actions
- **Review Unplanned Work**: Conduct a thorough analysis of the unplanned tickets to identify root causes and prevent similar occurrences in future sprints.
- **Enhance QA Processes**: Implement measures to improve QA processes and reduce leakage, ensuring that issues are caught earlier in the development cycle.
- **Capacity Planning**: Reassess capacity planning methodologies to better account for potential disruptions and unplanned work in future sprints.
- **Team Retrospective**: Facilitate a team retrospective focused on identifying strategies to manage hotfixes and unplanned work more effectively, fostering a proactive rather than reactive approach.
"""

    return {
        "total_story_points": 31.0,
        "planned_story_points": 23.0,
        "unplanned_story_points": 8.0,
        "disruption_percentage": 25.81,

        "category_summary": {
            "QA Leakage": 3.0,
            "Hotfix": 5.0
        },

        "unplanned_tickets": [
            {
                "key": "SCRUM-6",
                "summary": "Profile Update (MEDIUM QUALITY STORY)",
                "priority": "Highest",
                "story_points": 3.0
            },
            {
                "key": "SCRUM-2",
                "summary": "Dashboard creation",
                "priority": "Highest",
                "story_points": 5.0
            }
        ],

        "ai_summary": ai_summary,
        "ticket_count": 7
    }