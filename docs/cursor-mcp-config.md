# Cursor MCP Configuration for GA4

## Step-by-Step Cursor Configuration

### 1. Open Cursor Settings

1. Launch Cursor
2. Open Settings:
   - **macOS:** `Cmd + ,`
   - **Windows/Linux:** `Ctrl + ,`

### 2. Navigate to MCP Settings

1. In the settings sidebar, click on **"Features"**
2. Click on **"MCP"** (Model Context Protocol)

### 3. Add GA4 MCP Server

Click the **"+ Add New MCP Server"** button and configure:

#### Server Configuration:
- **Name:** `GA4 Analytics`
- **Type:** `stdio`
- **Command:** `ga4-mcp-server`

#### Alternative Configuration (if PATH issues):
If the above doesn't work, use the full path:
- **Command:** `/Users/samumetso/Library/Python/3.11/bin/ga4-mcp-server`

### 4. Save and Restart

1. Click **"Save"** or **"Add Server"**
2. **Restart Cursor completely** (close and reopen)

### 5. Verify Installation

After restarting Cursor:

1. Open a new Composer session
2. The GA4 MCP server should appear in your MCP servers list
3. You may need to click the refresh button to populate the tool list

## Environment Setup Required

Before using the MCP server, you need to:

1. **Set up Google Cloud credentials:**
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
   ```

2. **Add to your shell profile for persistence:**
   ```bash
   echo 'export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"' >> ~/.zshrc
   source ~/.zshrc
   ```

## Testing the Integration

In Cursor's Composer, try these queries:

### Basic Connection Test:
```
"Show me the available GA4 tools and what they can do"
```

### Sample Analytics Query:
```
"Get the total users for my GA4 property for the past 7 days"
```

### Advanced Query:
```
"Show me the top 10 pages by pageviews for the last month, including bounce rate"
```

## Troubleshooting

### Common Issues:

1. **"ga4-mcp-server command not found"**
   - Use full path: `/Users/samumetso/Library/Python/3.11/bin/ga4-mcp-server`
   - Or add to PATH as shown above

2. **"GOOGLE_APPLICATION_CREDENTIALS not set"**
   - Set the environment variable as shown above
   - Restart Cursor after setting the variable

3. **"Server not appearing in Cursor"**
   - Restart Cursor completely
   - Check MCP server configuration
   - Try refreshing the MCP servers list

4. **"Authentication failed"**
   - Verify service account has access to GA4 property
   - Check that JSON key file exists and is readable
   - Ensure correct path in GOOGLE_APPLICATION_CREDENTIALS

### Debug Steps:

1. **Test command in terminal:**
   ```bash
   ga4-mcp-server --help
   ```

2. **Verify environment variable:**
   ```bash
   echo $GOOGLE_APPLICATION_CREDENTIALS
   ```

3. **Check file permissions:**
   ```bash
   ls -la $GOOGLE_APPLICATION_CREDENTIALS
   ```

## Next Steps

1. Complete Google Cloud setup (see `docs/mcp-setup.md`)
2. Configure your service account credentials
3. Test the integration with sample queries
4. Start analyzing your GA4 data!

## Example Queries for GA4 Analysis

Once configured, you can ask natural language questions like:

- "What's the conversion rate for the past month?"
- "Show me user demographics breakdown"
- "Compare this month's traffic to last month"
- "What are the most popular landing pages?"
- "Show me the bounce rate by device category"
- "What's the average session duration?"
