import streamlit as st

# Using st.form to create a form
with st.form("chat_form"):
    # HTML content for the form layout with color styling and borders
    st.markdown(
        '''
        <style>
        .form-label {
            color: #007acc;
            font-weight: bold;
        }
        .form-section {
            color: #007acc;
            font-weight: bold;
        }
        .checkbox-label {
            color: #007acc;
        }
        .pain-slider, .other-symptoms {
            color: #007acc;
        }
        input[type="text"], select, textarea {
            border: 2px solid #007acc;
            border-radius: 4px;
            padding: 8px;
            width: 100%;
            box-sizing: border-box;
            margin-bottom: 10px;
        }
        input[type="checkbox"] {
            accent-color: #007acc;
            margin-right: 5px;
        }
        .submit-button {
            color: #007acc;
            background-color: white;
            border: 2px solid #007acc;
            border-radius: 4px;
            padding: 10px 20px;
            cursor: pointer;
        }
        .submit-button:hover {
            background-color: #007acc;
            color: white;
        }
        .form-container {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .submit-container {
            display: flex;
            justify-content: flex-end;
        }
        </style>
        <div class="form-container">
            <table style="width: 100%; border-spacing: 10px;">
                <!-- Patient Info Row -->
                <tr>
                    <td style="width: 33%;">
                        <label class="form-label" for="patient_name">Patient Name:</label>
                        <input type="text" id="patient_name" name="patient_name"/>
                    </td>
                    <td style="width: 33%;">
                        <label class="form-label" for="patient_age">Patient Age:</label>
                        <input type="text" id="patient_age" name="patient_age"/>
                    </td>
                    <td style="width: 33%;">
                        <label class="form-label" for="patient_gender">Patient Gender:</label>
                        <select id="patient_gender" name="patient_gender">
                            <option value="Male">Male</option>
                            <option value="Female">Female</option>
                            <option value="Other">Other</option>
                        </select>
                    </td>
                </tr>
                <!-- Symptom Details Row -->
                <tr>
                    <td colspan="3">
                        <div class="form-section">Respiratory Symptoms</div>
                        <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                            <div style="flex: 1;">
                                <input type="checkbox" id="cough" name="cough">
                                <label class="checkbox-label" for="cough">Cough</label>
                            </div>
                            <div style="flex: 1;">
                                <input type="checkbox" id="shortness_of_breath" name="shortness_of_breath">
                                <label class="checkbox-label" for="shortness_of_breath">Shortness of Breath</label>
                            </div>
                            <div style="flex: 1;">
                                <input type="checkbox" id="chest_pain" name="chest_pain">
                                <label class="checkbox-label" for="chest_pain">Chest Pain</label>
                            </div>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td colspan="3">
                        <div class="form-section">Digestive Symptoms</div>
                        <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                            <div style="flex: 1;">
                                <input type="checkbox" id="nausea" name="nausea">
                                <label class="checkbox-label" for="nausea">Nausea</label>
                            </div>
                            <div style="flex: 1;">
                                <input type="checkbox" id="vomiting" name="vomiting">
                                <label class="checkbox-label" for="vomiting">Vomiting</label>
                            </div>
                            <div style="flex: 1;">
                                <input type="checkbox" id="diarrhea" name="diarrhea">
                                <label class="checkbox-label" for="diarrhea">Diarrhea</label>
                            </div>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td colspan="3">
                        <div class="form-section">General Symptoms</div>
                        <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                            <div style="flex: 1;">
                                <input type="checkbox" id="fever" name="fever">
                                <label class="checkbox-label" for="fever">Fever</label>
                            </div>
                            <div style="flex: 1;">
                                <input type="checkbox" id="fatigue" name="fatigue">
                                <label class="checkbox-label" for="fatigue">Fatigue</label>
                            </div>
                            <div style="flex: 1;">
                                <input type="checkbox" id="headache" name="headache">
                                <label class="checkbox-label" for="headache">Headache</label>
                            </div>
                        </div>
                    </td>
                </tr>
                <!-- Additional Row for Pain Level and Other Symptoms -->
                <tr>
                    <td colspan="3">
                        <div class="pain-slider">Pain Level</div>
                        <input type="range" id="pain_level" name="pain_level" min="0" max="10" value="0" style="width: 100%;"/>
                        <label for="pain_level">Pain Level (0-10)</label>
                    </td>
                </tr>
                <tr>
                    <td colspan="3">
                        <div class="other-symptoms">Other Symptoms</div>
                        <textarea id="other_symptoms" name="other_symptoms" rows="3"></textarea>
                    </td>
                </tr>
            </table>
            <!-- Submit Button -->
            <div class="submit-container">
                <!-- Only the Streamlit submit button is included here -->
                <!-- st.form_submit_button will render the button -->
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    # Submit button inside the form
    submitted = st.form_submit_button("Send")

# Handle form submission
if submitted:
    # Retrieve values from all components
    st.write("Patient Name:", st.session_state.get("patient_name", ""))
    st.write("Patient Age:", st.session_state.get("patient_age", ""))
    st.write("Patient Gender:", st.session_state.get("patient_gender", ""))
    st.write("Cough:", st.session_state.get("cough", False))
    st.write("Shortness of Breath:", st.session_state.get("shortness_of_breath", False))
    st.write("Chest Pain:", st.session_state.get("chest_pain", False))
    st.write("Nausea:", st.session_state.get("nausea", False))
    st.write("Vomiting:", st.session_state.get("vomiting", False))
    st.write("Diarrhea:", st.session_state.get("diarrhea", False))
    st.write("Fever:", st.session_state.get("fever", False))
    st.write("Fatigue:", st.session_state.get("fatigue", False))
    st.write("Headache:", st.session_state.get("headache", False))
    st.write("Other Symptoms:", st.session_state.get("other_symptoms", ""))
    st.write("Pain Level:", st.session_state.get("pain_level", 0))
