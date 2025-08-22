# GA4 Analysis & MCP Integration Platform

**GA4 Analysis** - A comprehensive Google Analytics 4 data analysis platform that integrates with Model Context Protocol (MCP) to provide advanced analytics, insights, and automated reporting capabilities for web analytics professionals and data analysts.

## Prerequisites

- Python 3.10 or higher
- Google Cloud Platform account
- GA4 property with appropriate access

## Setup Instructions

### 1. Install Dependencies

```bash
pip install google-analytics-mcp
```

### 2. Google Cloud Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable the following APIs:
   - Google Analytics Data API
   - Google Analytics Reporting API
4. Create a service account and download the JSON key
5. Add the service account email to your GA4 property with "Viewer" role

### 3. Environment Configuration

Set the environment variable for Google credentials:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
```

### 4. Cursor MCP Configuration

1. Open Cursor Settings
2. Navigate to Features > MCP
3. Add new MCP server:
   - **Name:** GA4 MCP
   - **Type:** stdio
   - **Command:** `google-analytics-mcp`
4. Save and restart Cursor

## Usage

Once configured, you can use natural language queries to analyze your GA4 data directly in Cursor's Composer.

Example queries:
- "Show me the top 10 pages by pageviews last month"
- "What's the conversion rate for the past 7 days?"
- "Compare user sessions between this month and last month"

## Project Structure

```
ga4analysis/
├── README.md
├── requirements.txt
├── .env.example
├── scripts/
│   └── setup.sh
└── docs/
    └── mcp-setup.md
```
