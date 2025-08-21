#!/bin/bash

# GA4 MCP Server Test Script

echo "🧪 Testing GA4 MCP Server Setup..."
echo ""

# Check if ga4-mcp-server command is available
echo "1. Checking ga4-mcp-server command..."
if command -v ga4-mcp-server &> /dev/null; then
    echo "✅ ga4-mcp-server command found"
else
    echo "❌ ga4-mcp-server command not found"
    echo "   Try: export PATH=\"/Users/samumetso/Library/Python/3.11/bin:\$PATH\""
    exit 1
fi

# Check if GOOGLE_APPLICATION_CREDENTIALS is set
echo ""
echo "2. Checking Google Cloud credentials..."
if [ -z "$GOOGLE_APPLICATION_CREDENTIALS" ]; then
    echo "❌ GOOGLE_APPLICATION_CREDENTIALS not set"
    echo "   Set it with: export GOOGLE_APPLICATION_CREDENTIALS='/path/to/your/service-account-key.json'"
else
    echo "✅ GOOGLE_APPLICATION_CREDENTIALS is set: $GOOGLE_APPLICATION_CREDENTIALS"
    
    # Check if the file exists
    if [ -f "$GOOGLE_APPLICATION_CREDENTIALS" ]; then
        echo "✅ Credentials file exists"
    else
        echo "❌ Credentials file not found at: $GOOGLE_APPLICATION_CREDENTIALS"
    fi
fi

# Test the server help command
echo ""
echo "3. Testing server help command..."
if ga4-mcp-server --help &> /dev/null; then
    echo "✅ GA4 MCP server is working"
else
    echo "❌ GA4 MCP server test failed"
    echo "   Run: ga4-mcp-server --help"
fi

echo ""
echo "🎯 Next steps if tests pass:"
echo "1. Configure Cursor MCP settings (see docs/cursor-mcp-config.md)"
echo "2. Restart Cursor"
echo "3. Test with a GA4 query in Composer"
