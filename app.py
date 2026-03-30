import streamlit as st
import random
import string

# --- Core Functions ---
def generate_keys():
    """Generates and saves a new set of cipher keys to the session state."""
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars_list = list(chars)
    key_list = chars_list.copy()
    random.shuffle(key_list)
    
    st.session_state['chars'] = chars_list
    st.session_state['key'] = key_list

def encrypt(message, chars, key):
    """Encrypts the message using the current key."""
    encrypted_message = ""
    for char in message:
        if char in chars:
            index = chars.index(char)
            encrypted_message += key[index]
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(encrypted_message, chars, key):
    """Decrypts the message using the current key."""
    decrypted_message = ""
    for char in encrypted_message:
        if char in key:
            index = key.index(char)
            decrypted_message += chars[index]
        else:
            decrypted_message += char
    return decrypted_message

# --- App Initialization ---
# This ensures the key is only generated once when the app first loads,
# unless the user explicitly clicks the "Generate New Key" button.
if 'chars' not in st.session_state or 'key' not in st.session_state:
    generate_keys()

# --- Streamlit UI ---
st.title("🔐 Secret Message App")
st.write("Welcome to the Encrypting & Decrypting Messages program!")

# UI: Key Management
st.write("---")
if st.button("Generate New Random Key"):
    generate_keys()
    st.success("A new secret key has been generated!")

# UI: Show the mapping so the user can see what is happening under the hood
with st.expander("View Current Cipher Key"):
    # Joining the lists into strings makes them easier to read on screen
    st.text(f"Original: {''.join(st.session_state['chars'])}")
    st.text(f"Secret:   {''.join(st.session_state['key'])}")

st.write("---")

# UI: User Inputs
mode = st.radio("What would you like to do?", ("Encrypt", "Decrypt"))
message = st.text_area(f"Enter the message to {mode.lower()}:")

# UI: Process and Output
if message:
    if mode == "Encrypt":
        result = encrypt(message, st.session_state['chars'], st.session_state['key'])
        st.subheader("Encrypted Message:")
        st.code(result) # Displayed as code so it's easy to copy
    elif mode == "Decrypt":
        result = decrypt(message, st.session_state['chars'], st.session_state['key'])
        st.subheader("Decrypted Message:")
        st.code(result)