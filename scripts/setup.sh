#!/bin/bash

# GA4 MCP Server Setup Script
# This script helps set up the Google Analytics 4 MCP server

echo "🚀 Setting up GA4 MCP Server..."

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"

# Install requirements
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

# Check if Google Cloud credentials are set
if [ -z "$GOOGLE_APPLICATION_CREDENTIALS" ]; then
    echo "⚠️  Warning: GOOGLE_APPLICATION_CREDENTIALS environment variable not set"
    echo "   Please set it to point to your service account JSON file:"
    echo "   export GOOGLE_APPLICATION_CREDENTIALS='/path/to/your/service-account-key.json'"
else
    echo "✅ Google Cloud credentials configured: $GOOGLE_APPLICATION_CREDENTIALS"
    
    # Check if the credentials file exists
    if [ -f "$GOOGLE_APPLICATION_CREDENTIALS" ]; then
        echo "✅ Credentials file found"
    else
        echo "❌ Credentials file not found at: $GOOGLE_APPLICATION_CREDENTIALS"
    fi
fi

echo ""
echo "🎯 Next steps:"
echo "1. Set up Google Cloud service account (see docs/mcp-setup.md)"
echo "2. Configure Cursor MCP settings"
echo "3. Test the connection with a simple query"
echo ""
echo "✨ Setup complete! Check the README.md for detailed instructions."
echo ""
echo "📋 Quick Setup Checklist:"
echo "□ 1. Set up Google Cloud service account (docs/mcp-setup.md)"
echo "□ 2. Set GOOGLE_APPLICATION_CREDENTIALS environment variable"
echo "□ 3. Configure Cursor MCP settings (docs/cursor-mcp-config.md)"
echo "□ 4. Restart Cursor"
echo "□ 5. Test with a simple GA4 query"
echo ""
echo "🔧 Test GA4 MCP server:"
echo "ga4-mcp-server --help"
