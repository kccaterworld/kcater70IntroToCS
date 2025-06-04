import matplotlib.pyplot as plt

summary = "Deepfakes, identity theft, scams, and data misuse are growing concerns as AI can impersonate or manipulate people using realistic, AI-generated content. This raises serious risks for misinformation (false information shared unknowingly), disinformation (intentional lies), and propaganda (biased content meant to influence opinions). While regulations like GDPR and CCPA, along with some AI ethics policies, offer a foundation, stronger measures are needed. Greater transparency, enhanced data rights, and stricter penalties for misuse are essential to protect individuals from harm and ensure responsible use of AI technologies."

# Categories from the data
categories = [
    "Worry AI steals info",
    "Don't trust/use AI",
    "Think AI brainwashes",
    "AI should be unregulated"
]

# Example counts based on the data (replace with actual numbers)
counts = [10, 7, 4, 3]

# Pastel colors
colors = ["#AEC6CF", '#FFD1DC', '#C1E1C1', '#FDFD96']

plt.figure(figsize=(8,5))
bars = plt.bar(categories, counts, color=colors, edgecolor='gray')

plt.title("AI Concerns from Respondents", fontsize=14)
plt.ylabel("Number of People", fontsize=12)
plt.ylim(0, max(counts) + 3)

# Add counts to the tops of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, int(yval), ha='center', fontsize=11)

plt.tight_layout()
plt.show()