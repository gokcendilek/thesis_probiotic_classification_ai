#  Probiotic Microorganism Classification Using AI

A comprehensive machine learning and deep learning study for classifying probiotic microorganisms, comparing multiple algorithms to evaluate their performance using FTIR spectral data.

##  Table of Contents
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Models Compared](#models-compared)
- [Performance Metrics](#performance-metrics)
- [Getting Started](#getting-started)
- [Contributors](#contributors)
- [Resources](#resources)

##  Project Overview

This thesis project focuses on the classification of probiotic microorganisms using advanced machine learning and deep learning techniques. The study utilizes FTIR (Fourier-Transform Infrared Spectroscopy) spectral data to identify and classify different probiotic strains, providing a comparative analysis of various AI algorithms.

##  Project Structure
```
Thesis_probiotic_classification_ai/
├── AKIS_SEMASI_FLOWCHART/    # Project flowcharts and visual diagrams
├── FTIR_DATA/                 # FTIR-based spectral data for classification
├── KODLAR/                    # Python scripts and Jupyter notebooks
├── MAKale/                    # Academic articles and references
├── TEZ(doc_pdf)/              # Thesis documents (PDF and DOC formats)
├── VIDEO/                     # Presentation and demo videos
└── README.md                  # Project documentation
```

##  Technologies Used

- **Python 3.x**
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **Deep Learning**: TensorFlow, Keras
- **Visualization**: Matplotlib, Seaborn
- **Development Environment**: Jupyter Notebook

##  Models Compared

### Traditional Machine Learning
- **K-Nearest Neighbors (KNN)**
- **Random Forest**
- **Support Vector Machine (SVM)**
- **Logistic Regression**
- **Extra Trees Classifier**

### Ensemble Methods
- **AdaBoost** (Adaptive Boosting)
- **Gradient Boosting**
- **XGBoost** (Extreme Gradient Boosting)
- **LightGBM** (Light Gradient Boosting Machine)
- **HistGradient Boosting** (Histogram-based Gradient Boosting)

### Deep Learning
- **LSTM** (Long Short-Term Memory)
- **CNN** (Convolutional Neural Network)
- **Augmented CNN Models**
- **Ensemble Learning Approaches**

##  Performance Metrics

The models are evaluated using the following metrics:
-  **Accuracy**
-  **Precision**
-  **Recall**
-  **F1-Score**
-  **Confusion Matrix**
-  **ROC-AUC**

## Model Performance Results

### Machine Learning & Ensemble Models

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| **CNN (Augmented Data)** | **0.9231** | **0.9400** | **0.9300** | **0.9300** |
| Extra Trees | 0.8667 | 0.9048 | 0.8667 | 0.8704 |
| XGBoost | 0.8667 | 0.9048 | 0.8667 | 0.8704 |
| HistGradient Boosting | 0.8667 | 0.8778 | 0.8667 | 0.8660 |
| LightGBM | 0.8667 | 0.8778 | 0.8667 | 0.8660 |
| Random Forest + XGBoost | 0.8667 | 0.9048 | 0.8667 | 0.8704 |
| LightGBM + Extra Trees | 0.8667 | 0.8778 | 0.8667 | 0.8660 |
| XGBoost + Extra Trees | 0.8667 | 0.9048 | 0.8667 | 0.8704 |
| All Four Models | 0.8667 | 0.9048 | 0.8667 | 0.8704 |
| Random Forest | 0.8000 | 0.8222 | 0.8000 | 0.8054 |
| Support Vector Machine (SVC) | 0.8000 | 0.8750 | 0.8000 | 0.8027 |
| Gradient Boosting | 0.7333 | 0.7333 | 0.7333 | 0.7333 |
| K-Nearest Neighbors (KNN) | 0.7333 | 0.7460 | 0.7333 | 0.7222 |
| AdaBoost | 0.6667 | 0.8333 | 0.6667 | 0.6296 |
| Logistic Regression | 0.6000 | 0.5937 | 0.6000 | 0.5778 |

### Deep Learning Models

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| **CNN (Augmented Data)** | **0.9231** | **0.9400** | **0.9300** | **0.9300** |
| LSTM | 0.3846 | 0.3800 | 1.0000 | 0.5600 |
| Hybrid (CNN+LSTM) | 0.3846 | 0.3800 | 1.0000 | 0.5600 |

### Key Findings

- **Best Overall Performance**: CNN with Augmented Data achieved the highest scores across all metrics (92.31% accuracy)
- **Strong Traditional ML Performance**: Multiple ensemble methods achieved 86.67% accuracy
- **Deep Learning Advantage**: CNN significantly outperformed LSTM and hybrid approaches
- **Data Augmentation Impact**: Augmented CNN showed substantial improvement over traditional models

##  Getting Started

### Prerequisites
```bash
pip install pandas numpy scikit-learn tensorflow keras matplotlib seaborn jupyter
```

### Installation
```bash
git clone https://github.com/gokcendilek/Thesis_probiotic_classification_ai.git
cd Thesis_probiotic_classification_ai
```

### Running the Code
```bash
jupyter notebook
# Navigate to KODLAR/ directory and open the notebooks
```

## 👥 Contributors
<table>
<tr>
<td align="center">
<a href="https://github.com/gokcendilek">
<img src="https://github.com/gokcendilek.png" width="100px;" alt="Gökçen Dilek Alak"/><br />
<sub><b>Gökçen Dilek Alak</b></sub>
</a><br />
Researcher
</td>
<td align="center">
<a href="https://github.com/OzgurBeyOnline">
<img src="https://github.com/OzgurBeyOnline.png" width="100px;" alt="Özgür Bey"/><br />
<sub><b>Özgür Bey</b></sub>
</a><br />
Researcher
</td>
</tr>
</table>

---
 

##  Resources

-  [Project Flowchart (PDF)](diagrams/Akis_Semasi(Flowchart).pdf)
-  [Dataset (Excel)](data/ferm_plantarium_enterokok.xlsx)
- 📹 [Thesis Presentation Video](https://drive.google.com/file/d/16DkJBCyzFWY3Mdcnaon4dv51ucUa4XxD/view?usp=drive_link)


##  License

This project is part of an academic thesis. Please contact the contributors for usage permissions.

##  Contact

For questions or collaboration opportunities, please reach out through GitHub issues or contact the contributors directly.

---

