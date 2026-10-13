import streamlit as st
import pandas as pd
import plotly.express as px
from detector import PotholeDetector
from severity import classify_severity, road_condition_score
from report_generator import generate_pdf_report
import tempfile

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Road Damage Detection System",
    page_icon="🛣️",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

st.sidebar.title("🛣️ Road Damage Detection")

page = st.sidebar.radio(
    "Navigation",
    ["Detection", "Dashboard", "About"]
)

confidence = st.sidebar.slider(
    "Detection Sensitivity",
    0.1,
    1.0,
    0.40,
    0.05
)

# ---------------- LOAD MODEL ----------------

try:
    detector = PotholeDetector("best.pt", confidence)
except Exception as e:
    st.error(f"Model Loading Error: {e}")
    st.stop()

# ===================================================
# DETECTION PAGE
# ===================================================

if page == "Detection":

    st.title("🔎 Road Damage Detection System")

    st.caption(
        "Upload road images or videos to detect potholes using YOLOv8."
    )

    tab1, tab2 = st.tabs([
        "📸 Image Detection",
        "🎥 Video Detection"
    ])

    # ===================================================
    # IMAGE TAB
    # ===================================================

    with tab1:

        uploaded_file = st.file_uploader(
            "Upload Road Image",
            type=["jpg", "jpeg", "png"]
        )

        if uploaded_file is not None:

            tf = tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".jpg"
            )

            tf.write(uploaded_file.read())
            tf.close()

            img, results = detector.detect_image(tf.name)

            st.image(
                img,
                channels="BGR",
                use_container_width=True
            )

            total = len(results)

            severity = [
                classify_severity(r["area"])
                for r in results
            ]

            score = road_condition_score(
                total,
                severity
            )

            col1, col2, col3 = st.columns(3)

            col1.metric("Potholes", total)
            col2.metric("Road Score", score)
            col3.metric(
                "Status",
                "Good" if score > 70 else "Poor"
            )

            if severity:

                df = pd.DataFrame({
                    "Severity": severity
                })

                fig = px.histogram(
                    df,
                    x="Severity",
                    color="Severity",
                    title="Severity Distribution"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            try:

                pdf = generate_pdf_report(
                    total,
                    score,
                    severity,
                    "Image"
                )

                with open(pdf, "rb") as f:

                    st.download_button(
                        "📄 Download Image Report",
                        data=f,
                        file_name="image_report.pdf",
                        mime="application/pdf"
                    )

            except Exception as e:
                st.error(f"PDF Generation Error: {e}")

    # ===================================================
    # VIDEO TAB
    # ===================================================

    with tab2:

        uploaded_video = st.file_uploader(
            "Upload Road Video",
            type=["mp4", "avi", "mov"]
        )

        if uploaded_video is not None:

            tf = tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".mp4"
            )

            tf.write(uploaded_video.read())
            tf.close()

            output_video, results = detector.detect_video(tf.name)

            st.video(output_video)

            total = len(results)

            severity = [
                classify_severity(r["area"])
                for r in results
            ]

            score = road_condition_score(
                total,
                severity
            )

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Potholes Detected",
                total
            )

            col2.metric(
                "Road Score",
                score
            )

            if score >= 80:
                status = "Excellent"
            elif score >= 60:
                status = "Good"
            elif score >= 40:
                status = "Moderate"
            else:
                status = "Poor"

            col3.metric(
                "Condition",
                status
            )

            if severity:

                df = pd.DataFrame({
                    "Severity": severity
                })

                fig = px.pie(
                    df,
                    names="Severity",
                    title="Severity Distribution"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            try:

                pdf = generate_pdf_report(
                    total,
                    score,
                    severity,
                    "Video"
                )

                with open(pdf, "rb") as f:

                    st.download_button(
                        "📄 Download Video Report",
                        data=f,
                        file_name="video_report.pdf",
                        mime="application/pdf"
                    )

            except Exception as e:
                st.error(f"PDF Generation Error: {e}")

# ===================================================
# DASHBOARD PAGE
# ===================================================

elif page == "Dashboard":

    st.title("📊 Analytics Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Roads", "158")
    c2.metric("Potholes Found", "763")
    c3.metric("Critical Areas", "42")
    c4.metric("Avg Road Score", "78")

    st.subheader("Road Health Overview")

    data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Potholes": [50, 80, 65, 45, 35]
    })

    fig = px.line(
        data,
        x="Month",
        y="Potholes",
        markers=True,
        title="Monthly Pothole Statistics"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ===================================================
# ABOUT PAGE
# ===================================================

elif page == "About":

    st.title("ℹ️ About")

    st.markdown("""
### AI-Based Pothole Detection System

This project uses:

✅ YOLOv8 Object Detection

✅ Computer Vision

✅ Severity Analysis

✅ Road Health Scoring

✅ PDF Report Generation

Developed for smart road monitoring and maintenance.
""")