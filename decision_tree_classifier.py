"""
Decision Tree Classifier
Trains a decision tree classifier on the Iris dataset for binary classification.
"""

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
from sklearn import tree

def run_decision_tree():
    """
    Load Iris dataset, train a Decision Tree classifier, and display results.
    CLI version - uses print statements.
    """
    # Load Iris dataset
    print("Loading Iris dataset...")
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Binary classification: setosa vs. non-setosa
    y_binary = (y == 0).astype(int)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_binary, test_size=0.2, random_state=42
    )

    print("Training Decision Tree model...")
    # Initialize and train the Decision Tree model
    decision_tree = DecisionTreeClassifier()
    decision_tree.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = decision_tree.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\n{'='*60}")
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    print(f"{'='*60}")

    # Display classification report
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, 
                                target_names=['Non-Setosa', 'Setosa']))

    # Display confusion matrix
    print("\nConfusion Matrix:")
    cm = confusion_matrix(y_test, y_pred)
    print(f"                Predicted")
    print(f"              Non-Setosa  Setosa")
    print(f"Actual Non-Setosa    {cm[0][0]:4d}    {cm[0][1]:4d}")
    print(f"      Setosa         {cm[1][0]:4d}    {cm[1][1]:4d}")

    # Ask user if they want to visualize the tree
    visualize = input("\nWould you like to visualize the decision tree? (y/n): ").strip().lower()
    
    if visualize == 'y':
        print("Generating decision tree visualization...")
        plt.figure(figsize=(12, 8))
        tree.plot_tree(decision_tree, 
                      feature_names=iris.feature_names, 
                      class_names=['Non-Setosa', 'Setosa'], 
                      filled=True)
        plt.title("Decision Tree Classifier - Iris Dataset")
        plt.show()
        print("Visualization displayed!")

def run_decision_tree_classifier(show_tree=False):
    """
    Streamlit-compatible version of decision tree classifier.
    
    Args:
        show_tree: Boolean, whether to display tree visualization
    """
    try:
        import streamlit as st
    except ImportError:
        # Fallback to CLI version
        run_decision_tree()
        return
    
    # Load Iris dataset
    st.info("📊 Loading Iris dataset...")
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Binary classification: setosa vs. non-setosa
    y_binary = (y == 0).astype(int)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_binary, test_size=0.2, random_state=42
    )

    # Initialize and train the Decision Tree model
    decision_tree = DecisionTreeClassifier()
    decision_tree.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = decision_tree.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    # Display results
    st.success(f"✅ Model trained successfully!")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Accuracy", f"{accuracy * 100:.2f}%")
    with col2:
        st.metric("Training Samples", len(X_train))
    with col3:
        st.metric("Test Samples", len(X_test))
    
    # Classification Report
    st.subheader("📋 Classification Report")
    report = classification_report(y_test, y_pred, 
                                  target_names=['Non-Setosa', 'Setosa'],
                                  output_dict=True)
    st.dataframe(report, use_container_width=True)
    
    # Confusion Matrix
    st.subheader("📊 Confusion Matrix")
    cm = confusion_matrix(y_test, y_pred)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Matrix Values:**")
        st.dataframe(cm, use_container_width=True)
    with col2:
        st.markdown("**Visualization:**")
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
        ax.set_title('Confusion Matrix')
        ax.set_xticks([0, 1])
        ax.set_yticks([0, 1])
        ax.set_xticklabels(['Non-Setosa', 'Setosa'])
        ax.set_yticklabels(['Non-Setosa', 'Setosa'])
        for i in range(2):
            for j in range(2):
                ax.text(j, i, str(cm[i][j]), ha='center', va='center', 
                       color='white' if cm[i][j] > cm.max()/2 else 'black')
        st.pyplot(fig)
    
    # Decision Tree Visualization
    if show_tree:
        st.subheader("🌳 Decision Tree Visualization")
        fig, ax = plt.subplots(figsize=(16, 10))
        tree.plot_tree(decision_tree, 
                      feature_names=iris.feature_names, 
                      class_names=['Non-Setosa', 'Setosa'], 
                      filled=True,
                      ax=ax)
        ax.set_title("Decision Tree Classifier - Iris Dataset", fontsize=14, fontweight='bold')
        st.pyplot(fig)

if __name__ == "__main__":
    run_decision_tree()
