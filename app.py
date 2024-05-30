import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import base64

st.set_page_config(layout='wide',
                   page_title='Nyan Lynn Tun | Data Engineer',
                   page_icon=':male-technologist:')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")

st.title("Nyan Lynn Tun | Data Engineering Portfolio")
st.write("### BI Developer/ Data Engineer")
st.markdown(
    """ 
    <p style="text-align:justify;">
    Experienced Data Engineer proficient in Python, SSIS, and Airflow working on Azure and AWS.
    Proficient in data modeling, database management, data governance and adept at building efficient ETL pipelines.
    Proven track record of delivering scalable solutions, translating business needs into effective data workflows for enhanced efficiency.
    </p>
    """, unsafe_allow_html=True
)

st.write("____")
st.markdown("Reach out to me via the following channels: ")
with st.container():
    linkedIn,g_hub,email,ph_no,i=st.columns([1,1,1,1,8])
    with linkedIn:
        st.markdown(
    """<a href="https://www.linkedin.com/in/nyan-lynn-tun-a6aa2a1aa/">
    <img src="data:image/png;base64,{}" width="50">
    </a>""".format(
        base64.b64encode(open("animations/linkedin.1024x1024-2.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
    with g_hub:
        st.markdown(
    """<a href="https://github.com/plebnyan">
    <img src="data:image/png;base64,{}" width="50">
    </a>""".format(
        base64.b64encode(open("animations/github-6980894_1280.webp", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
    with email:
        st.markdown(
    """<a href="mailto:nlt1166@outlook.com">
    <img src="data:image/png;base64,{}" width="50">
    </a>""".format(
        base64.b64encode(open("animations/email-2.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
        
st.write("____")

with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About Me', 'Projects', 'Contact'],
        icons=['person', 'code-slash', 'chat-left-text-fill'],
        orientation='horizontal'
    )

if selected == "About Me":
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write("### Work Experiences")
            st.markdown(
                """
                <h5>Business Intelligence Developer <br> City Holdings Limited | Yangon</h5>
                """, unsafe_allow_html=True
            )
            st.markdown("<b> From Sep-2023 - Present </b>", unsafe_allow_html=True)
            st.write("Responsibilities")
            st.markdown(
                """
                <ul style="line-height: 1.5;">
                    <li>Deliver regular business insight reports with data-driven recommendations to senior management.</li>
                    <li>Develop and maintain interactive dashboards using Power BI, SQL, and Python to track KPIs and transactions.</li>
                    <li>Manage incentives and commissions for KBZpay Agents and Merchants, ensuring accuracy and timely payouts.</li>
                    <li>Conduct ad-hoc data analysis, collaborate across teams, and participate in projects to support business goals.</li>
                    <li>Implement efficient data ecosystems, automate reporting processes, and facilitate collaboration with external data teams for better integration and accuracy.</li>
                </ul>
                """, unsafe_allow_html=True
            )
            st.markdown("<b>Tech Stack : SQL, Python, Airflow, SSIS, Power BI, Azure, AWS</b>", unsafe_allow_html=True)
            
            st.write("-------------")
            st.markdown(
                """
                <h5>Data Analyst <br>  KBZ Bank (KBZ Pay) | Yangon</h5>
                """, unsafe_allow_html=True
            )
            st.markdown("<b>From Feb-2023 - Sep-2023</b>", unsafe_allow_html=True)
            st.write("Responsibilities")
            st.markdown(
                """
                <ul>
                    <li>Deliver business insight reports with data-driven recommendations to senior management.</li>
                    <li>Create and maintain interactive dashboards to track transaction KPIs.</li>
                    <li>Calculate and monitor incentives and commissions for KBZpay Agents and Merchants.</li>
                    <li>Perform ad-hoc data analysis to support various business initiatives.</li>
                    <li>Collaborate with cross-functional teams to analyze complex datasets.</li>
                                    </ul>
                """, unsafe_allow_html=True
            )
            st.markdown("<b>Tech Stack : SQL, Python, Power BI, SSIS, Excel</b>", unsafe_allow_html=True)
            
            st.write("-------------")
            st.markdown(
                """
                <h5>Data Analyst <br> Million Mart Group | Yangon</h5>
                """, unsafe_allow_html=True
            )
            st.markdown("<b>From May-2021 to Jan-2023</b>", unsafe_allow_html=True)
            st.write("Responsibilities")
            st.markdown(
                """
                <ul>
                    <li>Extract and transform sales data from POS and ERP databases to analyze KPIs and metrics with Power BI and dashboards</li>
                    <li>Create daily, weekly, and monthly reports on sales trends and customer buying behavior.</li>
                    <li>Perform analysis on competitors' prices across the country to give useful insight to procurement department</li>
                    <li>Measure ongoing promotions performance with KPI and metrics</li>
                    <li>Generate sales forecasting reports for 30 retail outlets.</li>
                    <li>Perform complex SQL query to provide data requests from internal department or external vendors</li>
                </ul>
                """, unsafe_allow_html=True
            )
            st.markdown("<b>Tech Stack : SQL, Excel, Python, SAP</b>", unsafe_allow_html=True)

if selected == "Projects":
    st.write("---")
    st.markdown("""
                <h3>Building a webscraping Pipeline</h3>
                """, unsafe_allow_html=True)
    st.markdown("""
<h5>Project Description</h5>
<p>I scrapped data from https://www.jobnet.com.mm/ using Python and embedded in Apache Airflow pipeline and stored the output csv files in AWS S3 Bucket then insert it into a Postgre DB to save historical data and serve as a data source for an analytic dashboard.<p>
<h5>Tools & AWS Services Used in this Project </h5> 
<p>For scripting language, I used python to utalize BS4, pandas and request libraries to extract publically available data from the jobnet.com. </p>
""",unsafe_allow_html=True)
    st.markdown(""" 
<h5><a href="https://github.com/plebnyan/job-net-pipeline-portfolio">Visit Github Repo</a></h5>

""",unsafe_allow_html=True)
    st.write("---")
    st.markdown("""
                <h3>Japan Visa Application Analysis Pipeline with Spark on Azure</h3>
                """, unsafe_allow_html=True)
    
    st.markdown("""
<h5>Project Description</h5>
<p>The data set used in this project is Kaggle Japanese Visa Application. I processed the flat file (csv) on the Spark Cluster which is hosted on Azure VM.
    The data cleaning include changing countrie names to international standard, cleaning null values using pySpark. Then create visualization using plotly to share the insight extracted from the dataset.<p>
<h5>Tech stack used in this project</h5> 
<p>pySpark, python, Azure VM, Docker </p>
""",unsafe_allow_html=True)
    st.markdown(""" 
<h5><a href="https://github.com/plebnyan/azure-spark-cluster-de-project/tree/master">Visit Github Repo</a></h5>

""",unsafe_allow_html=True)
if selected == "Contact":
    st.write("Contact info will be here")
