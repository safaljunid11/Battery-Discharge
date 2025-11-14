#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

st.set_page_config(page_title="Battery Discharge Test", page_icon="🔋")

st.title("🔋 Battery Discharge Test Analysis")

st.write("This tool helps determine the health and standby status of a battery bank based on test parameters.")

# --- Actual Discharge Duration (Dropdown in minutes/hours) ---

options = {
    "0 minutes": 0.0,
    "30 minutes": 0.5,
    "1 hour": 1.0,
    "1 hour 30 minutes": 1.5,
    "2 hours": 2.0,
    "2 hours 30 minutes": 2.5,
    "3 hours": 3.0,
    "3 hours 30 minutes": 3.5,
    "4 hours": 4.0,
    "4 hours 30 minutes": 4.5,
    "5 hours": 5.0
}




# --- User Inputs ---
selected_label = st.selectbox("Actual Discharge Duration", list(options.keys()))
a1 = options[selected_label] 
a2 = st.number_input("Rated Battery Capacity (Ah)", min_value=0.0, step=0.1)
a3 = st.number_input("Load Current per Charger (A)", min_value=0.0, step=0.1)

if st.button("Calculate"):
    if a3 == 0:
        st.error("Load Current (A) cannot be zero.")
    elif a1 > 5:
        st.error("Wrong Input: Discharge duration must be 5 hours or less.")
    else:
        d1 = a1 / 5
        s1 = (a2 / a3) * d1

        st.subheader("Results")
        st.write(f"**Discharge Test Ratio:** {d1:.2f}")
        st.write(f"**Standby Time:** {s1:.2f} hours")

        # --- Conditions and Actions ---
        if d1 < 0.8 and s1 >= 8:
            st.warning("Battery bank is unhealthy but standby time is acceptable.")
            st.info("""
            **Action:**
            1. Replace bank battery once average conductance ≤ 60%.
            2. Replace battery bank to be scrapped.
            """)

        elif d1 < 0.8 and s1 < 8:
            st.error("Battery bank is unhealthy and standby time is unacceptable.")
            st.info("""
            **Action:**
            1. Replace battery bank immediately.
            2. Replace battery bank to be scrapped.
            """)

        elif d1 >= 0.8 and s1 >= 8:
            st.success("Battery bank is healthy and standby time is acceptable.")
            st.info("""
            **Action:**
            1. Continue battery bank maintenance as per the maintenance schedule.
            """)

        elif d1 >= 0.8 and s1 < 8:
            st.warning("Battery bank is healthy but standby time is unacceptable.")
            st.info("""
            **Action:**
            1. Replace battery bank with higher capacity battery.
            2. Replace battery bank to be relocated.
            """)

            


# In[ ]:




