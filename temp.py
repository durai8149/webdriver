import random


# import os
# import csv

# # Specify the directory containing CSV files
# directory = '/home/saliv/Devops/Python/webdriver/'  # Replace with your folder path

# # Loop through each file in the directory
# for filename in os.listdir(directory):
#     if filename.endswith('.csv'):
#         filepath = os.path.join(directory, filename)
#         print(f"Opening file: {filename}")

#         # Open and read the CSV file
#         with open(filepath, mode='r') as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 print(row[0])
#                 # print(row)  # Print each row or process it as needed
#                 # for user_data in row:
#                 #     print(user_data[0])


positive_feedback = [
    "Clear explanation",
    "Well structured",
    "Easy flow",
    "Organized session",
    "Strong delivery",
    "Effective methods",
    "Great pacing",
    "Logical order",
    "Concise points",
    "Straightforward teaching",
    "Very clear",
    "Easy understanding",
    "Deep insight",
    "Concept clarity",
    "Simple breakdown",
    "Meaningful lessons",
    "Explained well",
    "No confusion",
    "Clear thoughts",
    "Understood easily",
    "Highly knowledgeable",
    "Expert approach",
    "Strong background",
    "Deep knowledge",
    "Solid understanding",
    "Well prepared",
    "Confident delivery",
    "Knows subject",
    "Answers thoroughly",
    "Impressive expertise",
    "Very engaging",
    "Kept attention",
    "Interactive session",
    "Fun learning",
    "Great energy",
    "Lively class",
    "Encouraged questions",
    "Student involvement",
    "Supportive vibe",
    "Made interesting",
    "Real-life examples",
    "Useful resources",
    "Helpful materials",
    "Relevant content",
    "Clear visuals",
    "Great slides",
    "Practical examples",
    "Strong references",
    "Good handouts",
    "Visual support",
    "Friendly tone",
    "Encouraging words",
    "Open communication",
    "Listened well",
    "Helpful feedback",
    "Answered patiently",
    "Very approachable",
    "Respectful attitude",
    "Clear voice",
    "Positive attitude",
    "Goal-focused",
    "Productive time",
    "Learned a lot",
    "Worthwhile session",
    "Time-efficient",
    "High impact",
    "Focused session",
    "Good outcomes",
    "Skill improvement",
    "Big improvement",
    "Very inspiring",
    "Encouraged learning",
    "Boosted confidence",
    "Motivated effort",
    "Uplifting tone",
    "Positive energy",
    "Pushed potential",
    "Growth mindset",
    "Passionate teaching",
    "Purpose-driven",
    "Useful skills",
    "Real-world use",
    "Actionable tips",
    "Career-related",
    "Applicable knowledge",
    "Everyday relevance",
    "Practical guidance",
    "Helpful advice",
    "Life lessons",
    "Hands-on learning",
    "Excellent session",
    "Great teacher",
    "Amazing class",
    "Loved it",
    "Truly helpful",
    "Best lesson",
    "Highly recommended",
    "Great improvement",
    "Valuable session",
    "Enjoyed thoroughly"
]


feedback = [random.choice(positive_feedback) for _ in range(10)]

for feed in [random.choice(feedback)]:
    print(feed)
    # print(f"Feedback: {feed}")
