import streamlit as st

def main():
    
    st.markdown(
        """
        <style>
            .main {
                background-color: #f2f2f2;
                text-align: justify;
                text-align: -webkit-center;
                text-align: -moz-center;
                text-align: center;
                padding: 10px;
            }
            .title {
                color: #008080;
                font-size: 25px;
                transition: transform 0.1s;
            }
            .title:hover {
                transform: scale(1.1);
            }
            .image {
                border-radius: 50%;
                width: 150px;
                height: 150px;
                object-fit: cover;
                transition: transform 0.5s;
            }
            .image:hover {
                transform: rotate(360deg);
            }
            .navigation {
                display: flex;
                justify-content: center;
                padding: 10px;
                transition: transform 0.5s;
            }
            .navigation:hover {
                transform: scale(1.1);
            }
            .navigation a {
                padding: 0 20px;
                text-decoration: none;
                color: #008080;
                font-size: 12px;
                cursor: pointer;
                transition: color 0.1s;
            }
            .navigation a:hover {
                color: #ff4500;
            }
            .project {
                padding: 30px;
                margin: 10px;
                background-color: #ffffff;
                border-radius: 5px;
                transition: transform 0.5s;
            }
            .project:hover {
                transform: scale(1.1);
            }
            .button {
                display: inline-block;
                padding: 10px 20px;
                margin: 10px;
                background-color: skyblue;
                color: #ffffff;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                text-decoration: none;
                transition: background-color 0.5s;
            }
            .button:hover {
                background-color: #008080;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="main">
            <h2 class="title">Welcome to My Portofolio</h2>
            <div class="navigation">
                <a href="#home">Home</a>
                <a href="#about">About Me</a>
                <a href="#contact">Contact</a>
                <a href="#projects">Projects</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="main" id="home">
            <h3></h3>
            <img class="image" src="https://lh3.googleusercontent.com/a/ACg8ocI9zdpXHBgAuxaYJ_87083DQ10epjpIh0896lJr0se-WCM=s288-c-no" alt="Soni Agung Wahyudiyanta">
            <h3 style="font-size:12px;">Soni Agung Wahyudiyanta</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="main" id="about">
            <h3>About Me</h3>
            <p style ="text-align: justify;">I am dedicated to honing my data analysis skills through web research, forum engagement, and self-directed learning, alongside hands-on experience gained from boot camps. Proficient in Production Planning Control (PPC), I excel in leveraging MS Excel for precise production forecasting and scheduling. As an industrious student at Pelita Bangsa University, pursuing Industrial Engineering, I blend theoretical knowledge with practical insights, fostering a promising career trajectory.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="main" id="contact">
            <h3>Contact</h3>
            <p>WhatsApp: <a href="https://wa.link/kssl0s">0859-4377-1157</a></p>
            <p>Email: <a href="mailto:sonyagung308@gmail.com">sonyagung308@gmail.com</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="main" id="projects">
            <h3>Projects</h3>
            <div class="project">
                <h4 style="font-size:18px;">Bank Customer Churn Prediction | EDA | Machine Learning</h4>
                <p>This project focuses on predicting customer churn in the banking sector using machine learning techniques. It involves data preprocessing, exploratory data analysis, and building predictive models.</p>
                <img class="image" src="data:image/jpeg;base64,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" alt="Bank Customer Churn Prediction">
                <a class="button" href="https://github.com/Sony-Agung/bankcustomer-churn/blob/main/Final_Project_Bank_Customer_Churn_Prediction%20(1).ipynb">View Project</a>
                <a class="button" href="https://bankcustomer-churn.streamlit.app/">Application</a>
            </div>
        </div>

         <div class="main" id="">
            <h3></h3>
            <div class="project">
                <h4 style="font-size:18px;">Analisis Ergonomi dalam Proses Produksi Machining untuk Meningkatkan Efisiensi | EDA | Machine Learning</h4>
                <p>Topik ini berkaitan dengan penelitian tentang bagaimana penerapan prinsip ergonomi dapat meningkatkan efisiensi dan produktivitas dalam proses produksi mesin. Analisis Data Eksploratori (EDA) dan pembelajaran mesin (Machine Learning) dapat membantu mengidentifikasi pola-pola yang relevan dan memprediksi solusi ergonomi yang optimal</p>
                <img class="image" src="https://soloabadi.com/wp-content/uploads/2020/08/operator-cnc.jpg" alt="Bank Customer Churn Prediction">
                <a class="button" href="https://github.com/Sony-Agung/predict_ergo/blob/main/Analisis%20Ergonomi%20dalam%20Proses%20Produksi%20Machining%20untuk%20Meningkatkan%20Efisiensi.ipynb">View Project</a>
                <a class="button" href="https://prediksi-ergo.streamlit.app/">Application</a>
            </div>
        </div>

        <div class="main" id="">
            <h3></h3>
            <div class="project">
                <h4 style="font-size:18px;">Predict Student Exam | EDA | Machine Learning</h4>
                <p>This topic involves researching how certain factors can influence student exam outcomes. EDA is used to understand patterns in student data, while machine learning is used to create a predictive model for student performance based on relevant factors.</p>
                <img class="image" src="data:image/jpeg;base64,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" alt="Bank Customer Churn Prediction">
                <a class="button" href="https://github.com/Sony-Agung/predict-students-exam/blob/main/app.py">View Project</a>
                <a class="button" href="https://predict-students-exam.streamlit.app/">Application</a>
            </div>
        </div>

         <div class="main" id="">
            <h3></h3>
            <div class="project">
                <h4 style="font-size:18px;">Kesejahteraan Pekerja Indonesia | EDA</h4>
                <p>Penelitian ini berfokus pada analisis data eksploratori untuk memahami faktor-faktor yang memengaruhi kesejahteraan pekerja di Indonesia. EDA digunakan untuk menganalisis data sosial-ekonomi dan demografi yang berkontribusi terhadap kesejahteraan pekerja.</p>
                <img class="image" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0j7IKEbAfwWKeM4uCbDSGtJAKxb1u5Nuf4g&usqp=CAU" alt="Bank Customer Churn Prediction">
                <a class="button" href="https://github.com/Sony-Agung/projek/blob/main/Kesejahteraan_Pekerja_Indonesia.ipynb">View Project</a>
            </div>
        </div>

        <div class="main" id="">
            <h3></h3>
            <div class="project">
                <h4 style="font-size:18px;">Tingkat Penganggur Terbuka Berdasarkan Pendidikan di Jawa Barat | EDA   </h4>
                <p>Penelitian ini bertujuan untuk menganalisis tingkat pengangguran terbuka di Jawa Barat berdasarkan tingkat pendidikan. EDA digunakan untuk memahami hubungan antara tingkat pendidikan dan tingkat pengangguran serta faktor-faktor lain yang memengaruhinya.</p>
                <img class="image" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRIu5yRPHVODTSn4ptiKp5W4NK4kY2C8VxqQ&usqp=CAU" alt="Bank Customer Churn Prediction">
                <a class="button" href="https://github.com/Sony-Agung/projek/blob/main/Tingkat%20Penganggur%20Terbuka%20Berdasarkan%20Pendidikan%20di%20Jawa%20Barat.ipynb">View Project</a>
            </div>
      

        <div class="main" id="">
            <h3></h3>
            <div class="project">
                <h4 style="font-size:18px;">HR Dataset | SVM | Machine Learning Supervised</h4>
                <p>The HR dataset is used to build a predictive model using the SVM method in supervised machine learning. The goal is to classify HR data to identify patterns in employee recruitment, development, and retention.</p>
                <img class="image" src="data:image/png;base64,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" alt="Bank Customer Churn Prediction">
                <a class="button" href="https://github.com/Sony-Agung/projek/blob/main/Supervised%20II%20(svm)%20binary(yes%20or%20true).ipynb">View Project</a>
            </div>
        </div>

        <div class="main" id="">
            <h3></h3>
            <div class="project">
                <h4 style="font-size:18px;">Mall Customers | K-means | Unsupervised Machine Learning</h4>
                <p>Mall customer analysis using the K-means algorithm in unsupervised machine learning. The goal is to cluster customers based on shopping behavior and preferences, enabling the implementation of appropriate marketing strategie.</p>
                <img class="image" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfD8dGHu9SOJYuvoK5ZX26NUCEege9Kcw9UQ&usqp=CAU" alt="Bank Customer Churn Prediction">
                <a class="button" href="https://github.com/Sony-Agung/projek/blob/main/unsupervised%20I.ipynb">View Project</a>
            </div>
        </div>

        <div class="main" id="">
            <h3></h3>
            <div class="project">
                <h4 style="font-size:18px;">Credit card Details Binary Classification Problem | EDA | Machine Learning</h4>
                <p>The binary classification problem on credit card data utilizes EDA to analyze credit card spending patterns and payment behavior. Machine learning is used to create a predictive model to identify the risk of fraud or payment delays.</p>
                <img class="image" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbgI4RGuNmo2O0N6RRAR8-rvngP756Vdn5CA&usqp=CAU" alt="Bank Customer Churn Prediction">
                <a class="button" href="https://github.com/Sony-Agung/projek/blob/main/Credit%20card%20Details%20Binary%20Classification%20Problem.ipynb">View Project</a>
            </div>
        </div>

         <div class="main" id="">
            <h3></h3>
            <div class="project">
                <h4 style="font-size:18px;">Analisa Penjualan Sederhana | EDA |</h4>
                <p></p>
                <img class="image" src="https://lh4.googleusercontent.com/3_jziqRe4bEt86rFULiogTCkHMHqlGAGhcb-tfkMv1VA7d0SiDznagdbX9sgcYnuV_m4jsmiY9nmHjyHBLFLDhukkxVCpePcNmR8TizcuVhdCOCP5XVtGNoGrkLdg-tF8I4FO8bN" alt="Bank Customer Churn Prediction">
                <a class="button" href="https://github.com/Sony-Agung/projek/blob/main/Analisa%20Penjualan%20Sederhana.ipynb">View Project</a>
            </div>
        </div>

        <div class="main" id="">
            <h3></h3>
            <div class="project">
                <h4 style="font-size:18px;">KORBAN TEWAS DALAM KONFLIK ISRAEL - PALESTINA (2000 - 2023) | EDA |</h4>
                <p></p>
                <img class="image" src="https://static.promediateknologi.id/crop/0x0:0x0/0x0/webp/photo/jawapos/2023/02/Bendera-Palestina-dan-Israel-iStock.jpg" alt="Bank Customer Churn Prediction">
                <a class="button" href="https://github.com/Sony-Agung/projek/blob/main/KORBAN_TEWAS_DALAM_KONFLIK_ISRAEL_PALESTINA_2000_2023.ipynb">View Project</a>
            </div>
        </div>
        <div class="main" id="">
            <h3></h3>
            <div class="project">
                <h4 style="font-size:18px;">Daya Tampung Universitas 2018 - 2023 | EDA |</h4>
                <p></p>
                <img class="image" src="https://disk.mediaindonesia.com/thumbs/1800x1200/news/2020/10/1f35a6e4dc44b9ac053963322b153631.jpg" alt="Bank Customer Churn Prediction">
                <a class="button" href="https://github.com/Sony-Agung/projek/blob/main/Daya_Tampung_Universitas%20(2).ipynb">View Project</a>
            </div>
        </div>

    
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
