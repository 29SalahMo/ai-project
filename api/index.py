"""
Vercel serverless function wrapper for Streamlit app
Note: Streamlit apps work better on platforms like Streamlit Cloud, Heroku, or Railway
This is a workaround for Vercel deployment
"""

import subprocess
import sys
import os

def handler(request):
    """Vercel serverless handler"""
    # Note: Streamlit requires a persistent server, which Vercel doesn't support well
    # This is a basic wrapper - for best results, use Streamlit Cloud instead
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html'
        },
        'body': '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>AI Project - Streamlit App</title>
            <meta http-equiv="refresh" content="0; url=https://share.streamlit.io">
        </head>
        <body>
            <h1>AI Project</h1>
            <p>Streamlit apps work best on <a href="https://share.streamlit.io">Streamlit Cloud</a></p>
            <p>For Vercel deployment, consider using a different framework or deploy to Streamlit Cloud.</p>
        </body>
        </html>
        '''
    }
