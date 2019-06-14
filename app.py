from flask import Flask, render_template, url_for, request, session, redirect, jsonify
import pickle

app = Flask(__name__)

# our data:
all_users = [{'email': 'p'}, {'email': 'asd'}]

# encrypting our data:
pickled_users = pickle.dumps(all_users)
unpickled_users = pickle.loads(pickled_users)


@app.route('/', methods=['GET'])
def showAll():
    # unpickling and rendering our data in a template:

    return render_template('index.html', users=unpickled_users)


@app.route('/new', methods=['POST', 'GET'])
def addNew():
    if request.method == 'GET':
        return render_template('new.html')

    # unpickling our data to check if it contained the new form data:

    formData = {'email': request.form['email']}

    if formData not in unpickled_users:
        unpickled_users.append(formData)
        print('-----added new email-----', unpickled_users)
        # once added new data, we pickle it all again:
        pickled_users = pickle.dumps(unpickled_users)
        return redirect(url_for('showAll'))
    return render_template('error.html')


@app.route('/error', methods=['GET'])
def showError():
    return render_template('error.html')


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)
