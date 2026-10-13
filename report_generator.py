from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


def generate_pdf_report(
    total,
    score,
    severity_list,
    source_type="Image"
):

    pdf_file = "report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    heading_style = styles["Heading2"]
    body_style = styles["BodyText"]

    elements = []

    # ==================================================
    # COVER PAGE
    # ==================================================

    elements.append(
        Paragraph(
            "AI-BASED POTHOLE DETECTION AND ROAD CONDITION MONITORING SYSTEM",
            title_style
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "Inspection Report",
            heading_style
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            f"Generated On: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
            body_style
        )
    )

    elements.append(
        Paragraph(
            f"Source Type: {source_type}",
            body_style
        )
    )

    elements.append(PageBreak())

    # ==================================================
    # SEVERITY COUNTS
    # ==================================================

    low = severity_list.count("Low")
    medium = severity_list.count("Medium")
    high = severity_list.count("High")

    # ==================================================
    # ROAD CONDITION
    # ==================================================

    if score >= 80:
        condition = "EXCELLENT"
    elif score >= 60:
        condition = "GOOD"
    elif score >= 40:
        condition = "MODERATE"
    elif score >= 20:
        condition = "POOR"
    else:
        condition = "CRITICAL"

    # ==================================================
    # EXECUTIVE SUMMARY
    # ==================================================

    elements.append(
        Paragraph(
            "Executive Summary",
            heading_style
        )
    )

    summary = f"""
    This report presents the results of automated road inspection
    using an AI-Based Pothole Detection and Road Condition
    Monitoring System built on YOLOv8.

    <br/><br/>

    Source Type: <b>{source_type}</b><br/>
    Total Potholes Detected: <b>{total}</b><br/>
    Road Condition Score: <b>{score}/100</b><br/>
    Overall Road Condition: <b>{condition}</b>
    """

    elements.append(
        Paragraph(summary, body_style)
    )

    elements.append(Spacer(1, 15))

    # ==================================================
    # DETECTION RESULTS
    # ==================================================

    elements.append(
        Paragraph(
            "Detection Results",
            heading_style
        )
    )

    detection_text = f"""
    <b>Total Potholes Detected:</b> {total}

    <br/><br/>

    <b>Severity Breakdown</b>

    <br/>

    Low Severity : {low}

    <br/>

    Medium Severity : {medium}

    <br/>

    High Severity : {high}
    """

    elements.append(
        Paragraph(detection_text, body_style)
    )

    elements.append(Spacer(1, 15))

    # ==================================================
    # ROAD CONDITION ASSESSMENT
    # ==================================================

    elements.append(
        Paragraph(
            "Road Condition Assessment",
            heading_style
        )
    )

    road_text = f"""
    <b>Road Score:</b> {score}/100

    <br/><br/>

    <b>Road Condition:</b> {condition}

    <br/><br/>

    Score Interpretation:

    <br/>
    80-100 : Excellent
    <br/>
    60-79 : Good
    <br/>
    40-59 : Moderate
    <br/>
    20-39 : Poor
    <br/>
    0-19 : Critical
    """

    elements.append(
        Paragraph(road_text, body_style)
    )

    elements.append(Spacer(1, 15))

    # ==================================================
    # MAINTENANCE RECOMMENDATIONS
    # ==================================================

    if score >= 80:

        recommendation = """
        • Road is in excellent condition.<br/>
        • Continue routine monitoring.<br/>
        • Preventive maintenance is sufficient.<br/>
        • No immediate repairs required.
        """

    elif score >= 60:

        recommendation = """
        • Minor road damage detected.<br/>
        • Repair medium severity potholes.<br/>
        • Schedule periodic inspections.<br/>
        • Continue monitoring affected sections.
        """

    elif score >= 40:

        recommendation = """
        • Moderate road deterioration observed.<br/>
        • Maintenance should be scheduled soon.<br/>
        • Repair damaged road surface.<br/>
        • Increase monitoring frequency.
        """

    else:

        recommendation = """
        • Severe road damage detected.<br/>
        • Immediate maintenance is required.<br/>
        • Safety warnings should be installed.<br/>
        • Road inspection by authorities is recommended.
        """

    elements.append(
        Paragraph(
            "Maintenance Recommendations",
            heading_style
        )
    )

    elements.append(
        Paragraph(
            recommendation,
            body_style
        )
    )

    elements.append(Spacer(1, 15))

    # ==================================================
    # RISK ASSESSMENT
    # ==================================================

    elements.append(
        Paragraph(
            "Risk Assessment",
            heading_style
        )
    )

    risk_text = """
    Potential impacts of detected potholes include:

    <br/><br/>

    • Tire damage<br/>
    • Suspension damage<br/>
    • Increased accident risk<br/>
    • Reduced ride comfort<br/>
    • Increased vehicle maintenance costs<br/>
    • Traffic congestion due to road deterioration
    """

    elements.append(
        Paragraph(
            risk_text,
            body_style
        )
    )

    elements.append(Spacer(1, 15))

    # ==================================================
    # TECHNICAL INFORMATION
    # ==================================================

    elements.append(
        Paragraph(
            "Technical Information",
            heading_style
        )
    )

    tech_text = f"""
    <b>Detection Model:</b> YOLOv8

    <br/>

    <b>Framework:</b> Ultralytics

    <br/>

    <b>Input Type:</b> {source_type}

    <br/>

    <b>Analysis Type:</b> Automated Road Inspection

    <br/>

    <b>Output:</b> Pothole Detection,
    Severity Classification and
    Road Condition Assessment
    """

    elements.append(
        Paragraph(
            tech_text,
            body_style
        )
    )

    elements.append(Spacer(1, 15))

    # ==================================================
    # CONCLUSION
    # ==================================================

    elements.append(
        Paragraph(
            "Conclusion",
            heading_style
        )
    )

    conclusion = f"""
    The AI-Based Pothole Detection System successfully analyzed
    the provided {source_type.lower()} and detected
    <b>{total}</b> potholes.

    <br/><br/>

    Based on severity classification and road condition
    evaluation, the road received a score of
    <b>{score}/100</b> and was classified as
    <b>{condition}</b>.

    <br/><br/>

    Appropriate maintenance actions are recommended
    to improve road quality, safety and driving comfort.
    """

    elements.append(
        Paragraph(
            conclusion,
            body_style
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "This report was generated automatically by the AI-Based Pothole Detection and Road Condition Monitoring System.",
            body_style
        )
    )

    # Build PDF

    doc.build(elements)

    return pdf_file