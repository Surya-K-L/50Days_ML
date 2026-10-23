
# ============================================================
# DAY 10: STUDENT PERFORMANCE ANALYSIS
# ============================================================

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 1. PROJECT PATHS AND SETTINGS
PROJECT_DIR = Path(__file__).resolve().parent
DATA_PATH = PROJECT_DIR / "data" / "student-mat.csv"
IMAGE_DIR = PROJECT_DIR / "images"
IMAGE_DIR.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid")
pd.set_option("display.max_columns", None)


# 2. LOAD DATASET
print("\n========== 1. LOAD DATASET ==========")

if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"Dataset not found at: {DATA_PATH}\n"
        "Place student-mat.csv inside the data folder."
    )

df = pd.read_csv(DATA_PATH, sep=";")

print("First five records:")
print(df.head())

print("\nDataset shape (rows, columns):", df.shape)
print("\nColumn names:")
print(df.columns.tolist())


# 3. UNDERSTAND THE DATA
print("\n========== 2. UNDERSTAND DATA ==========")

print("\nData types and non-null counts:")
df.info()

print("\nStatistical summary:")
print(df.describe().round(2))

print("\nMissing values per column:")
print(df.isnull().sum().sort_values(ascending=False))

print("\nNumber of duplicate rows:", df.duplicated().sum())


# 4. DATA QUALITY CHECKS
print("\n========== 3. DATA QUALITY ==========")

grade_columns = ["G1", "G2", "G3"]

print("\nGrade ranges (grades should be between 0 and 20):")
for col in grade_columns:
    print(f"{col}: minimum={df[col].min()}, maximum={df[col].max()}")

print("\nStudent counts by school:")
print(df["school"].value_counts())

print("\nStudy-time categories:")
print(df["studytime"].value_counts().sort_index())

print("\nNote: Do not automatically remove outliers or rows "
      "unless there is evidence they are errors.")


# 5. DESCRIPTIVE STATISTICS
print("\n========== 4. DESCRIPTIVE STATISTICS ==========")

print("\nFinal grade (G3) statistics:")
print(df["G3"].describe().round(2))

print("\nMean final grade:", round(df["G3"].mean(), 2))
print("Median final grade:", round(df["G3"].median(), 2))
print("Mode final grade:", df["G3"].mode().tolist())
print("Standard deviation:", round(df["G3"].std(), 2))

print("\nAverage absences:", round(df["absences"].mean(), 2))
print("Median absences:", df["absences"].median())


# 6. CREATE STUDY-TIME LABELS
study_labels = {
    1: "Less than 2 hours",
    2: "2 to 5 hours",
    3: "5 to 10 hours",
    4: "10+ hours"
}

df["studytime_label"] = df["studytime"].map(study_labels)


# 7. VISUALIZATION 1: DISTRIBUTION OF FINAL GRADES
print("\n========== 5. VISUALIZATIONS ==========")

plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="G3", bins=11, kde=True)
plt.title("Distribution of Final Mathematics Grades")
plt.xlabel("Final Grade (G3), out of 20")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "01_grade_distribution.png", dpi=300)
plt.close()


# 8. VISUALIZATION 2: AVERAGE GRADE BY STUDY TIME
study_order = [
    "Less than 2 hours",
    "2 to 5 hours",
    "5 to 10 hours",
    "10+ hours"
]

plt.figure(figsize=(9, 5))
sns.barplot(
    data=df,
    x="studytime_label",
    y="G3",
    order=study_order,
    errorbar=None
)
plt.title("Average Final Grade by Weekly Study Time")
plt.xlabel("Weekly Study Time")
plt.ylabel("Average Final Grade")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(IMAGE_DIR / "02_grade_by_study_time.png", dpi=300)
plt.close()


# 9. VISUALIZATION 3: ABSENCES VS FINAL GRADE
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="absences", y="G3", alpha=0.7)
plt.title("Student Absences vs Final Grade")
plt.xlabel("Number of Absences")
plt.ylabel("Final Grade (G3)")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "03_absences_vs_grade.png", dpi=300)
plt.close()


# 10. VISUALIZATION 4: PREVIOUS GRADE VS FINAL GRADE
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.regplot(data=df, x="G1", y="G3", ax=axes[0],
            scatter_kws={"alpha": 0.6})
axes[0].set_title("First Period Grade (G1) vs Final Grade")
axes[0].set_xlabel("G1")
axes[0].set_ylabel("G3")

sns.regplot(data=df, x="G2", y="G3", ax=axes[1],
            scatter_kws={"alpha": 0.6})
axes[1].set_title("Second Period Grade (G2) vs Final Grade")
axes[1].set_xlabel("G2")
axes[1].set_ylabel("G3")

plt.tight_layout()
plt.savefig(IMAGE_DIR / "04_previous_grades_vs_final.png", dpi=300)
plt.close()


# 11. VISUALIZATION 5: GRADES BY SCHOOL
plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x="school", y="G3")
plt.title("Final Grade Distribution by School")
plt.xlabel("School")
plt.ylabel("Final Grade (G3)")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "05_grades_by_school.png", dpi=300)
plt.close()


# 12. VISUALIZATION 6: CORRELATION HEATMAP
numeric_df = df.select_dtypes(include=np.number)
correlation = numeric_df.corr()

plt.figure(figsize=(12, 9))
sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0
)
plt.title("Correlation Between Numerical Variables")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "06_correlation_heatmap.png", dpi=300)
plt.close()


# 13. CORRELATION WITH FINAL GRADE
print("\n========== 6. CORRELATION ANALYSIS ==========")

grade_correlations = (
    correlation["G3"]
    .drop("G3")
    .sort_values(key=abs, ascending=False)
)

print("\nCorrelation of numerical features with G3:")
print(grade_correlations.round(3))

plt.figure(figsize=(9, 7))
grade_correlations.sort_values().plot(kind="barh")
plt.title("Correlation of Numerical Features with Final Grade")
plt.xlabel("Pearson Correlation with G3")
plt.ylabel("Feature")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "07_grade_correlations.png", dpi=300)
plt.close()


# 14. GROUP COMPARISONS
print("\n========== 7. GROUP COMPARISONS ==========")

print("\nAverage final grade by study time:")
print(
    df.groupby("studytime_label", observed=False)["G3"]
    .agg(["count", "mean", "median"])
    .round(2)
)

print("\nAverage final grade by school:")
print(df.groupby("school")["G3"].agg(["count", "mean"]).round(2))

print("\nAverage final grade by sex:")
print(df.groupby("sex")["G3"].agg(["count", "mean"]).round(2))


# 15. OUTLIER ANALYSIS USING THE IQR METHOD
print("\n========== 8. OUTLIER ANALYSIS ==========")

for col in ["G3", "absences"]:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outliers = df[
        (df[col] < lower_bound) |
        (df[col] > upper_bound)
    ]

    print(f"\nColumn: {col}")
    print("Lower bound:", round(lower_bound, 2))
    print("Upper bound:", round(upper_bound, 2))
    print("Potential outlier count:", len(outliers))

    if not outliers.empty:
        print(outliers[[col]].head(10))

print("\nPotential outliers require investigation; they are not "
      "automatically errors.")


# 16. AUTOMATICALLY SUMMARIZE SELECTED FINDINGS
print("\n========== 9. KEY FINDINGS ==========")

print("Number of students:", len(df))
print("Number of features:", df.shape[1])
print("Average final grade:", round(df["G3"].mean(), 2))
print("Median final grade:", round(df["G3"].median(), 2))
print("Average absences:", round(df["absences"].mean(), 2))

print("\nStudy time and average final grade:")
study_summary = df.groupby("studytime_label", observed=False)["G3"].mean()
print(study_summary.round(2))

if not grade_correlations.empty:
    strongest = grade_correlations.abs().idxmax()
    print(
        "\nStrongest absolute numerical correlation with G3:",
        strongest,
        "with correlation",
        round(grade_correlations[strongest], 3)
    )

print("\nIMPORTANT INTERPRETATION:")
print("- Correlation does not prove causation.")
print("- Study-time groups may differ in other ways.")
print("- G1 and G2 are earlier grades and strongly related to G3, "
      "but may be unavailable when predicting grades early in the year.")
print("- Findings describe this dataset and may not generalize "
      "to all students.")


# 17. SAVE CLEANED/ANALYSIS DATA SUMMARY
summary_path = PROJECT_DIR / "analysis_summary.txt"

with open(summary_path, "w", encoding="utf-8") as file:
    file.write("STUDENT PERFORMANCE ANALYSIS SUMMARY\n")
    file.write("=" * 40 + "\n")
    file.write(f"Number of students: {len(df)}\n")
    file.write(f"Number of columns: {df.shape[1]}\n")
    file.write(f"Average final grade: {df['G3'].mean():.2f}\n")
    file.write(f"Median final grade: {df['G3'].median():.2f}\n")
    file.write(f"Average absences: {df['absences'].mean():.2f}\n")
    file.write("\nCorrelation with final grade:\n")
    file.write(grade_correlations.round(3).to_string())
    file.write("\n\nStudy time summary:\n")
    file.write(study_summary.round(2).to_string())

print("\nAnalysis summary saved to:", summary_path)
print("Charts saved in:", IMAGE_DIR)
print("\nPROJECT COMPLETED SUCCESSFULLY!")
