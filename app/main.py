from app import app
import view
import os

# if __name__ == '__main__':
#     app.run()

port = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)