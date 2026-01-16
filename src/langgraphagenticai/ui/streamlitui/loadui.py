import streamlit as st
from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        # ---------- PAGE CONFIG ----------
        st.set_page_config(
            page_title=self.config.get_page_title(),
            page_icon="🤖",
            layout="wide",
            initial_sidebar_state="expanded"
        )

        # ---------- REFINED CSS (No Overlap) ----------
        st.markdown("""
            <style>
                /* Sidebar styling */
                [data-testid="stSidebar"] {
                    background-color: #ABABAB;
                }
                
                /* Selection Box Text & Dropdown Colors */
                div[data-baseweb="select"] > div {
                    background-color: #FFFFFF !important;
                    border: 1px solid #334155 !important;
                }
                
                /* Targeting the selected value text specifically */
                div[data-testid="stMarkdownContainer"] p {
                    word-wrap: break-word;
                }
                
                /* Ensure selectbox text is Blue */
                .stSelectbox div[data-testid="stMarkdownContainer"] {
                    color: #000000 !important;
                }

                /* Cleaner Labels without negative margins */
                .sidebar-label {
                    font-size: 0.7rem;
                    text-transform: uppercase;
                    letter-spacing: 0.08rem;
                    color: #000000;
                    margin-bottom: 4px; /* Space between label and widget */
                    font-weight: 600;
                }

                /* API Input styling */
                div[data-testid="stTextInput"] input {
                    background-color: #FFFFFF !important;
                    color: #000000 !important;
                    border: 1px solid #000000 !important;
                }
            </style>
        """, unsafe_allow_html=True)

        # ---------- MAIN HEADER ----------
        st.markdown(f'<h1 style="color:#1e293b; font-weight:800; margin-bottom:0;">{self.config.get_page_title()}</h1>', unsafe_allow_html=True)
        st.divider()

        # ---------- SIDEBAR ----------
        with st.sidebar:
            st.markdown("<h2 style='color:#000000; margin-top:0;'>Settings</h2>", unsafe_allow_html=True)
            st.markdown("<p style='color:#000000; font-size:0.85rem; margin-top:-15px;'>Manage AI parameters</p>", unsafe_allow_html=True)
            
            #st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)

            # ---------- LLM PROVIDER ----------
            st.markdown('<p class="sidebar-label">LLM Provider</p>', unsafe_allow_html=True)
            llm_options = self.config.get_llm_options()
            self.user_controls["selected_llm"] = st.selectbox(
                "LLM Provider",
                llm_options,
                label_visibility="collapsed",
                key="llm_box"
            )

            # ---------- DYNAMIC CONFIG ----------
            if self.user_controls["selected_llm"] == "Groq":
                st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
                
                st.markdown('<p class="sidebar-label">Select Model</p>', unsafe_allow_html=True)
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox(
                    "Model",
                    model_options,
                    label_visibility="collapsed",
                    key="model_box"
                )

                st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
                
                st.markdown('<p class="sidebar-label">API Access Key</p>', unsafe_allow_html=True)
                self.user_controls["GROQ_API_KEY"] = st.text_input(
                    "API Key",
                    type="password",
                    placeholder="Enter Key...",
                    label_visibility="collapsed",
                    key="api_box"
                )
                
                st.session_state["GROQ_API_KEY"] = self.user_controls["GROQ_API_KEY"]

                if self.user_controls["GROQ_API_KEY"]:
                    st.markdown("<p style='color:#4ade80; font-size:11px; margin-top:5px;'>● Authenticated</p>", unsafe_allow_html=True)
                else:
                    st.markdown("<p style='color:#f87171; font-size:11px; margin-top:5px;'>○ Key Required</p>", unsafe_allow_html=True)

            #st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)

            # ---------- USE CASE ----------
            st.markdown('<p class="sidebar-label">Active Workstream</p>', unsafe_allow_html=True)
            usecase_options = self.config.get_usecase_options()
            self.user_controls["selected_usecase"] = st.selectbox(
                "Use Case",
                usecase_options,
                label_visibility="collapsed",
                key="usecase_box"
            )

            # Dynamic Footer Spacer
            st.markdown("<div style='height: 20vh;'></div>", unsafe_allow_html=True)
            st.markdown("<p style='font-size:0.7rem; color:#475569; text-align:center; border-top: 0.5px solid #334155; padding-top:20px;'>SYSTEM CORE v1.0</p>", unsafe_allow_html=True)

        return self.user_controls