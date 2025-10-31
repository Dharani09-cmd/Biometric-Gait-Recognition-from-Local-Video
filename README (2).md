# 🧠 Biometric Gait Recognition from Local Video

This project was created by **Dharani Priya G** and team to identify individuals based on their **unique walking styles** using AI-powered gait analysis.

Our work is inspired by **Marian Margeta’s Gait Recognition Repository**:  
🔗 [https://github.com/marian-margeta/gait-recognition](https://github.com/marian-margeta/gait-recognition)

We enhanced the approach using **dummy pose estimation** and **joint coordinate tracking**, plotting motion graphs for 8 key joints:
> Left & Right Knees, Wrists, Hips, Pelvis, and Head Top.

Then, we applied **Fourier Transform** to these motion graphs to generate unique gait signatures for individual recognition.

---

## ⚙️ How to Run the Project

1️⃣ Clone the repository:
```bash
git clone https://github.com/Dharani09-cmd/Biometric-Gait-Recognition-from-Local-Video.git
```

2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

3️⃣ Run the main program:
```bash
python "Gait Recognition main.py"
```

4️⃣ Use the GUI to:
- 🎞️ Insert training videos → “INSERT TRAINING VIDEO”
- 🎥 Insert testing videos → “INSERT TESTING VIDEO”
- 🧩 Compare and get recognition results → “COMPARE”

> ⚠️ **Note:**  
> Tkinter doesn’t fully support multithreading. Run only one or two GUI options at a time.  
> Keep a plain white image named `white.png` in your working directory.

---

## 🧰 Software Requirements

| Library | Version |
|----------|----------|
| numpy | 1.16.4 |
| scipy | < 1.2.0 |
| matplotlib | 3.1.0 |
| opencv-python | 4.1.0 |
| tkinter | 8.6 |
| mttkinter | 0.6.1 |
| imutils | 0.5.2 |
| pickle | 4.0 |
| scikit-learn | 0.21.2 |

---

## 👨‍💻 Team Members & Collaborators

| Name | GitHub Profile |
|------|----------------|
| **Dharani Priya G** | [@Dharani09-cmd](https://github.com/Dharani09-cmd) |
| **Umesh** | [@2310030033-umesh](https://github.com/2310030033-umesh) |
| **Chaitanya** | [@2310030083chaitanya](https://github.com/2310030083chaitanya) |
| **CHSP Sreekar** | [@CHSPsreekar](https://github.com/CHSPsreekar) |
| **Sonali** | [@sonali703](https://github.com/sonali703) |
| **Allamsetty Jaya Soumya** | [@soumya326](https://github.com/soumya326) |
