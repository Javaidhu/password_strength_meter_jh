import streamlit as st
import re

# 🛡️ Page Configuration
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")

# 🔒 Title
st.title("🔑 Password Strength Meter")
st.markdown("Welcome to the **Password Strength Meter!** Enter your password below to check its strength. 🚀")

# 📝 Password Input
password = st.text_input("🔐 Enter your password", type="password")

# 📌 Strength Analysis
feedback = []
score = 0

if password:
    # Check password length
    if len(password) < 8:
        feedback.append("❌ Password should be at least **8 characters long**.")
    else:
        score += 1

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one uppercase letter** (A-Z).")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one lowercase letter** (a-z).")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one digit** (0-9).")

    # Check for special characters
    if re.search(r'[@$!%*?&]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one special character** (@, $, !, %, *, ?, &).")

    # 💪 Strength Evaluation
    if score == 5:
        st.success("✅ **Strong Password!** 🔥 Your password is secure.")
    elif score == 4:
        st.warning("⚠️ **Moderate Password.** Consider adding more complexity.")
    else:
        st.error("❌ **Weak Password!** Please improve your password.")

    # 💡 Display Suggestions
    if feedback:
        st.markdown("### 💡 Password Suggestions:")
        for item in feedback:
            st.write(f"- {item}")

else:
    st.info("🔹 **Enter a password to check its strength!**")
