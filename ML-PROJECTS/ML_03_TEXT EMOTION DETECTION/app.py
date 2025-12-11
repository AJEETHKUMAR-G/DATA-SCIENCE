import pandas as aju
import streamlit as st
import numpy as np
import altair as alt # This library is used for data visualization
import joblib

pipe_lr = joblib.load(open('model/text_emotion.pkl','rb'))

emoj = {"anger": "😠", "disgust": "🤮", "fear": "😨😱", "happy": "🤗", "joy": "😂", "neutral": "😐", "sad": "😔",
        "sadness": "😔", "shame": "😳", "surprise": "😮"}

def predict_emotions(texts):
    res = pipe_lr.predict([texts])
    return res[0]
def get_prediction_proba(texts):
    res = pipe_lr.predict_proba([texts])
    return res

def main():
    st.title("EMOTION DETECTION USING TEXT")
    st.subheader("Express your emotion in Text")

    with st.form(key = 'my_form'):
        raw_text = st.text_area("Type Here")
        submit_text = st.form_submit_button(label = 'Detect')

    if submit_text:
        col1,col2 = st.columns(2)
        prediction = predict_emotions(raw_text)
        probability = get_prediction_proba(raw_text)

        with col1:
            st.success("Original Text")
            st.write(raw_text)

            st.success("Prediction")
            emoj_icon = emoj[prediction]
            st.write("{}:{}".format(prediction,emoj_icon))
            st.write("confidence:{}".format(np.max(probability)))

        with col2:
            st.success("Prediction Probability")
            prob_df = aju.DataFrame(probability,columns=pipe_lr.classes_)
            prob_df_clean = prob_df.T.reset_index()
            prob_df_clean.columns = ["emotions", "probability"]

            fig = alt.Chart(prob_df_clean).mark_bar().encode(x='emotions', y='probability', color='emotions')
            st.altair_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()

