from flask import render_template
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the SOLUTION_STEVE_LIN_1.yml file to configure the endpoints
app.add_api('SOLUTION_STEVE_LIN_1.yaml')

def _app_run():
    app.run(host='0.0.0.0', port=8080, debug=True)

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:8080/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

# The main function
def main():
    _app_run()

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    main()
