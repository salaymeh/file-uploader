from flask import Flask, jsonify,request
from flask_cors import CORS, cross_origin
from psql import get_db_conn


# Define a function to process each row as it becomes available
def process_row(row):
    # Convert the row to a dictionary
    row_dict = {
        "id": row[0],
        "filename": row[1]
    }
    # Return the row as a JSON object
    return row_dict

# Create a Flask app
app = Flask(__name__)
CORS(app, resources={
    r"/files/*": {"origins": ["http://localhost:5173", "http://127.0.0.1:5000"], "supports_credentials": True},
    r"/upload": {"origins": ["http://localhost:5173", "http://127.0.0.1:5000"], "supports_credentials": True, "methods": ["POST", "OPTIONS"]},
    r"/files/delete": {"origins": ["http://localhost:5173", "http://127.0.0.1:5000"], "supports_credentials": True, "methods": ["DELETE", "OPTIONS"]}
})



# Define a route to retrieve the "files" table as a JSON object
@app.route('/files', methods=['GET'])
@cross_origin(origin='http://localhost:5173', supports_credentials=True)
def get_files():
    # Open a connection to the database
    conn = get_db_conn()
    cur = conn.cursor()

    # Use a loop to fetch each set of rows and return them as a JSON object
    rows = []
    cur.execute("SELECT * FROM files")
    for row in cur:
        row_dict = process_row(row)
        rows.append(row_dict)
    cur.close()
    conn.close()
    response = jsonify(rows)
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

@app.route('/upload', methods=['POST'])
def upload_file():
    conn = get_db_conn()
    cur = conn.cursor()
    file = request.form['filename']
    print(file)
    cur.execute(f''' 
        INSERT INTO files (filename) VALUES ('{file}')
    ''')
    conn.commit()
    cur.close()
    conn.close()
    return "File uploaded successfully."




@app.route('/files/edit', methods=['POST'])
def edit_file():
    # Open a connection to the database
    conn = get_db_conn()
    cur = conn.cursor()

    # Get the data from the request form
    filename = request.form.get('filename')
    file_id = request.form.get('id')
    cur.execute(
        "UPDATE files SET filename = %s WHERE id = %s",
        (filename,file_id)
    )

    # Commit the transaction and close the database connection
    conn.commit()
    cur.close()
    conn.close()

    # Return a success message
    return "Data updated successfully."


@app.route('/files/delete/<int:file_id>', methods=['DELETE'])
def delete_file(file_id):
    # Open a connection to the database
    conn = get_db_conn()
    cur = conn.cursor()

    # Delete the row from the "files" table
    cur.execute(
        "DELETE FROM files WHERE id = %s",
        (file_id,)
    )

    # Commit the transaction and close the database connection
    conn.commit()
    cur.close()
    conn.close()

    # Return a success message
    return "Data deleted successfully."

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response