# ⚽ Football Data Dashboard

An interactive and data-driven web application that provides insights into football competition standings and top scorers. Built using Python, Streamlit, and Matplotlib, this dashboard allows users to explore key football statistics interactively.

---

## 🚀 **Project Overview**

This project fetches real-time football data from the **Football-Data.org API** and presents it in an engaging dashboard. Users can:

- View **competition standings** with details like points, goals scored, goals conceded, and goal difference.
- Explore **top goal scorers** and their performance statistics.
- Analyze **key insights** such as top attacking teams, top defensive teams, and efficient players.
- Interact with dynamic **visualizations**.

---

## 📊 **Features**

### 🏆 **Competition Standings**
- View the standings of teams in a competition.
- Analyze:
   - **Top 10 Teams by Points**
   - **Top 5 Defensive Teams**
   - **Top 5 Attacking Teams**
   - **Top 5 Teams by Points per Game**

### 👟 **Top Scorers**
- Explore top-performing players.
- Analyze:
   - **Top 5 Goal Scorers**
   - **Top 5 Assisters**
   - **Top 5 Players by Goals per Match**

### 📈 **Dynamic Visualizations**
- Bar charts for team and player statistics.
- Scatter plots for goals vs matches played and goals scored vs goals conceded.

---

## 🛠️ **Tech Stack**

- **Python:** Core programming language.
- **Streamlit:** For building an interactive web dashboard.
- **Pandas:** For data manipulation and analysis.
- **Matplotlib:** For creating visualizations.
- **Requests:** For interacting with the Football-Data.org API.

---

## ⚙️ **Setup and Installation**

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-username/football-dashboard.git
cd football-dashboard
```

2️⃣ Install Dependencies
Make sure you have Python installed. Then, run:

```bash
pip install -r requirements.txt
```

3️⃣ Fetch Data
Run the data-fetching script to save the latest football data:

```bash
python fetch_football_data.py
```

This will generate two CSV files:
standings_data.csv
scorers_data.csv

4️⃣ Run the Dashboard
Start the Streamlit app:

```bash
streamlit run football_dashboard.py
```

5️⃣ Open in Your Browser
The app will open in your default browser at:

```arduino
http://localhost:8501
```

---

## 🌐 **Deployment on Streamlit Cloud**

To make the app publicly accessible:

1. Push your project to GitHub.
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud).
3. Connect your repository and deploy.

---

## 📂 **Project Structure**
```bash
football-dashboard/
│
├── fetch_football_data.py   # Fetches data from the API
├── football_dashboard.py    # Streamlit dashboard script
├── standings_data.csv       # Standings dataset (auto-generated)
├── scorers_data.csv         # Scorers dataset (auto-generated)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🧠 **How It Works**

### Data Fetching:
- API calls fetch competition standings and top scorers.
- Data is saved locally in CSV files.

### Data Visualization:
- Matplotlib creates charts for team and player performance.

### Interactive Dashboard:
- Streamlit dynamically displays charts and tables.

---

## ✅ **Future Enhancements**
- Add more detailed player analytics.
- Introduce filters for competitions and teams.
- Include historical data comparisons.

---

## 🧑‍💻 **Contributing**
Feel free to fork this project, open issues, and submit pull requests for any contributions or improvements!

---

## 📄 **License**
This project is licensed under the MIT License.

---

## 📬 **Contact**
- **Name:** Atharv Raotole
- **Email:** atharva.r29@gmail.com
- **GitHub:** [AtharvRaotole](https://github.com/AtharvRaotole)

Feel free to reach out with questions, feedback, or collaboration opportunities!

⭐ If You Like This Project, Give It a Star!

---
Happy Exploring! ⚽📊🎯

