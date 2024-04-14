from sklearn.metrics import f1_score
from your_youtube_comment_analyzer import analyze_youtube_comments, get_true_labels  # Import your functions

# Get the YouTube link from the user
youtube_link = input("Enter the YouTube link: ")

# Call your function to analyze comments for the given YouTube link and get predicted labels
predicted_labels = analyze_youtube_comments(youtube_link)

# Call your function to get true labels associated with the given YouTube link
true_labels = get_true_labels(youtube_link)

# Calculate F1 score
f1 = f1_score(true_labels, predicted_labels)

print("F1 Score:", f1)
