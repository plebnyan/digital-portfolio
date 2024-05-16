import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import base64


st.set_page_config(layout='wide',
                   page_title='Nyan Lynn Tun | Data Engineer',
                   page_icon=':coffee:')
html_code = """
    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="1dff6310-fd33-4f0a-b02c-0352559dbe6d" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>
    """

#st.write("##")
st.title("Nyan Lynn Tun | Data Engineering Portfolio")
st.write("### ")
st.write("### BI Developer/ Data Engineer")
st.markdown(
                """ 
                <p style="text-align:justify;">
                Experienced Data Engineer proficient in Python,SSIS,and Airflow working on Azure and AWS.
                Proficient in data modeling, database management, data governance and adept at building efficient ETL pipelines.
                Proven track record of delivering scalable solutions, translating business needs into effective data workflows for enhanced efficiency.
                </P>
                """,unsafe_allow_html=True)



st.write("____")

with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About','Projects','Contact'],
        icons=['person','code-slash','chat-left-text-fill'],
        orientation='horizontal'
    )
if selected == "About":

    with st.container():
        col1,col2 = st.columns([3,1])
        with col1:
            
            #st.write("### BI Developer/ Data Engineer")
            # st.markdown(
            #     """ 
            #     <p style="text-align:justify;">
            #     Experienced Data Engineer proficient in Python,SSIS,and Airflow working on Azure and AWS.
            #     Proficient in data modeling, database management, data governance and adept at building efficient ETL pipelines.
            #     Proven track record of delivering scalable solutions, translating business needs into effective data workflows for enhanced efficiency.
            #     </P>
            #     """,unsafe_allow_html=True)
            st.write("### Work Experiences")
            st.markdown("""
                <h5> Business Intelligence Developer @ City Holdings Limited | Yangon </h5>
                        """,unsafe_allow_html=True)
            st.markdown(" <b> From Sep-2023 - Present ",unsafe_allow_html=True)
            st.write("Responsibilities")
            st.markdown("""
                        <ul style="line-height: 1.5;">
                            <li>Responsible for building and maintaining data pipelines across different sectors.</li>
                            <li>Partially responsible for designing and building analytical data warehouse from scratch by collecting data from multiple sources.</li>
                            <li>Create and optimize downstream and upstream analytical data pipelines for multiple business reports.</li>
                            <li>Responsible for scheduling, orchestrating, and optimizing hundreds of multiple data pipelines.</li>
                            <li>Responsible for creating and updating data catalog, SOP, and ETL version control documentation.</li>
                            <li>Lead a team of 3 BI developers to re-design data architecture to ensure the single source of truth in multiple reports.</li>
                            <li>Enforce Power BI Developers to follow the standardized reporting framework.</li>
                            <li>Built Power BI dashboards and reports for certain departments.</li>
                            <li>Analyze and optimize Power BI data sources for the entire organization resulting in reducing significant data processing time.</li>
                        </ul>
                        """,unsafe_allow_html=True)
            st.markdown("""
                        <b> Tech Stack : SQL, Python, Airflow, SSIS, Power BI, Azure, AWS
                        """,unsafe_allow_html=True)
            
            st.write("-------------")
            st.markdown("""
                <h5> Data Analyst @ KBZ Bank (KBZ Pay) | Yangon </h5>
                        """,unsafe_allow_html=True)
            st.markdown(" <b> From Feb-2023 - Sep-2023 ",unsafe_allow_html=True)
            st.write("Responsibilities")
            st.markdown("""
                        <ul>
                            <li>Deliver weekly and monthly business insight reports to senior management, providing data-driven recommendations.</li>
                            <li>Create and maintain interactive Power BI, SQL, and Python dashboards to track KPIs in daily transactions.</li>
                            <li>Calculate and monitor incentives and commissions for KBZpay Agents and Merchants, ensuring accurate settlements and timely payouts.</li>
                            <li>Perform ad-hoc data analysis for various teams and departments, supporting business initiatives.</li>
                            <li>Collaborate with cross-functional teams to analyze and interpret complex datasets.</li>
                            <li>Manage databases, conduct SQL querying, and manipulate data for analysis and reporting.</li>
                            <li>Participate in project planning and execution to achieve objectives.</li>
                            <li>Designed and implemented a highly efficient local MS SQL data ecosystem, resulting in a significant reduction in team workload.</li>
                            <li>Successfully automated daily and weekly reports by creating robust data pipelines with Python and SQL, leading to enhanced operational efficiency.</li>
                            <li>Played a pivotal role in conducting crucial ad-hoc analytic projects to support internal decision-making, including a comprehensive feasibility study for the deployment of a new feature in the KBZPay app.</li>
                            <li>Fostered effective collaboration with an external data engineering team to ensure seamless data alignment across different departments, promoting better data integration and accuracy.</li>
                        </ul>

                        """,unsafe_allow_html=True)
            st.markdown("""
                        <b> Tech Stack : SQL, Python, Power BI, SSIS, Excel
                        """,unsafe_allow_html=True)
            
            st.write("-------------")
            st.markdown("""
                <h5> Data Analyst @ Million Mart Group | Yangon </h5>
                        """,unsafe_allow_html=True)
            st.markdown(" <b> From May-2021 to Jan-2023 ",unsafe_allow_html=True)
            st.write("Responsibilities")
            st.markdown("""
                        <ul>
                            <li>Extract and transform sales data from POS and ERP databases to analyze KPIs and metrics with Power BI and dashboards</li>
                            <li>Create daily, weekly, and monthly reports on sales trends and customer buying behavior.</li>
                            <li>Perform analysis on competitors' prices across the country to give useful insight to procurement department</li>
                            <li>Measure ongoing promotions performance with KPI and metrics</li>
                            <li>Generate sales forecasting reports for 30 retail outlets.</li>
                            <li>Perform complex SQL query to provide data requests from internal department or external vendors</li>
                        </ul>


                        """,unsafe_allow_html=True)
            st.markdown("""
                        <b> Tech Stack : SQL, Excel, Python, SAP
                        """,unsafe_allow_html=True)
if selected == "Projects":
    st.write("Projects will be here")
if selected == "Contact":
    st.write("contact info will be here")