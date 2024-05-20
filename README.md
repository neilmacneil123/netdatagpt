# Netdata GPT Monitor

![Netdata](https://img.shields.io/badge/Netdata-Monitoring-brightgreen)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT-blue)

This project integrates **Netdata** with **OpenAI's GPT** to monitor network performance and provide real-time feedback.

## 🚀 Features

- **Real-time Monitoring**: Utilizes Netdata for continuous monitoring.
- **AI-Powered Analysis**: Leverages OpenAI GPT to analyze metrics and provide insights.
- **Custom Alerts**: Configurable alerts and notifications.

## 📋 Setup

1. **Clone the repository**:
    ```sh
    git clone git@github.com:neilmacneil123/netdatagpt.git
    cd netdatagpt
    ```

2. **Install dependencies**:
    ```sh
    pip install requests openai python-dotenv
    ```

3. **Create a `.env` file**:
    ```sh
    echo "OPENAI_API_KEY=your_openai_api_key" > .env
    ```

4. **Run the script**:
    ```sh
    python netdata_gpt_monitor.py
    ```

## 🔧 Configuration

Update the `.env` file with your OpenAI API key:

```ini
OPENAI_API_KEY=your_openai_api_key

