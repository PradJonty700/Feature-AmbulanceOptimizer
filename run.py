# run.py
# This is the main entry point to start your Flask server.

from src import create_app
import os

# Create the Flask app instance by calling the factory function from our 'src' package.
app = create_app()

# This is a standard Python guard. The code inside this block will only run
# when you execute this file directly with 'python run.py'.
if __name__ == '__main__':
    # Get the port from an environment variable named 'PORT', or use 3000 as a default.
    port = int(os.environ.get('PORT', 3000))

    # Run the Flask development server.
    # debug=True: The server will automatically restart when you save a file.
    # host='0.0.0.0': Makes the server accessible on your local network, not just on your machine.
    app.run(debug=True, host='0.0.0.0', port=port)