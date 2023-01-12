# Calculate binary metrics via sklearn
import sklearn.metrics as metrics

def calculate_binary_metrics(y_label, y_predict):
    print("=============== Classification Report ===============")
    print(metrics.classification_report(y_label, y_predict))

    print("====================== Measures ======================")
    print(f"Accuracy  : {metrics.accuracy_score(y_label, y_predict)}")
    print(f"Precision : {metrics.precision_score(y_label, y_predict)}")
    print(f"Recall    : {metrics.recall_score(y_label, y_predict)}")
    print(f"F1-Score  : {metrics.f1_score(y_label, y_predict)}")

    print("\n================== Confusion Matrix ==================")
    print(metrics.confusion_matrix(y_label, y_predict))

def main():
    y_label = [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1]
    y_predict = [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    
    calculate_binary_metrics(y_label, y_predict)

if __name__ == "__main__":
    main()
