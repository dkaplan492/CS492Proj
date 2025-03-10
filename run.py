# Initializes and runs the Flask application so that the platform is accessible in website

import os
from src import create_app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render uses port 10000 by default
    app.run(host='0.0.0.0', port=port, debug=True)