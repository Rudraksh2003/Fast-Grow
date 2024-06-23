# Fast Grow Content Analyzer

![Fast Grow Logo](static/apple-touch-icon.png)



---

## Description

Welcome to Fast Grow, your one-stop destination for cutting-edge content analysis tools. At Fast Grow, we harness the power of advanced AI technology to provide two essential services: YouTube Comment Key Point Finder and Data Summarizer.

### YouTube Comment Key Point Finder

With our YouTube Comment Key Point Finder, we offer a revolutionary solution for content creators and marketers seeking valuable insights from audience feedback. Simply input the YouTube video link or comment section, and our AI algorithm swiftly identifies and highlights key points, enabling you to grasp the essence of user opinions and sentiments with unparalleled efficiency.

### Data Summarizer

Our Data Summarizer sets a new standard in data analysis. Whether you're a student, researcher, or professional, our intuitive platform allows you to upload any document and pose specific questions. Our AI engine meticulously scans the content, extracts relevant information, and generates concise summaries tailored to your inquiry. Gone are the days of laborious manual reading; with Fast Grow, access to comprehensive data summaries is just a click away.

Join the Fast Grow community today and revolutionize the way you analyze content. Experience the power of AI-driven insights and propel your growth journey with confidence.

## Technologies Used

### Backend and AI Framework

- **Flask Framework**: Fast Grow is built using Flask, a lightweight and efficient web framework for Python, enabling rapid development of web applications.
- **Python**: The project is primarily developed in Python, a versatile and powerful programming language well-suited for natural language processing (NLP) tasks.
- **Natural Language Processing (NLP)**: Leveraging NLP techniques and methodologies, Fast Grow extracts valuable insights from textual data, enabling users to understand and analyze content more effectively.
- **Libraries**:
  - **NumPy**: For efficient numerical operations and data manipulation.
  - **Pandas**: For data analysis and manipulation, particularly useful for handling tabular data.
  - **NLTK (Natural Language Toolkit)**: A comprehensive library for NLP tasks such as tokenization, stemming, and sentiment analysis.
  - **YouTube Data API**: Fast Grow integrates with the YouTube Data API to fetch comments from YouTube videos, providing valuable user feedback for analysis.
  - **Hugging Face API**: For text summarization, Fast Grow utilizes the Hugging Face API, which offers state-of-the-art natural language processing models and tools.
- **Sentiment Analysis**: Fast Grow employs sentiment analysis techniques to determine the polarity of sentences, categorizing them as negative, positive, or neutral. This helps users gauge the overall sentiment conveyed in the text.

### Containerization and Orchestration

- **Docker**: Used for containerizing the application to ensure consistency across different environments.
- **Kubernetes**: Employed for container orchestration, managing the deployment, scaling, and operations of application containers across clusters of hosts.

### CI/CD and Infrastructure

- **Jenkins**: Implemented CI/CD pipelines to automate the build, test, and deployment processes.
- **Terraform**: Used for Infrastructure as Code (IaC) to manage and provision AWS resources.


## Directory Structure

```plaintext
fast-grow/
├── comment-backend/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── ...
├── data-backend/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── ...
├── infrastructure/
│   ├── terraform/
│       ├── main.tf
│       ├── variables.tf
│       └── ...
├── jenkins/
   ├── Jenkinsfile
   └── ...

```

## To Run the App

### Prerequisites

- Docker
- Kubernetes (Minikube or any Kubernetes cluster)
- Python
- Flask
- YouTube Data API Key
- Hugging Face API Key

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Rudraksh2003/Fast-Grow.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Fast-Grow
   ```

3. **Add API Keys:**
   - Add YouTube API key in `Secrets.toml`
   - Add Hugging Face API key in `data.py`

4. **Open two separate terminals:**

   **Terminal 1:**
   ```bash
   python app.py
   ```

   **Terminal 2:**
   ```bash
   python data.py
   ```

### Kubernetes Setup

1. **Build Docker images:**
   ```bash
   docker build -t yourusername/fast-grow-app:latest -f Dockerfile.app .
   docker build -t yourusername/fast-grow-data:latest -f Dockerfile.data .
   ```

2. **Push Docker images to Docker Hub:**
   ```bash
   docker push yourusername/fast-grow-app:latest
   docker push yourusername/fast-grow-data:latest
   ```

3. **Apply Kubernetes manifests:**
   ```bash
   kubectl apply -f kubernetes/app-deployment.yaml
   kubectl apply -f kubernetes/app-service.yaml
   kubectl apply -f kubernetes/data-deployment.yaml
   kubectl apply -f kubernetes/data-service.yaml
   ```

4. **Check the status of pods and services:**
   ```bash
   kubectl get pods
   kubectl get services
   ```

### CI/CD Pipeline

- **Jenkinsfile**: Define the Jenkins pipeline for continuous integration and continuous deployment.

### Infrastructure as Code (IaC)

- **Terraform**: Define infrastructure resources in AWS EC2 for deployment.


## Contributors

- **[Ritu Raj Bhardwaj](https://github.com/Rituraj1001)**: Developed the AI framework and backend services.
- **[RUDRAKSH LADDHA](https://github.com/Rudraksh2003) **: Created static and dynamic files, integrated Flask to fetch HTML files, contributed to backend work, set up containers and Kubernetes, and implemented CI/CD with Jenkins and Terraform IaC. Also focused on UI/UX and made changes according to feedback.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

