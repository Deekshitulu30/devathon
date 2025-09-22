# personalized_medicine_prototype.py
import streamlit as st
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --------------------------
# Patient mock data
# --------------------------
patient = {
    "name": "Asha Patel",
    "age": 46,
    "sex": "F",
    "id": "PT-2025-0012",
    "photo": "https://via.placeholder.com/400x300.png?text=Patient+Profile",
    "summary": "Stage II breast cancer. ER+/HER2-. Prior chemo: none.",
    "genomic": [
        {"gene": "BRCA1", "variant": "c.68_69delAG", "significance": "Pathogenic"},
        {"gene": "PIK3CA", "variant": "p.H1047R", "significance": "Likely pathogenic"}
    ]
}

# --------------------------
# Mock vitals / response data
# --------------------------
vitals = pd.DataFrame({
    "time": ["Day 0", "Week 1", "Week 2", "Week 3", "Week 4"],
    "score": [72, 68, 75, 78, 82]
})

# --------------------------
# Mock AI inference function
# --------------------------
def get_recommendations(patient):
    recs = []
    genes = [g["gene"] for g in patient["genomic"]]

    if "BRCA1" in genes:
        recs.append({
            "title": "Consider PARP inhibitor",
            "reason": "BRCA1 pathogenic variant — targeted therapy sensitivity",
            "confidence": 0.87
        })

    if "PIK3CA" in genes:
        recs.append({
            "title": "PI3K inhibitor trial",
            "reason": "PIK3CA mutation — eligible for targeted trials",
            "confidence": 0.76
        })

    recs.append({
        "title": "Multidisciplinary tumor board review",
        "reason": "Integrate pathology, radiology, genomics and patient preferences",
        "confidence": 0.95
    })

    return recs

recommendations = get_recommendations(patient)

# --------------------------
# Streamlit UI
# --------------------------
st.set_page_config(page_title="AI Personalized Medicine Prototype", layout="wide")

st.title("🧬 AI Personalized Medicine — Prototype")
st.write("**Note:** This is a demo UI. Replace mock inference with real models & ensure privacy, security, and clinical validation.")

# Layout: two columns
col1, col2 = st.columns([1,2])

# --------------------------
# Left: Patient info
# --------------------------
with col1:
    st.image(patient["photo"], use_container_width=True)
    st.subheader(patient["name"])
    st.caption(f"ID: {patient['id']} · {patient['age']} yrs · {patient['sex']}")
    st.write(patient["summary"])

    st.markdown("**Genomic Variants:**")
    for g in patient["genomic"]:
        st.markdown(f"- **{g['gene']}** ({g['variant']}) — {g['significance']}")

    if st.button("Run AI Analysis"):
        st.success("✅ AI analysis completed!")

# --------------------------
# Right: Charts & AI recs
# --------------------------
with col2:
    st.subheader("Patient Vitals & Response")

    fig, ax = plt.subplots()
    ax.plot(vitals["time"], vitals["score"], marker="o")
    ax.set_xlabel("Time")
    ax.set_ylabel("Response Score")
    ax.set_title("Patient Response Over Time")
    st.pyplot(fig)

    st.subheader("AI Recommendations")
    for r in recommendations:
        st.markdown(f"**{r['title']}** ({round(r['confidence']*100)}% confidence)")
        st.caption(r["reason"])
        st.divider()

    st.info("Explainability: Key features — BRCA1 pathogenic, PIK3CA mutation, tumor grade.")
