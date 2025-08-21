# GA4 MCP Server Setup Guide

## Overview

This guide walks you through setting up the Google Analytics 4 (GA4) Model Context Protocol (MCP) server for use with Cursor.

## Prerequisites

- Python 3.10+
- Google Cloud Platform account
- GA4 property with data
- Cursor editor

## Step 1: Google Cloud Setup

### 1.1 Create/Select a Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Note your project ID for reference

### 1.2 Enable Required APIs

Enable the following APIs in your Google Cloud project:

- **Google Analytics Data API** (`analyticsdata.googleapis.com`)
- **Google Analytics Reporting API** (`analyticsreporting.googleapis.com`)

```bash
# Using gcloud CLI (optional)
gcloud services enable analyticsdata.googleapis.com
gcloud services enable analyticsreporting.googleapis.com
```

### 1.3 Create Service Account

1. Navigate to "IAM & Admin" > "Service Accounts"
2. Click "Create Service Account"
3. Provide a name (e.g., "ga4-mcp-server")
4. Click "Create and Continue"
5. Skip role assignment for now
6. Click "Done"

### 1.4 Generate Service Account Key

1. Click on the created service account
2. Go to "Keys" tab
3. Click "Add Key" > "Create new key"
4. Select "JSON" format
5. Download and save the JSON file securely

### 1.5 Grant GA4 Access

1. Go to your GA4 property in Google Analytics
2. Navigate to "Admin" > "Property" > "Property User Management"
3. Click the "+" button to add a user
4. Add the service account email address
5. Assign "Viewer" role
6. Click "Add"

## Step 2: Local Environment Setup

### 2.1 Install Dependencies

```bash
cd /Users/samumetso/aiprojects/ga4analysis
pip install -r requirements.txt
```

### 2.2 Configure Credentials

Set the environment variable to point to your service account key:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
```

To make this permanent, add it to your shell profile:

```bash
echo 'export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"' >> ~/.zshrc
source ~/.zshrc
```

### 2.3 Test Installation

Test if the MCP server is working:

```bash
google-analytics-mcp --help
```

## Step 3: Cursor Configuration

### 3.1 Open MCP Settings

1. Open Cursor
2. Go to Settings (Cmd/Ctrl + ,)
3. Navigate to "Features" > "MCP"

### 3.2 Add GA4 MCP Server

1. Click "+ Add New MCP Server"
2. Configure the server:
   - **Name:** `GA4 Analytics`
   - **Type:** `stdio`
   - **Command:** `google-analytics-mcp`

### 3.3 Restart Cursor

Close and reopen Cursor to load the new MCP server.

## Step 4: Testing

### 4.1 Verify Server Connection

In Cursor's Composer, try asking:

```
"Can you show me the available GA4 tools?"
```

### 4.2 Test Basic Query

Try a simple analytics query:

```
"Show me the total users for the past 7 days from my GA4 property"
```

## Troubleshooting

### Common Issues

1. **"google-analytics-mcp command not found"**
   - Ensure the package is installed: `pip install google-analytics-mcp`
   - Check your PATH includes pip install location

2. **"Authentication failed"**
   - Verify GOOGLE_APPLICATION_CREDENTIALS is set correctly
   - Check that the service account has access to your GA4 property
   - Ensure the JSON key file exists and is readable

3. **"Property not found"**
   - Verify the service account has "Viewer" access to your GA4 property
   - Check that you're using the correct property ID

4. **MCP server not appearing in Cursor**
   - Restart Cursor completely
   - Check the MCP server configuration
   - Look for error messages in Cursor's developer console

### Getting Help

- Check the [GA4 MCP GitHub repository](https://github.com/surendranb/google-analytics-mcp)
- Review [Cursor MCP documentation](https://cursor.directory/mcp)
- Verify your Google Cloud and GA4 setup

## Security Notes

- Keep your service account JSON key secure
- Never commit credentials to version control
- Use environment variables for sensitive data
- Regularly rotate service account keys
- Follow principle of least privilege for GA4 access
