# 🩸 AI-Powered Clinical Support System for Thalassemia Care

## 📌 Problem Statement
Thalassemia patients face numerous challenges, including:
- Difficulty in finding **regular blood donors**.
- Limited access to **quality medical care**.
- High **financial burden** due to lifelong treatment.
- Severe lack of **awareness** about thalassemia in India.

As a result, thousands of children are born with this condition each year without adequate medical care or support.  

**Hackathon Challenge:**  
Develop an **innovative, technology-driven solution** to support *Blood Warriors* in their mission to help thalassemia patients, leveraging **AI and other tools** to address key areas of opportunity or improve existing solutions.

---

## 💡 Our Solution: ThalCare AI
**ThalCare AI** is an AI-driven healthcare platform that connects **patients, donors, and healthcare providers** in real-time, improves awareness, and ensures efficient treatment planning.

### 🎯 Key Features
1. **AI Clinical Assistant (LLM-based)** – Provides treatment guidance, answers patient queries, and shares thalassemia-related information in multiple languages.
2. **Smart Donor Matching** – Uses geolocation (Google Maps API) to instantly find the nearest compatible blood donors.
3. **Secure Medical Records** – Stores patient history in HIPAA-compliant cloud databases.
4. **Awareness Chatbot** – Educates communities about thalassemia prevention and management.
5. **Real-Time Alerts** – Sends donor requests via SMS/WhatsApp using Twilio integration.

---

## 🏗️ System Architecture
nt/Doctor/Donor App] <---> [Streamlit Web Interface]
| |
v v
[AI LLM Engine] <----> [MongoDB + Firebase]
|
v
[APIs: Google Maps, Twilio, OpenAI]


---

## 🛠 Tech Stack
- **Programming:** Python
- **AI/NLP:** OpenAI API, Hugging Face Transformers
- **Frameworks:** FastAPI, Streamlit
- **Databases:** MongoDB, Firebase
- **Cloud Services:** Google Cloud Platform, AWS
- **APIs:** Google Maps API, Twilio API
- **Visualization:** Power BI / Tableau

---

## 🚀 Installation & Setup
```bash
# 1️⃣ Clone this repository
git clone https://github.com/yourusername/thalcare-ai.git
cd thalcare-ai

# 2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Add API keys in .env file
OPENAI_API_KEY=your_openai_key
GOOGLE_MAPS_API_KEY=your_google_maps_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token

# 5️⃣ Run the application
streamlit run app.py
```
-----

## 📊  Expected Impact
⏱ 50% reduction in donor search time.

📈 Increased awareness via multilingual chatbot.

🏥 Improved treatment outcomes with AI-assisted recommendations.

🤝 Better collaboration between patients, donors, and healthcare providers.


## 🏆 Hackathon Participation
This project was built for the AI for Good Hackathon 2025 in response to the Blood Warriors Challenge.

##👥 Team Members
Srushti Badukale – AI/NLP Development
Divya Patkar - PowerBI

## 📜 License
This project is licensed under the MIT License.
