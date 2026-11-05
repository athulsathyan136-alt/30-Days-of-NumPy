
import numpy as np

print("=" * 55)
print("STUDENT PERFORMANCE AND DATA ANALYTICS SYSTEM")
print("=" * 55)

# 1. Create student dataset
student_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108])

scores = np.array([
    [85, 90, 88],
    [70, 75, 80],
    [45, 55, 60],
    [92, 95, 94],
    [np.nan, 65, 70],
    [55, np.nan, 58],
    [78, 82, 85],
    [30, 40, 35]
], dtype=float)

print("\n1.Original Student Scores")
print("Columns: Maths , Science, English")
print(scores)

missing = np.isnan(scores)
print("\n2.Missing Data Analysis")
print("Missing value positions:")
print(missing)

print("Total missing values: ",np.count_nonzero(missing))

sub_mean = np.nanmean(scores,axis=0)

print("\n3.Subject Avereage")
print("Maths: ",sub_mean[0])
print("Science: ",sub_mean[1])
print("English:", sub_mean[2])

clean = np.where(np.isnan(scores),sub_mean,scores)
print("\n4.Cleaned Dataset")
print(clean)

total = np.sum(clean,axis=1)
avg = np.mean(clean,axis=1)

print("\n5.Stuents Performance")
for i in range(len(student_ids)):
    print("Students: ",student_ids[i],
          "| total: ",round(total[i],2),
          "| Average: ",round(avg[i],2))

status = np.where(avg>=50,"PASS","FAIL")

print("\n6. PASS / FAIL RESULTS")
for i in range(len(student_ids)):
    print(student_ids[i], ":", status[i])

grades = np.select(
    [
        avg >= 90,
        avg >= 80,
        avg >= 70,
        avg >= 60,
        avg >= 50
    ],
    ["A", "B", "C", "D", "E"],
    default="F"
)

print("\n7. STUDENT GRADES")
for i in range(len(student_ids)):
    print(student_ids[i], ":", grades[i])

# 8. Rank students by average marks
ranking_indices = np.argsort(avg)[::-1]

print("\n8. STUDENT RANKING")
for rank, index in enumerate(ranking_indices, start=1):
    print(
        "Rank:", rank,
        "| Student:", student_ids[index],
        "| Average:", round(avg[index], 2)
    )

# 9. Find highest and lowest performing students
best_index = np.argmax(avg)
lowest_index = np.argmin(avg)

print("\n9. TOP AND LOWEST PERFORMERS")
print("Top student:", student_ids[best_index])
print("Lowest student:", student_ids[lowest_index])

# 10. Subject-wise statistics
print("\n10. SUBJECT STATISTICS")

print("Subject maximum:", np.max(clean, axis=0))
print("Subject minimum:", np.min(clean, axis=0))
print("Subject mean:", np.mean(clean, axis=0))
print("Subject standard deviation:", np.std(clean, axis=0))

# 11. Percentile analysis
print("\n11. CLASS PERCENTILES")
print("25th percentile:", np.percentile(avg, 25))
print("50th percentile:", np.percentile(avg, 50))
print("75th percentile:", np.percentile(avg, 75))

# 12. Weighted performance using dot product
weights = np.array([0.40, 0.35, 0.25])

weighted_scores = np.dot(clean, weights)

print("\n12. WEIGHTED STUDENT SCORES")
print(weighted_scores)

# 13. Overall class performance
class_average = np.mean(avg)
pass_count = np.count_nonzero(status == "PASS")
fail_count = np.count_nonzero(status == "FAIL")

print("\n13. FINAL CLASS REPORT")
print("Class average:", round(class_average, 2))
print("Students passed:", pass_count)
print("Students failed:", fail_count)
print("Pass percentage:", round(pass_count / len(student_ids) * 100, 2), "%")

print("\n" + "=" * 55)
print("ANALYSIS COMPLETED")
print("=" * 55)