import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_distances
import re
import string
import os

# Text preprocessing without NLTK
def preprocess_text(text):
    text = str(text).lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    stop_words = set([
        'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves',
        'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him',
        'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its',
        'itself', 'they', 'them', 'their', 'theirs', 'themselves',
        'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those',
        'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have',
        'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an',
        'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while',
        'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between',
        'into', 'through', 'during', 'before', 'after', 'above', 'below',
        'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under',
        'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where',
        'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most',
        'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same',
        'so', 'than', 'too', 'very', 'can', 'will', 'just', 'don', 'should', 'now'
    ])
    clean_tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(clean_tokens)

# Resume Processing Pipeline
def process_resumes(file_path, n_clusters=5):
    df = pd.read_csv(file_path)

    if 'Resume' not in df.columns:
        raise ValueError("CSV must contain a 'Resume' column")

    df['Cleaned_Resume'] = df['Resume'].apply(preprocess_text)

    vectorizer = TfidfVectorizer(max_features=1000)
    X = vectorizer.fit_transform(df['Cleaned_Resume'])

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X)

    center_distances = cosine_distances(X, kmeans.cluster_centers_)
    max_dist = center_distances.max()
    df['Score'] = df.apply(lambda row: round(10 * (1 - center_distances[row.name][row['Cluster']] / max_dist), 2), axis=1)

    df = df.sort_values(by='Score', ascending=False)

    output_file = os.path.join(os.path.dirname(file_path), f"Processed_{os.path.basename(file_path)}")
    df.to_csv(output_file, index=False)
    return output_file

# GUI Code
class ResumeParserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Resume Parser")
        self.root.geometry("500x300")

        self.file_path = None

        self.label = tk.Label(root, text="AI Resume Parser", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.upload_btn = tk.Button(root, text="Select Resume CSV", command=self.upload_file)
        self.upload_btn.pack(pady=5)

        self.cluster_label = tk.Label(root, text="Number of Clusters:")
        self.cluster_label.pack()
        self.cluster_entry = tk.Entry(root)
        self.cluster_entry.insert(0, "5")
        self.cluster_entry.pack(pady=5)

        self.process_btn = tk.Button(root, text="Start Processing", command=self.process_file)
        self.process_btn.pack(pady=10)

        self.status = tk.Label(root, text="Status: Waiting", fg="blue")
        self.status.pack(pady=10)

    def upload_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[["CSV files", "*.csv"]])
        if self.file_path:
            self.status.config(text=f"Selected File: {os.path.basename(self.file_path)}")

    def process_file(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a CSV file first.")
            return

        try:
            clusters = int(self.cluster_entry.get())
            self.status.config(text="Processing...")
            output_file = process_resumes(self.file_path, clusters)
            self.status.config(text=f"Processing complete. Saved to: {os.path.basename(output_file)}")
            messagebox.showinfo("Success", f"Output saved as:\n{output_file}")
        except Exception as e:
            self.status.config(text="Error during processing.")
            messagebox.showerror("Error", str(e))

if __name__ == '__main__':
    root = tk.Tk()
    app = ResumeParserApp(root)
    root.mainloop()
