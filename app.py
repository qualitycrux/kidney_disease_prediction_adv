import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
#load model
model=pickle.load(open('model-kidney-disease.pkl','rb'))
scaller=pickle.load(open('scaller-kidney-disease.pkl','rb'))


# define function Prediction on new data using function
def predict_kidney_disease(age, bp, sg, al, hemo,pcv,rc,bu,bgr,sc,sod,pot,htn, dm, cad, appet, pc,pe,ane):
    # Create a DataFrame with input variables, following the correct order
    df_dict = {
        'age': [age],
        'bp': [bp],
        'sg': [sg],
        'al': [al],
        'hemo': [hemo],
        'pcv': [pcv],
        'rc': [rc],
        'bu': [bu],
        'bgr': [bgr],
        'sc': [sc],
        'sod':[sod],
        'pot':[pot],
        'htn': [htn],
        'dm': [dm],
        'cad': [cad],
        'appet': [appet],
        'pc': [pc],
        'pe' : [pe],
        'ane': [ane],
    }
    df = pd.DataFrame(df_dict)

    # Encode the categorical columns
    le = LabelEncoder()
    df['htn'] = le.fit_transform(df['htn'])
    df['dm'] = le.fit_transform(df['dm'])
    df['cad'] = le.fit_transform(df['cad'])
    df['appet'] = le.fit_transform(df['appet'])
    df['pc'] = le.fit_transform(df['pc'])
    df['pe'] = le.fit_transform(df['pe'])
    df['ane'] = le.fit_transform(df['ane'])

    # Scale the numeric columns using the previously fitted scaler
    numeric_cols=['age','bp','sg','al','hemo','pcv','rc','bu','bgr','sc','sod','pot']
    df[numeric_cols] = scaller.transform(df[numeric_cols])

    # Make the prediction
    prediction = model.predict(df)

    # Return the predicted class
    return prediction[0]



# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main{
    background-color:#f5f7fb;
}

.block-container{
    padding-top:2.5rem;
    padding-bottom:2rem;
    padding-left:2rem;
    padding-right:2rem;
}

.big-title{
    font-size:30px;
    font-weight:bold;
    color:#1565C0;
    text-align:center;
}

.sub-title{
    text-align:center;
    color:#666;
    font-size:18px;
    margin-bottom:25px;
}

.stButton>button{
    width:100%;
    background:#1565C0;
    color:white;
    font-size:22px;
    font-weight:bold;
    border-radius:10px;
    height:60px;
}

.stButton>button:hover{
    background:#0d47a1;
    color:white;
}

div[data-testid="stNumberInput"],
div[data-testid="stSelectbox"]{
    background:white;
    padding:5px;
    border-radius:10px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------
# Header
# ---------------------------------------

st.markdown("<div class='big-title'>Chronic Kidney Disease Prediction</div>",
            unsafe_allow_html=True)

st.markdown(
"<div class='sub-title'>Developed by <b>Muhammad Akhtar</div>",
unsafe_allow_html=True)

#st.divider()
st.subheader("Patient Details")
# ---------------------------------------
# Three Columns
# ---------------------------------------

col1, col2, col3 = st.columns(3)

with col1:



    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=48
    )

    bp = st.number_input(
        "Blood Pressure (Systolic)",
        min_value=10,
        max_value=300,
        value=80
    )

    sg = st.number_input(
        "Specific Gravity",
        min_value=1.005,
        value=1.020,
        format="%.3f"
    )

    al = st.number_input(
        "Albumin",
        min_value=0.0,
        value=1.0
    )

    hemo = st.number_input(
        "Hemoglobin",
        min_value=2.0,
        max_value=25.0,
        value=15.4
    )

    pcv = st.number_input(
        "Packed Cell Volume (PCV)",
        min_value=0.0,
        value=44.4
    )

    rc = st.number_input(
        "Red Blood Cell Count (RBC)",
        min_value=0.0,
        value=5.2
    )

with col2:
    bu = st.number_input(
        "Blood Urea",
        min_value=0.0,
        value=36.0
    )

    bgr = st.number_input(
        "Random Blood Glucose",
        min_value=0.0,
        value=121.0
    )

    sc = st.number_input(
        "Serum Creatinine",
        min_value=0.1,
        value=1.2
    )

    sod = st.number_input(
        "Sodium mEq/L",
        min_value=10.00 ,
        value=138.00
    )

    pot = st.number_input(
        "Potassium mEq/L",
        min_value=0.5,
        value=2.5
    )

    htn = st.selectbox(
        "Hypertension (High BP)",
        ["yes","no"]
    )





with col3:
    dm = st.selectbox(
        "Diabetes",
        ["yes", "no"]
    )
    cad = st.selectbox(
        "Coronary Artery Disease",
        ["yes","no"]
    )

    appet = st.selectbox(
        "Appetite",
        ["good","poor"]
    )

    pc = st.selectbox(
        "Protein in Urine",
        ["normal","abnormal"]
    )

    pe = st.selectbox(
        "Pedal Edema (Swelling of Feet)",
        ["no", "yes"]
    )
    ane = st.selectbox(
        "Aanemia",
        ["no", "yes"]
    )


st.markdown("<hr>", unsafe_allow_html=True)

# ---------------------------------------
 # Predict Button
# ---------------------------------------

if st.button("Predict Kidney Disease"):
    result = predict_kidney_disease(
        age,
        bp,
        sg,
        al,
        hemo,
        pcv,
        rc,
        bu,
        bgr,
        sc,
        sod,
        pot,
        htn,
        dm,
        cad,
        appet,
        pc,
        pe,
        ane
    )

    if result == 0:
        st.error(
            "Prediction: The patient is likely to have Chronic Kidney Disease."
        )
    else:
        st.success(
            "Prediction: The patient is NOT likely to have Chronic Kidney Disease."
        )

# ---------------------------------------
# Sample Data
# ---------------------------------------

st.divider()

with st.expander("Sample Data (Kidney Disease = YES)"):
    st.code("""
        48.0,	70.0,	1.005,	4.0,	11.2,	32,	3.9,	56.0,	117.0,	3.8,	111.0,	2.5,	yes,	no,	no,	poor,	abnormal,	yes,	yes	
        48.0,	70.0,	1.005,	4.0,	11.2,	32,	3.9,	56.0,	117.0,	3.8,	111.0,	2.5,	yes,	no,	no,	poor,	abnormal,	yes,	yes	
        """)

with st.expander("Sample Data (Kidney Disease = NO)"):
    st.code("""
        59.0,	100.0,	1.020,	4.0,	11.2,	30,	3.9,	40.0,	252.0,	3.2,	137.0,	4.7,	yes,	yes,	no,	    poor,	normal,	yes,	no
	    65.0,	80.0,	1.015,	0.0,	8.8,	25,	3.2,	37.0,	92.0,	1.5,	140.0,	5.2,	yes,	no,	    yes,	good,	normal,	yes,	no
        """)
